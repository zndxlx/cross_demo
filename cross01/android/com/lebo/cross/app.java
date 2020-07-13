
    package com.lebo.cross;
    
    public class app {

      static {
          System.loadLibrary("app");
      }   

      public native String hello();
    }