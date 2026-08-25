# Liquid IDE Packages

This repository publishes the **Liquid IDE** ARM64 package distribution for the embedded terminal runtime. The runtime owner identity is `com.liquidide`, and the package prefix is `/data/data/com.liquidide/files/usr`.

## APT repository

The signed APT base URL is:

`https://raw.githubusercontent.com/sumanworkspace-crypto/liquid-packages/main/apt/termux-main`

Use the `stable` suite and `main` component. The repository contains rebuilt ARM64 packages, including the essential bootstrap chain (`apt`, `dpkg`, `bash`, `curl`, `termux-tools`, `termux-exec`, `util-linux`, and their dependencies), plus architecture-independent packages. Repository metadata is signed by the Liquid IDE package key whose fingerprint is `5C05D78806B6B3352012409A55E04BB5AC59F602`.

## Bootstrap

`bootstrap/bootstrap-aarch64.zip` is the locally generated ARM64 bootstrap archive for the Liquid prefix. Its contents have been checked for ZIP integrity, the expected package-manager entries, the `com.liquidide` runtime prefix, and the absence of the old AndroidIDE package-path token.

## Verification status

The package artifacts were rebuilt with the Liquid package prefix and validated for Debian metadata, payload paths, symlink targets, and forbidden AndroidIDE identity tokens. The repository’s `InRelease` signature and all `Release` checksums pass local verification. A physical OnePlus CPH2569 running Android 15 still needs to perform the final install, `apt update`, package installation, SDK/JDK setup, Gradle sync, and APK/AAB build tests.

## Ownership and notices

Liquid IDE is the product and repository identity. This distribution includes modified GPL-licensed AndroidIDE/Termux-derived components and retains the applicable upstream license and copyright notices in [`THIRD_PARTY_NOTICES/GPL-3.0`](THIRD_PARTY_NOTICES/GPL-3.0). Liquid IDE does not claim authorship of upstream code.
