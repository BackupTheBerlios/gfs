Name: galeon
Summary: Gnome web browser based on mozilla gecko rendering engine
Version: 1.3.3
Release: 1.gfs
License: GPL
Group: Productivity/Networking/Web/Browsers
Source: http://galeon.sourceforge.net/files/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/build-root-%{name}
Requires: mozilla >= 1.3
Requires: glib2 >= 2
Requires: gtk2 >= 2
Requires: libxml2 >= 2.4
Requires: gconf2 >= 2
Requires: orbit2 >= 2
Requires: libbonobo >= 2
Requires: libbonoboui >= 2.1.1
Requires: bonobo-activation >= 2
Requires: libgnomeui >= 2
Requires: gnome-vfs2 >= 2
Requires: libglade2 >= 2
Packager: Hendrik Brandt
Distribution: SuSE
Prefix: /opt/gnome2
Vendor: The Gnome for SuSE Project

%description
Gnome 2 web browser

%prep
rm -rf $RPM_BUILD_ROOT 
mkdir $RPM_BUILD_ROOT

%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" \
./configure --prefix=%{prefix} \
            --localstatedir=/var/lib \
            --sysconfdir=%_sysconfdir%prefix \
	    --enable-nautilus-view=yes \
	    --disable-gtkhtml
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

%files -f ../file.list.%{name}
%defattr(-,root,root,0755)

%post
export GCONF_CONFIG_SOURCE=`/opt/gnome2/bin/gconftool-2 --get-default-source`
SCHEMAS="galeon.schemas"
for S in $SCHEMAS; do
    /opt/gnome2/bin/gconftool-2 --makefile-install-rule /etc/opt/gnome2/gconf/schemas/$S > /dev/null
done

scrollkeeper-update -v &>${T}/foo

%changelog
* Sat Mar 22 2003 - Hendrik Brandt
- initial build for The Gnome for SuSE Project <1.3.3>
