Name: glib2
Summary: The glib library of C routines
Version: 2.2.1
Release: 1.gfs
License: GPL
Group: Development/Libraries/C and C++
Source: ftp://ftp.gtk.org/pub/gtk/v2.2/glib-%{version}.tar.bz2
BuildRoot: %{_tmppath}/build-root-%{name}
Requires: pkgconfig >= 0.14.0
Requires: gtkdoc >= 1.0
Packager: Hendrik Brandt
Distribution: SuSE
Prefix: /usr
Url: http://www.gtk.org
Vendor: The Gnome for SuSE Project

%description
The glib library of C routines

%prep
rm -rf $RPM_BUILD_ROOT 
mkdir $RPM_BUILD_ROOT

%setup -q -n glib-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" \
./configure --prefix=%{prefix} \
	    --mandir=%_mandir \
	    --infodir=%_infodir \
	    --libdir=%_libdir \
	    --disable-gtk-doc \
	    --with-threads=posix
make -j 2

%install
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

%changelog
* Mon Feb 17 2003 - Hendrik Brandt
- initial build for The Gnome for SuSE Project