# Automate the installation of anki using a makefile
# To invoke it
# make -f <file_name> <target>

# Determine this makefile's path.
# Be sure to place this BEFORE `include` directives, if any.
THIS_FILE := $(lastword $(MAKEFILE_LIST))

PROGRAM := anki
SOFTWARE_DIR := ${HOME}/software
ZIP_DIR := ${SOFTWARE_DIR}/zipped/${PROGRAM}
UNZIP_DIR := ${SOFTWARE_DIR}/unZipped/${PROGRAM}

VERSION := 2.1.66
TAG := anki-$(VERSION)-linux-qt5
FILE_NAME := $(TAG).tar.zst
URL := https://github.com/ankitects/anki/releases/download/${VERSION}/${FILE_NAME}

ZIP_FILE_PATH := ${ZIP_DIR}/${FILE_NAME}
UNZIP_TAG_DIR := ${UNZIP_DIR}/${TAG}

install:
	$(MAKE) -f $(THIS_FILE) uninstall
	mkdir -p ${ZIP_DIR}
ifeq ($(wildcard ${ZIP_FILE_PATH}),)
	@echo "downloading ${FILE_NAME}"
	curl -L -O ${URL} --output-dir ${ZIP_DIR}
else
	@echo "${ZIP_FILE_PATH} exists. Skipping download."
endif
	mkdir -p ${UNZIP_DIR}
ifeq ($(wildcard ${UNZIP_TAG_DIR}),)
	@echo "unzipping to ${UNZIP_TAG_DIR}"
	tar xaf ${ZIP_FILE_PATH} -C ${UNZIP_DIR}
else
	@echo "${UNZIP_TAG_DIR} exists. Skipping unzipping step."
endif
	# The install script requires to be run from the directory it is in.
	cd ${UNZIP_TAG_DIR} && sudo ./install.sh

uninstall:
ifneq ($(wildcard /usr/local/share/anki/uninstall.sh),)
	sudo /usr/local/share/anki/uninstall.sh
endif

clean:
	rm -f ${ZIP_FILE_PATH}
	rm -rf ${UNZIP_TAG_DIR}

.PHONY: install uninstall clean

# Notes:
# * I was initially thinking of doing this by a shell script. Then I saw
#   https://github.com/trimclain/.dotfiles/blob/main/arch.mk which does this by
#   using a makefile. 'make' is the correct tool for this job.
# * Anki documentation recommends to call the uninstall script before
#   installing a new version. Initially, I tried invoking the 'uninstall'
#   target by doing
#
# install:
# 	unintstall
#
#   but this was invoking the executable '/opt/rajulocal/Jts/uninstall' which
#   is not what I want. I then followed the instructions in
#   https://stackoverflow.com/questions/5377297/how-to-manually-call-another-target-from-a-make-target
#   to call a local target from another target.
