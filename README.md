Qt Example project
===================

Tested for macOS 12.3 on MacBook Air M1.

    mkdir build
    cd build
    conan install .. -pr:b <build-profile> -pr:h <host-profile>
    conan build ..

For Android an additional step is required:

    cmake --build .. --target aab