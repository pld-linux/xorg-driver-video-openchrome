%define snap	20071201
Summary:	X.org video driver for VIA chipsets with onboard unichrome graphics
Summary(pl.UTF-8):	Sterownik obrazu X.org dla układów zintegrowanych VIA
Name:		xorg-driver-video-openchrome
Version:	0.1.%{snap}
Release:	1
License:	MIT
Group:		X11/Applications
# svn export http://svn.openchrome.org/svn/branches/experimental_branch xf86-video-openchrome
Source0:	xf86-video-openchrome.tar.bz2
# Source0-md5:	060c0e84d1a82303dd3d3e7b2b3b7a2b
Patch0:		%{name}-id.patch
URL:		http://www.openchrome.org/
BuildRequires:	Mesa-libGL-devel
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libdrm-devel >= 2.0
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 1.389
BuildRequires:	xorg-lib-libXvMC-devel
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-proto-xf86driproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRequires:	xorg-xserver-server-devel >= 1.0.99.901
%requires_xorg_xserver_videodrv
Requires:	xorg-xserver-server >= 1.0.99.901
Obsoletes:	X11-driver-via < 1:7.0.0
Obsoletes:	XFree86-driver-via < 1:7.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A free and Open Source video driver for the VIA/S3G UniChrome,
UniChrome Pro and Chrome9 graphics chipsets.

It support CLE266, KM400/KN400/KM400A/P4M800, CN400/PM800/PN800/PM880,
K8M800, CN700/VM800/P4M800Pro, CX700, P4M890, K8M890, and P4M900/VN896
chipsets.

X.org video driver for VIA chipsets with onboard unichrome graphics.
It supports VIA CLE266, KM400/KN400, K8M800/K8N800, PM800/PN800 and
CN400 chipsets.

%description -l pl.UTF-8
Darmowy i o otwartych źródłach sterownik obrazu X.org dla
zintegrowanych układów graficznych VIA opartych na układach Via/S3G
Unichrome, Unichrome Pro i Chrome9.

Obsługuje układy VIA CLE266, KM400/KN400, K8M800/K8N800, PM800/PN800
i CN400.

%prep
%setup -q -n xf86-video-openchrome
%patch0 -p1

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
	$RPM_BUILD_ROOT%{_libdir}/libviaXvMC*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/openchrome_drv.so
%ifarch %{ix86} %{x8664}
%attr(755,root,root) %{_libdir}/libchromeXvMC.so.*.*.*
%attr(755,root,root) %{_libdir}/libchromeXvMCPro.so.*.*.*
%endif
%{_mandir}/man4/openchrome.4*
