# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.22

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /opt/cmake/bin/cmake

# The command to remove a file.
RM = /opt/cmake/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/user/uvk

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/user/uvk/build/all/app

# Utility rule file for uvk_FILES.

# Include any custom commands dependencies for this target.
include CMakeFiles/uvk_FILES.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/uvk_FILES.dir/progress.make

uvk_FILES: CMakeFiles/uvk_FILES.dir/build.make
.PHONY : uvk_FILES

# Rule to build all files generated by this target.
CMakeFiles/uvk_FILES.dir/build: uvk_FILES
.PHONY : CMakeFiles/uvk_FILES.dir/build

CMakeFiles/uvk_FILES.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/uvk_FILES.dir/cmake_clean.cmake
.PHONY : CMakeFiles/uvk_FILES.dir/clean

CMakeFiles/uvk_FILES.dir/depend:
	cd /home/user/uvk/build/all/app && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/user/uvk /home/user/uvk /home/user/uvk/build/all/app /home/user/uvk/build/all/app /home/user/uvk/build/all/app/CMakeFiles/uvk_FILES.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/uvk_FILES.dir/depend

