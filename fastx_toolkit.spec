%include	/usr/lib/rpm/macros.perl
Summary:	The FASTX-Toolkit is a collection of command line tools for Short-Reads FASTA/FASTQ files preprocessing
#Summary(pl.UTF-8):	-
Name:		fastx_toolkit
Version:	0.0.13
Release:	1
License:	AGPL v3
Group:		Applications/Science
Source0:	http://hannonlab.cshl.edu/fastx_toolkit/%{name}-%{version}.tar.bz2
# Source0-md5:	6d233ff4ae3d52c457d447179f073a56
URL:		http://hannonlab.cshl.edu/fastx_toolkit/index.html
BuildRequires:	libgtextutils-devel
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The FASTX-Toolkit is a collection of command line tools for
Short-Reads FASTA/FASTQ files preprocessing.

#%description -l pl.UTF-8

%prep
%setup -q

%{__sed} -i -e '1s,^#!.*bash,#!/bin/bash,' scripts/*.sh

%build
%configure \
	--disable-wall

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README THANKS
%attr(755,root,root) %{_bindir}/*
