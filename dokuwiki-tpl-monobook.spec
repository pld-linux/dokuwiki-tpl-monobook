%define		_snap	2008-07-30
%define		_ver	%(echo %{_snap} | tr -d -)
%define		tpl	monobook
Summary:	Monobook template for DokuWiki
Summary(pl.UTF-8):	Szablon Monobook dla DokuWiki
Name:		dokuwiki-tpl-%{tpl}
Version:	%{_ver}
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://tatewake.com/wiki/_media/projects:monobook-%{_snap}.tar.bz2
# Source0-md5:	35608ad64b14c0ac2f61c0477609e3ab
Source1:	dokuwiki-find-lang.sh
URL:		http://tatewake.com/wiki/projects:monobook_for_dokuwiki
BuildRequires:	rpmbuild(macros) >= 1.268
Requires:	dokuwiki >= 20080505
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokudir		/usr/share/dokuwiki
%define		tpldir		%{dokudir}/lib/tpl/%{tpl}

%description
Gives DokuWiki the Wikipedia/Mediawiki look and feel, as well as more
functionality. Includes discussions without using a plugin and the
navigation can be edited like a wiki page.

%description -l pl.UTF-8
Ten szablon nadaje DokuWiki wygląd i zachowanie Wikipedii/Mediawiki, a
także trochę większą funkcjonalność. Zawiera dyskusje bez użycia
osobnej wtyczki, a nawigację można modyfikować podobnie jak stronę
wiki.

%prep
%setup -q -n %{tpl}

rm -f LICENSE # GPL v2

cat > INSTALL <<'EOF'
To activate this template add the following to your conf/local.php file:
$conf['template'] = '%{tpl}';
EOF

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{tpldir}
cp -a . $RPM_BUILD_ROOT%{tpldir}
rm -f $RPM_BUILD_ROOT%{tpldir}/{INSTALL,README}

# find locales
sh %{SOURCE1} %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc INSTALL README
%dir %{tpldir}
%{tpldir}/*.php
%{tpldir}/style.ini
%{tpldir}/common
%{tpldir}/conf
%{tpldir}/dokuwiki
%{tpldir}/monobook
%{tpldir}/user
# TODO: lang dirs inside. check if these can be also rpm lang tagged
%{tpldir}/wikipedia
