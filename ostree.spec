#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ostree
Version  : 2016.5
Release  : 2
URL      : http://pkgs.fedoraproject.org/repo/pkgs/ostree/ostree-2016.5.tar.xz/976de0b7774617b37e8d0b6d9b80f1ff/ostree-2016.5.tar.xz
Source0  : http://pkgs.fedoraproject.org/repo/pkgs/ostree/ostree-2016.5.tar.xz/976de0b7774617b37e8d0b6d9b80f1ff/ostree-2016.5.tar.xz
Summary  : Git for operating system binaries
Group    : Development/Tools
License  : BSD-2-Clause GPL-2.0 LGPL-2.0 MIT
Requires: ostree-bin
Requires: ostree-lib
Requires: ostree-doc
Requires: ostree-data
BuildRequires : bison
BuildRequires : docbook-xml
BuildRequires : gpgme-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libassuan-dev
BuildRequires : libcap-dev
BuildRequires : libgpg-error-dev
BuildRequires : libxslt-bin
BuildRequires : pkgconfig(e2p)
BuildRequires : pkgconfig(fuse)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(libgsystem)
BuildRequires : pkgconfig(liblzma)
BuildRequires : pkgconfig(libsoup-2.4)
BuildRequires : pkgconfig(zlib)

%description
OSTree
======
New! See the docs online at [Read The Docs (OSTree)](https://ostree.readthedocs.org/en/latest/ )

%package bin
Summary: bin components for the ostree package.
Group: Binaries
Requires: ostree-data

%description bin
bin components for the ostree package.


%package data
Summary: data components for the ostree package.
Group: Data

%description data
data components for the ostree package.


%package dev
Summary: dev components for the ostree package.
Group: Development
Requires: ostree-lib
Requires: ostree-bin
Requires: ostree-data
Provides: ostree-devel

%description dev
dev components for the ostree package.


%package doc
Summary: doc components for the ostree package.
Group: Documentation

%description doc
doc components for the ostree package.


%package lib
Summary: lib components for the ostree package.
Group: Libraries
Requires: ostree-data

%description lib
lib components for the ostree package.


%prep
%setup -q -n ostree-2016.5

%build
%autogen --disable-static
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make check ||:

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ostree
/usr/bin/rofiles-fuse
/usr/libexec/ostree/grub2-15_ostree

%files data
%defattr(-,root,root,-)
/usr/share/ostree/trusted.gpg.d/README-gpg

%files dev
%defattr(-,root,root,-)
/usr/include/ostree-1/ostree-async-progress.h
/usr/include/ostree-1/ostree-bootconfig-parser.h
/usr/include/ostree-1/ostree-core.h
/usr/include/ostree-1/ostree-deployment.h
/usr/include/ostree-1/ostree-diff.h
/usr/include/ostree-1/ostree-gpg-verify-result.h
/usr/include/ostree-1/ostree-mutable-tree.h
/usr/include/ostree-1/ostree-repo-file.h
/usr/include/ostree-1/ostree-repo.h
/usr/include/ostree-1/ostree-sepolicy.h
/usr/include/ostree-1/ostree-sysroot-upgrader.h
/usr/include/ostree-1/ostree-sysroot.h
/usr/include/ostree-1/ostree-types.h
/usr/include/ostree-1/ostree.h
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man5/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
