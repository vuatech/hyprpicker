Name:           hyprpicker
Version:        0.3.0
Release:        1
Summary:        A wlroots-compatible Wayland color picker
Group:          Utility/Hyrpland
License:        BSD-3-Clause AND HPND-sell-variant
URL:            https://github.com/hyprwm/hyprpicker
Source0:        https://github.com/hyprwm/hyprpicker/archive/v%{version}/%{name}-%{version}.tar.gz

# Upstream, fix build with Clang (error: invalid argument '-std=c++23' not allowed with 'C')
Patch0:        https://github.com/hyprwm/hyprpicker/commit/36d974181da499369fcf3cb78792a3553fbd37ea.patch

BuildRequires:  cmake
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(xkbcommon)

Recommends:     wl-clipboard

%description
A wlroots-compatible Wayland color picker that does not suck.

%prep
%autosetup -p1

%build
%cmake \
        -DCMAKE_INSTALL_MANDIR=%{_mandir} \
        -DCMAKE_BUILD_TYPE:STRING=Release
%make_build

%install
%make_install -C build

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*
