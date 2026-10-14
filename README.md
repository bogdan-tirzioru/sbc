# STM32MP157 Single-Board Computer

This repository contains the hardware design and software experiments for a custom single-board computer based on the **STM32MP157C**. The goal is to develop a practical ARM computer that boots Linux and can be used with standard peripherals: a USB keyboard and mouse, an external screen, a 3.3 V TTL UART, wired Ethernet, audio carried over HDMI, and multiple USB ports.

The repository is experimental and combines the current STM32MP157 SBC work with earlier BeagleBone Black and Buildroot experiments. It is not yet a turnkey board support package or a production-ready design.

## Project scope

The project covers the design and bring-up of a complete single-board computer, including:

- The STM32MP157C processor, external memory, power, boot and storage hardware, including an SD card slot for removable storage.
- Linux boot support for the Cortex-A7, including the required bootloader and device-tree configuration.
- Cortex-M4 firmware and its integration with Linux where useful.
- Board-level interfaces required for everyday computer use:
  - **Four USB-A host ports** for a standard USB keyboard and mouse, plus other peripherals. The four-port arrangement follows the STM32MP157 Discovery board as a reference; the hub topology and port power circuitry remain to be designed.
  - **Display output** for an external screen. The primary path is HDMI using the LTDC and a SiI9022A transmitter. The secondary path is analog VGA using the LTDC and a THS8136 DAC.
  - **UART** with 3.3 V TTL signaling for serial console and development access.
  - **Wired Ethernet** for network connectivity, using a conventional Ethernet interface. The link speed and connector implementation are to be confirmed against the board design.
  - **HDMI audio** carried with the display signal through the SiI9022A. The STM32MP157 must provide the transmitter with a digital audio stream, and Linux audio routing must be configured.
  - **SD card slot** for removable storage and file transfer. The card form factor and whether the card is used for boot, data storage, or both remain to be decided.
- Board validation and software bring-up for these functions.

The initial usability goal is that the board can boot Linux, accept input from a USB keyboard and mouse, drive an external screen, provide a 3.3 V TTL UART console, connect to wired Ethernet, provide analog audio out, expose four usable USB-A host ports, and access removable storage through an SD card.

### Scope boundaries and open design decisions

This scope defines the required user-facing capabilities, not the final implementation of every interface. The primary display path is HDMI through the SiI9022A; VGA through the THS8136 is the secondary option. Supported display timings and resolution, Ethernet link speed, HDMI audio format and channel configuration, USB hub topology and per-port power design, whether to include a separate USB-C OTG connector, SD card form factor and boot/data role, other storage arrangement, and enclosure remain to be specified. These should be recorded in the hardware requirements as the design is refined.

Earlier BeagleBone Black, Buildroot, Bluetooth study, and test application files remain in the repository as project history or learning material; they are not all part of the target SBC's required feature set.

## Hardware at a glance

The current board files identify the design as an STM32MP157C custom board. The device trees describe **1 GiB of DDR3L** using the Micron MT41K512M16VRP-107 memory device. The repository also contains an Altium project and component references for the board.

These files are design work in progress. The SiI9022A HDMI path is the primary display choice, with THS8136 VGA as the secondary path. Their presence in the repository does not mean either path is routed, tested, or supported by the current firmware.

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
