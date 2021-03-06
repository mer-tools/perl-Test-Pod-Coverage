#specfile originally created for Fedora, modified for Moblin Linux
Name:           perl-Test-Pod-Coverage
Version:        0
Release:        1
Summary:        Check for pod coverage in your distribution

Group:          Development/Libraries
License:        GPL or Artistic
URL:            http://search.cpan.org/dist/Test-Pod-Coverage/
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  perl(Pod::Coverage)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Checks for POD coverage in files for your distribution.


%prep
%setup -q -n %{name}-%{version}


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*


%check
make test


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Changes
%{perl_vendorlib}/Test/
%doc %{_mandir}/man3/*.3pm*


