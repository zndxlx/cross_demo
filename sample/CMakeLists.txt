cmake_minimum_required (VERSION 3.6)

project(sample)
include(./CMakeUtils.txt)
#include_directories(.)
#include_directories(./third)
include_directories(${PROJECT_SOURCE_DIR}/third)

file(GLOB SELF_TEMP_SRC_FILES RELATIVE ${PROJECT_SOURCE_DIR}  src/*.cc src/*.h)

message(STATUS "PROJECT_SOURCE_DIR=${PROJECT_SOURCE_DIR}")
message(STATUS "SELF_TEMP_SRC_FILES=${SELF_TEMP_SRC_FILES}")

list(APPEND SELF_SRC_FILES ${SELF_TEMP_SRC_FILES})

link_directories(${PROJECT_SOURCE_DIR}/third/cross)

add_executable(${PROJECT_NAME} ${SELF_SRC_FILES})


target_link_libraries(${PROJECT_NAME} cross01)
