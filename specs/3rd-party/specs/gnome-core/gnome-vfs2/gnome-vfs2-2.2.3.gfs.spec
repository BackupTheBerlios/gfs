Name: gnome-vfs2
Summary: Gnome virtual filesystem 2
Version: 2.2.3
Release: 1.gfs
License: GPL
Group: Development/Libraries/GNOME
Source: ftp://ftp.gnome.org/pub/gnome/sources/gnome-vfs/gnome-vfs-%{version}.tar.bz2
BuildRoot: %{_tmppath}/build-root-%{name}
Requires: glib2 >= 2
Requires: gconf2 >= 1.2.1
Requires: orbit2 >= 2.4
Requires: libbonobo >= 2
Requires: bonobo-activation >= 1
Requires: libxml2 >= 2.2.8
Requires: gnome-mime-data >= 2
Requires: gettext >= 0.10.40
Requires: intltool >= 0.22
Requires: pkgconfig >= 0.12.0
Requires: openssl >= 0.9.5
Packager: Hendrik Brandt
Distribution: SuSE
Prefix: /opt/gnome2
%define sysconfdir /etc/%{prefix}
Url: http://www.gnome.org
Vendor: The Gnome for SuSE Project

%description
Gnome virtual filesystem 2

%prep
rm -rf $RPM_BUILD_ROOT 
mkdir $RPM_BUILD_ROOT

%setup -q -n gnome-vfs-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" \
./configure --prefix=%{prefix} \
	    --libdir=%{prefix}/%_lib \
	    --mandir=%{_mandir} \
	    --enable-platform-gnome-2 \
	    --sysconfdir=%{sysconfdir} \
	    --disable-gtk-doc \
	    --enable-openssl
make -j 2

%install
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
export LIBRARY_PATH=$RPM_BUILD_ROOT/opt/gnome2/%_lib
make DESTDIR=$RPM_BUILD_ROOT install-strip
mkdir -p $RPM_BUILD_ROOT/usr/%_lib/pkgconfig
cp $RPM_BUILD_ROOT/opt/gnome2/%_lib/pkgconfig/*.pc $RPM_BUILD_ROOT/usr/%_lib/pkgconfig/
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
SCHEMAS="system_http_proxy.schemas"
for S in $SCHEMAS; do
    /opt/gnome2/bin/gconftool-2 --makefile-install-rule /etc/opt/gnome2/gconf/schemas/$S > /dev/null
done


ldconfig

%changelog
* Tue Mar 11 2003 - hendrik
- update to 2.2.3
- remove ogg-detect-patch

* Wed Feb 19 2003 - Hendrik Brandt
- initial build for The Gnome for SuSE Project