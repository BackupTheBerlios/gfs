Name: libgnomeui
Summary: User interface part of libgnome
Version: 2.2.0.1
Release: 1.gfs
License: GPL
Group: Development/Libraries/GNOME
Source: %{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/build-root-%{name}
Requires: pango >= 1.1.2
Requires: perl >= 5
Requires: gawk >= 3.1
Requires: popt >= 1.5
Requires: bison >= 1.28
Requires: gettext >= 0.10.40
Requires: esound >= 0.2.26
Requires: audiofile >= 0.2.3
Requires: libbonoboui >= 2
Requires: gconf2 >= 1.2
Requires: libgnome >= 2
Requires: libgnomecanvas >= 2
Requires: gnome-icon-theme
Requires: gnome-themes
Packager: Hendrik Brandt
Distribution: SuSE
Prefix: /opt/gnome2
Url: http://www.gnome.org
Vendor: The Gnome for SuSE Project

%define sysconfdir /etc%{prefix}

%description
User interface part of libgnome

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
	    --with-x \
	    --sysconfdir=%{sysconfdir} \
	    --disable-gtk-doc
make

%install
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
mkdir -p $RPM_BUILD_ROOT/etc%{prefix}/gconf/gconf.xml.defaults
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
* Wed Feb 19 2003 - Hendrik Brandt
- initial build for The Gnome for SuSE Project