NITRO_PARTS_DIR ?= ../..

UXN1230_DIR = $(NITRO_PARTS_DIR)/BrooksEE/UXN1230

UXN1230_INC_PATHS = $(UXN1230_DIR)/sim/ddr2 \
                    $(UXN1230_DIR)/lib/rtl/xilinx \

UXN1230_SIM_FILES = \
	$(UXN1230_DIR)/sim/UXN1230_tb.v \
	$(UXN1230_DIR)/lib/rtl/HostInterface/models/fx2.v \
        $(UXN1230_DIR)/sim/ddr2/ddr2_model_c3.v \

UXN1230_SYN_FILES = \
	$(UXN1230_DIR)/rtl/UXN1230.v \
	$(UXN1230_DIR)/lib/rtl/HostInterface/rtl/HostInterface.v \
	$(UXN1230_DIR)/rtl/ddr2/mig_38.v \
	$(UXN1230_DIR)/rtl/ddr2/infrastructure.v \
	$(UXN1230_DIR)/rtl/ddr2/memc_wrapper.v \
	$(UXN1230_DIR)/rtl/ddr2/mcb_ui_top.v \
	$(UXN1230_DIR)/rtl/ddr2/mcb_raw_wrapper.v \
	$(UXN1230_DIR)/rtl/ddr2/mcb_soft_calibration_top.v \
	$(UXN1230_DIR)/rtl/ddr2/mcb_soft_calibration.v \
	$(UXN1230_DIR)/rtl/ddr2/iodrp_controller.v \
	$(UXN1230_DIR)/rtl/ddr2/iodrp_mcb_controller.v \
	$(NITRO_PARTS_DIR)/Xilinx/Spartan/rtl/di2mig.v \

SIM_TOP_MODULE=UXN1230_tb
FPGA_TOP  = UXN1230
FPGA_PART = xc6slx16-csg324-2
FPGA_ARCH = spartan6
UCF_FILES += $(UXN1230_DIR)/xilinx/UXN1230.ucf
SPI_PROM_SIZE =  524288
