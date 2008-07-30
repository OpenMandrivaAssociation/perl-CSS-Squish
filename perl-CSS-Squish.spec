%define module   CSS-Squish

Name:		perl-%{module}
Version:    0.07
Release:    %mkrel 3
License:	Artistic or GPL
Group:		Development/Perl
Summary:    Compact many CSS files into one big file 
Url:		http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/CSS/%{module}-%{version}.tar.gz
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::LongString)
BuildRequires:  perl(URI)
BuildArch:      noarch
BuildRoot:	    %{_tmppath}/%{name}-%{version}

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
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES README
%{perl_vendorlib}/CSS/
%{_mandir}/man3/*


