%define		_snap	07202007
%define		_ver	%(echo %{_snap} | sed -e 's,\\(..\\)\\(..\\)\\(....\\),\\3\\1\\2,')
%define		_tpl	monobook
Summary:	Monobook template for DokuWiki
Name:		dokuwiki-tpl-%{_tpl}
Version:	%{_ver}
Release:	0.1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://tatewake.com/wiki/_media/projects:monobook-%{_snap}.zip
# Source0-md5:	69f0dfd21dc921f86be4fd9f8ec9ea4f
URL:		http://tatewake.com/wiki/projects:monobook_for_dokuwiki
BuildRequires:	rpmbuild(macros) >= 1.268
Requires:	dokuwiki >= 20070626
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_dokudir	/usr/share/dokuwiki
%define		_tpldir		%{_dokudir}/lib/tpl/%{_tpl}

%description
Gives DokuWiki the Wikipedia/Mediawiki look and feel, as well as more
functionality. Includes discussions without using a plugin and the
navigation can be edited like a wiki page.

%prep
%setup -q -n %{_tpl}

rm -f LICENSE # GPL v2

cat > INSTALL <<'EOF'
To activate this template add the following to your conf/local.php file:
$conf['template'] = '%{_tpl}';
EOF

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_tpldir}
cp -a . $RPM_BUILD_ROOT%{_tpldir}
rm -f $RPM_BUILD_ROOT%{_tpldir}/{INSTALL,README}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc INSTALL README
%{_tpldir}