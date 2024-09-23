SRC_DIR := ../clicks
BUILD_DIR := build
SRCS := $(wildcard $(SRC_DIR)/**/**/*.mnfs)  
BINS := $(patsubst %.mnfs, $(BUILD_DIR)/%.mnfb, $(notdir $(SRCS)))  

$(BUILD_DIR)/%.mnfb: $(SRC_DIR)/**/**/%.mnfs
	mkdir -p $(dir $@)
	./manifesto -I mnfs -O mnfb -o $@ $<

all: $(BINS)

install:
	mkdir -p $(DESTDIR)/lib/firmware/mikrobus
	install -m 0644 $(BUILD_DIR)/*.mnfb $(DESTDIR)/lib/firmware/mikrobus

PHONY: clean
clean:
	rm -r $(BUILD_DIR) || true


