Name: gconf2
Summary: Gnome Configuration System and Daemon
Version: 2.2.0
Release: 1.gfs
License: GPL
Group: System/GUI/GNOME
Source: ftp://ftp.gnome.org/pub/gnome/sources/GConf/2.2/GConf-%{version}.tar.bz2
BuildRoot: %{_tmppath}/build-root-%{name}
Requires: glib2 >= 2.2
Requires: orbit2 >= 2.4
Requires: libxml2 >= 2.5
Requires: linc >= 0.5
Requires: gtk2 >= 2.2
Packager: Hendrik Brandt
Distribution: SuSE
Prefix: /opt/gnome2
Url: http://www.gnome.org
Vendor: The Gnome for SuSE Project

%define sysconfdir /etc%{prefix}

%description
Gnome Configuration System and Daemon

%prep
rm -rf $RPM_BUILD_ROOT 
mkdir $RPM_BUILD_ROOT

%setup -q -n GConf-%{version}


%build
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" \
./configure --prefix=%{prefix} \
--libdir=%{prefix}/%_lib \
--sysconfdir=%{sysconfdir} \
--disable-gtk-doc \
--enable-gconf2-source="source"

make -s CFLAGS="$RPM_OPT_FLAGS"

%install
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make DESTDIR=$RPM_BUILD_ROOT install-strip
mkdir -p $RPM_BUILD_ROOT/usr/%_lib/pkgconfig
cp $RPM_BUILD_ROOT/%{prefix}/%_lib/pkgconfig/*.pc $RPM_BUILD_ROOT/usr/%_lib/pkgconfig/
mkdir -p $RPM_BUILD_ROOT/usr/share/aclocal
cp $RPM_BUILD_ROOT/%{prefix}/share/aclocal/* $RPM_BUILD_ROOT/usr/share/aclocal/
FILLUP_DIR=$RPM_BUILD_ROOT/var/adm/fillup-templates
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
%run_ldconfig

%changelog
* Tue Feb 18 2003 - Hendrik Brandt
- initial build for The Gnome for SuSE Project <2.2.0>