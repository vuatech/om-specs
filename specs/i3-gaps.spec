%global __requires_exclude perl\\(AnyEvent::I3\\)

%global real_name i3
%global upstream_version 4.18

Name:           i3-gaps
Version:        4.21.1
Release:        1
Summary:        A fork of i3wm tiling window manager with more features, including gaps
License:        BSD
Group:          System/X11
URL:            https://github.com/Airblader/i3

Source0: 	https://github.com/Airblader/i3/releases/download/%{version}/%{real_name}-%{version}.tar.xz
Source1: 	%{real_name}-logo.svg

Patch1:		fix-ev.patch

BuildRequires: pkgconfig(libev)
BuildRequires: pkgconfig(xkbfile)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(yajl)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xcb-util)
BuildRequires: x11-proto-devel
BuildRequires: xcb-util-wm-devel
BuildRequires: pkgconfig(libev)
BuildRequires: meson
BuildRequires: bison
BuildRequires: doxygen
BuildRequires: flex
BuildRequires: asciidoc
BuildRequires: graphviz
BuildRequires: bzip2
BuildRequires: pkgconfig(xcb-cursor)
BuildRequires: pkgconfig(xcb-keysyms)
BuildRequires: pkgconfig(xcb-icccm)
BuildRequires: pkgconfig(xcb-xrm)
BuildRequires: pkgconfig(pango)
BuildRequires: pkgconfig(pangocairo)
BuildRequires: pkgconfig(libstartup-notification-1.0)
BuildRequires: pkgconfig(libpcre)
BuildRequires: pkgconfig(libpcre2-8)
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(xkbcommon-x11)
BuildRequires: pkgconfig(yajl)
BuildRequires: xmlto
BuildRequires: perl-ExtUtils-MakeMaker

Requires:       rxvt-unicode
Requires:       x11-apps
Recommends:     dmenu
#Recommends:     i3-gaps-doc
Recommends:	i3status
Conflicts:	i3-wm

%description
A fork of i3wm tiling window manager with more features, including gaps

#package doc
#Summary:        i3-gaps window manager documentation
#Group:          System/X11
#BuildRequires:  doxygen
#BuildArch:      noarch
#Requires:       %{name} = %{version}-%{release}
#Conflicts:	i3-doc
#
#description doc
#Asciidoc and doxygen documentations for i3-gaps.


%prep
%setup -q -n i3-%{version}
%autopatch -p1

%build
%meson

%meson_build

%install
%meson_install

mkdir -p %{buildroot}/%{_mandir}/man1/
install -Dpm0644 man/*.1 %{buildroot}/%{_mandir}/man1/

%posttrans
if [ "$1" -eq 1 ]; then
	if [ -e %{_datadir}/xsessions/31i3.desktop ]; then
		rm -rf %{_datadir}/xsessions/31i3.desktop
	fi
	if [ -e %{_sysconfdir}/X11/dm/Sessions/31i3.desktop ]; then
		rm -rf %{_sysconfdir}/X11/dm/Sessions/31i3.desktop
	fi
fi

%files
%defattr(-,root,root,-)
%doc LICENSE
%{_bindir}/%{real_name}*
%{_includedir}/%{real_name}/*
%dir %{_sysconfdir}/%{real_name}/
%config(noreplace) %{_sysconfdir}/%{real_name}/config
%config(noreplace) %{_sysconfdir}/%{real_name}/config.keycodes
%{_datadir}/xsessions/*.desktop
%{_mandir}/man*/%{real_name}*
#{_datadir}/pixmaps/i3*
%{_datadir}/applications/*.desktop
%exclude %{_docdir}/i3/*


#files doc
#defattr(-,root,root,-)
#doc docs/*.{html,png} pseudo-doc/doxygen/


%changelog
* Fri Feb 18 2011 Joao Victor Duarte Martins <jvdm@mandriva.com.br> 3.e.bf2-1mdv2011.0
+ Revision: 638328
- fix BuildRoot and add bzip2 to BuildRequires
- fix group tag
- fix package name and rename spec file
- First initial commit.
- create i3-wm

