Name: nautilus2
Summary: A (the) filemanager for the Gnome 2 desktop
Version: 2.2.2
Release: 1.gfs
License: GPL
Group: Productivity/File utilities
Source: ftp://ftp.gnome.org/pub/gnome/sources/nautilus/nautilus-%{version}.tar.bz2
BuildRoot: %{_tmppath}/build-root-%{name}
Requires: glib2 >= 2
Requires: pango >= 1.1.2
Requires: gtk2 >= 2.2
Requires: libxml2 >= 2.4.7
Requires: gnome-vfs2 >= 2.1.5
Requires: esound >= 0.2.27
Requires: bonobo-activation >= 2
Requires: eel2 >= %version
Requires: libgnomeui >= 2.1.1
Requires: gnome-desktop >= 2.1
Requires: libart_lgpl >= 2.3.10
Requires: libbonoboui >= 2
Requires: librsvg2 >= 2.0.1
Requires: orbit2 >= 2.4
Requires: scrollkeeper >= 0.3.11
Packager: Hendrik Brandt
Distribution: SuSE
Prefix: /opt/gnome2
Url: http://www.gnome.org
Vendor: The Gnome for SuSE Project
Docdir: %{_defaultdocdir}/nautilus2

%define sysconfdir /etc%{prefix}


%description
A (the) filemanager for the Gnome 2 desktop

%prep
rm -rf $RPM_BUILD_ROOT 
mkdir $RPM_BUILD_ROOT

%setup -q -n nautilus-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" \
./configure --prefix=%{prefix} \
	    --enable-gdialog=yes \
	    --with-x \
	    --libdir=%{prefix}/%_lib \
	    --sysconfdir=%{sysconfdir} \
	    --datadir=%{prefix}/share \
	    --localstatedir=/var/lib \
	    --enable-platform-gnome-2

make

%install
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
export LD_LIBRARY=%{buildroot}%{prefix}/%_lib
make DESTDIR=$RPM_BUILD_ROOT install-strip
mkdir -p %{buildroot}/usr/%_lib/pkgconfig
cp %{buildroot}%{prefix}/%_lib/pkgconfig/*.pc %{buildroot}/usr/%_lib/pkgconfig/
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
SCHEMAS="apps_nautilus_preferences.schemas"
for S in $SCHEMAS; do
    /opt/gnome2/bin/gconftool-2 --makefile-install-rule /etc/opt/gnome2/gconf/schemas/$S > /dev/null
done

scrollkeeper-update -v &>${T}/foo

%changelog
* Tue Mar 11 2003 - hendrik
- update to 2.2.2
- remove patches

* Fri Feb 21 2003 - Hendrik Brandt
- initial build for The Gnome for SuSE Project <2.2.1> 