# TODO locale file
Summary:	D-Bus service providing high-level OBEX client and server side functionality
Summary(pl.UTF-8):	Usługa D-Bus dostarczająca wysokopoziomową funkcjonalność klientą i serwera OBEX
Name:		obex-data-server
Version:	0.3.1
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://tadas.dailyda.com/software/%{name}-%{version}.tar.gz
# Source0-md5:	4b5ded97cd9e7c62243062ec19a3ac9e
URL:		http://wiki.muiline.com/obex-data-server
BuildRequires:	GConf2-devel >= 2.6
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	bluez-libs-devel
BuildRequires:	dbus-glib-devel >= 0.60
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
%configure
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
