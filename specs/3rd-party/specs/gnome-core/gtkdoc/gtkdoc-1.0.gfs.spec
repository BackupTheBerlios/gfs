Name: gtkdoc
Summary: GTK+ documentation generator
Version: 1.0
Release: 1.gfs
License: GPL-2
Group: Productivity/Publishing/SGML
Source: gtk-doc-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-build
Requires: pkgconfig >= 0.12.0
Requires: openjade >= 1.3.1
Requires: docbook-xml-website >= 2
Requires: docbook-dsssl-stylesheets >= 1.77
Requires: perl >= 5
Requires: libxslt >= 1.0.25
Requires: libxml2 >= 2.5.0
Packager: Hendrik Brandt
Distribution: SuSE
Prefix: /usr
Url: http://www.gtk.org
Vendor: The Gnome for SuSE Project

%description
GTK+ documentation generator


%prep
rm -rf $RPM_BUILD_ROOT 
mkdir $RPM_BUILD_ROOT

%setup -n gtk-doc-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" \
./configure --prefix=%{prefix} \
	    --with-dsssl-dir=%prefix/share/sgml/docbkdsl \
	    --mandir=%_mandir
make -j 2

%install
make DESTDIR=$RPM_BUILD_ROOT install-strip

echo $RPM_BUILD_ROOT
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
- initial build for The Gnome for SuSE Project <1.0>