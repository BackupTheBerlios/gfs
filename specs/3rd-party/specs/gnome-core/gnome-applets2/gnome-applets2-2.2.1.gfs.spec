Name: gnome-applets2
Summary: Applets for the Gnome 2 Desktop and Panel
Version: 2.2.1
Release: 1.gfs
License: GPL
Group: System/GUI/GNOME
Source: ftp://ftp.gnome.org/pub/gnome/sources/gnome-applets/gnome-applets-%{version}.tar.bz2
BuildRoot: %{_tmppath}/build-root-%{name}
Requires: gtk2 >= 2.2
Requires: libwnck >= 0.13
Requires: gail >= 0.13
Requires: gconf2 >= 1.2.1
Requires: gnome-vfs2 >= 2
Requires: libgtop2 >= 2
Requires: gnome-panel >= 2
Requires: libglade2 >= 2
Requires: libgnomeui >= 2
Packager: Hendrik Brandt
Distribution: SuSE
Prefix: /opt/gnome2
Url: http://www.gnome.org
Vendor: The Gnome for SuSE Project
Docdir: %_defaultdocdir/%name
%define sysconfdir /etc%prefix

%description
Applets for the Gnome 2 Desktop and Panel

%prep
rm -rf $RPM_BUILD_ROOT 
mkdir $RPM_BUILD_ROOT

%setup -q -n gnome-applets-%version

%build
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" \
./configure --prefix=%{prefix} \
	    --libdir=%prefix/%_lib \
	    --sysconfdir=%sysconfdir \
	    --datadir=%prefix/share \
	    --localstatedir=/var/lib \
	    --with-x \
	    --enable-panelmenu=yes \
	    --enable-platform-gnome-2
	    
make 

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

%post
export GCONF_CONFIG_SOURCE=`/opt/gnome2/bin/gconftool-2 --get-default-source`
SCHEMAS="battstat.schemas \
cdplayer.schemas \
charpick.schemas \
drivemount.schemas \
geyes.schemas \
gkb.schemas \
gtik.schemas \
gweather.schemas \
mini-commander.schemas \
modemlights.schemas \
multiload.schemas \ 
panel-menu.schemas"
for S in $SCHEMAS; do
    /opt/gnome2/bin/gconftool-2 --makefile-install-rule /etc/opt/gnome2/gconf/schemas/$S > /dev/null
done

scrollkeeper-update -v &>${T}/foo

%files -f ../file.list.%{name}
%defattr(-,root,root,0755)

%changelog
* Tue Mar 18 2003 - hendrik
- update to 2.2.1

* Fri Feb 21 2003 - Hendrik Brandt
- inittial build for The Gnome for SuSE Project <2.2.0>