Name: totem
Summary: Movie player for Gnome 2 based on xine
Version: 0.95.1
Release: 1.gfs
License: GPL
Group: Productivity/Multimedia/Video/Players
Source: http://www.hadess.net/files/software/totem/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/build-root-%{name}
Requires: glib2 >= 2.2
Requires: gtk2 >= 2.2
Requires: libgnomeui >= 2.2
Requires: libglade2 >= 2
Requires: gnome-vfs2 >= 2.2
Requires: xine-lib >= 1_beta8
Packager: Hendrik Brandt
Distribution: SuSE
Prefix: /opt/gnome2
Vendor: The Gnome for SuSE Project

%description
Movie player for Gnome 2 based on xine

%prep
rm -rf $RPM_BUILD_ROOT 
mkdir $RPM_BUILD_ROOT

%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" \
./configure --prefix=%{prefix} \
            --localstatedir=/var/lib \
            --sysconfdir=%_sysconfdir%prefix
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
SCHEMAS="totem.schemas \
         totem-video-thumbnail.schemas"
for S in $SCHEMAS; do
    /opt/gnome2/bin/gconftool-2 --makefile-install-rule /etc/opt/gnome2/gconf/schemas/$S > /dev/null
done

scrollkeeper-update -v &>${T}/foo


%changelog
* Sat Mar 22 2003 - hendrik brandt
- initial build for The Gnome for SuSE Project (0.5.3)
