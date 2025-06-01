Name:		picom
Version:	12.4
Release:	1
Source0:	https://github.com/yshui/picom/archive/v%{version}/%{name}-v%{version}.tar.gz
Summary:	picom is a compositor for X, and a fork of Compton.
URL:		https://github.com/yshui/picom
License:	MPL-2.0 AND MIT
Group:		System/X11/Other
BuildRequires:	meson
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(x11-xcb)
BuildRequires:	pkgconfig(xcb)
BuildRequires:	pkgconfig(xcb-util)
BuildRequires:	pkgconfig(xcb-damage)
BuildRequires:	pkgconfig(xcb-xfixes)
BuildRequires:	pkgconfig(xcb-shape)
BuildRequires:	pkgconfig(xcb-render)
BuildRequires:	pkgconfig(xcb-renderutil)
BuildRequires:	pkgconfig(xcb-randr)
BuildRequires:	pkgconfig(xcb-composite)
BuildRequires:	pkgconfig(xcb-image)
BuildRequires:	pkgconfig(xcb-present)
BuildRequires:	pkgconfig(xcb-glx)
BuildRequires:	pkgconfig(pixman-1)
BuildRequires:	pkgconfig(libconfig)
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(egl)
BuildRequires:	pkgconfig(epoxy)
BuildRequires:	pkgconfig(libpcre2-8)
BuildRequires:	pkgconfig(libev)
BuildRequires:	uthash-devel

BuildSystem:	meson	

%description
picom is a compositor for X, and a fork of Compton.

%prep
%autosetup -p1

%files
%license	COPYING	LICENSE.spdx LICENSES/MIT	LICENSES/MPL-2.0
%doc		README.md	CONTRIBUTORS	picom.sample.conf	data/animation_presets.conf
%{_sysconfdir}/xdg/autostart/picom.desktop
%{_bindir}/compton*
%{_bindir}/picom*
%{_libdir}/pkgconfig/picom-api.pc
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/48x48/apps/compton.png
%{_datadir}/icons/hicolor/scalable/apps/compton.svg
