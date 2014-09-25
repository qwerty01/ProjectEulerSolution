################################################################################
# Copyright (C) 2014 Qwerty01 (qw3rty01@gmail.com, http://github.com/qwerty01) #
#                                                                              #
# This program is free software; you can redistribute it and/or modify it      #
# under the terms of the GNU General Public License as published by the Free   #
# Software Foundation; either version 2 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# This program is distributed in the hope that it will be useful, but WITHOUT  #
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or        #
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for    #
# more details.                                                                #
#                                                                              #
# You should have received a copy of the GNU General Public License along with #
# this program; if not, write to the Free Software Foundation, Inc.,           #
# 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.                #
################################################################################

#############
# Languages #
#############
LANGUAGES = cpp python csharp nasm

###############
# Directories #
###############
# C++
CPPDIR=cpp
# Python
PYDIR=python
# C#
CSDIR=csharp
# NASM
NASMDIR=nasm

##################
# Compiler Tools #
##################
# C++
CC=g++
# Python
PY=python
PYC=python -m py_compile
# C#
CS=csc
# NASM
NASM=nasm -fwin32

#####################
# Cleanup Variables #
#####################
# C++
CLEANCPP=$(CPPDIR)/*.exe $(CPPDIR)/*.o
# Python
CLEANPY=$(PYDIR)/*.pyc
# C#
CLEANCS=$(CSDIR)/*.exe
# NASM
CLEANNASM=$(NASMDIR)/*.exe $(NASMDIR)/*.obj
# Clean
CLEANDIRS=$(CLEANCPP) $(CLEANPY) $(CLEANCS) $(CLEANNASM)

###########
# Objects #
###########
# C++
CPPOBJ=$(CPPDIR)/p1.o
# C#
CSNAME=p1.cs
CSOBJ=$(CSDIR)/$(CSNAME)
# NASM
NASMOBJ=$(NASMDIR)/p1.obj

###############
# Executables #
###############
# C++
CPPEXEC=$(CPPDIR)/p1.exe
# Python
PYEXEC=$(PYDIR)/p1.pyc
# C#
CSTARG=p1.exe
CSEXEC=$(CSDIR)/$(CSTARG)
# NASM
NASMEXEC=$(NASMDIR)/p1.exe

#################
# Main Makefile #
#################
default:
	@echo ""
	@echo "Project Euler Problem 1"
	@echo "===================================================================="
	@echo "  Multiples of 3 and 5"
	@echo "  --------------------"
	@echo "    If we list all the natural numbers below 10 that are multiples"
	@echo "    of 3 or 5, we get 3, 5, 6 and 9."
	@echo "    The sum of these multiples is 23."
	@echo ""
	@echo "    Find the sum of all the multiples of 3 or 5 below 1000."
	@echo ""
	@echo "    https://projecteuler.net/problem=1"
	@echo ""
	@echo "    To build and run a particular language, type:"
	@echo "    make [language]"
	@echo ""
	@echo "  Available languages:"
	@for i in $(LANGUAGES); \
	do \
		echo "    $$i"; \
	done

all: cpp python csharp nasm

cpp:
	@echo "===================================================================="
	@echo "Compiling C++"
	@echo "  Folder:     ./$(CPPDIR)"
	@echo "  Executable: ./$(CPPEXEC)"
	@echo ""
	@echo "-Building-"
	@$(MAKE) --no-print-directory $(CPPEXEC)
	@echo "--------------------------------------------------------------------"
	@echo "Answer:"
	@$(CPPEXEC)

python:
	@echo "===================================================================="
	@echo "Compiling Python"
	@echo "  Folder:     ./$(PYDIR)"
	@echo "  Executable: ./$(PYEXEC)"
	@echo ""
	@echo "-Building-"
	@$(MAKE) --no-print-directory $(PYEXEC)
	@echo "--------------------------------------------------------------------"
	@echo "Answer:"
	@$(PY) $(PYEXEC)

csharp:
	@echo "===================================================================="
	@echo "Compiling C#"
	@echo "  Folder:     ./$(CSDIR)"
	@echo "  Executable: ./$(CSEXEC)"
	@echo ""
	@echo "-Building-"
	@$(MAKE) --no-print-directory $(CSEXEC)
	@echo "--------------------------------------------------------------------"
	@echo "Answer:"
	@$(CSEXEC)

nasm:
	@echo "===================================================================="
	@echo "Compiling NASM"
	@echo "  Folder:     ./$(NASMDIR)"
	@echo "  Executable: ./$(NASMEXEC)"
	@echo ""
	@echo "-Building-"
	@$(MAKE) --no-print-directory $(NASMEXEC)
	@echo "--------------------------------------------------------------------"
	@echo "Answer:"
	@$(NASMEXEC)

clean:
	@echo "===================================================================="
	@echo "Cleaning Directories"
	@for i in $(CLEANDIRS); \
	do \
		echo "  $$i"; \
		rm -f $$i; \
	done

#######
# C++ #
#######
$(CPPEXEC): $(CPPOBJ)
	@echo ""
	@echo "-Output-"
	@echo "  $@"
	@$(CC) -o $@ $<

$(CPPDIR)/%.o: $(CPPDIR)/%.cpp
	@echo "  CC $<"
	@$(CC) -o $@ -c $<

##########
# Python #
##########
$(PYDIR)/%.pyc: $(PYDIR)/%.py
	@echo "  PYC $<"
	@$(PYC) $<

######
# C# #
######
$(CSEXEC): $(CSOBJ)
	@echo "  $@"
	@cd $(CSDIR); $(CS) //nologo /reference:System.Core.dll /out:"$(CSTARG)" \
	"$(CSNAME)"

########
# NASM #
########
$(NASMEXEC): $(NASMOBJ)
	@echo ""
	@echo "-Output-"
	@echo "  $@"
	@$(CC) -o $@ $<

$(NASMDIR)/%.obj: $(NASMDIR)/%.asm
	@echo "  NASM $<"
	@$(NASM) $<

.PHONY: all python cpp csharp nasm clean
