%define upstream_name	 Reaper
%define upstream_version 1.00

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Support for reaping child processes via $SIG{CHLD} 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Reaper/%{upstream_name}-%{upstream_version}.tar.gz

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

Obsoletes: perl-reaper
Provides:  perl-reaper
Provides:  perl(reaper)

%description
Support for reaping child processes via $SIG{CHLD} 

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
find -type f | xargs chmod 644
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/*/*
