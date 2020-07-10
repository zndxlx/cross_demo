cmake_minimum_required (VERSION 3.6)

set(CMAKE_INSTALL_PREFIX "${CMAKE_BINARY_DIR}" CACHE PATH "Installation directory" FORCE)
message(STATUS "CMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}")

project (common)

include(../CMakeUtils.txt)
include(../CMakeExtraFlags.txt)

include_directories(.)


file(GLOB SELF_TEMP_SRC_FILES RELATIVE ${PROJECT_SOURCE_DIR} *.cc *.h)
list(APPEND SELF_SRC_FILES ${SELF_TEMP_SRC_FILES})
source_group(src FILES ${SELF_SRC_FILES})



add_library(${PROJECT_NAME} STATIC ${SELF_SRC_FILES})

install(TARGETS ${PROJECT_NAME} ARCHIVE DESTINATION ${CMAKE_SYSTEM_NAME}.out)
