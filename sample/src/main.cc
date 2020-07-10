#include <iostream>
#include "cross/app/app_logic.h"
#include "cross/common/common.h"
#include "cross/xlog/xlog.h"

using namespace std;
int main(){
    std::cout << "test" << std::endl;  
    cross::app::testApp();
    cross::common::testCommon();
    cross::xlog::testXlog();
}