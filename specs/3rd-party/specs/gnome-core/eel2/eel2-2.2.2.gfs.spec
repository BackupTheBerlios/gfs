Name: eel2
Summary: The Eazel Extentions Library for Nautilus 2
Version: 2.2.2
Release: 1.gfs
License: GPL
Group: Development/Libraries/GNOME
Source: ftp://ftp.gnome.org/pub/gnome/sources/eel/2.2/eel-%{version}.tar.bz2
BuildRoot: %{_tmppath}/build-root-%{name}
Requires: glib2 >= 2
Requires: gconf2 >= 1.2
Requires: gtk2 >= 2
Requires: libart_lgpl >= 2.3.8
Requires: libxml2 >= 2.4.7
Requires: gnome-vfs2 >= 2
Requires: popt >= 1.5
Requires: libglade2 >= 2
Requires: libgnomeui >= 2
Requires: gail >= 0.16
Packager: Hendrik Brandt
Distribution: SuSE
Prefix: /opt/gnome2
Url: http://www.gnome.org
Vendor: The Gnome for SuSE Project
Docdir: %{_defaultdocdir}/eel2

%define sysconfdir /etc%{prefix}

%description
The Eazel Extentions Library for Nautilus 2

%prep
rm -rf $RPM_BUILD_ROOT 
mkdir $RPM_BUILD_ROOT

%setup -q -n eel-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" \
./configure --prefix=%{prefix} \
	    --libdir=%{prefix}/%_lib \
	    --sysconfdir=%{sysconfdir} \
	    --datadir=%{prefix}/share \
	    --localstatedir=/var/lib \
	    --enable-platform-gnome-2

make

%install
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make DESTDIR=$RPM_BUILD_ROOT install-strip
mkdir -p %{buildroot}/usr/%_lib/pkgconfig
cp %{buildroot}%{prefix}/%_lib/pkgconfig/*.pc %{buildroot}/usr/%_lib/pkgconfig/
unset GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL

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
* Thu Feb 20 2003 - Hendrik Brandt
- initial build for The Gnome for SuSE Project <2.2.1>