%{?scl:%scl_package perl-IPC-System-Simple }

Name:		%{?scl_prefix}perl-IPC-System-Simple 
Version:	1.25
Release:	11%{?dist}
License:	GPL+ or Artistic 
Group:		Development/Libraries
Summary:	Run commands simply, with detailed diagnostics 
URL:		http://search.cpan.org/dist/IPC-System-Simple
Source0:	http://search.cpan.org/CPAN/authors/id/P/PJ/PJF/IPC-System-Simple-%{version}.tar.gz 
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(id -un)
BuildArch:	noarch
BuildRequires:	%{?scl_prefix}perl-generators
BuildRequires:	%{?scl_prefix}perl(BSD::Resource)
BuildRequires:	%{?scl_prefix}perl(Carp)
BuildRequires:	%{?scl_prefix}perl(Config)
BuildRequires:	%{?scl_prefix}perl(constant)
BuildRequires:	%{?scl_prefix}perl(Exporter)
BuildRequires:	%{?scl_prefix}perl(ExtUtils::MakeMaker) >= 6.30
BuildRequires:	%{?scl_prefix}perl(File::Basename)
BuildRequires:	%{?scl_prefix}perl(File::Spec)
BuildRequires:	%{?scl_prefix}perl(List::Util)
%if !%{defined perl_small}
BuildRequires:	%{?scl_prefix}perl(Pod::Coverage::TrustPod)
%endif
BuildRequires:	%{?scl_prefix}perl(POSIX)
BuildRequires:	%{?scl_prefix}perl(re)
BuildRequires:	%{?scl_prefix}perl(Scalar::Util)
BuildRequires:	%{?scl_prefix}perl(strict)
BuildRequires:	%{?scl_prefix}perl(Test)
BuildRequires:	%{?scl_prefix}perl(Test::More)
BuildRequires:	%{?scl_prefix}perl(Test::NoWarnings)
%if !%{defined perl_small}
%if !%{defined perl_bootstrap}
# Break build-cycle: perl-IPC-System-Simple → perl-Test-Perl-Critic
# → perl-Perl-Critic → perl-PPI → perl-IO-All → perl-File-MimeInfo
# → perl-File-BaseDir → perl-IPC-System-Simple
BuildRequires:	%{?scl_prefix}perl(Test::Perl::Critic)
%endif
BuildRequires:	%{?scl_prefix}perl(Test::Pod)
BuildRequires:	%{?scl_prefix}perl(Test::Pod::Coverage) >= 1.08
%endif
BuildRequires:	%{?scl_prefix}perl(warnings)
Requires:	%{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))

%description
Calling Perl's in-built 'system()' function is easy; determining if it
was successful is _hard_. Let's face it, '$?' isn't the nicest variable
in the world to play with, and even if you _do_ check it, producing a
well-formatted error string takes a lot of work. 'IPC::System::Simple'
takes the hard work out of calling external commands. In fact, if you
want to be really lazy, you can just write: 

    use IPC::System::Simple qw(system);

and all of your "system" commands will either succeed (run to completion and
return a zero exit value), or die with rich diagnostic messages.

%prep
%setup -q -n IPC-System-Simple-%{version}

# Avoid doc-file dependencies
chmod -c -x examples/*.pl

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor && make %{?_smp_mflags}%{?scl:'}

%install
rm -rf %{buildroot}
%{?scl:scl enable %{scl} '}make pure_install DESTDIR=%{buildroot}%{?scl:'}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
%{_fixperms} %{buildroot}

%check
%{?scl:scl enable %{scl} '}make test TEST_AUTHOR=1 AUTHOR_TESTING=1 RELEASE_TESTING=1%{?scl:'}

%clean
rm -rf %{buildroot}

%files
%doc Changes LICENSE README examples/
%{perl_vendorlib}/IPC/
%{_mandir}/man3/IPC::System::Simple.3pm*

%changelog
* Tue Jul 19 2016 Petr Pisar <ppisar@redhat.com> - 1.25-11
- SCL

* Wed May 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.25-10
- Perl 5.24 re-rebuild of bootstrapped packages

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.25-9
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.25-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.25-6
- Perl 5.22 re-rebuild of bootstrapped packages

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.25-5
- Perl 5.22 rebuild

* Tue Apr 21 2015 Petr Pisar <ppisar@redhat.com> - 1.25-4
- Break build-cycle: perl-IPC-System-Simple → perl-Test-Perl-Critic
  → perl-Perl-Critic → perl-PPI → perl-IO-All → perl-File-MimeInfo
  → perl-File-BaseDir → perl-IPC-System-Simple


* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.25-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Oct 20 2013 Paul Howarth <paul@city-fan.org> - 1.25-1
- Update to 1.25
  - No longer ship unrequired file Debian_CPANTS.txt (GH #7)

* Fri Oct 18 2013 Paul Howarth <paul@city-fan.org> - 1.24-1
- Update to 1.24
  - No longer mark BSD::Resource as required (GH #6)
  - Skip core-dump tests on OS X; they're not as straightforward as the test
    script would like (GH #5)

* Wed Oct  9 2013 Paul Howarth <paul@city-fan.org> - 1.23-1
- Update to 1.23
  - Silence "Statement unlikely to be reached" warning
  - Repository information fix, and typo fixes
  - Converted to using dzil
- Specify all dependencies
- Don't need to remove empty directories from the buildroot
- Restore EL-5 compatibility

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.21-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 31 2013 Petr Pisar <ppisar@redhat.com> - 1.21-7
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.21-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.21-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 23 2012 Petr Pisar <ppisar@redhat.com> - 1.21-4
- Perl 5.16 rebuild

* Thu Jan 12 2012 Paul Howarth <paul@city-fan.org> - 1.21-3
- Run author tests too for completeness
- Add buildreqs needed for author tests
- Add buildreqs for core perl modules, which may be dual-lived
- Use DESTDIR rather than PERL_INSTALL_ROOT
- Make %%files list more explicit

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 1.21-2
- Perl mass rebuild

* Fri Mar 18 2011 Iain Arnell <iarnell@gmail.com> - 1.21-1
- Update to latest upstream version
- Clean up spec for modern rpmbuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.18-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 20 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.18-5
- Rebuild to fix problems with vendorarch/lib (#661697)

* Sun May 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.18-4
- Mass rebuild with perl-5.12.0

* Mon Dec 07 2009 Stepan Kasal <skasal@redhat.com> - 1.18-3
- Rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Mar 05 2009 Chris Weyl <cweyl@alumni.drew.edu> - 1.18-1
- Submission

* Thu Mar 05 2009 Chris Weyl <cweyl@alumni.drew.edu> - 1.18-0
- Initial RPM packaging
- Generated with cpan2dist (CPANPLUS::Dist::RPM version 0.0.8)

