Name: xft
Summary: A library for configuring and customizing font access
Version: 2.1
Release: 1.gfs
License: fontconfig
Group: System/Libraries
Source: http://fontconfig.org/release/fcpackage.2_1.tar.gz
BuildRoot: %{_tmppath}/build-root-%{name}
Requires: fontconfig
Packager: Hendrik Brandt
Distribution: SuSE
Prefix: /usr/X11R6
Url: http://fontconfig.org
Vendor: The Gnome for SuSE Project

Patch0: xft-2.0.1-cvs-update-20021221.patch

%description
A library for configuring and customizing font access

%prep
rm -rf $RPM_BUILD_ROOT 
mkdir $RPM_BUILD_ROOT

%setup -q -n fcpackage.2_1/Xft/
%patch0 -p1

%build

CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" \
./configure --prefix=%{prefix} --with-x --localstatedir=/var/lib
make

%install
make prefix=$RPM_BUILD_ROOT/usr libdir=$RPM_BUILD_ROOT/%{_libdir} install

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


%changelog
* Mon Feb 17 2003 - Hendrik Brandt
- initial build for The Gnome on SuSE Project <2.1>