cmake_minimum_required(VERSION 3.20)

set(CMAKE_CXX_STANDARD 17)

set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOUIC ON)

if(ANDROID)
    set(ANDROID_PACKAGE_SOURCE_DIR "${CMAKE_SOURCE_DIR}/android")
endif()

project(qt-app LANGUAGES CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)

set(basic_setup_args KEEP_RPATHS)

if(ANDROID)
    set(basic_setup_args ${basic_setup_args} NO_OUTPUT_DIRS)
endif()

conan_basic_setup(${basic_setup_args})

find_package(
    Qt6
        COMPONENTS
            Core
            Gui
            Qml
            Quick
            QuickControls2
        REQUIRED
)

if(ANDROID)
    add_library(${PROJECT_NAME} SHARED)
    set_property(
        TARGET
            ${PROJECT_NAME}
        PROPERTY
            LIBRARY_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/android-build/libs/${ANDROID_ABI}"
    )
else()
    qt_add_executable(${PROJECT_NAME} main.cpp)

    if(WIN32)
        target_link_options(${PROJECT_NAME} PRIVATE "/SUBSYSTEM:WINDOWS" "/ENTRY:mainCRTStartup")
    endif()
endif()

qt_add_qml_module(
    ${PROJECT_NAME}
        URI qt_app
        VERSION 1.0
        QML_FILES
            qml/main.qml
)

target_link_libraries(
    ${PROJECT_NAME}
        PUBLIC
            Qt6::Core
            Qt6::Gui
            Qt6::Qml
            Qt6::Quick
            Qt6::QuickControls2
)

if(IOS)
    if(IS_CI_BUILD)
        set_property(TARGET ${PROJECT_NAME} PROPERTY XCODE_ATTRIBUTE_CODE_SIGN_IDENTITY "Sign identity")
        set_property(TARGET ${PROJECT_NAME} PROPERTY XCODE_ATTRIBUTE_DEVELOPMENT_TEAM "TeamID")
        set_property(TARGET ${PROJECT_NAME} PROPERTY XCODE_ATTRIBUTE_CODE_SIGNING_ALLOWED "NO")
    endif()

    set_property(TARGET ${PROJECT_NAME} APPEND_STRING PROPERTY LINK_FLAGS " -Wl,-e,_qt_main_wrapper")

    set_target_properties(
        ${PROJECT_NAME}
            PROPERTIES
                MACOSX_BUNDLE TRUE
                MACOSX_BUNDLE_INFO_PLIST "${CMAKE_CURRENT_LIST_DIR}/ios/Info.plist"
                XCODE_ATTRIBUTE_ENABLE_BITCODE "NO"
                XCODE_ATTRIBUTE_COMBINE_HIDPI_IMAGES FALSE
                XCODE_ATTRIBUTE_TARGETED_DEVICE_FAMILY "1,2"
                XCODE_ATTRIBUTE_ASSETCATALOG_COMPILER_APPICON_NAME "AppIcon"
    )
endif()
