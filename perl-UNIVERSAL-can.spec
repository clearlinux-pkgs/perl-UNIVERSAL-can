#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-UNIVERSAL-can
Version  : 1.20140328
Release  : 6
URL      : https://cpan.metacpan.org/authors/id/C/CH/CHROMATIC/UNIVERSAL-can-1.20140328.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/C/CH/CHROMATIC/UNIVERSAL-can-1.20140328.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libu/libuniversal-can-perl/libuniversal-can-perl_1.20140328-1.debian.tar.xz
Summary  : 'work around buggy code calling UNIVERSAL::can() as a function'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl Artistic-2.0 GPL-1.0 GPL-2.0 MIT
Requires: perl-UNIVERSAL-can-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
UNIVERSAL::can
--------------
This module attempts to work around people calling UNIVERSAL::can() as a
function, which it is not.

%package dev
Summary: dev components for the perl-UNIVERSAL-can package.
Group: Development
Provides: perl-UNIVERSAL-can-devel = %{version}-%{release}

%description dev
dev components for the perl-UNIVERSAL-can package.


%package license
Summary: license components for the perl-UNIVERSAL-can package.
Group: Default

%description license
license components for the perl-UNIVERSAL-can package.


%prep
%setup -q -n UNIVERSAL-can-1.20140328
cd ..
%setup -q -T -D -n UNIVERSAL-can-1.20140328 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/UNIVERSAL-can-1.20140328/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-UNIVERSAL-can
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-UNIVERSAL-can/LICENSE
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-UNIVERSAL-can/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/UNIVERSAL/can.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/UNIVERSAL::can.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-UNIVERSAL-can/LICENSE
/usr/share/package-licenses/perl-UNIVERSAL-can/deblicense_copyright
