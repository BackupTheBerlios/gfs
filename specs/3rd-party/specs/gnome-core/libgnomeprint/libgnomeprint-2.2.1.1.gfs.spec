Name: libgnomeprint
Summary: Printer handling library for Gnome 2
Version: 2.2.1.1
Release: 1.gfs
License: GPL
Group: Development/Libraries/GNOME
Source: %{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/build-root-%{name}
Requires: glib2 >= 2
Requires: pango >= 1
Requires: fontconfig >= 1
Requires: libart_lgpl >= 2.3.7
Requires: libxml2 >= 2.4.23
Requires: freetype >= 2.0.5
Packager: Hendrik Brandt
Distribution: SuSE
Prefix: /opt/gnome2
Url: http://www.gnome.org
Vendor: The Gnome for SuSE Project
%define sysconfdir /etc%{prefix}
%define INSTALL_DIR install -d -m755
%define INSTALL_DATA install -m644

%description
Printer handling library for Gnome 2

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
	    --sysconfdir=%{sysconfdir}
make -j 2

%install
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
export LIBRARY_PATH=$RPM_BUILD_ROOT%{prefix}/%_lib
make DESTDIR=$RPM_BUILD_ROOT install-strip
mkdir -p $RPM_BUILD_ROOT/usr/%_lib/pkgconfig
cp $RPM_BUILD_ROOT%{prefix}/%_lib/pkgconfig/*.pc $RPM_BUILD_ROOT/usr/%_lib/pkgconfig/
%{INSTALL_DIR} $RPM_BUILD_ROOT%{prefix}/share/fonts/pfbs
%{INSTALL_DIR} $RPM_BUILD_ROOT%{prefix}/share/gnome-print/fonts
%{INSTALL_DIR} $RPM_BUILD_ROOT/sbin/conf.d
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
* Wed Feb 17 2003 - Hendrik Brandt
- initial build for The Gnome for SuSE Project