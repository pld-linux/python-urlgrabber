Summary:	A high-level cross-protocol url-grabber
Summary(pl):	Wysokopoziomowa biblioteka do wychwytywania URL-i do wielu protoko³ów
Name:		python-urlgrabber
Version:	3.1.0
Release:	1
License:	LGPL
Group:		Libraries/Python
Source0:	http://linux.duke.edu/projects/urlgrabber/download/urlgrabber-%{version}.tar.gz
# Source0-md5:	2a92d8ce0d89c5e772a98e9b8dcd5b73
URL:		http://linux.duke.edu/projects/urlgrabber/
Provides:	urlgrabber
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A high-level cross-protocol url-grabber for Python supporting HTTP,
FTP and file locations. Features include keepalive, byte ranges,
throttling, authentication, proxies and more.

%description -l pl
Wysokopoziomowa biblioteka Pythona do wychwytywania URL-i dla wielu
protoko³ów, obs³uguj±ca odno¶niki HTTP, FTP i file. Mo¿liwo¶ci
obejmuj± po³±czenia keepalive, przedzia³y bajtów, t³umienie,
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
