Summary:	X.org video driver for VIA Unichrome graphics chipsets
Summary(pl.UTF-8):	Sterownik obrazu X.org dla układów zintegrowanych VIA Unichrome
Name:		xorg-driver-video-openchrome
Version:	0.5.0
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-openchrome-%{version}.tar.bz2
# Source0-md5:	316aaf97eb152eef71dac70c349fb8c7
URL:		http://www.openchrome.org/
BuildRequires:	Mesa-libGL-devel
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libdrm-devel >= 2.4.4
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 1.389
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXvMC-devel
BuildRequires:	xorg-lib-libpciaccess-devel >= 0.11.0
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-glproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-proto-xextproto-devel >= 7.0.99.1
BuildRequires:	xorg-proto-xf86driproto-devel
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xorg-xserver-server-devel >= 1.0.99.901
%{?requires_xorg_xserver_videodrv}
Requires:	libdrm >= 2.4.4
Requires:	xorg-lib-libpciaccess >= 0.11.0
Requires:	xorg-xserver-libdri >= 1.0.99.901
Requires:	xorg-xserver-libglx >= 1.0.99.901
Requires:	xorg-xserver-server >= 1.0.99.901
Provides:	xorg-driver-video
Obsoletes:	X11-driver-via < 1:7.0.0
Obsoletes:	XFree86-driver-via < 1:7.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for VIA chipsets with integrated Unichrome graphics
engine.

It supports the following VIA chipsets:
- CLE266 (VT3122),
- CN400, CN700,
- KM400/KN400/P4M800 (VT3205),
- K8M800/K8N800 (VT3204),
- PM800/PM880/PN800/CN400 (VT3259),
- VM800/VN800/CN700/P4M800Pro (VT3314),
- CX700 (VT3324),
- P4M890 (VT3327),
- K8M890/K8N890 (VT3336),
- P4M900/CN896/VN896 (VT3364),
- VX800 (VT3353),
- VX855 (VT3409),
- VX900 (VT3410).

%description -l pl.UTF-8
Sterownik obrazu X.org do układów VIA ze zintegrowanym silnikiem
graficznym Unichrome.

Obsługuje układy VIA:
- CLE266 (VT3122),
- CN400, CN700,
- KM400/KN400/P4M800 (VT3205),
- K8M800/K8N800 (VT3204),
- PM800/PM880/PN800/CN400 (VT3259),
- VM800/VN800/CN700/P4M800Pro (VT3314),
- CX700 (VT3324),
- P4M890 (VT3327),
- K8M890/K8N890 (VT3336),
- P4M900/CN896/VN896 (VT3364),
- VX800 (VT3353),
- VX855 (VT3409),
- VX900 (VT3410).

%prep
%setup -q -n xf86-video-openchrome-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la \
	$RPM_BUILD_ROOT%{_libdir}/libchromeXvMC*.{la,so}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/openchrome_drv.so
%ifarch %{ix86} %{x8664}
%attr(755,root,root) %{_libdir}/libchromeXvMC.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libchromeXvMC.so.1
%attr(755,root,root) %{_libdir}/libchromeXvMCPro.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libchromeXvMCPro.so.1
%endif
%{_mandir}/man4/openchrome.4*
