%define		_modname	classkit
%define		_status		beta

Summary:	%{_modname} - runtime redefinition of class methods
Summary(pl):	%{_modname} - modyfikacja metod klasy w czasie dzia³ania skryptu
Name:		php-pecl-%{_modname}
Version:	0.1.1
Release:	1
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_modname}-%{version}.tgz
# Source0-md5:	f5f71a6c9e31248d803f541c34ea866a
URL:		http://pecl.php.net/package/classkit/
BuildRequires:	libtool
BuildRequires:	php-devel >= 3:5.0.0
Requires:	php-common >= 3:5.0.0
Obsoletes:	php-pear-%{_modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/php
%define		extensionsdir	%{_libdir}/php

%description
Allows a running script to add, remove, rename, and redefine class
methods without reloading.

In PECL status of this extension is: %{_status}.

%description -l pl
To rozszerzenie pozwala na dodawanie, usuwanie, zmianê nazwy oraz
redefiniowanie metod klasy bez konieczno¶ci ponownego uruchamiania
skryptu.

To rozszerzenie ma w PECL status: %{_status}.

%prep
%setup -q -c

%build
cd %{_modname}-%{version}
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{extensionsdir}

install %{_modname}-%{version}/modules/%{_modname}.so $RPM_BUILD_ROOT%{extensionsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/php-module-install install %{_modname} %{_sysconfdir}/php-cgi.ini

%preun
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove %{_modname} %{_sysconfdir}/php-cgi.ini
fi

%files
%defattr(644,root,root,755)
%doc %{_modname}-%{version}/README
%attr(755,root,root) %{extensionsdir}/%{_modname}.so
