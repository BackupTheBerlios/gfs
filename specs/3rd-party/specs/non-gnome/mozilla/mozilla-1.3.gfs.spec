Name: mozilla
Summary: The Mozilla web browser
Version: 1.3
Release: 1.gfs
License: GPL
Group: Productivity/Networking/Web/Browsers
Source: ftp://ftp.mozilla.org/pub/mozilla/releases/1.3/src/mozilla-source-1.3.tar.bz2
BuildRoot: %{_tmppath}/build-root-%{name}
Requires: xf86
Requires: orbit2 >= 2.4
Requires: libidl >= 0.8.0
Requires: zlib >= 1.1.4
Requires: fontconfig >= 2.1
Requires: xft >= 2.0.1
Requires: libjpeg >= 6
Requires: expat
Requires: zip
Requires: unzip
Requires: gtk2 >= 2.2
Requires: glib2 >= 2.2
Requires: pango >= 1.2.1
Requires: gpg >= 1.2.1
Packager: Hendrik Brandt
Distribution: SuSE
Prefix: /opt/mozilla
Url: http://www.gnome.org
Vendor: The Gnome for SuSE Project
Docdir: %_defaultdocdir/%name

%description
The Mozilla web browser

%prep
rm -rf $RPM_BUILD_ROOT 
mkdir $RPM_BUILD_ROOT

%setup -q -n mozilla

%build
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" \
./configure --prefix=%{prefix} \
	    --bindir=%prefix \
	    --libdir=%prefix/lib \
	    --includedir=%prefix/include \
	    --enable-configure \
	    --disable-tests \
	    --disable-debug \
	    --disable-dtd-debug \
            --sysconfdir=/etc \
	    --disable-logging \
	    --disable-short-wchar \
	    --enable-mathml \
	    --enable-xinerama \
	    --enable-reorder \
	    --enable-strip \
	    --enable-ldap \
            --localstatedir=/var/lib \
	    --enable-toolkit-gtk2 \
	    --enable-default-toolkit=gtk2 \
	    --disable-toolkit-qt \
	    --disable-toolkit-xlib \
	    --disable-toolkit-gtk \
	    --enable-xft \
	    --disable-freetype2 \
	    --disable-svg \
	    --enable-calender \
	    --disable-pedantic \
	    --disable-short-wchar \
	    --disable-xprint \
	    --enable-mathml \
	    --without-system-nspr \
	    --enable-nspr-autoconf \
	    --with-system-zlib \
	    --enable-xsl \
	    --enable-crypto \
	    --enable-extensions="xmlterm,xmlextras,access-builtin,interfaceinfo,wallet,typeaheadfind,irc,cookie" \
	    --enable-optimize="-O2" \
	    --with-default-mozilla-five-home=%prefix
make -j 3

%install
make DESTDIR=$RPM_BUILD_ROOT install

mkdir -p %buildroot/usr/bin
cp %buildroot%prefix/mozilla %buildroot/usr/bin/

mkdir -p %buildroot/usr/%_lib
mv %buildroot%prefix/%_lib/pkgconfig %buildroot/usr/%_lib/

cd $RPM_BUILD_ROOT

find . -type d -fprint $RPM_BUILD_DIR/file.list.%{name}.dirs
find . -type f -fprint $RPM_BUILD_DIR/file.list.%{name}.files.tmp
sed '/\/man\//s/$/.gz/g' $RPM_BUILD_DIR/file.list.%{name}.files.tmp > $RPM_BUILD_DIR/file.list.%{name}.files
find . -type l -fprint $RPM_BUILD_DIR/file.list.%{name}.libs
sed '1,2d;s,^\.,\%attr(-\,root\,root) \%dir ,' $RPM_BUILD_DIR/file.list.%{name}.dirs > $RPM_BUILD_DIR/file.list.%{name}
sed 's,^\.,\%attr(-\,root\,root) ,' $RPM_BUILD_DIR/file.list.%{name}.files >> $RPM_BUILD_DIR/file.list.%{name}
sed 's,^\.,\%attr(-\,root\,root) ,' $RPM_BUILD_DIR/file.list.%{name}.libs >> $RPM_BUILD_DIR/file.list.%{name}

gzip %buildroot%prefix/man/man1/mozilla.1


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
- initial build for The Gnome for SuSE Project <1.3>
