Name: libbonoboui
Summary: UI-part of libbonobo
Version: 2.2.0.1
Release: 1.gfs
License: GPL
Group: Development/Libraries/GNOME
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/2.2/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/build-root-%{name}
Requires: libbonobo >= 2.2.1
Requires: gtk2 >= 2.2
Requires: bonobo-activation >= 1
Requires: libbonobo >= 2
Requires: libglade2 >= 2
Requires: libgnome >= 2
Requires: libgnomecanvas >= 2
Requires: gconf2 >= 1.2.1
Requires: libxml2 >= 2.4.20
Packager: Hendrik Brandt
Distribution: SuSE
Prefix: /opt/gnome2
Url: http://www.gnome.org
Vendor: The Gnome for SuSE Project

%description
UI-part of libbonobo

%prep
rm -rf $RPM_BUILD_ROOT 
mkdir $RPM_BUILD_ROOT

%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" \
./configure --prefix=%{prefix} \
	    --libdir=%{prefix}/%_lib \
	    --with-native-locale=yes \
	    --with-xinput=xfree \
	    --mandir=%{_mandir} \
	    --infodir=%{_infodir} \
	    --sysconfdir=%{_sysconfdir} \
	    --disable-gtk-doc
make -j 2

%install
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
export LIBRARY_PATH=$RPM_BUILD_ROOT%{prefix}/%_lib
make DESTDIR=$RPM_BUILD_ROOT install-strip
mkdir -p $RPM_BUILD_ROOT/usr/%_lib/pkgconfig
cp $RPM_BUILD_ROOT%{prefix}/%_lib/pkgconfig/*.pc $RPM_BUILD_ROOT/usr/%_lib/pkgconfig/
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
* Tue Mar 18 2003 - hendrik
- update to 2.2.0.1

* Wed Feb 19 2003 - Hendrik Brandt
- initial build for The Gnome for SuSE Project <2.2.0>