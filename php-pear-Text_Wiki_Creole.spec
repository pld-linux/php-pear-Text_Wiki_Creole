%include	/usr/lib/rpm/macros.php
%define		_class		Text
%define		_subclass	Wiki_Creole
%define		_status		stable
%define		_pearname	Text_Wiki_Creole
Summary:	%{_pearname} - Creole parser and renderer for Text_Wiki
Summary(pl):	%{_pearname} - parser i renderer Creole dla Text_Wiki
Name:		php-pear-%{_pearname}
Version:	1.0.0
Release:	0.1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	947fe4e75dcc949e431c313462a41df5
URL:		http://pear.php.net/package/Text_Wiki_Creole/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-PEAR >= 1.4.0b1
Requires:	php-pear-Text_Wiki >= 1.0.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Parses Creole mark-up to tokenize the text for Text_Wiki rendering and
also renders for wiki conversion. You can see a reference for this
syntax here: http://www.wikicreole.org/

In PEAR status of this package is: %{_status}.

%description -l pl
Klasa ta parsuje znaczniki Creole w celu rozk�adu tekstu dla
renderingu Text_Wiki jak i konwersji mi�dzy wiki. Opis sk�adni
dost�pny jest pod adresem: http://www.wikicreole.org/

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Text/Wiki/Parse/Creole
%{php_pear_dir}/Text/Wiki/Render/Creole
%{php_pear_dir}/Text/Wiki/Render/Creole.php
%{php_pear_dir}/Text/Wiki/Creole.php
