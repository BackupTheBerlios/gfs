Name: gdm2
Summary: Gnome 2 display manager
Version: 2.4.1.3
Release: 1.gfs
License: GPL
Group: System/GUI/GNOME
Source: ftp://ftp.gnome.org/pub/gnome/sources/gdm/2.4/gdm-%{version}.tar.bz2
BuildRoot: %{_tmppath}/build-root-%{name}
Requires: gtk2 >= 2
Requires: pam >= 0.72
Requires: libglade2 >= 2
Requires: librsvg2 >= 2
Requires: libxml2 >= 2.4.12
Requires: libgnomeui >= 2
Requires: libgnomecanvas >= 2
Packager: Hendrik Brandt
Distribution: SuSE
Prefix: /opt/gnome2
Url: http://www.gnome.org
Vendor: The Gnome for SuSE Project
Docdir: %_defaultdocdir

%description
Gnome 2 display manager

%prep
rm -rf $RPM_BUILD_ROOT 
mkdir $RPM_BUILD_ROOT

%setup -q -n gdm-%version

%build
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" \
./configure --prefix=%{prefix} \
	    --libdir=%prefix/%_lib \
	    --sysconfdir=%_sysconfdir%prefix \
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
scrollkeeper-update -v &>${T}/foo
ldconfig
SuSEconfig

echo "\n\n Please edit your gdm.conf and change Group from 'gdm' to 'shadow'"

%changelog
* Sun Mar 2 2003 - Hendrik Brandt
- initial build for The Gnome for SuSE Project <2.4.1.3>