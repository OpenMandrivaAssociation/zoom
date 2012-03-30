Name:		zoom
Version:	1.1.5
Release:	%mkrel 1
Summary:	Z-Machine: it plays text adventure games written in ZCode
Group:		Games/Other
License:	GPLv2+
URL:		http://www.logicalshift.co.uk/unix/zoom/
Source0:	http://www.logicalshift.co.uk/unix/zoom/%{name}-%{version}.tar.gz
Patch0:		zoom-1.1.3-enable-antialiasing.patch
Patch1:		zoom-1.1.4-xft.patch
BuildRequires:	X11-devel
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
