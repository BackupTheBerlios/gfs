Name: libbonobo
Summary: A CORBA framework
Version: 2.2.1
Release: 1.gfs
License: GPL
Group: Development/Libraries/GNOME
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/build-root-%{name}
Requires: glib2 >= 2.2
Requires: orbit2 >= 2.4
Requires: bonobo-activation >= 2.2.1.1
Packager: Hendrik Brandt
Distribution: SuSE
Prefix: /opt/gnome2
%define sysconfdir /etc%prefix
Url: http://www.gnome.org
Vendor: The Gnome for SuSE Project
Docdir: %prefix/doc

%description
A CORBA framework

%prep
rm -rf $RPM_BUILD_ROOT 
mkdir $RPM_BUILD_ROOT

%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" \
./configure --prefix=%{prefix} \
	    --libdir=%{prefix}/%_lib \
	    --sysconfdir=%{sysconfdir} \
	    --disable-gtk-doc \
	    $MYARCH_FLAGS

make 

%install
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make DESTDIR=$RPM_BUILD_ROOT install-strip
mkdir -p $RPM_BUILD_ROOT/usr/%_lib/pkgconfig
cp $RPM_BUILD_ROOT/%{prefix}/%_lib/pkgconfig/*.pc $RPM_BUILD_ROOT/usr/%_lib/pkgconfig/
for FILE in "$RPM_BUILD_ROOT/bin/*"; do
    file "$FILE" | grep -q not\ stripped && strip $FILE
done
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
* Tue Mar 18 2003 - hendrik
- update to 2.2.1

* Wed Feb 19 2003 - Hendrik Brandt
- initial build for The Gnome for SuSE Project <2.2.0>