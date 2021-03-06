Name: gnome-pilot
Summary: Gnome 2 pilot apps
Version: 2.0.1
Release: 1.gfs
License: GPL
Group: System/Libraries
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/2.0/%name-%version.tar.bz2
BuildRoot: %{_tmppath}/build-root-%{name}
Requires: perl >= 5
Requires: control-center2 >= 2
Requires: libgnome >= 2
Requires: gnome-panel >= 2
Requires: pilot-link >= 0.11
Requires: gnome-vfs2 >= 2
Requires: libglade2 >= 2
Packager: Hendrik Brandt
Distribution: SuSE
Prefix: /opt/gnome2
Url: http://www.gnome.org
Vendor: The Gnome for SuSE Project
Docdir: %_defaultdocdir/%name

%define patch_src=ftp://ftp.berlios.de/pub/gfs/patches/%name

Patch0: %patch_src-2.0.1-pisock.patch
Patch1: %patch_src-0.1.70-usb.patch

%description
Gnome 2 pilot apps

%prep
rm -rf $RPM_BUILD_ROOT 
mkdir $RPM_BUILD_ROOT

%setup -q
%patch0 -p1
%patch1 -p1

%build
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" \
./configure --prefix=%{prefix} \
            --sysconfdir=%_sysconfdir%prefix \
            --localstatedir=/var/lib \
            --with-vfs \
            --enable-network \
            --enable-usb \
            --enable-pilotlinktest
make -j 2

%install
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make DESTDIR=$RPM_BUILD_ROOT install-strip
mkdir -p %buildroot/usr/%_lib/pkgconfig
cp %buildroot%prefix/%_lib/pkgconfig/* %buildroot/usr/%_lib/pkgconfig/
unset GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL

cd $RPM_BUILD_ROOT


find . -type d -fprint $RPM_BUILD_DIR/file.list.%{name}.dirs
find . -type f -fprint $RPM_BUILD_DIR/file.list.%{name}.files.tmp
sed '/\/man\//s/$/.gz/g' $RPM_BUILD_DIR/file.list.%{name}.files.tmp > $RPM_BUILD_DIR/file.list.%{name}.files
find . -type l -fprint $RPM_BUILD_DIR/file.list.%{name}.libs
sed '1,2d;s,^\.,\%attr(-\,root\,root) \%dir ,' $RPM_BUILD_DIR/file.list.%{name}.dirs > $RPM_BUILD_DIR/file.list.%{name}
sed 's,^\.,\%attr(-\,root\,root) ,' $RPM_BUILD_DIR/file.list.%{name}.files >> $RPM_BUILD_DIR/file.list.%{name}
sed 's,^\.,\%attr(-\,root\,root) ,' $RPM_BUILD_DIR/file.list.%{name}.libs >> $RPM_BUILD_DIR/file.list.%{name}

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf $RPM_BUILD_DIR/file.list.%{name}
rm -rf $RPM_BUILD_DIR/file.list.%{name}.libs
rm -rf $RPM_BUILD_DIR/file.list.%{name}.files
rm -rf $RPM_BUILD_DIR/file.list.%{name}.files.tmp
rm -rf $RPM_BUILD_DIR/file.list.%{name}.dirs

%files -f ../file.list.%{name}
%defattr(-,root,root,0755)

%post
export GCONF_CONFIG_SOURCE=`/opt/gnome2/bin/gconftool-2 --get-default-source`
SCHEMAS="pilot.schemas"
for S in $SCHEMAS; do
    /opt/gnome2/bin/gconftool-2 --makefile-install-rule /etc/opt/gnome2/gconf/schemas/$S > /dev/null
done

scrollkeeper-update -v &>${T}/foo


%changelog
* Fri Mar 14 2003 - hendrik
- update to 2.0.1
- add some patches

* Mon Mar 10 2003 - Hendrik Brandt
- initial build for The Gnome for SuSE Project <2.0.0>
