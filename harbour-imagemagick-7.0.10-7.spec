%define debug_build    0
%define maj            7
%define mfr_version    %{maj}.0.10
%define mfr_revision   7
%define source_version %{mfr_version}-%{mfr_revision}

%define quantum_depth  16
%define clibver        7
%define libspec        -%{maj}_Q%{quantum_depth}HDRI

Name:           ImageMagick
Version:        %{mfr_version}.%{mfr_revision}
Release:        1
Summary:        Viewer and Converter for Images

Group:          Applications/Multimedia
License:        ImageMagick
URL:            https://imagemagick.org/
Source0:        https://imagemagick.org/download/ImageMagick-%{mfr_version}-%{mfr_revision}.tar.xz

BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires: gcc
BuildRequires: libtool-ltdl-devel
BuildRequires: libjpeg-turbo-devel
BuildRequires: libpng-devel
BuildRequires: libtiff-devel
Requires:	   libstdc++
Requires:	   libgcc
Requires:	   libgomp
Requires:	   libjpeg-turbo
Requires:	   libpng
Requires:      libtiff
# delegation of video things:
Recommends:    ffmpeg-tools
#Requires:	   bzip2-libs

%package devel
Summary:        Development files for ImageMagick
Group:          Development/Libraries
Requires:       ImageMagick = %{version}
Requires:       glibc-devel

%description
ImageMagick is a software suite to create, edit, compose, or convert bitmap
images. 

%description devel
ImageMagick is a software suite to create, edit, compose, or convert bitmap
images. 
Development files.


%prep
%setup -q -n ImageMagick-%{source_version}


%build
%configure \
  --disable-silent-rules \
  --enable-shared \
  --without-frozenpaths \
  --without-magick_plus_plus \
  --with-modules \
  --without-perl \
  --without-x \
  --without-lcms \
  --without-gcc-arch
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%license LICENSE
%dir %{_sysconfdir}/ImageMagick-%{maj}
%config %{_sysconfdir}/ImageMagick-%{maj}/colors.xml
%config %{_sysconfdir}/ImageMagick-%{maj}/delegates.xml
%config %{_sysconfdir}/ImageMagick-%{maj}/log.xml
%config %{_sysconfdir}/ImageMagick-%{maj}/mime.xml
%config %{_sysconfdir}/ImageMagick-%{maj}/policy.xml
%config %{_sysconfdir}/ImageMagick-%{maj}/quantization-table.xml
%config %{_sysconfdir}/ImageMagick-%{maj}/thresholds.xml
%config %{_sysconfdir}/ImageMagick-%{maj}/type-apple.xml
%config %{_sysconfdir}/ImageMagick-%{maj}/type-dejavu.xml
%config %{_sysconfdir}/ImageMagick-%{maj}/type-ghostscript.xml
%config %{_sysconfdir}/ImageMagick-%{maj}/type-urw-base35.xml
%config %{_sysconfdir}/ImageMagick-%{maj}/type-windows.xml
%config %{_sysconfdir}/ImageMagick-%{maj}/type.xml
%{_bindir}/[^MW]*
%{_libdir}/libMagickCore*.so.%{clibver}*
%{_libdir}/libMagickWand*.so.%{clibver}*
%dir %{_libdir}/ImageMagick*
%{_libdir}/ImageMagick*/config*
%{_libdir}/ImageMagick*/modules*

%files devel
%doc ChangeLog NEWS.txt
%{_mandir}/man1/*
%{_libdir}/libMagickCore*.so
%{_libdir}/libMagickWand*.so
%dir %{_includedir}/ImageMagick*
%{_includedir}/ImageMagick*/MagickCore
%{_includedir}/ImageMagick*/MagickWand
%{_bindir}/MagickCore-config
%{_bindir}/MagickWand-config
%{_libdir}/pkgconfig/MagickCore*.pc
%{_libdir}/pkgconfig/ImageMagick*.pc
%{_libdir}/pkgconfig/MagickWand*.pc
%{_mandir}/man1/*-config.1.gz

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%changelog
* Thu Apr 23 16:50:46 CEST 2020 Nephros <sailfish@nephros.org> 7.0.10.7-1
- version bump, fix security issue
* Mon Mar  2 17:01:35 CET 2020 Nephros <sailfish@nephros.org> 7.0.9.27-1
- version bump
* Sun Feb  9 13:06:09 CET 2020 Nephros <sailfish@nephros.org> 7.0.9.22-2
- run ldconfig in post/postun
- bump version to -22, move doc and man to -devel package

# this is a non-ASCII character to shut up rpmlint: «
# vim: fileencoding=utf-8

