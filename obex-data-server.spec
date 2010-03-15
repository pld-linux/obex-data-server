# TODO locale file
Summary:	D-Bus service providing high-level OBEX client and server side functionality
Summary(pl.UTF-8):	Usługa D-Bus dostarczająca wysokopoziomową funkcjonalność klienta i serwera OBEX
Name:		obex-data-server
Version:	0.4.5
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://tadas.dailyda.com/software/%{name}-%{version}.tar.gz
# Source0-md5:	8b11e7527c1e3a36a2a9a0c52816ec7b
URL:		http://wiki.muiline.com/obex-data-server
BuildRequires:	GConf2-devel >= 2.6
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	bluez-libs-devel >= 4.2
BuildRequires:	dbus-glib-devel >= 0.70
BuildRequires:	glib2-devel >= 1:2.10.0
BuildRequires:	gtk+2-devel >= 1:2.0
BuildRequires:	openobex-devel >= 1.3
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
Requires(post,preun):	GConf2 >= 2.6
Requires:	dbus-glib >= 0.60
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
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/obex-data-server
%{_datadir}/dbus-1/services/obex-data-server.service
%dir %{_sysconfdir}/obex-data-server
%{_sysconfdir}/obex-data-server/*.xml
%{_mandir}/man1/obex-data-server.1*
