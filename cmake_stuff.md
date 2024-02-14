#### Variables:
`set(CMAKE_TRY_COMPILE_TARGET_TYPE "STATIC_LIBRARY")`  
#### Cmake with toolchain
`cmake -DCMAKE_TOOLCHAIN_FILE=../cmake-modules/gcc-arm-toolchain.cmake ..`  
#### Add multiple include paths
```
set(MYLIB_INCLUDE_DIR
    ${mylib_src_dir}/src/ses-proxy-srv/inc
    ${mylib_src_dir}/src/ses-route-srv/inc
    ${mylib_src_dir}/src/ses-tsn-api-srv/inc
    ${mylib_src_dir}/src/smp-stk/inc
    ${mylib_src_dir}/src/tsn-model-srv/inc
)

set_target_properties(mylib_lib PROPERTIES INTERFACE_INCLUDE_DIRECTORIES "${MYLIB_INCLUDE_DIR}")
```

