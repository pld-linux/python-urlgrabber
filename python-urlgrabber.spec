Summary:	A high-level cross-protocol url-grabber
Summary(pl.UTF-8):	Wysokopoziomowa biblioteka do wychwytywania URL-i do wielu protokołów
Name:		python-urlgrabber
Version:	3.9.1
Release:	6
Epoch:		1
License:	LGPL v2.1+
Group:		Libraries/Python
Source0:	http://urlgrabber.baseurl.org/download/urlgrabber-%{version}.tar.gz
# Source0-md5:	00c8359bf71062d0946bacea521f80b4
Patch1:		urlgrabber-HEAD.patch
URL:		http://urlgrabber.baseurl.org/
BuildRequires:	python >= 1:2.5
BuildRequires:	python-devel
BuildRequires:	python-pycurl >= 7.19
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-libs
Requires:	python-pycurl >= 7.19
Conflicts:	c-ares < 1.6.0-2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A high-level cross-protocol url-grabber for Python supporting HTTP,
FTP and file locations. Features include keepalive, byte ranges,
throttling, authentication, proxies and more.

%description -l pl.UTF-8
Wysokopoziomowa biblioteka Pythona do wychwytywania URL-i dla wielu
protokołów, obsługująca odnośniki HTTP, FTP i file. Możliwości
obejmują połączenia keepalive, przedziały bajtów, tłumienie,
uwierzytelnianie, proxy itp.

%prep
%setup -q -n urlgrabber-%{version}
%patch1 -p1

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/urlgrabber-%{version}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%attr(755,root,root) %{_bindir}/urlgrabber
%{py_sitescriptdir}/urlgrabber
%{py_sitescriptdir}/urlgrabber-*.egg-info
