Name: pango
Summary: I18n-Text rendering and layout library
Version: 1.2.1
Release: 1.gfs
License: GPL
Group: System/Libraries
Source: %{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/build-root-%{name}
Requires: glib2 >= 2.2
Requires: fontconfig >= 2.1
Requires: freetype2 >= 2.0.9
Requires: pkgconfig >= 0.12.0
Packager: Hendrik Brandt
Distribution: SuSE
Prefix: /usr
Url: http://www.pango.org
Vendor: The Gnome for SuSE Project

%define patch_src=ftp://ftp.berlios.de/pub/gfs/patches/%name

# Some enhancements from RedHat
Patch0: %patch_src-1.0.99.020606-xfonts.patch

# caching fontsets speedup patch from cvs
Patch1: %patch_src-1.2.1-cvs_fontset_caching.patch


%description
I18n-Text rendering and layout library

%prep
rm -rf $RPM_BUILD_ROOT 
mkdir $RPM_BUILD_ROOT

%setup -q

%patch0 -p1
%patch1 -p1

%build
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" \
./configure --prefix=%{prefix} \
	    --with-x \
	    --libdir=%_libdir \
	    --with-native-locale=yes \
	    --with-xinput=xfree \
	    --mandir=%_mandir \
	    --infodir=%_infodir \
	    --sysconfdir=%_sysconfdir \
	    --without-qt
make

%install
export LIBRARY_PATH=$RPM_BUILD_ROOT/usr/%{_lib}:$RPM_BUILD_ROOT/usr/%{_lib}/pango/modules
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
pango-querymodules > /etc/pango/pango.modules


%changelog
* Wed Feb 26 2003 - Hendrik Brandt
- add some stuff from RedHat and Gentoo
* Mon Feb 17 2003 - Hendrik Brandt
- initial build for The Gnome for SuSE Project <1.2.1>