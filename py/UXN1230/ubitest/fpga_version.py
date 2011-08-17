from ubitest.basetest import BaseTest
import logging
log=logging.getLogger(__name__)

class FPGAVerTest(BaseTest):

    def collect(self,dev,data):
        data['version'] = dev.get("FPGA", "version")
        log.info("FPGA VERSION = 0x%x" % data["version"])

    def analyze(self,data,ana):
        pass

    def screen(self,data,ana,results):
        results['version'] = self.screen_result(
            assertion = bool(data['version']),
            criteria = "version not zero",
            desc = "Queried FPGA VERSION=0x%x" % data["version"])


if __name__=='__main__':
    FPGAVerTest.main()

