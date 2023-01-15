Qt Example project
===================

Tested for macOS 12.3 on MacBook Air M1, for Ubuntu 20.04 and Windows 11.

    mkdir build
    cd build
    conan install ..
    conan build ..

For Android an additional step is required:

    cmake --build .. --target aab
