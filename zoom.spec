%define name	zoom 
%define version 1.1.4
%define release %mkrel 1

Name:           %{name}
Summary:        Z-Machine: it plays text adventure games written in ZCode
Version:        %{version}
Release:        %{release}
URL:            http://www.logicalshift.co.uk/unix/zoom/ 
Source0:        http://www.logicalshift.co.uk/unix/zoom/%{name}-%{version}.tar.gz
Patch0:		zoom-1.1.3-enable-antialiasing.patch
License:        GPLv2+ 
Group:          Games/Other
#BuildRequires:	xorg-x11-devel fontconfig-devel zlib-devel libpng-devel t1lib-devel #from ALT linux
BuildRequires:  X11-devel libxrender-devel
BuildRequires:	libpng-devel t1lib-devel libxft-devel fontconfig-devel zlib-devel
BuildRoot:      %{_tmppath}/%{name}-buildroot

%description
Zoom is an interpreter for playing all of Infocom's text adventures and
newer games using the same format (Z-CODE), like the ones produced using
the Inform compiler.

It has a fast interpreter core behind an X11 interface.

%prep
%setup -q
%patch0 -p0

%build
%configure --bindir=%{_gamesbindir} --datadir=%{_gamesdatadir}
%make

%install
rm -rf %{buildroot}
%makeinstall bindir=%{buildroot}%{_gamesbindir} datadir=%{buildroot}%{_gamesdatadir}
mkdir %{buildroot}%{_gamesdatadir}/%{name}/games

%clean
rm manual/Makefile* -f
rm -rf %{buildroot}

%files
%defattr(-,root,root,0755)
%doc AUTHORS COPYING ChangeLog NEWS README THANKS TODO manual
%{_gamesbindir}/%name
%dir %_gamesdatadir/%name
%_gamesdatadir/%name/%{name}rc
%dir %_gamesdatadir/%name/games
