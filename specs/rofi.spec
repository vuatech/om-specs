Summary:	A window switcher, application launcher and dmenu replacement
Name:		rofi
Version:	1.7.8
Release:	1
License:	MIT
URL:		https://github.com/DaveDavenport/rofi
Source0:	https://github.com/DaveDavenport/rofi/releases/download/%{version}/%{name}-%{version}.tar.xz
BuildRequires:	meson
BuildRequires:	bison
BuildRequires:	doxygen
BuildRequires:	flex
BuildRequires:	graphviz
BuildRequires:	giflib-devel
BuildRequires:  pkgconfig(alsa)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(cairo-xcb)
BuildRequires:	pkgconfig(check) >= 0.11.0
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	pkgconfig(libstartup-notification-1.0)
BuildRequires:  pkgconfig(libmpdclient)
BuildRequires:  pkgconfig(libnl-3.0)
BuildRequires:	pkgconfig(pango)
BuildRequires:	pkgconfig(pangocairo)
BuildRequires:	pkgconfig(xcb)
BuildRequires:	pkgconfig(xcb-aux)
BuildRequires:	pkgconfig(xcb-ewmh)
BuildRequires:	pkgconfig(xcb-icccm)
BuildRequires:	pkgconfig(xcb-randr)
BuildRequires:	pkgconfig(xcb-xinerama)
BuildRequires:	pkgconfig(xcb-xkb)
BuildRequires:	pkgconfig(xcb-xrm)
BuildRequires:	pkgconfig(xcb-cursor)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	pkgconfig(xkbcommon-x11)
BuildRequires:	pkgconfig(xkeyboard-config)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-server)

# https://github.com/sardemff7/libgwater
Provides:	bundled(libgwater)
# https://github.com/sardemff7/libnkutils
Provides:	bundled(libnkutils)

Requires:	%{name}-themes = %{EVRD}

%description
Rofi is a dmenu replacement. Rofi, like dmenu, will provide the user with a
textual list of options where one or more can be selected. This can either be,
running an application, selecting a window or options provided by an external
script.

%package devel
Summary:	Development files for %{name}
Requires:	%{name} = %{EVRD}
%rename %{name}-devel-doc

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package themes
Summary:	Themes for %{name}
BuildArch:	noarch

%description themes
The %{name}-themes package contains themes for %{name}.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%ninja_install -C build

%files
%doc README.md
%license COPYING
%{_bindir}/rofi
%{_bindir}/rofi-sensible-terminal
%{_bindir}/rofi-theme-selector
%{_datadir}/applications/rofi-theme-selector.desktop
%{_datadir}/applications/rofi.desktop
%{_datadir}/icons/hicolor/scalable/apps/rofi.svg
%{_mandir}/man1/rofi*
%{_mandir}/man5/rofi*

%files themes
%license COPYING
%{_datarootdir}/rofi

%files devel
%{_includedir}/rofi
%{_libdir}/pkgconfig/rofi.pc
