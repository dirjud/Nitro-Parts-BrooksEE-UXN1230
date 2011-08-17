from ubitest.basetest import BaseTest
import numpy
import logging
log = logging.getLogger(__name__)
import conf

DRAM_SIZE_BYTES = 2**26

def check_status(dev, data):
    data["status"] = dev.get_subregs("DRAM_CTRL", "status")

    if not(data["status"].calib_done):
        raise Exception("FPGA not done calibrating DRAM lines")

#    if not(data["status"].pll_locked):
#        raise Exception("FPGA PLL for DRAM not locked")

    if data["status"].read_overflow or data["status"].write_underrun or data["status"].selfrefresh_mode or data["status"].write_error or data["status"].read_error or data["status"].rst:
        raise Exception("Error in DRAM.status")

################################################################################
class DramPatTest(BaseTest):
    """Fills the DRAM with toggled data (0xAAAA, 0x5555) and then reads it
    back to verify it."""
    def collect(self, dev, data):
        check_status(dev, data)
        data["len"] = N = DRAM_SIZE_BYTES;
        bufW  = "\xAA\xAA\x55\x55" * (N/4)
        dev.write("DRAM", 0, bufW, 15000)
        bufR = "\x00" * N
        dev.read("DRAM", 0, bufR, 15000)
        data["passing"] = bufW == bufR
        if 0: # normally don't save off the data because it is too big
            data["bufW"] = bufW
            data["bufR"] = bufR

    def analyze(self,data,ana):
        pass

    screens = { 'DRAM Pattern Test' : "Writes pattern bytes to DRAM and read it back to verify", }

    def screen(self,data,ana,results):
        results["DRAM Pattern Test"]["result"] = data["passing"]

################################################################################
class DramRandTest(BaseTest):
    """Fills the DRAM with random data and then reads it back to verify"""
    def collect(self, dev, data):
        check_status(dev, data)
        data["len"] = N = DRAM_SIZE_BYTES;
        offset = N/2
        bufW  = (numpy.random.rand(N/2)*2**16).astype(numpy.uint16)
        log.debug("Writing %d random bytes to the dram" % (len(bufW)*2))
        dev.write("DRAM", 0, bufW, 15000)
        bufR = numpy.zeros_like(bufW)
        bufR2 = numpy.zeros_like(bufW[offset/2:])
        log.debug("Reading %d bytes back from the dram" % (len(bufW)*2))
        dev.read("DRAM", 0, bufR, 15000)
        dev.read("DRAM", offset, bufR2, 15000)
        j = (bufW != bufR)
        k = (bufW[offset/2:] != bufR2)
        data["passing"] = not(j.any()) and not(k.any())

        if 0: #normally don't save off the data because it is too big
            data["fail_locs%d"%i] = numpy.nonzero(j)
            data["bufW"] = bufW
            data["bufR"] = bufR
            data["bufR2"] = bufR2

    def analyze(self,data,ana):
        pass

    screens = { 'DRAM Random Data Test' : "Writes random bytes to DRAM and reads it back to verify", }

    def screen(self,data,ana,results):
        results["DRAM Random Data Test"]["result"] = data["passing"]

################################################################################
class DramAddrTest(BaseTest):
    """Writes pattern of known length to specific location. Then
    writes a second pattern of known length in front of the initial
    pattern. Then reads them both back in one read and verifies the
    pattern. This checks that the dram addressing scheme is working
    correctly."""
    def collect(self, dev, data):
        check_status(dev, data)

        N=2**10;
        bufW1 = "\xAA" * N
        bufW2 = "\x55" * N
        bufR  = "\x00" * (2*N)

        addr = 100
        dev.write("DRAM", addr+len(bufW1), bufW2)
        dev.write("DRAM", addr, bufW1)
        dev.read("DRAM", addr, bufR)

        data["passing"] = bufW1+bufW2 == bufR
        data["bufW1"]   = bufW1;
        data["bufW2"]   = bufW2;
        data["bufR"]    = bufR;
        
    def analyze(self, data, ana):
        pass

    screens = { 'DRAM Address Test' : "Address Write to two different addresses as two writes. Then read it back as one", 
                }

    def screen(self, data, ana, results):
        results["DRAM Address Test"]["result"] = data["passing"]



if __name__=='__main__':
#    DramPatTest.main()
    DramRandTest.main()

