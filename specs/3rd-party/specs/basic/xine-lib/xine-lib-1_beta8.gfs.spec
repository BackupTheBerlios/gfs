Name: xine-lib
Summary: Core libraries for Xine
Version: 1_beta8
Release: 1.gfs
License: GPL
Group: System/Libraries
Source: http://xine.sourceforge.net/files/xine-lib-1-beta8.tar.gz
BuildRoot: %{_tmppath}/build-root-%{name}
Requires: flac
Requires: libogg
Requires: arts
Requires: alsa
Requires: libdvdread
Requires: aalib
Packager: Hendrik Brandt
Distribution: SuSE
Prefix: /usr
Url: http://xinehq.de
Vendor: The Gnome for SuSE Project

%description
Core libraries for Xine

%prep
rm -rf $RPM_BUILD_ROOT 
mkdir $RPM_BUILD_ROOT

%setup -q -n xine-lib-1-beta8

%build
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" \
./configure --prefix=%{prefix} \
	    --libdir=%_libdir \
	    --sysconfdir=%_sysconfdir \
	    --mandir=%_mandir \
	    --with-x \
	    --with-included-gettext 
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

%post
ldconfig

%changelog
* Tue Mar 11 2003 - Hendrik
- update to 1_beta8

* Sun Feb 23 2003 - Hendrik Brandt
- initial build for The Gnome for SuSE Project <1_beta5>