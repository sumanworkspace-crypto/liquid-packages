# Liquid IDE Packages

This is the public package repository prototype for **Liquid IDE**. It is intended for the embedded Liquid IDE terminal runtime, whose package identity is `com.liquidide` and whose prefix is `/data/data/com.liquidide/files/usr`.

The repository currently contains a verified Liquid-owned `termux-keyring_3.11_all.deb` prototype. It is not yet a complete production Termux distribution; `bash`, `dpkg`, `apt`, `curl`, `termux-tools`, and all runtime dependencies must be rebuilt for Liquid before using this repository for a final setup release.

## Repository URL

The currently verified public raw-content APT base URL is:

`https://raw.githubusercontent.com/sumanworkspace-crypto/liquid-packages/main/apt/termux-main`

GitHub Pages can be enabled later if the account grants Pages administration permission; the package files are already laid out for that deployment.

## Ownership and notices

Liquid IDE is the product and repository identity. This repository also contains or will contain modified GPL-licensed AndroidIDE/Termux-derived components. Upstream license and copyright notices are retained in `UPSTREAM_NOTICES/`. Liquid IDE does not claim authorship of upstream code.
