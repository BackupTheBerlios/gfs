Name: fontconfig
Summary: A library for configuring and customizing font access
Version: 2.1
Release: 4.gfs
License: fontconfig
Group: System/Libraries
Source: http://fontconfig.org/releases/fcpackage.2_1.tar.gz
BuildRoot: %{_tmppath}/build-root-%{name}
Requires: freetype2
Packager: Hendrik Brandt
Distribution: SuSE
Prefix: /usr/X11R6
Url: http://fontconfig.org
Vendor: The Gnome for SuSE Project

%define patch_src=ftp://ftp.berlios.de/pub/gfs/patches/%name

# CVS-update from XFree86
Patch1: %patch_src-2.1-cvs-update-20021221.patch

# some patches from RedHat
Patch2: %patch_src-2.0-defaultconfig.patch
Patch3: %patch_src-2.1-slighthint.patch

# blacklist of certain fonts that freetype can't handle
Patch4: %patch_src-0.0.1.020826.1330-blacklist.patch

# fix config script to always include x11 fontpath and remove date
Patch5: %patch_src-2.1-x11fontpath-date-configure-v2.patch

%description
A library for configuring and customizing font access

%prep
rm -rf $RPM_BUILD_ROOT 
mkdir $RPM_BUILD_ROOT

%setup -q -n fcpackage.2_1/fontconfig/
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p2

%build
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" \
./configure --prefix=%{prefix} \
	    --libdir=%_libdir \
	    --with-x \
	    --localstatedir=/var/lib \
	    --sysconfdir=/etc
make

%install
make prefix=$RPM_BUILD_ROOT/usr libdir=$RPM_BUILD_ROOT/%{_libdir} sysconfdir=%_sysconfdir install


cd $RPM_BUILD_ROOT


find . -type d -fprint $RPM_BUILD_DIR/file.list.%{name}.dirs
find . -type f -fprint $RPM_BUILD_DIR/file.list.%{name}.files.tmp
sed '/\/man\//s/$/.gz/g' $RPM_BUILD_DIR/file.list.%{name}.files.tmp > $RPM_BUILD_DIR/file.list.%{name}.files
find . -type l -fprint $RPM_BUILD_DIR/file.list.%{name}.libs
sed '1,2d;s,^\.,\%attr(-\,root\,root) \%dir ,' $RPM_BUILD_DIR/file.list.%{name}.dirs > $RPM_BUILD_DIR/file.list.%{name}
sed 's,^\.,\%attr(-\,root\,root) ,' $RPM_BUILD_DIR/file.list.%{name}.files >> $RPM_BUILD_DIR/file.list.%{name}
sed 's,^\.,\%attr(-\,root\,root) ,' $RPM_BUILD_DIR/file.list.%{name}.libs >> $RPM_BUILD_DIR/file.list.%{name}

mv $RPM_BUILD_DIR/file.list* $RPM_BUILD_DIR/fcpackage.2_1/

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
/sbin/conf.d/SuSEconfig.fonts

%postun
/sbin/conf.d/SuSEconfig.fonts

%changelog
* Mon Feb 17 2003 - Hendrik Brandt
- initial build for The Gnome on SuSE Project <2.1>