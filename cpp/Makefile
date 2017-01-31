#
BIN_NAME := main 
CC := g++
X_FLAGS := -Wall -std=c++11


#Includes
INCDIRS := 
INCDIRS_TEST := -I/usr/local/Cellar/gtest/1.7.0/include

# Library
LD_FLAGS := 
LD_FLAGS_TEST := -L/usr/local/Cellar/gtest/1.7.0/lib -lgtest -lgtest_main -lpthread

CC_FLAGS := $(X_FLAGS) $(INCDIRS) $(LD_FLAGS)
CC_FLAGS_TEST := $(X_FLAGS) -g $(INCDIRS_TEST) $(LD_FLAGS_TEST)

# list of test drivers
TESTSOURCES := $(wildcard test/test*.cpp)
# names of test executables

CFILES := $(shell find src -mindepth 1 -maxdepth 4 -name "*.c")
CXXFILES := $(shell find src -mindepth 1 -maxdepth 4 -name "*.cpp")


INFILES := $(CFILES) $(CXXFILES)

OBJFILES := $(CXXFILES:src/%.cpp=%) $(CFILES:src/%.c=%)
DEPFILES := $(CXXFILES:src/%.cpp=%) $(CFILES:src/%.c=%)
OFILES := $(OBJFILES:%=obj/%.o)
TESTFILES := $(TESTSOURCES:test/%.cpp=%)
OTESTFILES := $(OFILES) $(TESTFILES:%=obj/test/%.o)
OTESTFILES := $(filter-out obj/main.o, $(OTESTFILES))

release: CC_FLAGS += -O3 -DNDEBUG
release: all

debug: CC_FLAGS += -g3 -DDEBUG
debug: clean all

profile: CC_FLAGS += -pg
profile: clean all

all: $(BIN_NAME)

testAll: $(OTESTFILES)
	$(CC) $(CC_FLAGS_TEST) -o testAll $(OTESTFILES) 

$(BIN_NAME): $(OFILES)
	$(CC) $(CC_FLAGS) -o $(BIN_NAME) $(OFILES) 

obj/test/%.o: test/%.cpp
	@if [ ! -d `dirname $@` ]; then mkdir -p `dirname $@`; fi
	$(CC) -c $(CC_FLAGS_TEST) $< -o $@

obj/%.o: src/%.cpp
	@if [ ! -d `dirname $@` ]; then mkdir -p `dirname $@`; fi
	$(CC) -c $(CC_FLAGS) $< -o $@

run:
	./$(BIN_NAME)

clean:
	@rm -rf $(BIN_NAME) obj/* testAll
