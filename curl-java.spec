Summary:	Java wrapper to the curl library
Name:		curl-java
Version:	0.2.3
Release:	3
Group:		Development/Java
License:	MIT
URL:		http://curl.haxx.se/libcurl/java/
Source0:	http://www.gknw.de/mirror/curl/curl_java/%{name}-%{version}.tar.bz2
BuildRequires:	java-rpmbuild
BuildRequires:	curl-devel
Requires:	curl
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
This package allows to use the curl API library (http://curl.haxx.se/libcurl/)
from a Java program.
  This is not (yet) a complete interface implementation: it is however possible
to send and/or receive data via specific subclassing.

%prep
%setup -q

%build
%configure2_5x \
	--with-jdk-home=%{java_home}
%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std
#	We do not need .la files since dynamic library is never ld-linked.
rm -rf %{buildroot}%{_libdir}/*.la

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog README
%{_libdir}/*.so*
%{_datadir}/java/*.jar


%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2.3-2mdv2011.0
+ Revision: 610178
- rebuild

* Sun Apr 18 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.3-1mdv2010.1
+ Revision: 536071
- import curl-java


