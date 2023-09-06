SRC_DIR := manifests
BUILD_DIR := build
SRCS = $(wildcard $(SRC_DIR)/*.mnfs)
BINS = $(patsubst $(SRC_DIR)/%.mnfs,$(BUILD_DIR)/%.mnfb,$(SRCS))
SRCS_UNTESTED = $(wildcard $(SRC_DIR)/CLICKS_UNTESTED/*.mnfs)
BINS_UNTESTED = $(patsubst $(SRC_DIR)/CLICKS_UNTESTED/%.mnfs,$(BUILD_DIR)/untested/%.mnfb,$(SRCS))

all: $(BINS) $(UNTESTED_BINS)

# usage: manifesto [-h] [-I {mnfs,mnfb}] [-o OUT] [-O {mnfs,mnfb}] [-s] infile
$(BINS): $(BUILD_DIR)/%.mnfb : $(SRC_DIR)/%.mnfs
	mkdir -p $(dir $@)
	./manifesto/manifesto -I mnfs -O mnfb -o $@ $<

install:
	mkdir -p $(DESTDIR)/usr/bin
	install -m 0755 ./manifesto/manifesto $(DESTDIR)/usr/bin/
	mkdir -p $(DESTDIR)/lib/firmware/mikrobus
	install -m 0644 $(BUILD_DIR)/*.mnfb $(DESTDIR)/lib/firmware/mikrobus
	mkdir -p $(DESTDIR)/lib/firmware/mikrobus/untested
	install -m 0644 $(BUILD_DIR)/untested/*.mnfb $(DESTDIR)/lib/firmware/mikrobus/untested

PHONY: clean
clean:
	rm -r $(BUILD_DIR) || true
