%define libname %mklibname KF6FileMetaData
%define devname %mklibname KF6FileMetaData -d
%define git 20230811

Name: kf6-kfilemetadata
Version: 5.240.0
Release: %{?git:0.%{git}.}1
Source0: https://invent.kde.org/frameworks/kfilemetadata/-/archive/master/kfilemetadata-master.tar.bz2#/kfilemetadata-%{git}.tar.bz2
Summary: A library for extracting file metadata
URL: https://invent.kde.org/frameworks/kfilemetadata
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: python
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6Xml)
BuildRequires: cmake(KF6Archive)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: pkgconfig(libattr)
BuildRequires: pkgconfig(taglib)
BuildRequires: pkgconfig(libappimage)
BuildRequires: pkgconfig(libavformat)
BuildRequires: pkgconfig(libavutil)
BuildRequires: pkgconfig(exiv2)
BuildRequires: pkgconfig(poppler-qt6)
BuildRequires: ebook-tools-devel
Requires: %{libname} = %{EVRD}
# FIXME There's some more file formats supported by extra library
# requirements. Add them once we've packaged all relevant libraries.

%description
A library for extracting file metadata

%package -n %{libname}
Summary: A library for extracting file metadata
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
A library for extracting file metadata

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

A library for extracting file metadata

%prep
%autosetup -p1 -n kfilemetadata-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang %{name} --all-name --with-qt --with-html

%files -f %{name}.lang
%{_datadir}/qlogging-categories6/kfilemetadata.*

%files -n %{devname}
%{_includedir}/KF6/KFileMetaData
%{_libdir}/cmake/KF6FileMetaData
%{_qtdir}/mkspecs/modules/qt_KFileMetaData.pri
%{_qtdir}/doc/KF6FileMetaData.*

%files -n %{libname}
%{_libdir}/libKF6FileMetaData.so*
%{_qtdir}/plugins/kf6/kfilemetadata
