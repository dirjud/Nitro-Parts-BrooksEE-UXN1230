M24XXDIR= ../../../Microchip/M24XX/fx2/
M25PDIR=../../../Numonyx/M25P/fx2/
SPARTANDIR=../../../Xilinx/Spartan/fx2/

# possible env flags
# -D DEBUG_FIRMWARE - enable stdio & printf on sio-0 (57600 buad)
SDCCFLAGS := $(SDCCFLAGS) -I. -I$(FX2DIR) -I$(M24XXDIR) -I$(M25PDIR) -I$(SPARTANDIR)
BASENAME=firmware

SOURCES = $(FX2DIR)firmware.c \
		  $(FX2DIR)main.c \
		  handlers.c \
		  $(FX2DIR)dummy.c \
		  $(FX2DIR)boot.c \
		  $(FX2DIR)fx2term.c \
		  $(M25PDIR)m25p.c \
		  $(M24XXDIR)m24xx.c \
		  $(SPARTANDIR)spartan.c
A51_SOURCES = $(FX2DIR)dscr.a51 $(FX2DIR)fx2_sfr.a51

VID=0x1fe1
PID=0x1230

FIRMWARE_VERSION=0x1