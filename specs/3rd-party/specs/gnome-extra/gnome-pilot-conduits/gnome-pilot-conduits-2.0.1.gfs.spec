Name: gnome-pilot-conduits
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
Requires: gnome-pilot >= 2
Packager: Hendrik Brandt
Distribution: SuSE
Prefix: /opt/gnome2
Url: http://www.gnome.org
Vendor: The Gnome for SuSE Project
Docdir: %_defaultdocdir/%name

%description
Gnome 2 pilot apps

%prep
rm -rf $RPM_BUILD_ROOT 
mkdir $RPM_BUILD_ROOT

%setup -q

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



%changelog
* Fri Mar 14 2003 - hendrik
- update to 2.0.1

* Mon Mar 10 2003 - Hendrik Brandt
- initial build for The Gnome for SuSE Project <2.0.0>
