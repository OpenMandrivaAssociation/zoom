%define name	zoom 
%define version 1.1.4
%define release %mkrel 2

Name:           %{name}
Summary:        Z-Machine: it plays text adventure games written in ZCode
Version:        %{version}
Release:        %{release}
URL:            http://www.logicalshift.co.uk/unix/zoom/ 
Source0:        http://www.logicalshift.co.uk/unix/zoom/%{name}-%{version}.tar.gz
Patch0:		zoom-1.1.3-enable-antialiasing.patch
Patch1:		zoom-1.1.4-xft.patch
License:        GPLv2+ 
Group:          Games/Other
BuildRequires:	libx11-devel
BuildRequires:	libxext-devel
BuildRequires:	libxrender-devel
BuildRequires:	libxft-devel
BuildRequires:	libpng-devel
BuildRequires:	t1lib-devel
BuildRoot:      %{_tmppath}/%{name}-buildroot

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
rm -rf %{buildroot}
%makeinstall_std
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
