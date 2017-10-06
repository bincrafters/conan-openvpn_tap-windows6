from conans import ConanFile, tools, os

class OpenVPNTapWindows6Conan(ConanFile):
    name = "openvpn_tap-windows-6"
    version = "20171006" 
    description = "An NDIS 6 implementation of the TAP-Windows driver, used by OpenVPN and other apps. "
    license = "https://github.com/OpenVPN/tap-windows6/blob/master/COPYING"
    url = "https://github.com/bincrafters/conan-libtins"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=True"
    lib_short_name = "tap-windows6"
           
    def source(self):
        source_url = "https://github.com/OpenVPN/tap-windows6"
        self.run("git clone --recursive --depth=1 --branch=develop {0}.git".format(source_url))

    def build(self):
        self.run("python buildtap.py -b -s {0}".format(self.lib_short_name))

    def package(self):
        self.copy("LICENSE", dst=".", keep_path=False)
        self.copy("*.h", dst="include", src=os.path.join(self.name, "include"))
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so*", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)
        self.copy("*.lib", dst="lib", keep_path=False)
            
    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
