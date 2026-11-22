# lapis

Project site for the Lenovo Yoga Tab Plus (TB520FU) Linux port.

The pages are static HTML. GitHub Actions deploys them to GitHub Pages from `main`. The kernel is [linux-lapis](https://github.com/Lenovo-Yoga-Tab-Plus/linux-lapis). The pacman repository is [lapis-pkgs](https://github.com/Lenovo-Yoga-Tab-Plus/lapis-pkgs).

The install guide covers unlocking the bootloader, a TWRP multiboot carve of an `arch` partition, and installing the root filesystem on the whole `userdata` partition. This repository does not contain `sn.img`, a TWRP image, or a built EndeavourOS zip.
