import VUXN1230_tb as tb
from nitro_parts.BrooksEE import UXN1230
import time
import logging
import uuid

import ubitest
from ubitest.devfactory import DevFactory as dfbase
import nitro
import conf

class DevFactory(dfbase):

    log=logging.getLogger(__name__)

    def __init__(self,config):
        dfbase.__init__(self,config)

        self.p=conf.Configurable ( "Device Factory",
            ( conf.StringParam ( "VCD Filename", "" ), ),
            config.key,
            True )

    def get_key(self,dev):
        return "VERILATOR_SIM"

    def get_device(self, wait_for_removal):
        vcd_filename = self.p._('VCD Filename')
        vcd_filename = "sim.vcd"
        print "VCD FILENAME=",vcd_filename
        if vcd_filename:
            tb.init(vcd_filename)
        else:
            tb.init()

        dev = UXN1230.UXN1230(tb.get_dev())
        UXN1230.init_dev(dev)
        return dev 

    def finished(self,dev):
        tb.end()
