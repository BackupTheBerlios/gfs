Name: scrollkeeper
Summary: Catalog management system for documentation
Version: 0.3.11
Release: 100.gfs
License: LGPL
Group: Development/Libraries/C and C++
Source: http://scrollkeeper.sourceforge.net/files/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/build-root-%{name}
Requires: libxml2 >= 2.4.19
Requires: libxslt >= 1.0.14
Requires: zlib >= 1.1.3
Requires: docbook_4
Packager: Hendrik Brandt
Distribution: SuSE
Prefix: /usr
Url: http://scrollkeeper.sourceforge.net
Vendor: The Gnome for SuSE Project

%define xmlcatalog %{_sysconfdir}/xml/catalog
%define localstatedir /var
%define INSTALL_DIR install -d -m755

%description
Catalog management system for documentation

%prep
rm -rf $RPM_BUILD_ROOT 
mkdir $RPM_BUILD_ROOT

%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" \
./configure --prefix=%{prefix} \
	    --localstatedir=%{localstatedir} \
	    --sysconfdir=%{_sysconfdir} \
	    --libdir=%{_libdir} \
	    --mandir=%{_mandir} \
	    --with-omfdirs=/opt/gnome/share/omf:/opt/gnome2/share/omf \
	    --enable-nls
make -j 2

%install
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make DESTDIR=$RPM_BUILD_ROOT install-strip
%{INSTALL_DIR} %{buildroot}/sbin/conf.d
unset GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL

cd $RPM_BUILD_ROOT


find . -type d -fprint $RPM_BUILD_DIR/file.list.%{name}.dirs
find . -type f -fprint $RPM_BUILD_DIR/file.list.%{name}.files.tmp
sed '/\/man\//s/$/.gz/g' $RPM_BUILD_DIR/file.list.%{name}.files.tmp > $RPM_BUILD_DIR/file.list.%{name}.files
find . -type l -fprint $RPM_BUILD_DIR/file.list.%{name}.libs
sed '1,2d;s,^\.,\%attr(-\,root\,root) \%dir ,' $RPM_BUILD_DIR/file.list.%{name}.dirs > $RPM_BUILD_DIR/file.list.%{name}
sed 's,^\.,\%attr(-\,root\,root) ,' $RPM_BUILD_DIR/file.list.%{name}.files >> $RPM_BUILD_DIR/file.list.%{name}
sed 's,^\.,\%attr(-\,root\,root) ,' $RPM_BUILD_DIR/file.list.%{name}.libs >> $RPM_BUILD_DIR/file.list.%{name}

%post
echo "Installing catalog..."
/usr/bin/xmlcatalog --noout --add "public" \
    "-//OMF//DTD Scrollkeeper OMF Variant V1.0//EN" \
    "`echo "/usr/share/xml/scrollkeeper/dtds/scrollkeeper-omf.dtd" |sed -e "s://://:g"`" \
    /etc/xml/catalog
echo "Rebuilding Scrollkeeper database..."
scrollkeeper-rebuilddb -q -p /var/lib/scrollkeeper
echo "Updating Scrollkeeper database..."
scrollkeeper-update -v &>${T}/foo

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
- initial build for The Gnome for SuSE Project <0.3.11>