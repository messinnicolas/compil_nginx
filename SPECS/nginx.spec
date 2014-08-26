Name:		nginx
Version:	1.7.4
Release:	1.7.4
Summary:	Nginx is an open source server web

Group:		System Environment/Base
License:	Nginx
URL:		http://nginx.com
Source0:	http://nginx.org/download/nginx-1.7.4.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-root-%(%{__id_u} -n)

BuildArch:	noarch

%description
Nginx is the must opensource web server

%prep
%setup -n %{name}-%{version}

%build

%install
mkdir -p %{buildroot}%{_libdir}/%{name}-%{version}-%{release}/
cp -fr * %{buildroot}%{_libdir}/%{name}-%{version}-%{release}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)

%changelog
* Tue Aug 26 2014 messinnicolas <messinnicolas@gmail.com> - 1-0
- Initial Package
