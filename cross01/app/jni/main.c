
#include <string.h>
#include <jni.h>


JNIEXPORT jstring JNICALL
Java_com_lebo_cross_app_hello( JNIEnv* env, jobject thiz )
{
    return (*env)->NewStringUTF(env, "Hello from JNI !  Compiled with ABI ");
}
