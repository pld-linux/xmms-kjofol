Summary:	XMMS - Vis plugin to get kjofol skins
Summary(pl):	Plugin zapewniaj╠cy obsЁugЙ skСrek programu kjofol
Summary(ru):	XMMS - модуль для поддержки скинов от kjofol
Summary(uk):	XMMS - модуль для п╕дтримки ск╕н╕в в╕д kjofol
Name:		xmms-kjofol
Version:	0.95
Release:	1
License:	GPL v2
Group:		X11/Applications/Multimedia
Source0:	http://www.csse.monash.edu.au/~timf/kint_xmms-%{version}.tar.gz
Source1:	kjofol-skins.tar
URL:		http://www.dgs.monash.edu.au/~timf/xmms/
BuildRequires:	xmms-devel
BuildRequires:	libpng-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
In this package you can find the Visualization plugin that enable
K-Jofol skins support.

%description -l pl
DziЙki wtyczce z tego pakietu mo©na u©ywaФ w XMMS-ie skСrek programu
K-Jofol.

%description -l uk
Цей пакет м╕стить в╕зуальний модуль, що реал╕зу╓ п╕дтримку ск╕н-файл╕в
в╕д K-Jofol.

%description -l ru
Этот пакет содержит визуальный модуль, реализующий поддержку
скин-файлов от K-Jofol.

%package skins
Summary:	Some kjofol skins for XMMS
Summary(pl):	Kilka skСrek
Summary(ru):	Некоторые скины от kjofol для XMMS
Summary(uk):	Деяк╕ "ск╕ни" в╕д kjofol для XMMS
Group:		X11/Applications/Multimedia
Requires:	%{name}

%description skins
In this package you can find several cute K-Jofol skins for XMMS.

%description skins -l pl
Kilka Ёadnych skСrek z K-Jofol.

%description skins -l uk
Цей пакет м╕стить к╕лька гарних ск╕н-файл╕в в╕д K-Jofol для XMMS.

%description skins -l ru
Этот пакет содержит несколько красивых скин-файлов от K-Jofol для
XMMS.

%prep
%setup -q -a 1 -n xmms-kj

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -DHAVE_LIBPNG -DXMMS_DIR=\\\"`xmms-config --data-dir`\\\" \
	-DKJSKIN=\\\"`xmms-config --data-dir`/kjofol/default.zip\\\" `xmms-config --cflags`" \
	LDFLAGS="%{rpmldflags}" \
	VFLAGS="-DXMMS_VIS=1" \
	VLDFLAGS="-shared"

mv kj libkjofol.so

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/xmms/Visualization,%{_datadir}/xmms/kjofol}

install libkjofol.so $RPM_BUILD_ROOT%{_libdir}/xmms/Visualization
install default.zip penguin.zip kjofol/* $RPM_BUILD_ROOT%{_datadir}/xmms/kjofol

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.txt 
%{_libdir}/xmms/Visualization/libkjofol*
%dir %{_datadir}/xmms/kjofol
%{_datadir}/xmms/kjofol/default.zip

%files skins
%defattr(644,root,root,755)
%{_datadir}/xmms/kjofol/atomic.zip
%{_datadir}/xmms/kjofol/bio_hazard.zip
%{_datadir}/xmms/kjofol/bluestrain.zip
%{_datadir}/xmms/kjofol/happy_2_0.zip
%{_datadir}/xmms/kjofol/illusion.zip
%{_datadir}/xmms/kjofol/knine.zip
%{_datadir}/xmms/kjofol/maegashira_1_01.zip
%{_datadir}/xmms/kjofol/nokiamp_1_0.zip
%{_datadir}/xmms/kjofol/Okovoid.zip
%{_datadir}/xmms/kjofol/penguin.zip
%{_datadir}/xmms/kjofol/phong.zip
%{_datadir}/xmms/kjofol/scathe.zip
%{_datadir}/xmms/kjofol/shuttle_1_0.zip
%{_datadir}/xmms/kjofol/spectre.zip
%{_datadir}/xmms/kjofol/walkjofol.zip
%{_datadir}/xmms/kjofol/xl_size.zip
%{_datadir}/xmms/kjofol/x_ray_1_0.zip
