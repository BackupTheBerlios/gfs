Name: eog2
Summary: Image viewer for Gnome 2
Version: 2.2.1
Release: 1.gfs
License: GPL
Group: Amusements/Games
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/eog-%{version}.tar.bz2
BuildRoot: %{_tmppath}/build-root-%{name}
Requires: gconf2 >= 1.2.1
Requires: gnome-vfs2 >= 2.0.4
Requires: libgnomeui >= 2.0.6
Requires: libbonoboui >= 2.0.3
Requires: bonobo-activation >= 1.0.3
Requires: libglade2 >= 2.0.1
Requires: librsvg2 >= 2.0.1
Packager: Hendrik Brandt
Distribution: SuSE
Prefix: /opt/gnome2
Url: http://www.gnome.org
Vendor: The Gnome for SuSE Project
Docdir: %_defaultdocdir/%name
%define sysconfdir /etc%prefix


%description
Image viewer for Gnome 2

%prep
rm -rf $RPM_BUILD_ROOT 
mkdir $RPM_BUILD_ROOT

%setup -q -n eog-%version

%build
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" \
./configure --prefix=%{prefix} \
	    --sysconfdir=%sysconfdir \
	    --datadir=%prefix/share \
	    --localstatedir=/var/lib \
	    --enable-platform-gnome-2
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

%post
export GCONF_CONFIG_SOURCE=`/opt/gnome2/bin/gconftool-2 --get-default-source`
SCHEMAS="eog.schemas"
for S in $SCHEMAS; do
    /opt/gnome2/bin/gconftool-2 --makefile-install-rule /etc/opt/gnome2/gconf/schemas/$S > /dev/null
done

scrollkeeper-update -v &>${T}/foo


%changelog
* Tue Mar 11 2003 - hendrik
- update to 2.2.1

* Wed Feb 26 2003 - Hendrik Brandt
- initial build for The Gnome for SuSE Project <2.2.0>