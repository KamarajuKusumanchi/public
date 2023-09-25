# Automate the installation of anki using a makefile
# To invoke it
# make -f <file_name> <target>

# Determine this makefile's path.
# Be sure to place this BEFORE `include` directives, if any.
THIS_FILE := $(lastword $(MAKEFILE_LIST))

PROGRAM := anki
SOFTWARE_DIR := ${HOME}/software
ZIP_DIR := ${SOFTWARE_DIR}/zipped/${PROGRAM}

VERSION := 2.1.66
FILE_NAME := anki-$(VERSION)-linux-qt5.tar.zst
URL := https://github.com/ankitects/anki/releases/download/${VERSION}/${FILE_NAME}

ZIP_FILE_PATH := ${ZIP_DIR}/${FILE_NAME}

install:
	$(MAKE) -f $(THIS_FILE) uninstall
	mkdir -p ${ZIP_DIR}
	# cd ${ZIP_DIR}
ifeq ($(wildcard ${ZIP_FILE_PATH}),)
	@echo "downloading ${FILE_NAME}"
	curl -L -O ${URL} --output-dir ${ZIP_DIR}
else
	@echo "${ZIP_FILE_PATH} exists. Skipping download."
endif

uninstall:
ifneq ($(wildcard /usr/local/share/anki/uninstall.sh),)
	sudo /usr/local/share/anki/uninstall.sh
endif

.PHONY: install uninstall


# Notes:
# * I was initially thinking of doing this by a shell script. Then I saw
#   https://github.com/trimclain/.dotfiles/blob/main/arch.mk which does this by
#   using a makefile. 'make' is the correct tool for this job.
# * Anki documentation recommends to call the uninstall script before
#   installing a new version. Initially, I tried invoking the 'uninstall'
#   target by doing
# install:
# 	unintstall
#   but this was invoking the executable '/opt/rajulocal/Jts/uninstall' which
#   it not what I want. I then followed the instructions in
#   https://stackoverflow.com/questions/5377297/how-to-manually-call-another-target-from-a-make-target
#   which shows how to call a local target from another target.
