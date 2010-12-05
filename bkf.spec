Summary:	A simple client for BitMover
Name:		bkf
Version:	2.0
Release:	%mkrel 2
License:	GPLv2
Group:		Development/Other
URL:		http://www.bitkeeper.com/
Source0:	http://www.bitmover.com/bk-client%{version}.shar.bz2
Patch0:		bk-client-2.0-conflicting_types_for_getline_fix.diff
Requires:	patch
BuildRequires:	sharutils
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
A simple client for BitMover

%prep

%setup -q -c -T -n %{name}-%{version}
bzcat %{SOURCE0} > bk-client%{version}.shar
sh bk-client%{version}.shar
mv bk-client%{version}/* .
rm -rf bk-client%{version}
%patch0 -p0 -b .conflicting_types_for_getline

head -7 bkf.c > LICENSE

%build
gcc %{optflags} bkf.c -o bkf

%install 
rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -m0755 bkf %{buildroot}%{_bindir}/

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc demo.sh LICENSE
%attr(0755,root,root) %{_bindir}/bkf

