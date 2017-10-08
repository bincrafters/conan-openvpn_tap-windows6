# tap-windows6 is an NDIS 6 implementation of the TAP-Windows driver, used by OpenVPN and other apps.

[Conan.io](https://conan.io) package for [openvpn_tap-windows6](https://github.com/OpenVPN/tap-windows6) project

The packages generated with this **conanfile** can be found in [Bintray](https://bintray.com/bincrafters/public-conan/openvpn_tap-windows6%3Abincrafters).

## Conan "latest" version convention

This project has not adopted semantic versioning, so this package offers a versioning strategy on the packages by using a "conan alias" named "latest". 

[Conan Alias feature Explained](http://conanio.readthedocs.io/en/latest/reference/commands/alias.html?highlight=conan%20alias)

In summary, users can reference the version of "latest" in their requirements as shown in the example below to get the latest release of this package.  "latest" is just an alias which redirects to an actual version of the package with a number. In lieu of a semantic version number, a datestamp will be used as the version number on the concrete Bincrafters packages and the `source()` method of each version of the recipe will use the latest commit on the master branch of the target project, as of that date. 

## For Users: Use this packages

### Basic setup

    $ conan install tap-windows6openvpn_tap-windows6/latest@bincrafters/stable

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    tap-windows6/latest@bincrafters/stable

    [generators]
    txt

Complete the installation of requirements for your project running:

    $ mkdir build && cd build && conan install ..
	
Note: It is recommended that you run conan install from a build directory and not the root of the project directory.  This is because conan generates *conanbuildinfo* files specific to a single build configuration which by default comes from an autodetected default profile located in ~/.conan/profiles/default .  If you pass different build configuration options to conan install, it will generate different *conanbuildinfo* files.  Thus, they should not be added to the root of the project, nor committed to git. 

## For Packagers: Publish this Package

The example below shows the commands used to publish to bincrafters conan repository. To publish to your own conan respository (for example, after forking this git repository), you will need to change the commands below accordingly. 

## Build  

This is a header only library, so nothing needs to be built.

## Package 

    $ conan create bincrafters/stable
	
## Add Remote

	$ conan remote add bincrafters "https://api.bintray.com/conan/bincrafters/public-conan"

## Upload
	
To upload a package with an alias involved, it's a three-step process. 

The first step is standard, upload the concrete package you've recently built:

    $ conan upload openvpn_tap-windows6/latest@bincrafters/stable --all -r bincrafters

The second step is to create or update the "alias package" on your local machine:

	$ conan alias openvpn_tap-windows6/latest@bincrafters/stable tap-windows6/20171006@bincrafters/stable

The third step is to upload the alias package:

	$conan upload openvpn_tap-windows6/latest@bincrafters/stable --all -r bincrafters
	
	
### License
[GPL-2.0](https://github.com/OpenVPN/tap-windows6/blob/master/COPYING)