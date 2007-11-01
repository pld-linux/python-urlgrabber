Summary:	A high-level cross-protocol url-grabber
Summary(pl.UTF-8):	Wysokopoziomowa biblioteka do wychwytywania URL-i do wielu protokołów
Name:		python-urlgrabber
# 3.0.x is stable series (we use that one)
# 3.1.x is devel series
Version:	3.0.0
Release:	1
Epoch:		1
License:	LGPL v2.1+
Group:		Libraries/Python
Source0:	http://linux.duke.edu/projects/urlgrabber/download/urlgrabber-%{version}.tar.gz
# Source0-md5:	3cdb34db3269baf8006da35b9f82d9c9
URL:		http://linux.duke.edu/projects/urlgrabber/
BuildRequires:	python >= 1:2.4
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-libs
Provides:	urlgrabber
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

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install \
	--root=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_docdir}/urlgrabber-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%attr(755,root,root) %{_bindir}/urlgrabber
%{py_sitescriptdir}/urlgrabber
