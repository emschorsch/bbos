from osandio.fileCompression import UnzipProgramController
import subprocess
import os
import logging

class _7ZipController(UnzipProgramController):
    def __init__(self, locationOf7Zip):
        self.locationOf7Zip = os.path.abspath(locationOf7Zip)

    def unzip(self, fileName, outputDir):
        # unzipCommand = self.locationOf7Zip + " x -y -o" + outputDir + " " + fileName
        unzipCommand2 = "unzip " + fileName + " -d " + outputDir

        logging.info("running:"+unzipCommand2)
        subprocess.call(unzipCommand2, shell=True)



