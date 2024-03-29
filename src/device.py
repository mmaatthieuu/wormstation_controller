from PyQt5 import QtGui, QtCore
import paramiko
import os
import time
from datetime import datetime
import subprocess

from math import log10,ceil
from src.QontrollerUI import *

class Device:

    def __init__(self, name, id, uptodate=None):
        self.name = name
        self.id = id
        self.uptodate = uptodate

        self.ssh = paramiko.SSHClient()
        
        self.username = "matthieu"

        self.connected = False
        self.ssh_connect()




    def __del__(self):
        self.ssh.close()

    @property
    def is_running(self):
        stdin, stdout, stderr = self.ssh.exec_command("pgrep picam", get_pty=True)
        if stdout.readline() == '':
            return False
        else:
            return True

    @property
    def is_uptodate(self):
        stdin, stdout, stderr = self.ssh.exec_command("cd /home/matthieu/piworm && git fetch --dry-run", get_pty=True)
        if stdout.readline() == '':
            print(self.name + " up to date")
            return True
        else:
            print("Update available for " + self.name)
            return False

    def update(self):
        if self.is_running:
            print("Device %s is running : update skipped" % self.name)
        else:
            ## hard pull
            # stdin, stdout, stderr = self.ssh.exec_command(
            #    "cd /home/matthieu/piworm && git reset --hard origin/main && git pull", get_pty=True)
            stdin, stdout, stderr = self.ssh.exec_command("cd /home/matthieu/piworm && git pull", get_pty=True)
            for line in iter(stdout.readline, ""):
                print(line, end="")
            print("Device %s updated" % self.name)

    def ssh_connect(self):
        self.connected = False
        i = 0
        while (not self.connected and i < 3):
            try:
                self.ssh.load_system_host_keys()
                self.ssh.connect(self.name, port=22, username=self.username, timeout=3)
                self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                self.connected = True
            except paramiko.ssh_exception.SSHException as e:
                print(e)
                if os.name == 'nt':
                    subprocess.run([r'type', r'%userprofile%\.ssh\id_rsa.pub','|','ssh',f'{self.username}@{self.name}',r"cat >> .ssh/authorized_keys"], shell=True)
                else:
                    os.system(f"ssh-copy-id {self.username}@{self.name}")
                i += 1
            except paramiko.ssh_exception.NoValidConnectionsError as e:
                print(e)
                print(f'Device {self.name} is unreachable.')

                i += 1

            finally:
                return self.connected

    def receive_json_config_file(self, file):
        with self.ssh.open_sftp() as sftp:
            remote_folder = f"/home/{self.username}/.config/wormstation"
            remote_path = f'{remote_folder}/{os.path.basename(file)}'
            try:
                sftp.mkdir(remote_folder)
            except IOError:
                # Folder already exists
                pass

            sftp.put(file, remote_path)

        return remote_path


    def get_frame(self,settings_remote_path):
        if self.is_running:
            return self.import_last_frame_from_device()
        else:
            return self.acquire_new_frame(settings_remote_path)

    def read_remote_frame(self, filename):
        sftp = self.ssh.open_sftp()
        frame_bytes = sftp.file(filename, mode='r').read()

        ba = QtCore.QByteArray(frame_bytes)
        new_pixmap = QtGui.QPixmap()
        ok = new_pixmap.loadFromData(ba, "JPG")

        sftp.close()

        return new_pixmap

    def import_last_frame_from_device(self):
        try:
            print("Device is running : getting last frame")
            return self.read_remote_frame("/home/matthieu/tmp/last_frame.jpg")
        except FileNotFoundError:
            print("No frame ready")
            return None

    def acquire_new_frame(self, config_file):
        self.start(config_file, background_mode=False)
        """
        command = 'picam -o /home/matthieu/tmp/preview.jpg -v -t 0 -avg %d -ti %f -q %d -ss %d -br %d -iso %d -l %d -vv -a' % \
                  (s.averaging, s.time_interval, s.jpg_quality, s.shutter_speed, s.brightness, s.iso, s.led_intensity)
        stdin, stdout, stderr = self.ssh.exec_command(command, get_pty=True)
        for line in iter(stdout.readline, ""):
            print(line, end="")
        """
        return self.read_remote_frame("/home/matthieu/tmp/last_frame.jpg")

    def record(self, config_file):

        print(self.name)
        if self.is_running:
            print("WARNING : Device %s is already running. Recording ignored")
        else:
            #print(s)
            print("\n\n\n")
            self.start(config_file, background_mode=True)

    def start(self, config_file, background_mode=False):

        rec_command = f'picam {config_file}'

        if background_mode:
            log_folder = self.create_log_folder()
            command = f'nohup {rec_command}'
        else:
            command = rec_command

        print(command)
        try:
            stdin, stdout, stderr = self.ssh.exec_command(command, get_pty=True)
            for line in iter(stdout.readline, ""):
                print(line, end="")

        except paramiko.ssh_exception.SSHException as e:
            print(e)
            print(f"Connection with device {self.name} lost")


    def stop(self):
        stdin, stdout, stderr = self.ssh.exec_command("pkill picam", get_pty=True)
        print("Device %s stopped" % self.name)

    def shutdown(self):
        print("shutting down %s" % self.name)
        stdin, stdout, stderr = self.ssh.exec_command("sudo poweroff", get_pty=True)
        del self

    def reboot(self):
        print("Rebooting %s" % self.name)
        stdin, stdout, stderr = self.ssh.exec_command("sudo reboot", get_pty=True)
        del self

    def turn_on_led(self):
        stdin, stdout, stderr = self.ssh.exec_command("python ~/piworm/src/led_control/turn_on_led.py", get_pty=True)

    def turn_off_led(self):
        stdin, stdout, stderr = self.ssh.exec_command("python ~/piworm/src/led_control/turn_off_led.py", get_pty=True)

    def create_log_folder(self):
        log_folder = f"/home/{self.username}/log"
        try:
            with self.ssh.open_sftp() as sftp:
                sftp.mkdir(log_folder)
        except:
            pass

        return log_folder

    def clear_tmp_folder(self):
        print(f'Clear folder /home/matthieu/.wormstation_tmp/ on {self.name}')
        stdin, stdout, stderr = self.ssh.exec_command("rm -rf /home/matthieu/.wormstation_tmp/*", get_pty=True)
