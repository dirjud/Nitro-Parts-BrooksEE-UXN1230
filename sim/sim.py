import VUXN1230_tb as tb
from nitro_parts.BrooksEE import UXN1230
from nitro_parts.BrooksEE.UXN1230 import ubitest
import logging
logging.basicConfig(level=logging.DEBUG)
import numpy, conf


if 1:
    tb.init("sim.vcd")
else:
    tb.init()

dev = UXN1230.UXN1230(tb.get_dev())
d = {}
execfile("../terminals.py", d)
dev.set_di(d["di"])


#t = ubitest.DramPatTest(config)

buf1 = "\xAA\x55" * 8
dev.write("DRAM", 0, buf1)

buf2 = "\x00" * len(buf1)
dev.read("DRAM", 0, buf2)



tb.adv(100)
tb.end()
