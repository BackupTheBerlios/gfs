Name: gpg
Summary: The GNU Privacy Guard
Version: 1.2.1
Release: 1.gfs
License: GPL
Group: Productivity/Security
Source: ftp://ftp.gnupg.org/gcrypt/gnupg/gnupg-%version.tar.bz2
BuildRoot: %{_tmppath}/build-root-%{name}
Requires: perl
Requires: zlib
Packager: Hendrik Brandt
Distribution: SuSE
Prefix: /usr
Url: http://www.gnupg.org
Vendor: The Gnome for SuSE Project

%description
The GNU Privacy Guard

%prep
rm -rf $RPM_BUILD_ROOT 
mkdir $RPM_BUILD_ROOT

%setup -q -n gnupg-%version

%build
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" \
./configure --prefix=%{prefix} \
            --sysconfdir=%_sysconfdir \
            --localstatedir=/var/lib \
	    --enable-nls \
	    --with-included-zlib
make -j 2

%install
make DESTDIR=$RPM_BUILD_ROOT install-strip

cd $RPM_BUILD_ROOT

gzip %buildroot%prefix/info/gpgv.info
gzip %buildroot%prefix/info/gpg.info


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
* Mon Mar 10 2003 - Hendrik Brandt
- initial build for The Gnome for SuSE Project <1.2.1>
