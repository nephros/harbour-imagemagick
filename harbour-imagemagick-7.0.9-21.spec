%define debug_build    0
%define maj            7
%define mfr_version    %{maj}.0.9
%define mfr_revision   21
%define source_version %{mfr_version}-%{mfr_revision}

%define quantum_depth  16
%define clibver        7
%define libspec        -%{maj}_Q%{quantum_depth}HDRI

Name:           ImageMagick
Version:        %{mfr_version}.%{mfr_revision}
Release:        5
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
%doc ChangeLog NEWS.txt
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
%{_mandir}/man1/*
%{_libdir}/libMagickCore*.so.%{clibver}*
%{_libdir}/libMagickWand*.so.%{clibver}*
%dir %{_libdir}/ImageMagick*
%{_libdir}/ImageMagick*/config*
%{_libdir}/ImageMagick*/modules*

%files devel
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

%changelog
* Sat Feb  8 12:03:51 CET 2020 Nephros <sailfish@nephros.org> 7.0.9.21-4
- make dependency on ffmpeg-tools weak (recommends)
* Sat Feb  8 11:34:55 CET 2020 Nephros <sailfish@nephros.org> 7.0.9.21-3
- add tiff support/dep
* Fri Feb  7 14:41:29 CET 2020 Nephros <sailfish@nephros.org> 7.0.9.21
- add proper files/install section, thanks, SuSE spec file!
* Fri Feb  7 13:46:29 CET 2020 Nephros <sailfish@nephros.org> 7.0.9
- initial creation of .spec file

# this is a non-ASCII character to shut up rpmlint: «
# vim: fileencoding=utf-8

