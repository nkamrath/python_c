cmake_minimum_required(VERSION 3.12	)

project(test)

#gather all the c++ files for library compilation
file(GLOB SOURCES src/*.cpp)

#add the c++ code as  library to be compiled for usage with python
add_library(test SHARED ${SOURCES})

#ensure the file suffix is .so to be cross-platform
set_target_properties(test PROPERTIES SUFFIX ".so")

#copy the python script from the src dir to the build dir
configure_file("${CMAKE_CURRENT_SOURCE_DIR}/src/test.py" "${CMAKE_CURRENT_BINARY_DIR}/test.py" COPYONLY)

ADD_CUSTOM_TARGET(run
  COMMAND make
  COMMAND python test.py)
