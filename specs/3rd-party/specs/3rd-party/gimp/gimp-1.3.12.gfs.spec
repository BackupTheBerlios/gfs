Name: gimp
Summary: The GIMP - The GIMP - The GIMP - The GIMP - The GIMP - The GIMP
Version: 1.3.12
Release: 1.gfs
License: GPL
Group: Productivity/Graphics/Bitmap Editors
Source: %{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/build-root-%{name}
Requires: gtk2 >= 2
Requires: pango >= 1
Requires: glib2 >= 2
Requires: libgtkhtml >= 2
Requires: libpng >= 1.2.1
Requires: libjpeg >= 6.0
Requires: libtiff >= 3.5.7
Requires: libart_lgpl >= 2.3.8
Requires: python >= 2.2
Requires: pygtk >= 1.99.13
Requires: libgimpprint >= 4.3
Packager: Hendrik Brandt
Distribution: SuSE
Prefix: /usr
Url: http://www.gimp.org
Vendor: The Gnome for SuSE Project

%description
The GIMP - The GIMP - The GIMP - The GIMP - The GIMP - The GIMP

%prep
rm -rf $RPM_BUILD_ROOT 
mkdir $RPM_BUILD_ROOT

%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" \
./configure --prefix=%{prefix} \
            --localstatedir=/var/lib \
            --enable-python \
            --with-gnome-datadir=/opt/gnome2 \
            --with-x \
            --enable-default-binary \
            --disable-perl
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
* Sun Mar 9 2003 - Hendrik Brandt
- initial build for The Gnome for SuSE Project <1.3.12>
