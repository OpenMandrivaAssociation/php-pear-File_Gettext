%define	_class	File
%define	_subclass	Gettext
%define	modname	%{_class}_%{_subclass}

Name:		php-pear-%{modname}
Version:	0.4.2
Release:	3
Summary:	GNU Gettext file parser
License:	PHP License
Group:		Development/PHP
Url:		http://pear.php.net/package/File_Gettext/
Source0:	http://download.pear.php.net/package/File_Gettext-%{version}.tgz
BuildArch:	noarch
BuildRequires:	php-pear
Requires(post,preun):	php-pear
Requires:	php-pear

%description
Reader and writer for GNU PO and MO files.

%prep
%setup -qc
mv package.xml %{modname}-%{version}/%{modname}.xml

%install
cd %{modname}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{modname}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{modname}.xml %{buildroot}%{_datadir}/pear/packages

%files
%{_datadir}/pear/%{_class}
%{_datadir}/pear/data/%{modname}
%{_datadir}/pear/packages/%{modname}.xml

