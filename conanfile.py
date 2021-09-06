from conans import ConanFile, CMake, tools, __version__ as conan_version

assert conan_version >= tools.Version('1.35'), 'Conan version is too old.'


class Qt5ExampleConan(ConanFile):
    name = 'qt5example'
    version = '0.0.0'
    generators = 'cmake'

    settings = "os", "arch", "compiler", "build_type"

    exports_sources = (
        'CMakeLists.txt',
        'main.cpp',
        'qml/main.qml',
        'qml.qrc'
    )

    requires = 'qt/5.15.2@nap/devel'

    options = {
        'ci_build': [False, True],
    }

    default_options = {
        'ci_build': False
    }

    def build(self):
        self.cmake.build()

    def package(self):
        self.cmake.install()

    @property
    def cmake(self):
        generator = 'Xcode' if self.settings.os == 'iOS' else 'Ninja'
        cmake = CMake(self, generator=generator)
        # cmake.definitions['CMAKE_FIND_DEBUG_MODE'] = True
        cmake.definitions['CMAKE_FIND_ROOT_PATH_MODE_PACKAGE'] = 'BOTH'
        cmake.definitions['CMAKE_FIND_ROOT_PATH_MODE_INCLUDE'] = 'BOTH'
        cmake.definitions['CMAKE_FIND_ROOT_PATH_MODE_LIBRARY'] = 'BOTH'
        cmake.definitions['CONAN_DISABLE_CHECK_COMPILER'] = True

        cmake.definitions['CMAKE_SYSTEM_NAME'] = self.cmake_system_name

        if self.settings.os == 'Android':
            cmake.definitions['ANDROID'] = True
            cmake.definitions['ANDROID_SDK'] = '/Users/user/Library/Android/sdk'
            cmake.definitions['ANDROID_ABI'] = 'arm64-v8a'
        elif self.settings.os == 'iOS':
            cmake.definitions['iOS'] = True

        if self.options.ci_build:
            cmake.definitions['IS_CI_BUILD'] = True

        cmake.configure()

        return cmake

    @property
    def cmake_system_name(self):
        if self.settings.os == 'Macos':
            return 'Darwin'
        return self.settings.os
