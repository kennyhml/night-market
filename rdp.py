import requests
import zipfile
import subprocess


class Installer:
    zip_link = "https://github.com/stascorp/rdpwrap/releases/download/v1.6.2/RDPWrap-v1.6.2.zip"
    updater_link = "https://github.com/asmtron/rdpwrap/raw/master/autoupdate.zip"
    rdp_dir = "C:\\Program Files\\RDP Wrapper test"

    def download(self, url, target_dir):
        print(f"Started downloading zip...")

        # Downloading the file by sending the request to the URL
        req = requests.get(url)

        # Split URL to get the file name
        filename = target_dir + url.split("/")[-1]

        # Writing the file to the local file system
        with open(filename, "wb") as output_file:
            output_file.write(req.content)
        print("Download completed!")

    def unpack(self, file, target_dir):
        print(f"Unpacking {file} to {target_dir}")
        # unpack the zip to our targets folder
        with zipfile.ZipFile(file, "r") as zip_ref:
            zip_ref.extractall(target_dir)

    def run_batch(self, dir):
        print(f"Executing {self.rdp_dir + dir}")
        subprocess.call([self.rdp_dir + dir])

        print(f"Executed {dir} successfully!")

    def setup_files(self):
        self.download(self.zip_link, "images/temp/")
        self.download(self.updater_link, "images/temp/")

        self.unpack("images/tempautoupdate.zip", self.rdp_dir)
        self.unpack("images/temp/RDPWrap-v1.6.2.zip", self.rdp_dir)

    def run_installers(self):
        self.run_batch("\\helper\\autoupdate__enable_autorun_on_startup.bat")
        self.run_batch("\\autoupdate.bat")


install = Installer()
install.setup_files()
install.run_installers()