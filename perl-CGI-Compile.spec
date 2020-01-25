#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	CGI
%define		pnam	Compile
Summary:	CGI::Compile - Compile .cgi scripts to a code reference like ModPerl::Registry
Name:		perl-CGI-Compile
Version:	0.22
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/CGI/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a6b364e8f3eb45f63d69ae6d5602eb21
URL:		http://search.cpan.org/dist/CGI-Compile/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(File::pushd)
BuildRequires:	perl(Test::NoWarnings)
BuildRequires:	perl-Test-Requires
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CGI::Compile is an utility to compile CGI scripts into a code
reference that can run many times on its own namespace, as long as the
script is ready to run on a persistent environment.

NOTE: for best results, load CGI::Compile before any modules used by
your CGIs.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
        --destdir=$RPM_BUILD_ROOT \
        --installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/CGI/*.pm
%{_mandir}/man3/*
