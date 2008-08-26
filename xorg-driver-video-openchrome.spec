Summary:	X.org video driver for VIA Unichrome graphics chipsets
Summary(pl.UTF-8):	Sterownik obrazu X.org dla układów zintegrowanych VIA Unichrome
Name:		xorg-driver-video-openchrome
Version:	0.2.903
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-openchrome-%{version}.tar.bz2
# Source0-md5:	c0820787e89958c9114d359b6a3cd464
URL:		http://www.openchrome.org/
BuildRequires:	Mesa-libGL-devel
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libdrm-devel >= 2.0
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 1.389
BuildRequires:	xorg-lib-libXvMC-devel
BuildRequires:	xorg-lib-libpciaccess-devel >= 0.8.0
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-proto-xextproto-devel
BuildRequires:	xorg-proto-xf86driproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRequires:	xorg-xserver-server-devel >= 1.0.99.901
%requires_xorg_xserver_videodrv
Requires:	xorg-xserver-server >= 1.0.99.901
Obsoletes:	X11-driver-via < 1:7.0.0
Obsoletes:	XFree86-driver-via < 1:7.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for VIA chipsets with integrated Unichrome graphics
engine.

It supports VIA CLE266, KM400/KN400, CN400, CN700, K8M800/K8N800,
PM800/PN800, P4M800Pro, VN800, PM880, K8M890/K8N890, CN896, VN896 and
P4M900 chipsets.

%description -l pl.UTF-8
Sterownik obrazu X.org do układów VIA ze zintegrowanym silnikiem
graficznym Unichrome.

Obsługuje układy VIA CLE266, KM400/KN400, CN400, CN700, K8M800/K8N800,
PM800/PN800, P4M800Pro, VN800, PM880, K8M890/K8N890, CN896, VN896 oraz
P4M900.

%prep
%setup -q -n xf86-video-openchrome-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la \
	$RPM_BUILD_ROOT%{_libdir}/libchromeXvMC*.{la,so}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/openchrome_drv.so
%ifarch %{ix86} %{x8664}
%attr(755,root,root) %{_libdir}/libchromeXvMC.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libchromeXvMC.so.1
%attr(755,root,root) %{_libdir}/libchromeXvMCPro.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libchromeXvMCPro.so.1
%endif
%{_mandir}/man4/openchrome.4*
