/**
 * Copyright (C) 2009 BrooksEE, LLC.
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 2.1 of the License, or (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this library; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
 **/


#include <handlers.h>
#include <fx2regs.h>
#include <fx2term.h>
#include <m25p.h> // fpga prom
#include <m24xx.h> // fx2 prom
#include <spartan.h>
#include "terminals.h"
#include <dummy.h>

io_handler __code io_handlers[] = {
 DECLARE_DUMMY_HANDLER(TERM_DUMMY),
 DECLARE_FX2_HANDLER(TERM_FX2),
 DECLARE_FX2SFR_HANDLER(TERM_FX2_SFR),
 DECLARE_M24XX_HANDLER(TERM_FX2_PROM),
 DECLARE_M25P_CTRL_HANDLER(TERM_FPGA_PROM_CTRL),
 DECLARE_M25P_DATA_HANDLER(TERM_FPGA_PROM),
 DECLARE_SPARTAN_PARPRG_HANDLER(TERM_PROGRAM_FPGA),
 DECLARE_SPARTAN_CTRL_HANDLER(TERM_FPGA_CTRL),
 DECLARE_SPARTAN_HANDLER(0)
};

