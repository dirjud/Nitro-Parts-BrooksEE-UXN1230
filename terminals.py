import nitro, os
from nitro import DeviceInterface, Terminal, Register, SubReg

di=DeviceInterface(
    name='UXN1230', 

    terminal_list=[
        ########################################################################
        Terminal(
            name='DUMMY',
            comment='Dummy Terminal',
            regAddrWidth=16, 
            regDataWidth=16,
            ),
        Terminal(
            name='FPGA',
            comment='FPGA registers',
            addr=0x1,
            regAddrWidth=16, 
            regDataWidth=16,
            register_list=[
                Register(name='version',
                         type='int',
                         mode='read',
                         subregs=[SubReg(name="minor", width=8),
                                  SubReg(name="major", width=8),],
                         comment='FPGA release version',
                         ),
                Register(name='sw_reset',
                         type='int',
                         mode='write',
                         width=1,
                         comment='Software reset of the FPGA.',
                         init=0,
                         ),
                Register(name="mode",
                         type="int",
                         mode="write",
                         subregs=[
                                  SubReg(name="en1_8V", width=1, init=1, comment="Enables 1.8V voltage regulator to sdram. Normally you will not need to turn this off."),
                                  ],
                         comment="Mode settings",
                         ),
                Register(name="led",
                         type="int",
                         mode="write",
                         subregs=[
                                  SubReg(name="sel", width=4, init=0, comment="Selects what drives the LEDs on the UXN1230 board.", valuemap=dict(clocks=0x0, static=0x1, off=0xF)),
                                  SubReg(name="static", width=4, init=0xF, comment="Sets the static values driven to the LEDs when led.sel is 'static'"),
                                  SubReg(name="driver", width=1, init=0, comment="Controls the 5V LED driver on port JP1 of the UXN1230 board."),
                                  ],
                         comment="Mode settings",
                         ),
                ]),

        ########################################################################
        Terminal(
            name='PROGRAM_FPGA',
            addr=0x104,
            regAddrWidth=16,
            regDataWidth=16,
            comment='Termanial for writing FPGA bit file for programming the FPGA',
            ),

        ########################################################################
        Terminal(
            name='DRAM',
            comment='DRAM Read/Write Port',
            regAddrWidth=32, 
            regDataWidth=16,
            ),

        Terminal(
            name='DRAM_CTRL',
            comment='DRAM control and status registers',
            regAddrWidth=16, 
            regDataWidth=16,
            register_list=[
                Register(name='status',
                         type='int',
                         mode='read',
                         subregs=[SubReg(name="mcb", width=32, comment="Status Regsiter from MCB block"),
                                  SubReg(name="write_error", width=4, comment="Status indicator from dram fifo"),
                                  SubReg(name="write_underrun", width=4, comment="Status indicator from dram fifo"),
                                  SubReg(name="read_error", width=4, comment="Status indicator from dram fifo"),
                                  SubReg(name="read_overflow", width=4, comment="Status indicator from dram fifo"),
                                  SubReg(name='pll_locked',   width=1, comment='Indicates whether PLL generating SDRAM clock is locked.'),
                                  SubReg(name='calib_done',   width=1, comment='Indicates whether calibration is done so that MCB can be used.'),
                                  SubReg(name='selfrefresh_mode',   width=1, comment='Indicates whether PLL generating SDRAM clock is locked.'),
                                  SubReg(name="rst", width=1, comment="rst returned from the infrastructure block"),
                                  ],
                         comment='Status Register',
                         ),
                Register(name='mcb_reset',
                         type='trigger',
                         mode='write',
                         width=1,
                         comment="Resets the dram memory controller block (MCB).",
                         ),
                Register(name='mode',
                         type='int',
                         mode='write',
                         subregs=[SubReg(name='selfrefresh',init=0,width=1,comment='Puts dram controller in self refresh mode. See Xilinx UG388 MCB User Guide for more information'),
                                  ],
                         comment='Mode Register',
                         ),
                ]),

        ],
    )

# load the baseline UXN1212 terminals
import nitro
di=nitro.load_di("Cypress/CY7C68013/CY7C68013.xml", di)
di = nitro.load_di("Xilinx/Spartan/Spartan.xml", di)
di["FX2_SFR"]["IOA"]["A0"].name = "init_b"
di["FX2_SFR"]["IOA"]["A1"].name = "done"
di["FX2_SFR"]["IOA"]["A3"].name = "prog_b"
# load the FPGA prom terminals
di = nitro.load_di("Numonyx/M25P/M25P.xml", di)
di["DATA"].name = "FPGA_PROM"
di["CTRL"].name = "FPGA_PROM_CTRL"


