Name: libgnome
Summary: Essential Gnome Libraries
Version: 2.2.0.1
Release: 1.gfs
License: GPL
Group: Development/Libraries/GNOME
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/2.2/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/build-root-%{name}
Requires: libxslt >= 1.0.18
Requires: glib2 >= 2.0.3
Requires: gconf2 >= 1.2
Requires: libbonobo >= 2
Requires: gnome-vfs2 >= 2
Requires: esound >= 0.2.26
Requires: audiofile >= 0.2.3
Requires: libxml2 >= 2.4.22
Packager: Hendrik Brandt
Distribution: SuSE
Prefix: /opt/gnome2
%define sysconfdir /etc%{prefix}
Url: http://www.gnome.org
Vendor: The Gnome for SuSE Project

%description
Essential Gnome Libraries

%prep
rm -rf $RPM_BUILD_ROOT 
mkdir $RPM_BUILD_ROOT

%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" \
./configure --prefix=%{prefix} \
	    --libdir=%prefix/%_lib \
	    --mandir=%{_mandir} \
	    --sysconfdir=%{sysconfdir} \
	    --disable-gtk-doc
make

%install
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make DESTDIR=$RPM_BUILD_ROOT install-strip
mkdir -p $RPM_BUILD_ROOT/usr/%_lib/pkgconfig
cp $RPM_BUILD_ROOT%{prefix}/%{_lib}/pkgconfig/*.pc $RPM_BUILD_ROOT/usr/%_lib/pkgconfig/
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
SCHEMAS="desktop_gnome_accessibility_keyboard.schemas \
desktop_gnome_applications_browser.schemas \
desktop_gnome_applications_help_viewer.schemas \
desktop_gnome_applications_terminal.schemas \
desktop_gnome_applications_window_manager.schemas \
desktop_gnome_background.schemas \
desktop_gnome_file_views.schemas \
desktop_gnome_interface.schemas \
desktop_gnome_peripherals_keyboard.schemas \
desktop_gnome_peripherals_mouse.schemas \
desktop_gnome_sound.schemas \
desktop_gnome_thumbnailers.schemas \
desktop_gnome_url_handlers.schemas"
for S in $SCHEMAS; do
    /opt/gnome2/bin/gconftool-2 --makefile-install-rule /etc/opt/gnome2/gconf/schemas/$S > /dev/null
done

%changelog
* Wed Feb 17 2003 - Hendrik Brandt
- initial build for The Gnome for SuSE Project