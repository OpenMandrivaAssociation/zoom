%define _disable_lto 1

Name:		zoom
Version:	1.1.5
Release:	4
Summary:	Z-Machine: it plays text adventure games written in ZCode
Group:		Games/Other
License:	GPLv2+
URL:		http://www.logicalshift.co.uk/unix/zoom/
Source0:	http://www.logicalshift.co.uk/unix/zoom/%{name}-%{version}.tar.gz
Patch0:		zoom-1.1.3-enable-antialiasing.patch
Patch1:		zoom-1.1.4-xft.patch
Patch2:		zoom-1.1.5-automake1.13.patch
Patch3:		zoom-1.1.5-clang.patch
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xrender) >= 0.9.6
BuildRequires:	pkgconfig(xft)
BuildRequires:	png-devel
BuildRequires:	t1lib-devel

%description
Zoom is an interpreter for playing all of Infocom's text adventures and
newer games using the same format (Z-CODE), like the ones produced using
the Inform compiler.

It has a fast interpreter core behind an X11 interface.

%prep
%setup -q
%patch0 -p0
%patch1 -p0 -b .xft
%patch2 -p0 -b .autoconf113
%patch3 -p1

%build
autoreconf -fi -Im4
%configure2_5x --bindir=%{_gamesbindir} --datadir=%{_gamesdatadir}
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std
%__mkdir_p %{buildroot}%{_gamesdatadir}/%{name}/games
%__rm -f manual/Makefile*

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root,0755)
%doc AUTHORS COPYING ChangeLog NEWS README THANKS TODO manual
%{_gamesbindir}/%{name}
%dir %{_gamesdatadir}/%{name}
%{_gamesdatadir}/%{name}/%{name}rc
%dir %{_gamesdatadir}/%{name}/games


%changelog
* Fri Mar 30 2012 Andrey Bondrov <abondrov@mandriva.org> 1.1.5-1mdv2011.0
+ Revision: 788381
- New version 1.1.5, spec cleanup, update BR

* Fri Jan 21 2011 Funda Wang <fwang@mandriva.org> 1.1.4-2
+ Revision: 631999
- check libxft via pkgconfig
- drop unused lib check

* Tue Jun 02 2009 Samuel Verschelde <stormi@mandriva.org> 1.1.4-1mdv2010.0
+ Revision: 382278
- update to new version 1.1.4

* Fri May 22 2009 Samuel Verschelde <stormi@mandriva.org> 1.1.3-1mdv2010.0
+ Revision: 378684
- fix buildrequires
- import zoom


