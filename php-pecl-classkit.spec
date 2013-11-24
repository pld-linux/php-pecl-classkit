%define		php_name	php%{?php_suffix}
%define		modname	classkit
%define		status		beta
Summary:	%{modname} - runtime redefinition of class methods
Summary(pl.UTF-8):	%{modname} - modyfikacja metod klasy w czasie działania skryptu
Name:		%{php_name}-pecl-%{modname}
Version:	0.4
Release:	3
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{modname}-%{version}.tgz
# Source0-md5:	3d04b0998e03e2375dfa2e118afeaaf3
URL:		http://pecl.php.net/package/classkit/
BuildRequires:	%{php_name}-devel >= 3:5.0.0
BuildRequires:	rpmbuild(macros) >= 1.650
%{?requires_php_extension}
Requires:	php(core) >= 5.0.4
Obsoletes:	php-pear-%{modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Allows a running script to add, remove, rename, and redefine class
methods without reloading.

In PECL status of this extension is: %{status}.

%description -l pl.UTF-8
To rozszerzenie pozwala na dodawanie, usuwanie, zmianę nazwy oraz
redefiniowanie metod klasy bez konieczności ponownego uruchamiania
skryptu.

To rozszerzenie ma w PECL status: %{status}.

%prep
%setup -qc
mv %{modname}-%{version}/* .

%build
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_sysconfdir}/conf.d,%{php_extensiondir}}

install -p modules/%{modname}.so $RPM_BUILD_ROOT%{php_extensiondir}
cat <<'EOF' > $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/%{modname}.ini
; Enable %{modname} extension module
extension=%{modname}.so
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%php_webserver_restart

%postun
if [ "$1" = 0 ]; then
	%php_webserver_restart
fi

%files
%defattr(644,root,root,755)
%doc README
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/%{modname}.ini
%attr(755,root,root) %{php_extensiondir}/%{modname}.so
