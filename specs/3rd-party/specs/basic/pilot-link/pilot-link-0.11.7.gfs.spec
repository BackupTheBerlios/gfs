Name: pilot-link
Summary: Suite of tools for moving  data between Palm devices and desktops
Version: 0.11.7
Release: 1.gfs
License: GPL
Group: Hardware/Palm
Source: http://pilot-link.org/source/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/build-root-%{name}
Requires: java2
Packager: Hendrik Brandt
Distribution: SuSE
Prefix: /usr
Url: http://www.gnu-designs.com/pilot-link
Vendor: The Gnome for SuSE Project

%description
Suite of tools for moving  data between Palm devices and desktops

%prep
rm -rf $RPM_BUILD_ROOT 
mkdir $RPM_BUILD_ROOT

%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" \
./configure --prefix=%{prefix} \
	    --mandir=%_mandir \
	    --libdir=%_libdir \
	    --localstatedir=/var/lib \
	    --with-java=yes
make

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
* Sun Feb 23 2003 - Hendrik Brandt
- initial build for The Gnome for SuSE Project <0.11.7>