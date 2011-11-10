Summary:	D-Bus service providing high-level OBEX client and server side functionality
Summary(pl.UTF-8):	Usługa D-Bus dostarczająca wysokopoziomową funkcjonalność klienta i serwera OBEX
Name:		obex-data-server
Version:	0.4.6
Release:	2
License:	GPL v2+
Group:		Applications/Communication
Source0:	http://tadas.dailyda.com/software/%{name}-%{version}.tar.gz
# Source0-md5:	961ca5db6fe9c97024e133cc6203cc4d
URL:		http://wiki.muiline.com/obex-data-server
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	bluez-libs-devel >= 4.2
BuildRequires:	dbus-glib-devel >= 0.70
BuildRequires:	glib2-devel >= 1:2.10.0
BuildRequires:	gdk-pixbuf2-devel >= 2.0
BuildRequires:	libusb-compat-devel >= 0.1
BuildRequires:	openobex-devel >= 1.3
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
Requires:	bluez-libs >= 4.2
Requires:	dbus-glib >= 0.70
Requires:	glib2 >= 1:2.10.0
Requires:	openobex >= 1.3
Provides:	dbus(org.openobex.client)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
obex-data-server is D-Bus service providing high-level OBEX client and
server side functionality. It currently supports OPP, FTP profiles and
Bluetooth transport.

%description -l pl.UTF-8
obex-data-server to usługa D-Bus udostępniająca wysokopoziomową
funkcjonalność klienta i serwera OBEX. Aktualnie obsługuje profile OPP
i FTP oraz transport Bluetooth.

%prep
%setup -q

%build
%{__aclocal}
%{__automake}
%{__autoheader}
%{__autoconf}
%configure \
	--enable-bip=gdk-pixbuf
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README dbus-api.txt
%attr(755,root,root) %{_bindir}/obex-data-server
%{_datadir}/dbus-1/services/obex-data-server.service
%dir %{_sysconfdir}/obex-data-server
%{_sysconfdir}/obex-data-server/capability.xml
%{_sysconfdir}/obex-data-server/imaging_capabilities.xml
%{_mandir}/man1/obex-data-server.1*
