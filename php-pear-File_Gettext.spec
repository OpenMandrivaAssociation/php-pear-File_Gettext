%define		_class		File
%define		_subclass	Gettext
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	0.4.2
Release:	1
Summary:	GNU Gettext file parser
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/File_Gettext/
Source0:	http://download.pear.php.net/package/File_Gettext-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
Reader and writer for GNU PO and MO files.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/data/%{upstream_name}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.4.1-6mdv2011.0
+ Revision: 667497
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.4.1-5mdv2011.0
+ Revision: 607099
- rebuild

* Mon Dec 14 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.4.1-4mdv2010.1
+ Revision: 478667
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.4.1-3mdv2010.0
+ Revision: 426622
- rebuild

* Wed Dec 31 2008 Oden Eriksson <oeriksson@mandriva.com> 0.4.1-2mdv2009.1
+ Revision: 321812
- rebuild

* Sat Aug 16 2008 Oden Eriksson <oeriksson@mandriva.com> 0.4.1-1mdv2009.0
+ Revision: 272584
- 0.4.1

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.4.0-3mdv2009.0
+ Revision: 224733
- rebuild

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 0.4.0-2mdv2008.1
+ Revision: 178508
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Apr 20 2007 Oden Eriksson <oeriksson@mandriva.com> 0.4.0-1mdv2008.0
+ Revision: 15536
- 0.4.0


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 0.3.4-2mdv2007.0
+ Revision: 81090
- Import php-pear-File_Gettext

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 0.3.4-2mdk
- new group (Development/PHP)

* Mon Nov 07 2005 Oden Eriksson <oeriksson@mandriva.com> 0.3.4-1mdk
- 0.3.4

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 0.3.3-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 0.3.3-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 0.3.3-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 0.3.3-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 0.3.3-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 0.3.3-1mdk
- initial Mandriva package (PLD import)


