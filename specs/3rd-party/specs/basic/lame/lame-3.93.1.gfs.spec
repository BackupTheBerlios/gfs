Name: lame
Summary: LAME ain't an MP3 encoder
Version: 3.93.1
Release: 1.gfs
License: GPL
Group: System/Libraries
Source: http://lame.sourceforge.net/files/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/build-root-%{name}
Packager: Hendrik Brandt
Distribution: SuSE
Prefix: /usr
Url: http://mp3dev.org
Vendor: The Gnome for SuSE Project
Requires: glibc

%description
LAME ain't an MP3 encoder

%prep
rm -rf $RPM_BUILD_ROOT 
mkdir $RPM_BUILD_ROOT

%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" \
./configure --prefix=%{prefix} \
	    --localstatedir=/var/lib \
	    --sysconfdir=%_sysconfdir \
	    --enable-nasm \
	    --enable-shared \
	    --enable-mp3rtp \
	    --enable-extopt=full \
	    --without-vorbis
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
* Sat Mar 1 2003 - Hendrik Brandt
- initial build for The Gnome for SuSE Project <3.93.1>