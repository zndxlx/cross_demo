cmake_minimum_required (VERSION 3.6)

set(CMAKE_INSTALL_PREFIX "${CMAKE_BINARY_DIR}" CACHE PATH "Installation directory" FORCE)
message(STATUS "CMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}")

add_subdirectory(common common)
add_subdirectory(app app)
add_subdirectory(xlog xlog)


project (cross)

#include(comm/CMakeUtils.txt)

#include_directories(.)
#include_directories(..)

#set(SELF_LIBS_OUT ${CMAKE_SYSTEM_NAME}.out)

if(ANDROID)

elseif(APPLE)

endif()





