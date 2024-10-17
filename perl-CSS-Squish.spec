%define upstream_name    CSS-Squish
%define upstream_version 0.10

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Compact many CSS files into one big file 
License:	Artistic or GPL+
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/CSS/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Test::LongString)
BuildRequires:	perl(URI)
BuildArch:	noarch

%description
This module takes a list of CSS files and concatenates them, making sure to 
honor any valid @import statements included in the files.

Following the CSS 2.1 spec, @import statements must be the first rules in 
a CSS file. Media-specific @import statements will be honored by enclosing 
the included file in an @media rule. This has the side effect of actually 
improving compatibility in Internet Explorer, which ignores media-specific 
@import rules but understands @media rules.

It is possible that feature versions will include methods to compact 
whitespace and other parts of the CSS itself, but this functionality 
is not supported at the current time.

%prep
%setup -q -n CSS-Squish-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc CHANGES README
%{perl_vendorlib}/CSS/
%{_mandir}/man3/*


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.100.0-2mdv2011.0
+ Revision: 680706
- mass rebuild

* Mon Nov 08 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.100.0-1mdv2011.0
+ Revision: 595092
- update to new version 0.10

* Fri Jan 15 2010 Jérôme Quelin <jquelin@mandriva.org> 0.90.0-1mdv2011.0
+ Revision: 491624
- update to 0.09

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.80.0-1mdv2010.0
+ Revision: 405958
- rebuild using %%perl_convert_version

* Thu May 07 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.08-1mdv2010.0
+ Revision: 373003
- new version

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.07-3mdv2009.0
+ Revision: 256383
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun Nov 11 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.07-1mdv2008.1
+ Revision: 107974
- update to new version 0.07

* Wed Nov 07 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.06-1mdv2008.1
+ Revision: 106811
- update to new version 0.06


* Thu Dec 14 2006 Michael Scherer <misc@mandriva.org> 0.05-1mdv2007.0
+ Revision: 97024
- Import perl-CSS-Squish

* Thu Dec 14 2006 Michael Scherer <misc@mandriva.org> 0.05-1mdv2007.1
- First Mandriva package

