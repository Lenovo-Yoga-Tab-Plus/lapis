# lapis

Site for the Lenovo Yoga Tab Plus (TB520FU) Linux port.

The pages are static HTML. GitHub Actions deploys `main` to GitHub Pages. The kernel is [linux-lapis](https://github.com/Lenovo-Yoga-Tab-Plus/linux-lapis). The pacman repository is [lapis-pkgs](https://github.com/Lenovo-Yoga-Tab-Plus/lapis-pkgs).

The install guide covers unlocking the bootloader, carving an `arch` partition with TWRP for multiboot, and installing the root filesystem on the whole `userdata` partition. This repository does not contain `sn.img`, a TWRP image, or a built EndeavourOS zip.
