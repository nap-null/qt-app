if(ANDROID)
    qt_add_library(${PROJECT_NAME} SHARED)
else()
    qt_add_executable(${PROJECT_NAME} main.cpp)
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

include(cmake/ios.cmake)