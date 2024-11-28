from conan import ConanFile
from conan.tools.files import copy
import os

class Stm32HALConan(ConanFile):
    name = "stm32-hal"
    version = "1.0"
    license = "MIT"
    description = "STM32 HAL library"
    topics = ("STM32", "HAL", "Embedded", "Microcontroller")
    settings = "os", "arch", "compiler", "build_type"
    exports_sources = "*"

    def package(self):
        copy(self, "*.h", src=os.path.join("drivers", "STM32L4xx_HAL_Driver", "Inc"), dst=os.path.join(self.package_folder, "include"))
        copy(self, "*.h", src=os.path.join("drivers", "CISM", "Inc"), dst=os.path.join(self.package_folder, "include"))
        copy(self, "*.c", src=os.path.join("drivers", "STM32L4xx_HAL_Driver", "Src"), dst=os.path.join(self.package_folder, "src"))
        copy(self, "*.c", src=os.path.join("drivers", "CISM", "Src"), dst=os.path.join(self.package_folder, "src"))

    def package_info(self):
        self.cpp_info.includedirs = ["include"]
        self.cpp_info.libdirs = ["lib"]
        self.cpp_info.srcdirs = ["src"]