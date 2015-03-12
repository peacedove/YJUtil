#
BIN_NAME := main 
CC = g++
CC_FLAGS = -Wall -std=c++11 -g -I/usr/local/include/libfreenect -I/usr/local/include/libusb-1.0 -I/usr/local/include/opencv -L/usr/local/Cellar/libfreenect/0.5.0/lib -lfreenect `pkg-config --libs opencv` -lopencvblobslib


CFILES := $(shell find src -mindepth 1 -maxdepth 4 -name "*.c")
CXXFILES := $(shell find src -mindepth 1 -maxdepth 4 -name "*.cpp")
 
INFILES := $(CFILES) $(CXXFILES)

OBJFILES := $(CXXFILES:src/%.cpp=%) $(CFILES:src/%.c=%)
DEPFILES := $(CXXFILES:src/%.cpp=%) $(CFILES:src/%.c=%)
OFILES := $(OBJFILES:%=obj/%.o)

all: $(BIN_NAME)

$(BIN_NAME): $(OFILES)
	$(CC) $(CC_FLAGS) -o $(BIN_NAME) $(OFILES) $(LINK_FLAGS)

obj/%.o: src/%.cpp
	@if [ ! -d `dirname $@` ]; then mkdir -p `dirname $@`; fi
	$(CC) -c $(CC_FLAGS) $< -o $@

run:
	./$(BIN_NAME)

clean:
	@rm -rf $(BIN_NAME) obj/*
