%define realname   CSS-Squish

Name:		perl-%{realname}
Version:    0.06
Release:    %mkrel 1
License:	Artistic or GPL
Group:		Development/Perl
Summary:    Compact many CSS files into one big file 
Source0:    ftp://ftp.perl.org/pub/CPAN/modules/by-module/CSS/CSS-Squish-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{realname}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(File::Spec)
BuildRequires: perl(Test::LongString)
BuildArch: noarch

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
%setup -q -n CSS-Squish-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc CHANGES README
%{perl_vendorlib}/CSS/
%{_mandir}/man3/*


