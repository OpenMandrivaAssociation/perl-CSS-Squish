%define upstream_name    CSS-Squish
%define upstream_version 0.10
Name:		perl-%{upstream_name}
Version:	0.10
Release:	4

Summary:	Compact many CSS files into one big file 
License:	Artistic or GPL+
Group:		Development/Perl
Url:		https://metacpan.org/dist/CSS-Squish
Source0:	https://cpan.metacpan.org/authors/id/T/TS/TSIBLEY/CSS-Squish-0.10.tar.gz

BuildRequires:	make
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
%setup -q -n CSS-Squish-0.10

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# soft: do not fail package on test failures
set +e
make test

%install
%makeinstall_std

%files
%doc CHANGES README
%{perl_vendorlib}/CSS/
%{_mandir}/man3/*


