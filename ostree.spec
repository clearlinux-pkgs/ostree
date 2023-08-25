#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
#
Name     : ostree
Version  : 2023.6
Release  : 62
URL      : https://github.com/ostreedev/ostree/releases/download/v2023.6/libostree-2023.6.tar.xz
Source0  : https://github.com/ostreedev/ostree/releases/download/v2023.6/libostree-2023.6.tar.xz
Summary  : Git for operating system binaries
Group    : Development/Tools
License  : BSD-2-Clause LGPL-2.0 LGPL-2.1
Requires: ostree-bin = %{version}-%{release}
Requires: ostree-config = %{version}-%{release}
Requires: ostree-data = %{version}-%{release}
Requires: ostree-lib = %{version}-%{release}
Requires: ostree-libexec = %{version}-%{release}
Requires: ostree-license = %{version}-%{release}
Requires: ostree-man = %{version}-%{release}
Requires: ostree-services = %{version}-%{release}
BuildRequires : attr-dev
BuildRequires : bison
BuildRequires : buildreq-configure
BuildRequires : docbook-xml
BuildRequires : gjs
BuildRequires : gjs-dev
BuildRequires : glib
BuildRequires : gnupg
BuildRequires : gpgme-dev
BuildRequires : gsettings-desktop-schemas
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libarchive-devel
BuildRequires : libassuan-dev
BuildRequires : libcap-dev
BuildRequires : libxslt-bin
BuildRequires : parallel
BuildRequires : pkgconfig(e2p)
BuildRequires : pkgconfig(fuse)
BuildRequires : pkgconfig(fuse3)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gpgme)
BuildRequires : pkgconfig(libcurl)
BuildRequires : pkgconfig(libgsystem)
BuildRequires : pkgconfig(liblzma)
BuildRequires : pkgconfig(libsodium)
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(zlib)
BuildRequires : pypi-pyaml
BuildRequires : util-linux
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# libostree
This project is now known as "libostree", though it is still appropriate to use
the previous name: "OSTree" (or "ostree"). The focus is on projects which use
libostree's shared library, rather than users directly invoking the command line
tools (except for build systems). However, in most of the rest of the
documentation, we will use the term "OSTree", since it's slightly shorter, and
changing all documentation at once is impractical. We expect to transition to
the new name over time.

%package bin
Summary: bin components for the ostree package.
Group: Binaries
Requires: ostree-data = %{version}-%{release}
Requires: ostree-libexec = %{version}-%{release}
Requires: ostree-config = %{version}-%{release}
Requires: ostree-license = %{version}-%{release}
Requires: ostree-services = %{version}-%{release}

%description bin
bin components for the ostree package.


%package config
Summary: config components for the ostree package.
Group: Default

%description config
config components for the ostree package.


%package data
Summary: data components for the ostree package.
Group: Data

%description data
data components for the ostree package.


%package dev
Summary: dev components for the ostree package.
Group: Development
Requires: ostree-lib = %{version}-%{release}
Requires: ostree-bin = %{version}-%{release}
Requires: ostree-data = %{version}-%{release}
Provides: ostree-devel = %{version}-%{release}
Requires: ostree = %{version}-%{release}

%description dev
dev components for the ostree package.


%package extras
Summary: extras components for the ostree package.
Group: Default

%description extras
extras components for the ostree package.


%package lib
Summary: lib components for the ostree package.
Group: Libraries
Requires: ostree-data = %{version}-%{release}
Requires: ostree-libexec = %{version}-%{release}
Requires: ostree-license = %{version}-%{release}

%description lib
lib components for the ostree package.


%package libexec
Summary: libexec components for the ostree package.
Group: Default
Requires: ostree-config = %{version}-%{release}
Requires: ostree-license = %{version}-%{release}

%description libexec
libexec components for the ostree package.


%package license
Summary: license components for the ostree package.
Group: Default

%description license
license components for the ostree package.


%package man
Summary: man components for the ostree package.
Group: Default

%description man
man components for the ostree package.


%package services
Summary: services components for the ostree package.
Group: Systemd services
Requires: systemd

%description services
services components for the ostree package.


%prep
%setup -q -n libostree-2023.6
cd %{_builddir}/libostree-2023.6
pushd ..
cp -a libostree-2023.6 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1692988932
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%configure --disable-static --with-curl \
--without-soup
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
%configure --disable-static --with-curl \
--without-soup
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
# Tests require some glib schemas to be initialized
target=$HOME/.local/share/glib-2.0/schemas
mkdir -p $target
glib-compile-schemas --targetdir=$target /usr/share/glib-2.0/schemas
export XDG_DATA_DIRS="$HOME/.local/share${XDG_DATA_DIRS:+:$XDG_DATA_DIRS}"
make %{?_smp_mflags} check || cat ./test-suite.log

%install
export SOURCE_DATE_EPOCH=1692988932
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ostree
cp %{_builddir}/libostree-%{version}/COPYING %{buildroot}/usr/share/package-licenses/ostree/ba8966e2473a9969bdcab3dc82274c817cfd98a1 || :
cp %{_builddir}/libostree-%{version}/bsdiff/LICENSE %{buildroot}/usr/share/package-licenses/ostree/4ee6d2132726e5074e6917e113cf34d3cf625ce2 || :
cp %{_builddir}/libostree-%{version}/libglnx/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/ostree/5c6c38fa1b6ac7c66252c83d1203e997ae3d1c98 || :
cp %{_builddir}/libostree-%{version}/libglnx/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/ostree/01a6b4bf79aca9b556822601186afab86e8c4fbf || :
pushd ../buildavx2/
%make_install_v3
popd
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/V3/usr/lib/ostree/ostree-prepare-root
/V3/usr/lib/ostree/ostree-remount
/usr/lib/ostree/ostree-prepare-root
/usr/lib/ostree/ostree-remount

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/ostree
/V3/usr/bin/rofiles-fuse
/usr/bin/ostree
/usr/bin/rofiles-fuse

%files config
%defattr(-,root,root,-)
/usr/lib/tmpfiles.d/ostree-tmpfiles.conf

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/OSTree-1.0.typelib
/usr/share/bash-completion/completions/ostree
/usr/share/gir-1.0/*.gir
/usr/share/ostree/trusted.gpg.d/README-gpg

%files dev
%defattr(-,root,root,-)
/usr/include/ostree-1/ostree-async-progress.h
/usr/include/ostree-1/ostree-autocleanups.h
/usr/include/ostree-1/ostree-bootconfig-parser.h
/usr/include/ostree-1/ostree-content-writer.h
/usr/include/ostree-1/ostree-core.h
/usr/include/ostree-1/ostree-deployment.h
/usr/include/ostree-1/ostree-diff.h
/usr/include/ostree-1/ostree-dummy-enumtypes.h
/usr/include/ostree-1/ostree-gpg-verify-result.h
/usr/include/ostree-1/ostree-kernel-args.h
/usr/include/ostree-1/ostree-mutable-tree.h
/usr/include/ostree-1/ostree-ref.h
/usr/include/ostree-1/ostree-remote.h
/usr/include/ostree-1/ostree-repo-deprecated.h
/usr/include/ostree-1/ostree-repo-file.h
/usr/include/ostree-1/ostree-repo-finder-avahi.h
/usr/include/ostree-1/ostree-repo-finder-config.h
/usr/include/ostree-1/ostree-repo-finder-mount.h
/usr/include/ostree-1/ostree-repo-finder-override.h
/usr/include/ostree-1/ostree-repo-finder.h
/usr/include/ostree-1/ostree-repo-os.h
/usr/include/ostree-1/ostree-repo.h
/usr/include/ostree-1/ostree-sepolicy.h
/usr/include/ostree-1/ostree-sign-ed25519.h
/usr/include/ostree-1/ostree-sign.h
/usr/include/ostree-1/ostree-sysroot-upgrader.h
/usr/include/ostree-1/ostree-sysroot.h
/usr/include/ostree-1/ostree-types.h
/usr/include/ostree-1/ostree-version.h
/usr/include/ostree-1/ostree.h
/usr/lib64/libostree-1.so
/usr/lib64/pkgconfig/ostree-1.pc

%files extras
%defattr(-,root,root,-)
/V3/usr/lib/systemd/system-generators/ostree-system-generator
/usr/lib/systemd/system-generators/ostree-system-generator

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libostree-1.so.1.0.0
/usr/lib64/libostree-1.so.1
/usr/lib64/libostree-1.so.1.0.0

%files libexec
%defattr(-,root,root,-)
/usr/libexec/libostree/grub2-15_ostree

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ostree/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/ostree/4ee6d2132726e5074e6917e113cf34d3cf625ce2
/usr/share/package-licenses/ostree/5c6c38fa1b6ac7c66252c83d1203e997ae3d1c98
/usr/share/package-licenses/ostree/ba8966e2473a9969bdcab3dc82274c817cfd98a1

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/ostree-admin-cleanup.1
/usr/share/man/man1/ostree-admin-config-diff.1
/usr/share/man/man1/ostree-admin-deploy.1
/usr/share/man/man1/ostree-admin-init-fs.1
/usr/share/man/man1/ostree-admin-instutil.1
/usr/share/man/man1/ostree-admin-os-init.1
/usr/share/man/man1/ostree-admin-pin.1
/usr/share/man/man1/ostree-admin-set-default.1
/usr/share/man/man1/ostree-admin-set-origin.1
/usr/share/man/man1/ostree-admin-stateroot-init.1
/usr/share/man/man1/ostree-admin-status.1
/usr/share/man/man1/ostree-admin-switch.1
/usr/share/man/man1/ostree-admin-undeploy.1
/usr/share/man/man1/ostree-admin-unlock.1
/usr/share/man/man1/ostree-admin-upgrade.1
/usr/share/man/man1/ostree-admin.1
/usr/share/man/man1/ostree-cat.1
/usr/share/man/man1/ostree-checkout.1
/usr/share/man/man1/ostree-checksum.1
/usr/share/man/man1/ostree-commit.1
/usr/share/man/man1/ostree-config.1
/usr/share/man/man1/ostree-create-usb.1
/usr/share/man/man1/ostree-diff.1
/usr/share/man/man1/ostree-export.1
/usr/share/man/man1/ostree-find-remotes.1
/usr/share/man/man1/ostree-fsck.1
/usr/share/man/man1/ostree-gpg-sign.1
/usr/share/man/man1/ostree-init.1
/usr/share/man/man1/ostree-log.1
/usr/share/man/man1/ostree-ls.1
/usr/share/man/man1/ostree-prepare-root.1
/usr/share/man/man1/ostree-prune.1
/usr/share/man/man1/ostree-pull-local.1
/usr/share/man/man1/ostree-pull.1
/usr/share/man/man1/ostree-refs.1
/usr/share/man/man1/ostree-remote.1
/usr/share/man/man1/ostree-reset.1
/usr/share/man/man1/ostree-rev-parse.1
/usr/share/man/man1/ostree-show.1
/usr/share/man/man1/ostree-sign.1
/usr/share/man/man1/ostree-static-delta.1
/usr/share/man/man1/ostree-summary.1
/usr/share/man/man1/ostree.1
/usr/share/man/man1/rofiles-fuse.1
/usr/share/man/man5/ostree.repo-config.5
/usr/share/man/man5/ostree.repo.5

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/ostree-boot-complete.service
/usr/lib/systemd/system/ostree-finalize-staged-hold.service
/usr/lib/systemd/system/ostree-finalize-staged.path
/usr/lib/systemd/system/ostree-finalize-staged.service
/usr/lib/systemd/system/ostree-prepare-root.service
/usr/lib/systemd/system/ostree-remount.service
