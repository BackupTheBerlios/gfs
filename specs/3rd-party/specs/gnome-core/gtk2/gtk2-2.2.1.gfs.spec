Name: gtk2
Summary: The Gimp Toolkit 2
Version: 2.2.1
Release: 1.gfs
License: GPL
Group: Development/Libraries/X11
Source: ftp://ftp.gtk.org/pub/gtk/v2.2/gtk+-%{version}.tar.bz2
BuildRoot: %{_tmppath}/build-root-%{name}
Requires: glib2 >= 2.2
Requires: atk >= 1.2.2
Requires: pango >= 1.2.1
Requires: pkgconfig >= 0.15.0
Packager: Hendrik Brandt
Distribution: SuSE
Prefix: /usr
Url: http://www.gtk.org
Vendor: The Gnome for SuSE Project

%define patch_src=ftp://ftp.berlios.de/pub/gfs/patches/gtk+

Patch0: %patch_src-2.0.6-exportsymbols.patch

# Patch for disabled icons
Patch1: %patch_src-2.2.1-disable_icons_smooth_alpha.patch

# Speedup metacity
Patch2: %patch_src-wm.patch

%description
The Gimp Toolkit 2

%prep
rm -rf $RPM_BUILD_ROOT 
mkdir $RPM_BUILD_ROOT

%setup -q -n gtk+-2.2.1
%patch0 -p1
%patch1 -p1
%patch2 -p0

%build
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" \
./configure --prefix=%{prefix} \
	    --libdir=%_prefix/%_lib \
	    --with-native-locale=yes \
	    --with-xinput=xfree \
	    --mandir=%_mandir \
	    --infodir=%_infodir \
	    --sysconfdir=%_sysconfdir \
	    --enable-shm \
	    --enable-xim \
	    --with-gdktarget=x11 \
	    --with-x \
	    --disable-gtk-doc \
	    --enable-fbmanager 
export LIBRARY_PATH=/usr/%_lib/glib2	    
make

%install
export LIBRARY_PATH=%buildroot/usr/%_lib:%buildroot/usr/%_lib/gtk-2.0/%version/loaders:%buildroot/usr/%_lib/gtk-2.0/%version
make DESTDIR=$RPM_BUILD_ROOT install-strip

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
mkdir -p /etc/gtk-2.0
gdk-pixbuf-query-loaders > /etc/gtk-2.0/gdk-pixbuf.loaders
gtk-query-immodules-2.0 > /etc/gtk-2.0/gtk.immodules


%changelog
* Wed Feb 26 2003 - Hendrik Brandt
- add some patches
* Mon Feb 17 2003 - Hendrik Brandt
- initial build for The Gnome for SuSE Project <2.2.1>