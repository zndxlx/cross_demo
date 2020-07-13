#!/usr/bin/env python
# -*- coding=utf-8 -*-
import os
import shutil
import time
import subprocess


COMM_COPY_HEADER_FILES = {
            "cross01/app/app_logic.h": "app",
            "cross01/common/common.h": "common",
            }        


WIN_COPY_EXT_FILES = {
            "cross01/xlog/xlog.h": "xlog"
}
  

def libtool_libs(src_libs, dst_lib):
    src_lib_str = ''
    for l in src_libs:
        src_lib_str = '%s %s'%(src_lib_str, l)

    print(src_lib_str)
    ret = os.system('libtool -static -o %s %s' %(dst_lib, src_lib_str))
    if ret != 0:
        print('!!!!!!!!!!!libtool %s fail!!!!!!!!!!!!!!!' %(dst_lib))
        return False

    return True

def lipo_libs(src_libs, dst_lib):
    src_lib_str = u''
    for l in src_libs:
        src_lib_str = '%s %s'%(src_lib_str, l)

    cmd = 'lipo -create %s -output %s' %(src_lib_str, dst_lib)
    ret = os.system(cmd)
    if ret != 0:
        print('!!!!!!!!!!!lipo_libs %s fail, cmd:%s!!!!!!!!!!!!!!!' %(dst_lib, cmd))
        return False

    return True

def lipo_thin_libs(src_lib, dst_lib, archs):

    tmp_results = []
    for arch in archs:
        if len(archs) == 1:
            tmp_result = dst_lib
        else:
            tmp_result = dst_lib + '.' + arch

        cmd = 'lipo %s -thin %s -output %s' %(src_lib, arch, tmp_result)
        ret = os.system(cmd)
        if ret != 0:
            print('!!!!!!!!!!!lipo_thin_libs %s fail, cmd:%s!!!!!!!!!!!!!!!' %(tmp_result, cmd))
            return False
        tmp_results.append(tmp_result)

    if len(archs) == 1:
        return True
    else:
        return lipo_libs(tmp_results, dst_lib)

GENERATE_DSYM_FILE_CMD = 'dsymutil %s -o %s'
def gen_dwarf_with_dsym(src_dylib, dst_dsym):
    os.system(GENERATE_DSYM_FILE_CMD %(src_dylib, dst_dsym))

def remove_cmake_files(path):
    cmake_files = path + '/CMakeFiles'
    if os.path.exists(cmake_files):
        shutil.rmtree(cmake_files)

    make_files = path + '/Makefile'
    if os.path.isfile(make_files):
        os.remove(make_files)

    cmake_cache = path + '/CMakeCache.txt'
    if os.path.isfile(cmake_cache):
        os.remove(cmake_cache)

    for f in glob.glob(path + '/*.a'):
        os.remove(f)
    for f in glob.glob(path + '/*.so'):
        os.remove(f)


def clean(path, incremental=False):
    if not incremental:
        for fpath, dirs, fs in os.walk(path):
            remove_cmake_files(fpath)

    if not os.path.exists(path):
        os.makedirs(path)

#目录清理，incremental表示是否删除里面的文件
#如果目录不存在会去创建该目录
def clean_windows(path, incremental):
    if not os.path.exists(path):
        os.makedirs(path)
        return
    
    if incremental:
        return;
    
    try:
        if os.path.exists(path):
            shutil.rmtree(path)
            if not os.path.exists(path):
                os.makedirs(path)
    except Exception:
        pass
        
def copy_windows_pdb(cmake_out, sub_folder, config, dst_folder):
    for sf in sub_folder:
        src_file = "%s/%s/" %(cmake_out, sf)
        dirs = glob.glob(src_file + "*.dir")
        if len(dirs) != 1:
            print("Warning: %s path error." %src_file)
            continue
        
        src_file = "%s/%s" %(dirs[0], config)
        pdbs = glob.glob(src_file + "/*.pdb")
        if len(pdbs) != 1:
            print("Warning: %s path error." %src_file)
            continue
        pdb = pdbs[0]
        if os.path.isfile(pdb):
            shutil.copy(pdb, dst_folder)
        else:
            print("%s not exists" %pdb)

def copy_file(src, dst):
    if not os.path.isfile(src):
        print('Warning: %s not exist' %(src))
        return;

    if dst.rfind("/") != -1 and not os.path.exists(dst[:dst.rfind("/")]):
        os.makedirs(dst[:dst.rfind("/")])

    shutil.copy(src, dst)

def copy_file_mapping(header_file_mappings, header_files_src_base, header_files_dst_end):
    for (src, dst) in header_file_mappings.items():
        copy_file(header_files_src_base + src, header_files_dst_end + "/" + dst + '/' + src[src.rfind("/"):])



def make_static_framework(src_lib, dst_framework, header_file_mappings, header_files_src_base='./'):
    if os.path.exists(dst_framework):
        shutil.rmtree(dst_framework)

    os.makedirs(dst_framework)
    shutil.copy(src_lib, dst_framework)

    framework_path = dst_framework + '/Headers'  
    for (src, dst) in header_file_mappings.items():
        copy_file(header_files_src_base + src, framework_path + "/" + dst + '/' + src[src.rfind("/"):])

    return True

def parse_as_git(path):
    curdir = os.getcwd()
    os.chdir(path)
    revision = os.popen('git rev-parse --short HEAD').read().strip()
    path = os.popen('git rev-parse --abbrev-ref HEAD').read().strip()
    url = ''
    os.chdir(curdir)

    return revision, path, url




import glob
if __name__ == '__main__':
    lipo_thin_libs(u'/Users/garry/Documents/gitcode/mmnet/mars/openssl/openssl_lib_iOS/libcrypto.a', u'/Users/garry/Documents/gitcode/mmnet/mars/openssl/openssl_lib_iOS/libcrypto_test.a', ['x86_64', 'arm64'])
