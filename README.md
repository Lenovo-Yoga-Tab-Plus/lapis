# lapis

Site for the Lenovo Yoga Tab Plus (TB520FU) Linux port.

The pages are static HTML. GitHub Actions builds the site, uploads the Pages artifact, and deploys it from the next job. The kernel is [linux-lapis](https://github.com/Lenovo-Yoga-Tab-Plus/linux-lapis). The pacman repository is [lapis-pkgs](https://github.com/Lenovo-Yoga-Tab-Plus/lapis-pkgs).

The install guide unlocks the bootloader with `unlock-bootloader.py`, carves an `arch` partition, and flashes Linux to slot A. Android’s boot image stays on slot B. This repository does not contain `sn.img`, a TWRP image, or a built EndeavourOS zip.
