Summary:	A simple client for BitMover
Name:		bkf
Version:	2.0
Release:	3
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



%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 2.0-2mdv2011.0
+ Revision: 610075
- rebuild

* Sun Jan 17 2010 Oden Eriksson <oeriksson@mandriva.com> 2.0-1mdv2010.1
+ Revision: 492752
- import bkf


* Sun Jan 17 2010 Oden Eriksson <oeriksson@mandriva.com> 2.0-1mdv2010.0
- renamed to just bkf
- license is now GPLv2

* Thu Jan 11 2007 Oden Eriksson <oeriksson@mandriva.com> 2.0-1mdv2007.1
- initial Mandriva package
