Name: orbit2
Summary: ORBit2 is a high-performance CORBA ORB
Version: 2.6.1
Release: 1.gfs
License: GPL
Group: System/Libraries
Source: ftp://ftp.gnome.org/pub/gnome/sources/ORBit2/ORBit2-%{version}.tar.bz2
BuildRoot: %{_tmppath}/build-root-%{name}
Requires: glib2 >= 2.2
Requires: popt >= 1.5
Requires: libidl >= 0.7.4
Requires: linc >= 1.0.0
Packager: Hendrik Brandt
Distribution: SuSE
Prefix: /usr
Url: http://www.gnome.org
Vendor: The Gnome for SuSE Project

%define sysconfdir /etc

%description
ORBit2 is a high-performance CORBA ORB

%prep
rm -rf $RPM_BUILD_ROOT 
mkdir $RPM_BUILD_ROOT

%setup -q -n ORBit2-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" \
./configure --prefix=%prefix \
	    --sysconfdir=%sysconfdir \
	    --libdir=/usr/lib \
	    --infodir=%_infodir
make

%install
make install DESTDIR=$RPM_BUILD_ROOT

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
* Tue Mar 18 2003 - hendrik
- update to 2.6.1

* Tue Feb 18 2003 - Hendrik Brandt
- initial build for The Gnome for SuSE Project <2.6.0>