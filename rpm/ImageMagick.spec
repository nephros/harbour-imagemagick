# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.32
# 

Name:       ImageMagick

# >> macros
# << macros
%define mfr_revision 5
%define maj 7
%define mfr_version %{maj}.1.0
%define quantum_depth 16
%define clibver 10
%define libspec -%{maj}_Q%{quantum_depth}HDRI
%define source_version %{mfr_version}-%{mfr_revision}

Summary:    Viewer and Converter for Images
Version:    7.1.0.5
Release:    1.1
Group:      Applications/Multimedia
License:    ImageMagick
URL:        https://imagemagick.org/
Source0:    %{name}-%{version}.tar.xz
Source100:  ImageMagick.yaml
Requires:   libgcc
Requires:   libgomp
Requires:   bzip2-libs
Requires:   libjpeg-turbo
Requires:   libpng
Requires:   libstdc++
Requires:   libtiff
Requires:   libwebp
Requires:   xz-libs
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  gcc
BuildRequires:  bzip2-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libtool-ltdl-devel
BuildRequires:  libwebp-devel

%description
ImageMagick®  is a software suite to create, edit, compose, or convert
bitmap images. 
It can read and write images in a variety of formats (over 200) including
PNG, JPEG, GIF, HEIC, TIFF, DPX, EXR, WebP, Postscript, PDF, and SVG.
ImageMagick can resize, flip, mirror, rotate, distort, shear and transform
images, adjust image colors, apply various special effects, or draw text,
lines, polygons, ellipses and Bézier curves.


%package devel
Summary:    Development files for %{name}
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
Development files for %{name}.

%prep
%setup -q -n %{name}-%{version}/upstream

# >> setup
# << setup

%build
# >> build pre
# << build pre

%configure --disable-static \
    --quiet \
    --enable-silent-rules \
    --enable-shared \
    --disable-docs \
    --disable-deprecated \
    --without-frozenpaths \
    --without-magick_plus_plus \
    --with-modules \
    --without-perl \
    --without-dps \
    --without-fftw \
    --without-flif \
    --without-fpx \
    --without-gcc-arch \
    --without-heic \
    --without-jbig \
    --without-lcms \
    --without-lqr \
    --without-openexr \
    --without-openjp2 \
    --without-pango \
    --without-raw \
    --without-x \
    --without-zstd


# >> build post
# Do *NOT* use %%{?_smp_mflags}, this causes PerlMagick to be silently misbuild
# make
#make %%{?_smp_mflags}
# lets try this from the macros
%{make_build}
# << build post

%install
rm -rf %{buildroot}
# >> install pre
make install DESTDIR=$RPM_BUILD_ROOT
# << install pre

# >> install post
# << install post

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

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
%{_usr}/share/ImageMagick-%{maj}/francais.xml
%{_usr}/share/ImageMagick-%{maj}/english.xml
%{_usr}/share/ImageMagick-%{maj}/locale.xml
%{_bindir}/[^MW]*
%{_libdir}/libMagickCore*.so.%{clibver}*
%{_libdir}/libMagickWand*.so.%{clibver}*
%dir %{_libdir}/ImageMagick*
%{_libdir}/ImageMagick*/config*
%{_libdir}/ImageMagick*/modules*
# >> files
# << files

%files devel
%defattr(-,root,root,-)
# >> files devel
%doc ChangeLog NEWS.txt
%{_libdir}/libMagickCore*.so
%{_libdir}/libMagickWand*.so
%{_libdir}/libMagickCore*.la
%{_libdir}/libMagickWand*.la
%dir %{_includedir}/ImageMagick*
%{_includedir}/ImageMagick*/MagickCore
%{_includedir}/ImageMagick*/MagickWand
%{_bindir}/MagickCore-config
%{_bindir}/MagickWand-config
%{_libdir}/pkgconfig/MagickCore*.pc
%{_libdir}/pkgconfig/ImageMagick*.pc
%{_libdir}/pkgconfig/MagickWand*.pc
# << files devel
