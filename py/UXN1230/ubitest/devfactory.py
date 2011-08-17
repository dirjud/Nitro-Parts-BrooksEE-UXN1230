from nitro_parts.BrooksEE import UXN1230
import time
import logging
import uuid

import ubitest
from ubitest.devfactory import DevFactory as dfbase

import nitro

import conf

uvid, upid = 0x1fe1, 0x1230
cvid, cpid = 0x04b4, 0x8613 # unprogrammed board


class DevFactory(dfbase):

    log=logging.getLogger(__name__)

    def __init__(self,config):
        dfbase.__init__(self,config)

        self.p=conf.Configurable ( "Device Factory",
            ( conf.StringParam ( "firmware path", "firmware.ihx" ), ),
            config.key,
            True )

    def get_device(self):
        dev=UXN1230.get_dev()

        # check if serial number has ever been set
        serial = dev.get_serial()
        self.log.info ( "Device Serial: %s" % serial )
        if serial == u'\uffff'* 8:
            while True:
                serial = "U" + str(uuid.uuid4())[-7:].upper()
                if serial not in list(self.config.datastore.iter_serialnums()):
                    break
                self.log.debug ( "Serial number conflict: %s.  Trying again." % serial )
            self.log.info ( "Setting new device serial to %s." % serial )
            dev.set_serial(serial)

        self.config.set_serial([serial])
        return dev 

    def finished(self,dev):
        dev.close()
