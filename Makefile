SRC_DIR := manifests
BUILD_DIR := build
SRCS = $(wildcard $(SRC_DIR)/*.mnfs)
BINS = $(patsubst $(SRC_DIR)/%.mnfs,$(BUILD_DIR)/%.mnfb,$(SRCS))

all: $(BINS)

# usage: manifesto [-h] [-I {mnfs,mnfb}] [-o OUT] [-O {mnfs,mnfb}] [-s] infile
$(BINS): $(BUILD_DIR)/%.mnfb : $(SRC_DIR)/%.mnfs
	mkdir -p $(dir $@)
	./manifesto -I mnfs -O mnfb -o $@ $<

install:
	mkdir -p $(DESTDIR)/usr/bin
	install -m 0755 ./manifesto $(DESTDIR)/usr/bin/
	mkdir -p $(DESTDIR)/lib/firmware/mikrobus
	install -m 0644 $(BUILD_DIR)/*.mnfb $(DESTDIR)/lib/firmware/mikrobus

PHONY: clean
clean:
	rm -r $(BUILD_DIR) || true
