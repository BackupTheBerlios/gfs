Name: metacity
Summary: Gnome 2.2 default window manager
Version: 2.4.34
Release: 1.gfs
License: GPL
Group: System/GUI/GNOME
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/build-root-%{name}
Requires: gtk2 >= 2.2
Requires: gconf2 >= 1.2
Requires: libglade2 >= 2
Requires: startup-notification >= 0.4
Packager: Hendrik Brandt
Distribution: SuSE
Prefix: /opt/gnome2
Url: http://people.redhat.com/~hp/metacity
Vendor: The Gnome for SuSE Project
Docdir: %_defaultdocdir/%name

%description
Gnome 2.2 default window manager

%prep
rm -rf $RPM_BUILD_ROOT 
mkdir $RPM_BUILD_ROOT

%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" \
./configure --prefix=%{prefix} \
	    --sysconfdir=%_sysconfdir/opt/gnome2 \
	    --datadir=/usr/share \
	    --localstatedir=/var/lib \
	    --with-x \
	    --enable-platform-gnome-2

make

%install
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make DESTDIR=$RPM_BUILD_ROOT install-strip
mkdir -p %buildroot/usr/%_lib/pkgconfig
cp %buildroot%prefix/%_lib/pkgconfig/*.pc %buildroot/usr/%_lib/pkgconfig/
mkdir -p %buildroot%prefix/share
cp -R %buildroot/usr/share/* %buildroot%prefix/share/

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
SCHEMAS="metacity.schemas"
for S in $SCHEMAS; do
    /opt/gnome2/bin/gconftool-2 --makefile-install-rule /etc/opt/gnome2/gconf/schemas/$S > /dev/null
done

scrollkeeper-update -v &>${T}/foo

%files -f ../file.list.%{name}
%defattr(-,root,root,0755)

%changelog
* Fri Feb 21 2003 - Hendrik Brandt
- initial build for The Gnome for SuSE Project <2.4.34>