Name: gst-plugins
Summary: Additional plugins for gstreamer
Version: 0.6.0
Release: 1.gfs
License: GPL
Group: Productivity/Multimedia/Other
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/build-root-%{name}
Requires: gstreamer >= 0.6
Requires: arts >= 1.0.2
Requires: alsa >= 0.9
Requires: esound 
Requires: libvorbis
Requires: libogg
Requires: gnome-vfs2 >= 2.2
Requires: libogg
Requires: libvorbis
Requires: mad
Requires: mpeg2dec
Requires: swfdec
Requires: a52dec
Packager: Hendrik Brandt
Distribution: SuSE
Prefix: /usr
Url: http://gstreamer.sourceforge.net
Vendor: The Gnome for SuSE Project

Patch0: %name-0.6-disable_ffmpeg_mpeg_typefind.patch
Patch1: %name-0.6-ffmpeg_ldflags.patch
Patch2: %name-0.6-ogg_detection_fix.patch

%description
Additional plugins for gstreamer

%prep
rm -rf $RPM_BUILD_ROOT 
mkdir $RPM_BUILD_ROOT

%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" \
./configure --prefix=%{prefix} \
	    --libdir=%_libdir \
	    --sysconfdir=%_sysconfdir/opt/gnome2 \
	    --localstatedir=/var/lib
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
SCHEMAS="gstreamer.schemas"
for S in $SCHEMAS; do
    /opt/gnome2/bin/gconftool-2 --makefile-install-rule /etc/opt/gnome2/gconf/schemas/$S > /dev/null
done
scrollkeeper-update -v &>${T}/foo
gst-registry

%changelog
* Fri Feb 28 2003 - Hendrik Brandt
- initial build for The Gnome for SuSE Project <0.6.0>