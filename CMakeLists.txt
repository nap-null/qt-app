cmake_minimum_required(VERSION 3.20)

set(CMAKE_CXX_STANDARD 17)

set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOUIC ON)

if(IOS)
    add_definitions(-DIOS)
endif()

if(ANDROID)
    set(ANDROID_PACKAGE_SOURCE_DIR "${CMAKE_SOURCE_DIR}/android")
endif()


project(qt5example LANGUAGES CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)

set(basic_setup_args KEEP_RPATHS)

if(ANDROID)
    set(basic_setup_args ${basic_setup_args} NO_OUTPUT_DIRS)
endif()

conan_basic_setup(${basic_setup_args})

find_package(
    Qt5
        COMPONENTS
            Core
            Widgets
            Qml
            Quick
            QuickControls2
            QuickTemplates2
            QmlWorkerScript
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
    add_executable(${PROJECT_NAME})

    add_definitions(-DBUILD_STATIC)
endif()

set(SOURCES qml/main.qml)

qt5_add_resources(SOURCES qml.qrc)

target_sources(${PROJECT_NAME} PUBLIC main.cpp ${SOURCES})

target_link_libraries(
    ${PROJECT_NAME}
        Qt5::Widgets
        Qt5::Qml
        Qt5::QmlModels
        Qt5::QmlWorkerScript
        Qt5::QuickTemplates2
        Qt5::QuickControls2
        Qt5::Quick
        Qt5::Gui
        Qt5::Core
        Qt5::Network
)

if(NOT ANDROID)
    target_link_libraries(
        ${PROJECT_NAME}
            qtquick2plugin
            qmlplugin
            qtquickcontrols2plugin
            modelsplugin
            workerscriptplugin
            labsmodelsplugin
            qquicklayoutsplugin
            windowplugin
            qtquicktemplates2plugin
    )
endif()

target_link_directories(
    ${PROJECT_NAME}
        PRIVATE
            ${CONAN_QT_ROOT}/plugins/platforms
            ${CONAN_QT_ROOT}/qml/QtQml
            ${CONAN_QT_ROOT}/qml/QtQuick.2
            ${CONAN_QT_ROOT}/qml/QtQml/Models.2
            ${CONAN_QT_ROOT}/qml/QtQml/WorkerScript.2
            ${CONAN_QT_ROOT}/qml/QtQuick/Controls.2
            ${CONAN_QT_ROOT}/qml/QtQuick/Window.2
            ${CONAN_QT_ROOT}/qml/QtQuick/Layouts
            ${CONAN_QT_ROOT}/qml/QtQuick/Templates.2
            ${CONAN_QT_ROOT}/qml/Qt/labs/qmlmodels
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