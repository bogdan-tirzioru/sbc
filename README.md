# STM32MP157 Single-Board Computer

This repository contains the hardware design and software experiments for a custom single-board computer based on the **STM32MP157C**. The project is a hands-on effort to build a first computer around an STMicroelectronics MPU, bring up embedded Linux, and learn the hardware and software layers involved.

The repository is experimental and combines the current STM32MP157 SBC work with earlier BeagleBone Black and Buildroot experiments. It is not yet a turnkey board support package or a production-ready design.

## Project goals

- Design a custom STM32MP157-based board with external DDR3L memory.
- Bring up the Cortex-A7 Linux system and boot chain.
- Explore the Cortex-M4 core and its interaction with Linux through remoteproc.
- Develop and document the hardware, device-tree configuration, and embedded Linux workflow.
- Keep earlier BeagleBone Black and Buildroot work as part of the learning history.

## Hardware at a glance

The current board files identify the design as an STM32MP157C custom board. The device trees describe **1 GiB of DDR3L** using the Micron MT41K512M16VRP-107 memory device. The repository also contains an Altium project and component references for the board.

These files are design work in progress. Their presence does not mean that every interface is routed, tested, or supported by the current firmware.

## Repository map

| Path | Contents |
| --- | --- |
| `schematic/` | Altium PCB project, schematics, symbol libraries, and project history |
| `firmware/CA7/DeviceTree/sbc/` | STM32MP157 device trees for Linux, TF-A, and U-Boot |
| `firmware/CM4/` | STM32CubeIDE Cortex-M4 project, HAL/CMSIS files, linker script, and remoteproc helper |
| `firmware/sbc.ioc` | STM32CubeMX configuration |
| `AN/` | Datasheets and application notes used during hardware design |
| `examples/` | Reference designs and display/interface materials |
| `beaglebone/` | BeagleBone Black notes, boot files, and experiments |
| `bildroot/` | Buildroot configuration and root filesystem overlay from earlier experiments |
| `bluetooth/` | Bluetooth for Linux developers study material and examples |
| `test_app/` | Small CMake/GDB test application; its current deployment settings are local to the original development setup |
| `commandsyocto.txt` | A few Yocto commands used in an external Poky workspace |

The directory is spelled `bildroot` in the repository.

## Software and boot flow

The STM32MP157 software is split between the Cortex-A7 Linux side and the Cortex-M4 firmware:

- **Cortex-A7:** Device-tree sources are provided for the Linux kernel, TF-A, and U-Boot. They are based on an STM32CubeMX-generated OpenSTLinux setup.
- **Cortex-M4:** The STM32CubeIDE project contains generated startup and peripheral initialization code, along with a shell helper for starting or stopping M4 firmware through Linux remoteproc.
- **Linux image build:** `commandsyocto.txt` shows basic commands for entering a Poky build environment and invoking BitBake. The Poky/OpenSTLinux layers and build environment are external to this repository; the checked-in command notes alone are not sufficient to reproduce a complete image build.

The device-tree sources currently identify an OpenSTLinux Mickledore / Linux 6.1 setup. Expect to adapt paths, layer versions, machine configuration, and boot settings to the exact board revision and local build environment.

## Getting started

1. Review the Altium project and the device-tree files for the intended hardware configuration.
2. Install the STM32MP1 development tools and obtain the matching OpenSTLinux/Yocto layers separately.
3. Configure a build for this custom board using the checked-in device trees and the correct DDR and boot settings.
4. Build the Linux image and bootloader, then validate boot and peripherals on the target board.
5. Build the Cortex-M4 project in STM32CubeIDE and test it through Linux remoteproc.

There is no repository-wide build script or validated, end-to-end setup guide yet. The commands in `test_app/CMakeLists.txt` also contain a development-machine IP address and are not a general deployment configuration.

## Current status

This is an evolving engineering and learning project. The repository contains a board schematic project, custom device-tree sources, and a generated Cortex-M4 firmware skeleton, alongside older experiments and reference material. A successful build or hardware validation should be treated as specific to the configuration and board revision tested; it is not implied by the presence of source files.

## Notes on contents and licensing

The repository includes vendor datasheets, application notes, development-board reference files, and third-party study material. Please follow the license and redistribution terms that accompany each item. Some source files contain their own license notices; no repository-wide license is declared at the root.
