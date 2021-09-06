Qt5 Example project
===================

Tested for macOS 11.5.2, iOS and Android.

    cd cmake-build-release
    conan install .. -pr:b default -pr:h <profile>
    conan build .. -bf . -sf ..

For Android an additional step is required:

    cmake --build . --target aab