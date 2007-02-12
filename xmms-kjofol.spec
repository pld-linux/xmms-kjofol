Summary:	XMMS - Vis plugin to get kjofol skins
Summary(pl.UTF-8):	Plugin zapewniający obsługę skórek programu kjofol
Summary(ru.UTF-8):	XMMS - модуль для поддержки скинов от kjofol
Summary(uk.UTF-8):	XMMS - модуль для підтримки скінів від kjofol
Name:		xmms-kjofol
Version:	0.95
Release:	2
License:	GPL v2
Group:		X11/Applications/Multimedia
Source0:	http://www.csse.monash.edu.au/~timf/kint_xmms-%{version}.tar.gz
# Source0-md5:	60cdb4e1bbc8d121c99da2f4d00813c2
Source1:	kjofol-skins.tar
# Source1-md5:	8a01be97c2bac9ffdffc5c24fc6a47a0
URL:		http://www.dgs.monash.edu.au/~timf/xmms/
BuildRequires:	libpng-devel
BuildRequires:	rpmbuild(macros) >= 1.125
BuildRequires:	xmms-devel
Requires:	xmms
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
In this package you can find the Visualization plugin that enable
K-Jofol skins support.

%description -l pl.UTF-8
Dzięki wtyczce z tego pakietu można używać w XMMS-ie skórek programu
K-Jofol.

%description -l uk.UTF-8
Цей пакет містить візуальний модуль, що реалізує підтримку скін-файлів
від K-Jofol.

%description -l ru.UTF-8
Этот пакет содержит визуальный модуль, реализующий поддержку
скин-файлов от K-Jofol.

%package skins
Summary:	Some kjofol skins for XMMS
Summary(pl.UTF-8):	Kilka skórek
Summary(ru.UTF-8):	Некоторые скины от kjofol для XMMS
Summary(uk.UTF-8):	Деякі "скіни" від kjofol для XMMS
Group:		X11/Applications/Multimedia
Requires:	%{name}

%description skins
In this package you can find several cute K-Jofol skins for XMMS.

%description skins -l pl.UTF-8
Kilka ładnych skórek z K-Jofol.

%description skins -l uk.UTF-8
Цей пакет містить кілька гарних скін-файлів від K-Jofol для XMMS.

%description skins -l ru.UTF-8
Этот пакет содержит несколько красивых скин-файлов от K-Jofol для
XMMS.

%prep
%setup -q -a 1 -n xmms-kj

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -DHAVE_LIBPNG -DXMMS_DIR=\\\"%{xmms_datadir}\\\" \
	-DKJSKIN=\\\"%{xmms_datadir}/kjofol/default.zip\\\" `xmms-config --cflags`" \
	LDFLAGS="%{rpmldflags}" \
	VFLAGS="-DXMMS_VIS=1" \
	VLDFLAGS="-shared"

mv kj libkjofol.so

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{xmms_visualization_plugindir} \
	$RPM_BUILD_ROOT%{xmms_datadir}/kjofol

install libkjofol.so $RPM_BUILD_ROOT%{xmms_visualization_plugindir}
install default.zip penguin.zip kjofol/* $RPM_BUILD_ROOT%{xmms_datadir}/kjofol

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.txt
%{xmms_visualization_plugindir}/libkjofol*
%dir %{xmms_datadir}/kjofol
%{xmms_datadir}/kjofol/default.zip

%files skins
%defattr(644,root,root,755)
%{xmms_datadir}/kjofol/atomic.zip
%{xmms_datadir}/kjofol/bio_hazard.zip
%{xmms_datadir}/kjofol/bluestrain.zip
%{xmms_datadir}/kjofol/happy_2_0.zip
%{xmms_datadir}/kjofol/illusion.zip
%{xmms_datadir}/kjofol/knine.zip
%{xmms_datadir}/kjofol/maegashira_1_01.zip
%{xmms_datadir}/kjofol/nokiamp_1_0.zip
%{xmms_datadir}/kjofol/Okovoid.zip
%{xmms_datadir}/kjofol/penguin.zip
%{xmms_datadir}/kjofol/phong.zip
%{xmms_datadir}/kjofol/scathe.zip
%{xmms_datadir}/kjofol/shuttle_1_0.zip
%{xmms_datadir}/kjofol/spectre.zip
%{xmms_datadir}/kjofol/walkjofol.zip
%{xmms_datadir}/kjofol/xl_size.zip
%{xmms_datadir}/kjofol/x_ray_1_0.zip
