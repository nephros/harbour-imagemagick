#
# spec file for package ImageMagick
#
# Copyright (c) 2020 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define debug_build    0
%define asan_build     0
%define maj            7
%define mfr_version    %{maj}.0.9
%define mfr_revision   19
%define quantum_depth  16s
%define source_version %{mfr_version}-%{mfr_revision}
%define clibver        7
%define cwandver       7
%define cxxlibver      4
%define libspec        -%{maj}_Q%{quantum_depth}HDRI
%define config_dir     ImageMagick-7
%define config_spec    config-7
# bsc#1088463
%define urw_base35_fonts 0

Name:           ImageMagick
Version:        %{mfr_version}.%{mfr_revision}
Release:        1.1
Summary:        Viewer and Converter for Images
License:        ImageMagick
Group:          Productivity/Graphics/Other
URL:            https://imagemagick.org/
Source0:        https://imagemagick.org/download/ImageMagick-%{mfr_version}-%{mfr_revision}.tar.bz2
Source1:        baselibs.conf
Source2:        https://imagemagick.org/download/ImageMagick-%{mfr_version}-%{mfr_revision}.tar.bz2.asc
Source3:        ImageMagick.keyring
# suse specific patches
Patch0:         ImageMagick-configuration-SUSE.patch
Patch2:         ImageMagick-library-installable-in-parallel.patch
#%%ifarch s390x s390 ppc64 ppc
Patch3:         ImageMagick-s390-disable-tests.patch
#%%endif
BuildRequires:  chrpath
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libjpeg-devel
BuildRequires:  libtool
BuildRequires:  libwmf-devel
BuildRequires:  lzma-devel
BuildRequires:  xdg-utils
BuildRequires:  zip
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?suse_version} >= 1315
BuildRequires:  dejavu-fonts
%endif
%if 0%{?suse_version} >= 1315
BuildRequires:  libjbig-devel
%endif
%if 0%{?suse_version} >= 1315
%if 0%{?suse_version} > 1500
BuildRequires:  p7zip-full
%else
BuildRequires:  p7zip
%endif
BuildRequires:  pkgconfig
%endif
%if 0%{?suse_version} >= 1315
BuildRequires:  pkgconfig(OpenEXR)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(ddjvuapi)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libtiff-4) >= 4.0.3
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libwebpmux)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(pango)
%if 0%{?suse_version} > 1315
BuildRequires:  pkgconfig(ijs)
# bsc#1088463
%if %{urw_base35_fonts}
BuildRequires:  urw-base35-fonts
%else
BuildRequires:  ghostscript-fonts-other
BuildRequires:  ghostscript-fonts-std
%endif
%else
BuildRequires:  ghostscript-fonts-other
BuildRequires:  ghostscript-fonts-std
BuildRequires:  ghostscript-library
%endif
%if 0%{?suse_version} > 1315
BuildRequires:  pkgconfig(libopenjp2) >= 2.1.0
%endif
%if 0%{?suse_version} > 1315
BuildRequires:  pkgconfig(lqr-1)
%endif
%else
BuildRequires:  OpenEXR-devel
BuildRequires:  fftw3-devel
BuildRequires:  freetype2-devel
BuildRequires:  ghostscript-fonts-other
BuildRequires:  ghostscript-fonts-std
BuildRequires:  ghostscript-library
BuildRequires:  libbz2-devel
BuildRequires:  libdjvulibre-devel
BuildRequires:  libexif-devel
BuildRequires:  librsvg-devel
BuildRequires:  libtiff-devel
BuildRequires:  libxml-devel
BuildRequires:  perl-parent
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(zlib)
%endif

%package -n perl-PerlMagick
Summary:        Perl interface for ImageMagick
Group:          Development/Libraries/Perl
Requires:       ImageMagick = %{version}
Requires:       libMagickCore%{libspec}%{clibver} = %{version}
Requires:       perl = %{perl_version}

%package devel
Summary:        Development files for ImageMagick's C interface
Group:          Development/Libraries/C and C++
Requires:       ImageMagick = %{version}
Requires:       glibc-devel
Requires:       libMagickCore%{libspec}%{clibver} = %{version}
Requires:       libMagickWand%{libspec}%{cwandver} = %{version}
# bnc#741947:
%if 0%{?suse_version} >= 1315
Requires:       pkgconfig(bzip2)
%else
Requires:       libbz2-devel
%endif

%if !%{debug_build}
%package extra
Summary:        Extra codecs for the ImageMagick image viewer/converter
Group:          Productivity/Graphics/Other
Requires:       ImageMagick = %{version}
Requires:       libMagickCore%{libspec}%{clibver} = %{version}
Recommends:     autotrace
Recommends:     dcraw
Recommends:     hp2xx
Recommends:     libwmf
Recommends:     netpbm
Recommends:     transfig
%endif

%package -n libMagickCore%{libspec}%{clibver}
Summary:        C runtime library for ImageMagick
Group:          Productivity/Graphics/Other
Recommends:     ghostscript
Suggests:       %{name}-extra = %{version}
Requires:       imagick-%{config_spec}
Recommends:     %{config_spec}-SUSE

%package -n libMagickWand%{libspec}%{cwandver}
Summary:        C runtime library for ImageMagick
Group:          Productivity/Graphics/Other

%package -n libMagick++%{libspec}%{cxxlibver}
Summary:        C++ interface runtime library for ImageMagick
Group:          Development/Libraries/C and C++
Requires:       %{name}

%package -n libMagick++-devel
Summary:        Development files for ImageMagick's C++ interface
Group:          Development/Libraries/C and C++
Requires:       libMagick++%{libspec}%{cxxlibver} = %{version}
Requires:       libstdc++-devel
%if 0%{?suse_version} >= 1315
Requires:       pkgconfig(ImageMagick) = %{mfr_version}
%else
Requires:       %{name}-devel = %{version}
%endif

%package doc
Summary:        Document Files for ImageMagick Library
Group:          Documentation/HTML
%if 0%{?suse_version} >= 1315
BuildArch:      noarch
%endif

%package %{config_spec}-upstream
Summary:        Upstream Configuration Files
Group:          Development/Libraries/C and C++
Provides:       imagick-%{config_spec}
Requires(post): update-alternatives
Requires(postun): update-alternatives

%package %{config_spec}-SUSE
Summary:        Upstream Configuration Files
Group:          Development/Libraries/C and C++
Provides:       imagick-%{config_spec}
Requires(post): update-alternatives
Requires(postun): update-alternatives

%description
ImageMagick is a robust collection of tools and libraries to read,
write, and manipulate an image in many image formats, including popular
formats like TIFF, JPEG, PNG, PDF, PhotoCD, and GIF. With ImageMagick,
you can create images dynamically, making it suitable for Web
applications. You can also resize, rotate, sharpen, color-reduce, or
add special effects to an image and save your completed work in many
different image formats. Image processing operations are available from
the command line as well as through C, C++, and Perl-based programming
interfaces.

%description devel
ImageMagick is a robust collection of tools and libraries to read,
write, and manipulate an image in many image formats, including popular
formats like TIFF, JPEG, PNG, PDF, PhotoCD, and GIF. With ImageMagick,
you can create images dynamically, making it suitable for Web
applications. You can also resize, rotate, sharpen, color-reduce, or
add special effects to an image and save your completed work in many
different image formats. Image processing operations are available from
the command line as well as through C, C++, and Perl-based programming
interfaces.

%if !%{debug_build}
%description extra
This package adds support for djvu, wmf and jpeg2000 formats and
installs optional helper applications.

ImageMagick is a robust collection of tools and libraries to read,
write, and manipulate an image in many image formats, including popular
formats like TIFF, JPEG, PNG, PDF, PhotoCD, and GIF. With ImageMagick,
you can create images dynamically, making it suitable for Web
applications. You can also resize, rotate, sharpen, color-reduce, or
add special effects to an image and save your completed work in many
different image formats. Image processing operations are available from
the command line as well as through C, C++, and Perl-based programming
interfaces.
%endif

%description -n libMagickCore%{libspec}%{clibver}
ImageMagick is a robust collection of tools and libraries to read,
write, and manipulate an image in many image formats, including popular
formats like TIFF, JPEG, PNG, PDF, PhotoCD, and GIF. With ImageMagick,
you can create images dynamically, making it suitable for Web
applications. You can also resize, rotate, sharpen, color-reduce, or
add special effects to an image and save your completed work in many
different image formats. Image processing operations are available from
the command line as well as through C, C++, and Perl-based programming
interfaces.

%description -n libMagickWand%{libspec}%{cwandver}
ImageMagick is a robust collection of tools and libraries to read,
write, and manipulate an image in many image formats, including popular
formats like TIFF, JPEG, PNG, PDF, PhotoCD, and GIF. With ImageMagick,
you can create images dynamically, making it suitable for Web
applications. You can also resize, rotate, sharpen, color-reduce, or
add special effects to an image and save your completed work in many
different image formats. Image processing operations are available from
the command line as well as through C, C++, and Perl-based programming
interfaces.

%description -n perl-PerlMagick
PerlMagick is an objected-oriented Perl interface to ImageMagick. Use
the module to read, manipulate, or write an image or image sequence
from within a Perl script. This makes it suitable for Web CGI scripts.

%description -n libMagick++%{libspec}%{cxxlibver}
This is Magick++, the object-oriented C++ API for the ImageMagick
image-processing library.

Magick++ supports an object model inspired by PerlMagick. Magick++
should be faster than PerlMagick since it is written in a compiled
language which is not parsed at run-time. This makes it suitable for
Web CGI programs. Images support implicit reference counting so that
copy constructors and assignment incur almost no cost. The cost of
actually copying an image (if necessary) is done just before
modification and this copy is managed automatically by Magick++.
De-referenced copies are automatically deleted. The image objects
support value (rather than pointer) semantics so it is trivial to
support multiple generations of an image in memory at one time.

%description -n libMagick++-devel
This is Magick++, the object-oriented C++ API for the ImageMagick
image-processing library.

Magick++ supports an object model inspired by PerlMagick. Magick++
should be faster than PerlMagick since it is written in a compiled
language which is not parsed at run-time. This makes it suitable for
Web CGI programs. Images support implicit reference counting so that
copy constructors and assignment incur almost no cost. The cost of
actually copying an image (if necessary) is done just before
modification and this copy is managed automatically by Magick++.
De-referenced copies are automatically deleted. The image objects
support value (rather than pointer) semantics so it is trivial to
support multiple generations of an image in memory at one time.

%description doc
HTML documentation for ImageMagick library and scene examples.

%description %{config_spec}-upstream
ImageMagick configuration as supplied by upstream. It does not
provide any security restrictions. ImageMagick will be vulnerable
for example by ImageTragick or PS/PDF coder issues. It should
be used in trusted environment. Version or maintenance updates
will not overwrite user changes in system configuration.

%description %{config_spec}-SUSE
ImageMagick configuration as provide by SUSE. It is more security
aware than config-upstream variant. It does disable some coders, 
that are insecure by design to prevent user to use them
inadvertently. Configuration can be subject of change by future
version and maintenance updates and system changes will not be
preserved.


%prep
%setup -q -n ImageMagick-%{source_version}
%patch2 -p1
%ifarch s390x s390 ppc ppc64
%patch3 -p1
%endif

%build
# bsc#1088463
%if %{urw_base35_fonts}
sed -i 's:type1:otf:'      config/type-urw-base35.xml.in
sed -i 's:metrics=[^ ]*::' config/type-urw-base35.xml.in
sed -i 's:\.t1:.otf:'      config/type-urw-base35.xml.in
%endif
# make library binary package parallel installable
export MODULES_DIRNAME="modules%{libspec}%{clibver}"
export SHAREARCH_DIRNAME="config%{libspec}%{clibver}"
%if %{debug_build}
export CFLAGS="%{optflags} -O0"
export CXXFLAGS="%{optflags} -O0"
%endif
%configure \
  --disable-silent-rules \
  --enable-shared \
  --without-frozenpaths \
  --with-magick_plus_plus \
%if !%{debug_build}
  --with-modules \
%else
  --without-modules \
%endif
  --with-threads \
%if %{urw_base35_fonts}
  --with-urw-base35-font-dir=/usr/share/fonts/truetype \
%else
  --with-gs-font-dir=/usr/share/fonts/ghostscript \
%endif
  --with-perl \
  --with-perl-options="INSTALLDIRS=vendor %{?perl_prefix} CC='gcc -L$PWD/magick/.libs' LDDLFLAGS='-shared -L$PWD/magick/.libs'" \
  --disable-static \
  --with-gvc \
  --with-djvu \
  --with-lcms \
  --with-jbig \
%if 0%{?suse_version} > 1315
  --with-openjp2 \
%endif
  --with-openexr \
  --with-rsvg \
  --with-webp \
  --with-wmf \
  --with-quantum-depth=%{quantum_depth} \
  --without-gcc-arch \
  --enable-pipes=no \
  --enable-reproducible-build=yes \
  --disable-openmp
%if %{asan_build}
sed -i -e 's/\(^CFLAGS.*\)/\1 -fsanitize=address/' \
       -e 's/\(^LIBS =.*\)/\1 -lasan/' \
       Makefile
%endif
# don't build together, PerlMagick could be miscompiled when using parallel build[1]
# [1] http://pkgs.fedoraproject.org/cgit/ImageMagick.git/tree/ImageMagick.spec
make %{?_smp_mflags} all
make -j1 perl-build
# mostly because */demo is used later with %check
# polutting dir with .libs etc.
cp -r Magick++/demo Magick++/examples
cp -r PerlMagick/demo PerlMagick/examples
# other improvements
chmod -x PerlMagick/demo/*.pl

%check
%if %{debug_build} || %{asan_build}
# testsuite does not succeed for some reason
# research TODO
exit 0
%endif
%ifarch i586
# do not report test issues related to 32-bit architectures upstream,
# they do not want to dedicate any time to fix them:
# https://github.com/ImageMagick/ImageMagick/issues/1215
rm PerlMagick/t/montage.t
sed -i -e 's:averageImages ::' -e 's:1..13:1..12:' Magick++/tests/tests.tap
%endif
make %{?_smp_mflags} check
export MAGICK_CODER_MODULE_PATH=$PWD/coders/.libs
export MAGICK_CODER_FILTER_PATH=$PWD/filters/.libs
export MAGICK_CONFIGURE_PATH=$PWD/config
cd PerlMagick
%if 0%{?suse_version} >= 1315
make %{?_smp_mflags} test
%else
make test_dynamic
%endif
cd ..

%install
%if 0%{?suse_version} >= 1315
%make_install pkgdocdir=%{_defaultdocdir}/%{name}-%{maj}/
%else
make install \
     DESTDIR=%{buildroot} \
     pkgdocdir=%{_defaultdocdir}/%{name}-%{maj}/
%endif
# configuration magic
mv -t %{buildroot}%{_sysconfdir}/%{name}* %{buildroot}%{_datadir}/%{name}*/*.xml
mv %{buildroot}%{_sysconfdir}/%{config_dir}{,-upstream}
cp -r %{buildroot}%{_sysconfdir}/%{config_dir}{-upstream,-SUSE}
patch --dir %{buildroot}%{_sysconfdir}/%{config_dir}-SUSE < %{PATCH0}
mkdir -p  %{buildroot}%{_sysconfdir}/alternatives/
ln -sf %{_sysconfdir}/alternatives/%{config_dir} %{buildroot}%{_sysconfdir}/%{config_dir}
# symlink header file relative to /usr/include/ImageMagick-7/
# so that inclusions like wand/*.h and magick/*.h work
ln -s ./MagickCore %{buildroot}%{_includedir}/%{name}-%{maj}/magick
ln -s ./MagickWand %{buildroot}%{_includedir}/%{name}-%{maj}/wand
# these will be included via %doc
rm -r %{buildroot}%{_datadir}/doc/%{name}-%{maj}/
rm %{buildroot}%{_libdir}/*.la
# remove RPATH from perl module
perl_module=$(find %{buildroot}%{_prefix}/lib/perl5 -name '*.so')
chmod 755 $perl_module
chrpath -d $perl_module
chmod 555 $perl_module
# remove %%{buildroot} from distributed file
sed -i 's:%{buildroot}::' %{buildroot}/%{_libdir}/ImageMagick-%{mfr_version}/config%{libspec}%{clibver}/configure.xml
#remove duplicates
%fdupes -s %{buildroot}%{_defaultdocdir}/%{name}-%{maj}
%fdupes -s %{buildroot}%{_includedir}/%{name}-%{maj}
%fdupes -s %{buildroot}%{_libdir}/pkgconfig
%perl_process_packlist

%post -n libMagickCore%{libspec}%{clibver} -p /sbin/ldconfig
%postun -n libMagickCore%{libspec}%{clibver} -p /sbin/ldconfig
%post -n libMagickWand%{libspec}%{cwandver} -p /sbin/ldconfig
%postun -n libMagickWand%{libspec}%{cwandver} -p /sbin/ldconfig
%post -n libMagick++%{libspec}%{cxxlibver} -p /sbin/ldconfig
%postun -n libMagick++%{libspec}%{cxxlibver} -p /sbin/ldconfig

%pretrans %{config_spec}-upstream -p <lua>
-- this %pretrans to be removed soon [bug#1122033#c37]
path = "%{_sysconfdir}/%{config_dir}"
st = posix.stat(path)
if st and st.type == "directory" then
  os.remove(path .. ".rpmmoved")
  os.rename(path, path .. ".rpmmoved")
end

%post %{config_spec}-upstream
%{_sbindir}/update-alternatives --install %{_sysconfdir}/%{config_dir}  %{config_dir}   %{_sysconfdir}/%{config_dir}-upstream  1

%postun %{config_spec}-upstream
if [ ! -d %{_sysconfdir}/%{config_dir}-upstream ] ; then
    %{_sbindir}/update-alternatives --remove %{config_dir}  %{_sysconfdir}/%{config_dir}-upstream
fi

%pretrans %{config_spec}-SUSE -p <lua>
-- this %pretrans to be removed soon [bug#1122033#c37]
path = "%{_sysconfdir}/%{config_dir}"
st = posix.stat(path)
if st and st.type == "directory" then
  os.remove(path .. ".rpmmoved")
  os.rename(path, path .. ".rpmmoved")
end

%post %{config_spec}-SUSE
%{_sbindir}/update-alternatives --install %{_sysconfdir}/%{config_dir}  %{config_dir}   %{_sysconfdir}/%{config_dir}-SUSE      10

%postun %{config_spec}-SUSE
if [ ! -d %{_sysconfdir}/%{config_dir}-SUSE ] ; then
    %{_sbindir}/update-alternatives --remove %{config_dir}  %{_sysconfdir}/%{config_dir}-SUSE
fi

%files
%license LICENSE
%doc ChangeLog NEWS.txt
%{_bindir}/[^MW]*
%{_mandir}/man1/*
%exclude %{_mandir}/man1/*-config.1%{ext_man}

%files -n libMagickCore%{libspec}%{clibver}
%license LICENSE
%doc ChangeLog NEWS.txt
%{_libdir}/libMagickCore*.so.%{clibver}*
%dir %{_libdir}/ImageMagick*
%if !%{debug_build}
%dir %{_libdir}/ImageMagick*/modules*
%dir %{_libdir}/ImageMagick*/modules*/*
%exclude %{_libdir}/ImageMagick*/modules*/*/wmf.*
%if 0%{?suse_version} > 1315
%exclude %{_libdir}/ImageMagick*/modules*/*/jp2.*
%endif
%exclude %{_libdir}/ImageMagick*/modules*/*/djvu.*
%{_libdir}/ImageMagick*/modules*/*/*.so
# don't remove la files, see bnc#579798
%{_libdir}/ImageMagick*/modules*/*/*.la
%endif
%{_libdir}/ImageMagick*/config*

%files -n libMagickWand%{libspec}%{cwandver}
%{_libdir}/libMagickWand*.so.%{cwandver}*

%if !%{debug_build}
%files extra
%{_libdir}/ImageMagick*/modules*/*/wmf.so
# don't remove la files, see bnc#579798
%if 0%{?suse_version} > 1315
%{_libdir}/ImageMagick*/modules*/*/jp2.so
%{_libdir}/ImageMagick*/modules*/*/jp2.la
%endif
%{_libdir}/ImageMagick*/modules*/*/djvu.so
%{_libdir}/ImageMagick*/modules*/*/djvu.la
%endif

%files devel
%{_libdir}/libMagickCore*.so
%{_libdir}/libMagickWand*.so
%dir %{_includedir}/ImageMagick*
%{_includedir}/ImageMagick*/MagickCore
%{_includedir}/ImageMagick*/MagickWand
%{_includedir}/ImageMagick*/magick
%{_includedir}/ImageMagick*/wand
%{_bindir}/MagickCore-config
%{_bindir}/MagickWand-config
%{_libdir}/pkgconfig/MagickCore*.pc
%{_libdir}/pkgconfig/ImageMagick*.pc
%{_libdir}/pkgconfig/MagickWand*.pc
%{_mandir}/man1/*-config.1%{ext_man}
%exclude %{_mandir}/man1/Magick++-config.1%{ext_man}

%files -n perl-PerlMagick
%doc PerlMagick/README.txt
%doc PerlMagick/examples
%{_mandir}/man3/*
%{perl_vendorarch}/auto/Image
%{perl_vendorarch}/Image

%files -n libMagick++%{libspec}%{cxxlibver}
%{_libdir}/libMagick++*.so.%{cxxlibver}*

%files -n libMagick++-devel
%doc Magick++/examples
%doc Magick++/NEWS Magick++/README Magick++/AUTHORS
%{_libdir}/libMagick++*.so
%{_includedir}/ImageMagick*/Magick++.h
%{_includedir}/ImageMagick*/Magick++
%{_bindir}/Magick++-config
%{_libdir}/pkgconfig/Magick++*.pc
%{_mandir}/man1/Magick++-config.1%{ext_man}

%files doc
%{_defaultdocdir}/%{name}-%{maj}

%files %{config_spec}-upstream
%dir %{_sysconfdir}/ImageMagick*-upstream/
%config(noreplace) %{_sysconfdir}/ImageMagick*-upstream/*
%{_sysconfdir}/%{config_dir}
%ghost %{_sysconfdir}/alternatives/%{config_dir}

%files %{config_spec}-SUSE
%dir %{_sysconfdir}/ImageMagick*-SUSE/
%config %{_sysconfdir}/ImageMagick*-SUSE/*
%{_sysconfdir}/%{config_dir}
%ghost %{_sysconfdir}/alternatives/%{config_dir}

%changelog
* Mon Jan 27 2020 pgajdos@suse.com
- version update to 7.0.9.19
  * Alpha draw primitive no longer returns a parser exception.
  * Support 32-bit tiled TIFF images.
  * New -connected-component options (reference
    https://imagemagick.org/script/connected-components.php).
  * Make PNG creation reproducible (reference
    https://github.com/ImageMagick/ImageMagick/pull/1270).
  * Refactor uninitialize variable patch for -fx "while(,)" expression.
* Tue Jan 21 2020 pgajdos@suse.com
- version update to 7.0.9.17
  * Allow larger negative interline spacing (reference
    https://imagemagick.org/discourse-server/viewtopic.php?f=1&t=37391).
  * Conditional compile for huge xml pages for RSVG delegate library.
  * Put "width" property in the PNG namespace (reference
    https://github.com/ImageMagick/ImageMagick/issues/1833).
  * -combine -colorspace sRGB no longer returns grayscale output (reference
    https://github.com/ImageMagick/ImageMagick/issues/1835).
  * Support Jzazbz colorspace (contributed by snibgo @
    http://im.snibgo.com/jzazbz.htm).
* Tue Jan 14 2020 pgajdos@suse.com
- version update to 7.0.9.16
  * Fixed three failing Magick.NET unit tests.
  * Also support svg:xml-parse-huge when using librsvg.
  * Optimize -evaluate-sequence option (reference
    https://github.com/ImageMagick/ImageMagick/issues/1824).
  * Support Fx do() iterator.
  * `magick -size 100x100 xc:black black.pnm` no longer creates a white image
    (reference https://github.com/ImageMagick/ImageMagick/issues/1817).
  * setjmp/longjmp in jpeg.c no longer trigger undefind behavior (reference
    https://imagemagick.org/discourse-server/viewtopic.php?f=3&t=37379).
  * Permit compositing in the CMYK colorspace (reference
    https://imagemagick.org/discourse-server/viewtopic.php?f=3&t=37368).
* Wed Jan  8 2020 pgajdos@suse.com
- version update to 7.0.9.14
  * Support extended Fx assignment operators (e.g. *=, /=, ++, --, etc.)
  * Support Fx for() iterator.
  * Optimize Fx performance.
  * Ensure circle.rb renders the same for IMv6 and IMv7
* Thu Jan  2 2020 pgajdos@suse.com
- version update to 7.0.9.13
  * xc:white no longer creates a black PNM image (reference
    https://github.com/ImageMagick/ImageMagick/issues/1817).
  * Sync pixel cache for -kmeans option.
  * Thread -kmeans option.
  * PSD: only set the alpha channel when type is not 0.
  * Fix Lab to custom profile (CMYK or RGB) conversion bug (reference
  https://imagemagick.org/discourse-server/viewtopic.php?f=3&t=37318).
  * Fix Build failure with MinGW-w64 (reference
    https://github.com/ImageMagick/ImageMagick6/issues/67).
  * Inject image profile properties immediately after the image is read.
  * Replace pseudo-random number generator with a Xoshiro generator.
  * The -layers optimize option requires a fully transparent previous image.
  * Some clang releases do not support _aligned_alloc().
  * Support -kmeans command-line option.
  * The -layers optimize option requires a fully transparent prenityCheckGetExtent() method (reference
    https://github.com/ImageMagick/ImageMagick/pull/1798).
  * The -layers optimize option requires a fully transparent previous image.
* Thu Dec 12 2019 pgajdos@suse.com
- version update to 7.0.9.8
  * -type bilevel behavior restored, it creates a black and white image.
  * Support Pocketmod image format, e.g.
    convert -density 300 pages?.pdf pocketmod:organize.pdf
  * Fixed numerous issues  posted to GitHub (reference
    https://github.com/ImageMagick/ImageMagick/issues).
  * Update documentation.
- deleted patches
  - ImageMagick-targa.patch (upstreamed)
* Wed Nov 27 2019 pgajdos@suse.com
- version update to 7.0.9.6
  * Increase the maximum number of bezier coordinates (reference
    https://github.com/ImageMagick/ImageMagick/issues/1784).
  * Santize "'" from SHOW and WIN delegates under Linux, '"\' for Windows
    (thanks to Enzo Puig).
  * Correct for TGA orientation (reference
    https://imagemagick.org/discourse-server/viewtopic.php?f=3&t=34757).
  * The result for -compose Copy -extent on a  MYK image is CMYK (reference
    https://imagemagick.org/discourse-server/viewtopic.php?f=3&t=37118).
  * Fix potential buffer overflow when reading a fax image (alert from
    Justin).
  * Support dng:use-camera-wb option.
- added patches
  https://github.com/ImageMagick/ImageMagick/issues/1792
  + ImageMagick-targa.patch
* Wed Nov 20 2019 pgajdos@suse.com
- version update to 7.0.9.5
  * Ensure Ascii85 compression is thread safe.
  * Santize ';' from SHOW and WIN delegates.
  * Add exception parameter to CMS transform methods.
  * Output exception there is an attempt to perform an operation not allowed by
    the security policy
  * JPEG and JPG are aliases in coder security policy.
  * Fixed numerous issues  posted to GitHub
* Wed Oct 30 2019 pgajdos@suse.com
- version update to 7.0.9.1
  * Fixed numerous issues  posted to GitHub (reference
    https://github.com/ImageMagick/ImageMagick/issues).
  * Support trim:background-color define for -trim option.
- modified sources
  %% baselibs.conf
* Mon Oct  7 2019 pgajdos@suse.com
- version update to 7.0.8.68
  * Support animated WebP encoding/decoding (reference
    https://github.com/ImageMagick/ImageMagick/pull/1708).
  * Text stroke cut off (reference
    https://imagemagick.org/discourse-server/viewtopic.php?f=1&t=36829).
  * Adds support for lossless JPEG1 recompression (reference
    https://imagemagick.org/discourse-server/viewtopic.php?f=2&t=36828).
  * line endings renedered as empty boxes (reference
    https://github.com/ImageMagick/ImageMagick/issues/1704).
* Mon Sep 23 2019 pgajdos@suse.com
- version update to 7.0.8.66
  * Support compound statements in FX while() (reference
    https://github.com/ImageMagick/ImageMagick/issues/1701).
  * Eliminate fault when trace delegate is not available.
  * Properly distinquish linear and non-linear gray colorspaces (reference
    https://github.com/ImageMagick/ImageMagick/issues/1680).
  * Support XPM symbolic (reference
    https://github.com/ImageMagick/ImageMagick/issues/1684).
  * DilateIntensity is channel independent (reference
    https://imagemagick.org/discourse-server/viewtopic.php?f=3&t=36641).
* Mon Sep  2 2019 pgajdos@suse.com
- version update to 7.0.8.63
  * Properly identify the DNG and AI image format (reference
    https://imagemagick.org/discourse-server/viewtopic.php?f=3&t=36581).
  * Added option to limit the maximum point size with -define
    caption:max-pointsize=pointsize.
  * Corrected JP2 numresolution calculation (reference:
    https://github.com/ImageMund and -swirl (reference
    https://imagemagick.org/discourse-server/viewtopic.php?f=3&t=36512).
  * Enable reading EXR image file from stdin.
  * Module is a reserved keyword for C++ 20 (reference
    https://github.com/ImageMagick/ImageMagick/issues/1650).
  * Improve GetNextToken() performance.
  * Heap-buffer-overflow in Postscript coder (reference
    https://github.com/ImageMagick/ImageMagick/issues/1644).
  * The -alpha shape option nondeteministic under OpenMP (reference
    https://imagemagick.org/discourse-server/viewtopic.php?f=3&t=36396).
  * Correction to the ModulusAdd and ModulusSubtract composite op (reference
    https://imagemagick.org/discourse-server/viewtopic.php?f=2&t=36413).
* Mon Jul 22 2019 pgajdos@suse.com
- version update to 7.0.8.56
  * Unexpected -alpha shape results (reference
    https://imagemagick.org/discourse-server/viewtopic.php?f=3&t=36396).
  * Converting from PDF to PBM inverts the image (reference
    https://github.com/ImageMagick/ImageMagick/issues/1643).
  * Heap-buffer overflow (reference
    https://github.com/ImageMagick/ImageMagick/issues/1641
  * PerlMagick test suite passes again (reference
    https://github.com/ImageMagick/ImageMagick/issues/1640)
  * resolve division by zero  (reference
    https://github.com/ImageMagick/ImageMagick/issues/1629).
  * introducing MagickLevelImageColors() MagickWand method.
  * Transient problem with text placement with gravity (reference
    https://github.com/ImageMagick/ImageMagick/issues/1633).
  * Support TIM2 image format (reference
    https://github.com/ImageMagick/ImageMagick/pull/1571).
  * For -magnify option, specify an alternative scaling method with -define
    magnify:method=method, choose from these methods: eagle2X, eagle3X,
    eagle3XB, epb2X, fish2X, hq2X,  scale2X (default), scale3X, xbr2X.
* Mon Jul 15 2019 pgajdos@suse.com
- version update to 7.0.8.53
  * Fix -fx parsing issue (reference
    https://imagemagick.org/discourse-server/viewtopic.php?f=3&t=36314).
  * Eliminate buffer overflow in TranslateEvent() (reference
    https://github.com/ImageMagick/ImageMagick/issues/1621).
  * Clone rather than copy X window name/icon.
  * Optimize PDF reader.
* Mon Jun 24 2019 pgajdos@suse.com
- version update to 7.0.8.50
  * Added support for reading all images from a HEIC image (reference
    https://github.com/ImageMagick/ImageMagick/issues/1391).
  * Heap-buffer-overflow in MagickCore/fourier.c (reference
  https://github.com/ImageMagick/ImageMagick/issues/1588).
  * Fixed a number of issues (reference
    https://imagemagick.org/discourse-server/viewforum.php?f=3).
  * Fixed a number of issues (reference
    https://github.com/ImageMagick/ImageMagick/issues).
* Tue Jun 18 2019 pgajdos@suse.com
- disable indirect reads [bsc#1138425]
  (https://imagemagick.org/script/security-policy.php)
- modified patches
  %% ImageMagick-configuration-SUSE.patch (refreshed)
* Wed Jun 12 2019 pgajdos@suse.com
- version update to 7.0.8.49
  * Add support for RGB565 image format (reference
    https://imagemagick.org/discourse-server/viewtopic.php?f=2&t=36078).
  * Use user defined allocator instead of `malloc` (reference
    https://github.com/ImageMagick/ImageMagick6/pull/49/).
  * Add static decorator to accelerator kernels (reference
    https://github.com/ImageMagick/ImageMagick/issues/1366).
* Mon Jun  3 2019 pgajdos@suse.com
- version update to 7.0.8.48
  * Fix transient convolution bug.
- deleted patches
  - ImageMagick-montage.t-failing.patch (upstreamed)
* Tue May 28 2019 pgajdos@suse.com
- version update to 7.0.8.47
  * Suppo  * Text improvements to the internal SVG renderer.
- disable failing averageImages test for i586
- modified patches
  disable also PCL [bsc#1136183]
  %% ImageMagick-configuration-SUSE.patch
- added patches
  https://github.com/ImageMagick/ImageMagick/issues/1580
  + ImageMagick-montage.t-failing.patch
* Mon May 27 2019 pgajdos@suse.com
- version update to 7.0.8.46
  * Return HEIC images in the sRGB colorspace.
  * Fix image signatures to ensure they are Q-depth invariant (reference
    https://imagemagick.org/discourse-server/viewtopic.php?f=1&t=35970).
  * Fixed a number of issues (reference
    https://imagemagick.org/discourse-server/viewforum.php?f=3).
  * Fixed a number of issues (reference
    https://github.com/ImageMagick/ImageMagick/issues).
* Mon May 13 2019 pgajdos@suse.com
- version update to 7.0.8.44
  * Fixed a number of issues (reference
    https://imagemagick.org/discourse-server/viewforum.php?f=3).
  * Fixed a number of issues (reference
    https://github.com/ImageMagick/ImageMagick/issues).
* Mon Apr 29 2019 pgajdos@suse.com
- version update to 7.0.8.42
  * Fixed a number of issues (reference
    https://imagemagick.org/discourse-server/viewforum.php?f=3).
  * Fixed a number of issues (reference
    https://github.com/ImageMagick/ImageMagick/issues).
* Tue Apr 23 2019 pgajdos@suse.com
- version update to 7.0.8.41
  * Fixed a number of issues (reference
    https://github.com/ImageMagick/ImageMagick/issues).
  * Honor SOURCE_DATE_EPOCH environment variable (reference
    https://github.com/ImageMagick/ImageMagick/pull/1496/).
  * Standardize on UTC time for any image format timestamp.
  * Add MagickAutoThresholdImage(), MagickCannyEdgeImage(),
    MagickComplexImages(), MagickConnectedComponentsImage(),
    MagickHoughLineImage(), MagickKuwaharaImage(), MagickLevelizeImageColors(),
    MagickLevelImageColors(), MagickMeanShiftImage(), MagickPolynomialImage(),
    MagickRangeThresholdImage(), MagickSetSeed(), MagickWaveletDenoiseImage()
    methods to MagickWand API.
* Tue Apr 23 2019 mvetter@suse.com
-bsc#1133110 - Remove jasper dependency from ImageMagick
* Tue Apr 16 2019 pgajdos@suse.com
- version update to 7.0.8.40
  * Fixed a number of issues (reference
    https://imagemagick.org/discourse-server/viewforum.php?f=3).
  * Fixed a number of issues (reference
    https://github.com/ImageMagick/ImageMagick/issues).
  * The -layers option compared pixels inocorrectly as opacity rather than
    alpha.
  * The -preview raise option now returns expected results.
  * Initialise ghostscript instances with NULL (reference
    https://github.com/ImageMagick/ImageMagick/pull/1538).
  * Modulo off by one patch for -virtual-pixel option (reference
    https://imagemagick.org/discourse-server/viewtopic.php?f=3&t=35789).
* Thu Apr  4 2019 pgajdos@suse.com
- version update to 7.0.8.37
  * Fixed -virtual-pixel option (reference
    https://imagemagick.org/discourse-server/viewtopic.php?f=3&t=35789).
  * -draw image DstOver is now responsive to the composite operator (reference
    https://imagemagick.org/discourse-server/viewtopic.php?f=1&t=35650).
  * Fixed a number of issues (reference
    https://github.com/ImageMagick/ImageMagick/issues).
* Mon Mar 18 2019 pgajdos@suse.com
- added temporary %%pretrans to ImageMagick-config-upstream and
  ImageMagick-config-SUSE [bsc#1122033comment#37]
* Mon Mar 18 2019 pgajdos@suse.com
- version update to 7.0.8.34
  * Associate one lock with each resource.
  * Report exception if opening TIFF did not work out.
  * Fixed numerous use of uninitialized values, integer overflow,  * -trim is no longer sensitive to the image virtual canvas.
* Mon Mar  4 2019 pgajdos@suse.com
- update to 7.0.8-30
  * Support define to remove additional background from an image during a
    trim, e.g. -define trim:percent-background=0%% -trim.
  * Fixed a number of issues (reference
    https://github.com/ImageMagick/ImageMagick/issues).
  * Fixed numerous use of uninitialized values, integer overflow, memory
    exceeded, and timeouts (credit to OSS Fuzz).
- deleted patches
  - ImageMagick-montage.t.patch (upstreamed)
* Thu Feb 28 2019 pgajdos@suse.com
- provide two new (conflicting) packages with configuration
  [bsc#1122033]:
  * ImageMagick-config-upstream
  - provides configuration provided by upstream (no restrictions)
  * ImageMagick-config-SUSE (preferred)
  - provides configuration provided by SUSE (with security
    restrictions)
  and use update-alternatives for selecting configurations.
- remove code for < 1315
- deleted patches
  - ImageMagick-disable-insecure-coders.patch (renamed)
- added patches
  + ImageMagick-configuration-SUSE.patch
* Tue Feb 19 2019 pgajdos@suse.com
- updated to 7.0.8-28
  * Fixed a number of issues (reference
    https://github.com/ImageMagick/ImageMagick/issues).
- deleted patches
  - ImageMagick-test-FITS.patch (upstreamed)
- deleted sources
  - input.fits (not needed)
- added patches
  https://github.com/ImageMagick/ImageMagick/issues/1484
  + ImageMagick-montage.t.patch
* Mon Feb 11 2019 Petr Gajdos <pgajdos@suse.com>
- update to 7.0.8-27:
  * Mod patch to properly handle subimage ranges (e.g. image.gif[2-3]).
- added ImageMagick-test-FITS.patch and input.fits temporarily
  https://github.com/ImageMagick/ImageMagick/issues/1478
- remove ImageMagick-clamp-after-edge.patch, it is solved another
  way (see [bsc#1106415c#10])
* Thu Feb  7 2019 Petr Gajdos <pgajdos@suse.com>
- update to 7.0.8-26:
  * Fixed a number of issues (reference
    https://github.com/ImageMagick/ImageMagick/issues).
* Thu Jan 31 2019 info@paolostivanin.com
- update to 7.0.8-25:
  * Eliminate spurious font warning (#1458)
  * Support HEIC EXIF & XMP profiles.
- changelog for 7.0.8-24:
  * Support -clahe option real clip limit
  * ShadeImage() kernels can return negative pixels, clamp to range (#1319)
  * Annotate with negative offsets no longer renders slanted text
* Mon Jan 14 2019 Petr Gajdos <pgajdos@suse.com>
- clamp after edge [bsc#1106415]
  + ImageMagick-clamp-after-edge.patch
* Mon Jan  7 2019 Petr Gajdos <pgajdos@suse.com>
- update to 7.0.8-23:
  * CacheInfo destructor must be aligned in DestroyPixelStream().
  * Support negative rotations in a geometry (e.g. -10x-10+10+10).
  * Return expected canvas offset after a crop with gravity.
* Fri Dec 28 2018 Petr Gajdos <pgajdos@suse.com>
- update to 7.0.8-21:
  * Check to ensure SeekBlob() offset can be represented in an off_t.
  * Cube image format returns a HALD image.
  * CLAHE tiles overlapped are now centered relative to the image.
* Wed Dec 19 2018 Petr Gajdos <pgajdos@suse.com>
- update to 7.0.8-17:
  * Support -clahe clip limit with percentages (e.g. -clahe
    50x50%%+128+3).
* Tue Dec 11 2018 Petr Gajdos <pgajdos@suse.com>
- update to 7.0.8-16:
  * Add support for -clahe clip limit with percentages (e.g. -clahe 2x2+128+3%%)
  * Check for modulo underflow.
  * Change SVG default DPI to 96 from 90 to meet recommendation of SVG2 & CSS.
  * Added support for the -clahe option: contrast limited adaptive histogram
    equalization.
  * Added support for GIMP 2.10 files (reference
    https://github.com/ImageMagick/ImageMagick/pull/1381).
* Wed O92]
  [bsc#1109976#c7]
* Mon Sep 24 2018 Petr Gajdos <pgajdos@suse.com>
- update to 7.0.8-12:
  * Added support for arithmetic coding to the jpeg encoder:
  - define jpeg:arithmetic-coding=true.
  * Fixed numerous use of uninitialized values, integer overflow, memory
    exceeded, and timeouts (credit to OSS Fuzz).
* Mon Sep  3 2018 pgajdos@suse.com
- update to 7.0.8-11:
  * Fixed numerous use of uninitialized values, integer overflow, memory
    exceeded, and timeouts (credit to OSS Fuzz).
  * Add support for "module" security policy.
* Wed Aug 22 2018 pgajdos@suse.com
- disable PS, PS2, PS3, XPS and PDF coders in default policy.xml
  [bsc#1105592]
* Fri Aug 17 2018 pgajdos@suse.com
- update to 7.0.8-10:
  * Added dcraw coder (dcraw:img.cr2) that can be used to force the use of the
    dcraw delegate when libraw is the default raw delegate.
  * Restored thread support for the HEIC coder.
  * ThumbnailImage function no longer reveals sensitive information (reference
    https://github.com/ImageMagick/ImageMagick/issues/1243).
- remove upstreamed ImageMagick-filter.t.patch
* Mon Aug  6 2018 pgajdos@suse.com
- update to 7.0.8-9:
  * XBM coder leaves the hex image data uninitialized if hex value of the
    pixel is negative.
  * More improvements to SVG text handling.
  * New -range threshold option that combines hard and soft thresholding.
  * Non-HDRI ScaleLongToQuantum() private method no longer adds a half interval.
  * Fixed memset() negative-size-param (reference
    https://github.com/ImageMagick/ImageMagick/issues/1217).
  * Fixed numerous use of uninitialized values, integer overflow, memory
    exceeded, and timeouts (credit to OSS Fuzz).
- fixed tests by ImageMagick-filter.t.patch
  https://github.com/ImageMagick/ImageMagick/issues/1241
* Tue Jul 17 2018 pgajdos@suse.com
- enable i586 tests again, except t/montage.t
* Mon Jul 16 2018 pgajdos@suse.com
- update to 7.0.8-6:
  * Improve SVG support for tspan element.
  * Add support for -fx image.extent.
  * Fixed a few potential memory leaks.
  * Fixed numerous use of uninitialized values, integer overflow, memory
    exceeded, and timeouts (credit to OSS Fuzz).
  * Support %%B property, the image file size without any decorations.
* Mon Jul  2 2018 kstreitova@suse.com
- use "BuildRequires: p7zip-full" for TW as 7za binary needed by
  ImageMagick was moved to this package (see bsc#899627 for more
  details about this change)
* Tue Jun 26 2018 pgajdos@suse.com
- update to 7.0.8-3:
  * Apply translate component of SVG transform rotate.
  * More robust SVG text handling.
  * Fixed numerous use of uninitialized values, integer overflow, memory
    exceeded, and timeouts (credit to OSS Fuzz).
  * Fixed an issue with stroke and label
* Wed Jun 13 2018 pgajdos@suse.com
- update to 7.0.8-0:
  * Fixed numerous use of uninitialized values, integer overflow, memory
    exceeded, and timeouts (credit to OSS Fuzz).
  * Heap buffer overflow fix (reference
    https://github.com/ImageMagick/ImageMagick/issues/1156).
  * Boundary issues with -gamma option when HDRI is enabled (reference
    https://github.com/ImageMagick/ImageMagick/issues/1151).
  * Properly initialize SVG color style.
  * A SVG rectangle with a width and height of 1 is a point.
  * Fixed memory corruption for MVG paths.
- consider test to be completely broken on i586, removing:
  - ImageMagick-relax-filter.t.patch
  - ImageMagick-tests.tap-attributes.patch
* Mon May 21 2018 pgajdos@suse.com
- update to 7.0.7-34:
  * Added support for reading eXIf chunks to the PNG coder.
  * Fixed numerous use of uninitialized t.
- removed upstreamed ImageMagick-draw-circle-primitive.patch
* Wed May  2 2018 pgajdos@suse.com
- instead of disabling test, apply upstream fix introduced
  few minutes after upstream report was made
  - ImageMagick-filter.t-primitive-circle.patch
  + ImageMagick-draw-circle-primitive.patch
* Wed May  2 2018 pgajdos@suse.com
- update to 7.0.7-29:
  * Fixed numerous use of uninitialized values, integer overflow,
    memory exceeded, and timeouts (credit to OSS Fuzz).
- turn off drawing primitive 'circle' test:
  + ImageMagick-filter.t-primitive-circle.patch
- dropped patches (upstreamed):
  - ImageMagick-CVE-2018-9135.patch
  - ImageMagick-write.t-pict.patch
* Wed Apr 11 2018 pgajdos@suse.com
- security update (webp.c)
  * CVE-2018-9135 [bsc#1087825]
    + ImageMagick-CVE-2018-9135.patch
* Tue Apr 10 2018 pgajdos@suse.com
- consider urw-base35-fonts [bsc#1088463]
* Tue Apr 10 2018 tchvatal@suse.com
- Drop buildrequire on mupdf-devel-static, there is only one occurance
  in all makefiles mentioning MUPDF_LIBS and it is always empty
- Format with minimal run of spec-cleaner
  * Use license
  * Sort BRs alphabetically
* Thu Apr  5 2018 fcrozat@suse.com
- Remove BuildRequires on dcraw, it is not needed at buildtime.
* Wed Apr  4 2018 pgajdos@suse.com
- do not run tests on i586 at all
* Mon Mar 26 2018 pgajdos@suse.com
- update to 7.0.7-28:
  * Fixed numerous use of uninitialized values, integer overflow, memory
    exceeded, and timeouts
- tesuite still fails, however:
  https://github.com/ImageMagick/ImageMagick/issues/1058
- added ImageMagick-write.t-pict.patch
- added ImageMagick-tests.tap-attributes.patch
* Mon Mar 19 2018 pgajdos@suse.com
- update to 7.0.7-27:
  * Fixed numerous use of uninitialized values, integer overflow,
    memory exceeded, and timeouts.
- remove ImageMagick-remove-test.tap-attributes.patch as the perl
  testsuite fails in bunch of tests anyway. Waiting for results of
  the upstream bug (https://github.com/ImageMagick/ImageMagick/issues/1019)
* Fri Mar 16 2018 pgajdos@suse.com
- added ImageMagick-remove-test.tap-attributes.patch, removes
  failing test on i586
  https://github.com/ImageMagick/ImageMagick/issues/1019
* Wed Mar 14 2018 pgajdos@suse.com
- update to 7.0.7-26
  * Fixed numerous use of uninitialized values, integer overflow, memory
    exceeded, and timeouts (credit to OSS Fuzz).
* Mon Mar  5 2018 pgajdos@suse.com
- update to 7.0.7-25
  * Fixed numerous use of uninitialized values, integer overflow,
    memory exceeded, and timeouts (credit to OSS Fuzz).
* Wed Feb 28 2018 pgajdos@suse.com
- update to 7.0.7-24
  * Do not refer to page in OptimizeLayerFrames (reference
    https://github.com/ImageMagick/ImageMagick/pull/987).
  * PerlMagick unit tests pass again.
  * Fixed numerous use of uninitialized values, integer overflow,
    memory exceeded, and timeouts (credit to OSS Fuzz).
- removed upstreamed
  - ImageMagick-write.t-PICT-signature.patch
  - ImageMagick-montage.t-directory-exception.patch
* Fri Feb 23 2018 pgajdos@suse.com
- upstream fixes the test by changing the signature
  - ImageMagick-820e636.patch
  + ImageMagick-write.t-PICT-signature.patch
* Wed Feb 21 2018 pgajdos@suse.com
- update to 7.0.7.23
  * Fixed numerous use of uninitialized values, integer overflow,
    memory exceeded, and timeouts (credit to OSS Fuzz).
  * Add list-length policy to limit the maximum image sequence length.
- added patches
  + ImageMagick-montage.t-directory-exception.patch
  + ImageMagick-820e636.patch
* Mon Feb 19 2018 crrodriguez@opensuse.org
- Add explicit buildrequires on: pkgconfig(libratio geometry, e.g. -crop 3:2.
  * Add support for reading the HEIC image format (reference
    https://github.com/ImageMagick/ImageMagick/issues/507).
  * Fixed numerous memory leaks, credit to OSS Fuzz.
* Tue Jan  9 2018 pgajdos@suse.com
- update to 7.0.7.21
  * Fix some enum values in the OpenCL code.
  * Fixed numerous memory leaks.
  * Check for webpmux library version 0.4.4.
  * Fix heap use after free error.
  * Fix error reading multi-layer XCF image file.
  * Fix possible stack overflow in WEBP reader.
* Tue Jan  2 2018 schwab@suse.de
- enable ImageMagick-s390-disable-tests.patch also for ppc, ppc64
* Wed Dec 27 2017 pgajdos@suse.com
- readd ImageMagick-relax-filter.t.patch for SLE15 i586
- enable ImageMagick-s390-disable-tests.patch also for s390, in
  addition to s390x
* Mon Dec 18 2017 pgajdos@suse.com
- update to 7.0.7-15
  * Overall standard deviation is the average of each pixel channel.
  * Support Stereo composite operator.
  * The -tint option no longer munges the alpha channel.
  * Don't delete in-memory blob when reading an image.
  * Support HDRI color profile management.
* Mon Dec  4 2017 pgajdos@suse.com
- remove forgotten 'exit 0' from check phase
* Wed Nov 22 2017 pgajdos@suse.com
- update to 7.0.7-11
  * no upstream change log in ChangeLog, as usually would be, except
    Release ImageMagick version 7.0.7-11,
    GIT revision 21635:0447c6b46:20171111
* Wed Nov  1 2017 pgajdos@suse.com
- update to 7.0.7-10
  * Fixed a problem with resource bookkeeping in
    AcquireMatrixInfo().
- update to 7.0.7-9
  * Encode JSON control characters.
  * Added support for reading mipmaps in dds images.
- removed unneded ImageMagick-relax-filter.t.patch
* Mon Oct 16 2017 pgajdos@suse.com
- disable failing tests on s390x [bsc#1062932]
  + ImageMagick-s390-disable-tests.patch
* Mon Oct 16 2017 pgajdos@suse.com
- update to 7.0.7-8
  * Return expected results for a percent 0 -chop option argument.
  * Tweaks to OpenMP support within ImageMagick.
  * Correct handling of GIF transparency.
- recommend ghostscript [bsc#1054924c#25]
* Thu Oct  5 2017 pgajdos@suse.com
- updated to 7.0.7-6
  * Reset the magick_list_initialized boolean when needed.
  * Fixed numerous memory leaks.
  * Support URW-base35 fonts.
  * Removed "ping_preserve_iCCP=MagickTrue;" statement that was
    inadvertently added to coders/png.c.
* Tue Oct  3 2017 pgajdos@suse.com
- %%make_install only for sle12 and higher
* Mon Oct  2 2017 jengelh@inai.de
- Update package summaries and RPM groups.
  Make use of %%make_install.
* Tue Sep 26 2017 pgajdos@suse.com
- updated to 7.0.7-4
  * Fixed numerous memory leaks.
  * Maximum valid hour is 23, not 24, in the PNG tIME chunk, and maximum
    valid minute is 59, not 60.
  * Use signed integer arithmetic to calculate timezone corrections.
* Mon Sep 11 2017 pgajdos@suse.com
- builds for sle11
* Mon Sep 11 2017 pgajdos@suse.com
- builds for sle12
* Mon Sep 11 2017 pgajdos@suse.com
-  updated to 7.0.7-1
  * Fixed numerous memory leaks.
  * Added -define tiff:write-layers=true to add support for writing
    layered tiff files.
  * Don't overwrite symbolic links when the shred policy is enabled.
  * Support -metric ssim, structual similarity index.
  * Fixed thread safety issue inside the pango and librsvg decoder.
  * Fixed bug with writing tIME chunk when timezone has a negative
    offset.
  * Support CubicSpline resize filter.  Define the lobes with the
  - define filter:lobes={2,3,4}.
  * Prevent assertion failure when creating PDF thumbnail.
* Thu Aug 31 2017 pgajdos@suse.com
- fix previous submission
- remotch configure ones
- Remove indirect-reads switch not present in configure.ac at all
* Mon Aug 28 2017 pgajdos@suse.com
- another attempt to make a libMagickCore* version installable with
  another version [bsc#1054659]
  + ImageMagick-library-installable-in-parallel.patch
* Mon Aug 14 2017 pgajdos@suse.com
- updated to 7.0.6-7
  * Improve EPS aliasing
  * Added a new option called 'dds:fast-mipmaps'
  * The mipmaps of a dds image can now be created from a list of images with
  - define dds:mipmaps=fromlist
  * Fixed numerous memory leaks
  * Put UTC time in the PNG tIME chunk instead of local time
  * Fixed numerous memory leaks
  * Properly set image->colorspace in the PNG decoder (previously
    it was setting image->gamma, but only setting image->colorspace
    for grayscale and gray-alpha images.
  * Fix improper use of NULL in the JNG decoder
  * Added "-define png:ignore-crc" option to PNG decoder. When you know
    your image has no CRC or ADLER32 errors, this can speed up decoding.
    It is also helpful in debugging bug reports from "fuzzers".
  * Off by one error for gradient coder
  * YUV coder no longer renders streaks
  * Fixed numerous memory leaks
  * Added experimental PNG orNT chunk, to store image->orientation.
  * Removed vpAg chunk write support
  * Fixed numerous memory leaks
  * Fix memory leaks when reading a malformed JNG image
  * Fixed numerous memory leaks
  * The -monochrome option no longer returns a blank canvas
  * coders/png.c: fixed memory leak of quantum_info
  * coders/png.c: fixed NULL dereference when trying to write an empty MNG
  * Added caNv, eXIf, and pHYs to the list of PNG chunks to be removed
    by the "-strip" option.
  * Implemented PNG eXIf chunk support
  * Support new -auto-threshold option.  OTSU and Triangle methods are
    currently supported.  Look for the Kapur method in the next release.
  * Fixed numerous memory leaks
  * Don't use variable float_t / double_t, bump SO
  * Support DNG images with libraw delegate library.
  * Reject PNG file that is too small (under 60 bytes) to contain
    a valid image.
  * Reject JPEG file that is too small (under 107 bytes) to contain
    a valid image.
  * Reject JNG file that is too small (under 147 bytes) to contain
    a valid image.
  * Stop a memory leak in read_user_chunk_callback()
* Thu Aug 10 2017 ro@suse.de
- workaround failed test
  + ImageMagick-relax-filter.t.patch (patch modified)
  on i586 with sse2 enabled, the Contrast test in filter.t fails
* Wed Jun 28 2017 pgajdos@suse.com
- updated to 7.0.6-0
  * coders/png.c: Accept exIf chunks whose data segment
    erroneously begins with "Exif\0\0".
  * Introduce SetMagickSecurityPolicy() (MagickCore) and
    MagickSetSecurityPolicy() (MagickWand) to set the ImageMagick security
    policy (reference https://github.com/ImageMagick/ImageMagick/issues/407).
  * Removed experimental PNG zxIF chunk support; the proposal is dead.
  * Fix choppy bitmap font rendering (reference
    https://www.imagemagick.org/discourse-server/viewtopic.php?f=3&t=32071).
  * The +opaque option is not longer a noop (reference
    https://www.imagemagick.org/discourse-server/viewtopic.php?f=3&t=32081).
  * Add support  for 'hex:' property.
  * Transient error validating the JPEG-2000 image format (reference
    https://github.com/ImageMagick/ImageMagick/issues/501).
  * Properly allocate DCM image colormap (reference
    https://www.imagemagick.org/discourse-server/viewtopic.php?f=3&t=32063).
  * Improper allocation of memory for IM instances without threads (reference
    https://github.com/Ierence
    https://www.imagemagick.org/discourse-server/viewtopic.php?f=2&t=31938).
* Fri May 19 2017 pgajdos@suse.com
- updated to 7.0.5-6
  * Revise DICOM window and rescale handling.
  * Restore the -alpha Shape option.
  * Fix transient PDF bug.
  * The +opaque option now works on all channels.
  * Ensure backwards compatibility for the -combine option.
  * Check for EOF conditions for RLE image format.
  * Reset histogram page geometry.
* Wed Apr 26 2017 pgajdos@suse.com
- updated to 7.0.5-5
  * Minimize buffer copies to improve OpenCL performance.
  * Morphology thinning is no longer a no-op.
  * Patch two PCD writer problems, corrupt output and dark pixels.
  * Support ICC based PDF's.
  * Fix improper EPS clip path rendering.
- workaround failed test
  + ImageMagick-relax-filter.t.patch
* Wed Mar 22 2017 pgajdos@suse.com
- updated to 7.0.5-4
  * new branch, see
    https://www.imagemagick.org/script/porting.php
- deleted unneded patches
  . ImageMagick-6.6.8.9-doc.patch
  . ImageMagick-6.6.8.9-examples.patch
  . ImageMagick-6.7.6.1-no-dist-lzip.patch
  . ImageMagick-6.8.4.0-dont-build-in-install.patch
  . ImageMagick-6.8.4.0-rpath.patch
  . ImageMagick-montage.t.patch
  . ImageMagick-6.8.5.7-no-XPMCompliance.patch
- renamed patches
  . ImageMagick-6.8.8-1-disable-insecure-coders.patch to
    ImageMagick-disable-insecure-coders.patch
* Mon Mar 20 2017 pgajdos@suse.com
- updated to 6.8.8-2
  * Support namespaces for the security policy.
  * Respect throttle policy.
  * Support the -authenticate option for PDF.
  * Fix Spurious memory allocation message.
  * Identical images should return inf for PSNR.
  * Fixed fd leak for webp coder.
  * Prevent random pixel data for corrupt JPEG image.
  * Support pixel-cache and shred security policies.
  * Fixed memory leak when creating nested exceptions in Magick++.
  * Eliminate bogus assertion.
  * Unbreak build without JPEG support.
  + ImageMagick-montage.t.patch
* Mon Feb 13 2017 pgajdos@suse.com
- updated to 6.9.7-7
  * Sanitize comments that include braces for the MIFF image format.
  * Uninitialized data in MAT image format.
  * see ChangeLog for full changelog
* Tue Jan 24 2017 pgajdos@suse.com
- updated to 6.9.7-5
  * Don't set background for transparent tiled images
  * Added support for RGB555, RGB565, ARGB4444 and ARGB1555 to the
    BMP encoder
  * Fix memory leak in MPC image format.
  * Increase memory allocation for TIFF pixels
  * etc. see ChangeLog
* Fri Dec  2 2016 pgajdos@suse.com
- updated to 6.9.6-6
  * If a convenient line break is not found, force it for caption: (reference
    https://www.imagemagick.org/discourse-server/viewtopic.php?f=3&t=30887).
  * Off by 1 error when computing the standard deviation (reference
    https://www.imagemagick.org/discourse-server/viewtopic.php?f=2&t=30866).
  * Apply Debian patches, (reference
    https://github.com/ImageMagick/ImageMagick/issues/304).
  * Permit EPT images with just a TIFF or EPS image, not both (reference
    https://www.imagemagick.org/discourse-server/viewtopic.php?f=3&t=30921).
  * The -clone option no longer leak memory.
- turn on make check along perl test
* Tue Nov 22 2016 pgajdos@suse.com
- Updated to 6.9.6-5
  * Web pages were broken when we moved to HTTPS protocol.
  * Restore -sharpen / -convolve options to work with CMYK (reference
    https://github.com/ImageMagick/ImageMagick/issues/299).
  * Off by one memory allocation (reference
    https://github.com/ImageMagick/ImageMagick/issues/296).
  * Prevent fault in MSL interpreter (reference
    https://www.imagemagick.org/discourse-servtch.
  * Fixed incorrect RLE decoding when reading a DCM image that contains
    multiple segments.
  * Fixed incorrect RLE decoding when reading an SGI image (reference
    https://www.imagemagick.org/discourse-server/viewtopic.php?f=3&t=30514)
* Mon Sep 26 2016 pgajdos@suse.com
- Updated to 6.9.5-10
  * Added layer RLE compression to the PSD encoder.
  * Added define 'psd:preserve-opacity-mask' to preserve the opacity mask
    in a PSD file.
  * Fixed issue where the display window was used instead of the data window
    when reading EXR files (reference
    https://www.imagemagick.org/discourse-server/viewtopic.php?f=3&p=137849).
* Fri Sep 16 2016 rpm@fthiessen.de
- Updated to 6.9.5-9
  * Prevent memory use after free
    (reference https://www.imagemagick.org/discourse-server/viewtopic.php?f=3&t=30245).
  * Prevent buffer overflow.
  * Prevent spurious removal of MPC cache files
    (reference https://www.imagemagick.org/discourse-server/viewtopic.php?f=3&t=30256).
  * Prevent buffer overflow and other problems in SIXEL, PDB, MAP,
    TIFF, and CALS coders.
  * Fix MSVG regression
    (reference https://github.com/ImageMagick/ImageMagick/issues/252).
  * Prevent buffer overflow in BMP & SGI coders.
  * Fixed incorrect padding calculation in PSD encoder.
* Mon Aug  1 2016 pgajdos@suse.com
- updated to 6.9.5-4
  * Prevent buffer overflow
* Fri Jul 29 2016 schuetzm@gmx.net
- updated to 6.9.5-3:
  * Fix MVG stroke-opacity (reference
    https://github.com/ImageMagick/ImageMagick/issues/229).
  * Prevent possible buffer overflow when reading TIFF images (bug report from
    Shi Pu of MS509 Team).
  * To comply with the SVG standard, use stroke-opacity for transparent strokes.
  * The histogram coder now returns the correct extent.
  * Use CopyMagickString() rather than CopyMagickMemory() for strings.
  * Correct for numerical instability (reference
    https://github.com/ImageMagick/ImageMagick/issues/218).
* Mon Jun  6 2016 pgajdos@suse.com
- updated to 6.9.4-7:
  * Fix small memory leak (patch provided by ?????? ??????).
  * Coder path traversal is not authorized (bug report provided by
    Masaaki Chida).
  * Turn off alpha channel for the compare difference image (reference
    http://www.imagemagick.org/discourse-server/viewtopic.php?f=3&t=29828).
  * Support configure script --enable-pipes option to enable pipes (|) in
    filenames.
  * Support configure script --enable-indirect-reads option to enable
    indirect reads (@) in filenames.
- remove ImageMagick-CVE-2016-5118.patch, use --enable-pipes=no instead
* Tue May 31 2016 pgajdos@suse.com
- updated to 6.9.4-5:
  * Most OpenCL operations are now executed asynchronous.
  * Security improvements to TEXT coder broke it (reference
    https://www.imagemagick.org/discourse-server/viewtopic.php?f=3&t=29754).
  * Fix stroke offset problem for -annotate (reference
    https://www.imagemagick.org/discourse-server/viewtopic.php?f=3&t=29626).
  * Add additional checks to DCM reader to prevent data-driven faults (bug
    report from Hanno Böck).
  * Fixed proper placement of text annotation for east / west gravity.
  2016-05-15  6.9.4-3 Cristy  <quetzlzacatenango@image...>
  * Fix pixel cache on disk regression (reference
    https://github.com/ImageMagick/ImageMagick/issues/202).
  * Quote passwords when passed to a delegate program.
  * Can read geo-related EXIF metdata once-again (reference
    https://github.com/ImageMagick/ImageMagick/issues/198).
  * Sanitize all delegate emedded formatting characters.
  * Don't sync pixel cache in AcquireAuthenticCacheView() (bug ray 17 2016 pgajdos@suse.com
- updated to 6.9.4-1:
  * Remove https delegate.
  * Check for buffer overflow in magick/draw.c/DrawStrokePolygon().
  * Replace show delegate title with image filename rather than label.
  * Fix GetNextToken() off by one error.
  * Remove support for internal ephemeral coder.
- refreshed ImageMagick-6.8.8-1-disable-insecure-coders.patch
- believe or not, correct license string is ImageMagick:
  http://spdx.org/licenses/ImageMagick.html
* Wed May 11 2016 chris@computersalat.de
- rework ImageMagick-6.8.8-1-disable-insecure-coders.patch
  * add new policy (TEXT, SHOW, WIN and PLT)
- rebase patches (p0)
  * ImageMagick-6.6.8.9-doc.patch
  * ImageMagick-6.6.8.9-examples.patch
  * ImageMagick-6.7.6.1-no-dist-lzip.patch
  * ImageMagick-6.8.4.0-dont-build-in-install.patch
  * ImageMagick-6.8.4.0-rpath.patch
  * ImageMagick-6.8.5.7-no-XPMCompliance.patch
  * ImageMagick-6.8.8-1-disable-insecure-coders.patch
* Thu May  5 2016 vcizek@suse.com
- Disable insecure coders [bnc#978061]
  * ImageMagick-6.8.8-1-disable-insecure-coders.patch
  * CVE-2016-3714
  * CVE-2016-3715
  * CVE-2016-3716
  * CVE-2016-3717
  * CVE-2016-3718
* Thu May  5 2016 pgajdos@suse.com
- Update to 6.9.3-10: fix imagetragick
* Thu Apr 14 2016 pgajdos@suse.com
- Update to 6.9.3-8:
  * Respect gravity when rendering text (e.g. convert -gravity center
    my.txt).
  * Return empty string for %%d property and no directory.
  * Return filename for the %%i property.
  * Fixed lost pixels in frequency space.
  * etc. see ChangeLog
* Tue Jan  5 2016 pgajdos@suse.com
- Update to 6.9.3-0:
  * Don't break on euro-style numbers.
  * 16-bit pnm images have a max value of 65535.
  * Fixed compile error when POSIX threads are not defined.
  * Fixed memory leak when reading incorrect PSD files.
  * Enhance PDF to properly handle unicode titles.
  * Fix memory leak in icon coder.
* Thu Dec 17 2015 pgajdos@suse.com
- Update to 6.9.2-8:
  * Gray artifacts in large gif when using -layers optimize.
  * The DICOM reader now handles the rescale intercept and slope.
  * Added 'bmp3:alpha' option for including the alpha channel when
    writing an image in the BMP3 format.
  * PixelColor off by one on i386.
  * Added local contrast enhancement.
  * Fixed bug in SetPixelCacheExtent that made images all black.
  * Added 6dot variant for unicode and iso braille formats.
  * Fixed alpha blending issue with semi-transparent pixels in the
    merged image of PSD files. This can be disabled by setting the
    option 'psd:alpha-unblend' to 'off'.
  * Fixed issue in jpeg:extent that prevented it from working.
  * Fixed memory leak when reading Photoshop layers in a TIFF file.
  * Support gradient:bounding-box, gradient:vector, gradient:center,
    and gradient:radius to shape the gradient rendering.
  * Recognize label:@- as stdin.
  * Make commas optional for coordinates.
* Mon Oct 12 2015 pgajdos@suse.com
- Update to 6.9.2-4:
  * Fixed accessing subimage in a TIFF photoshop layer.
  * Fixed out of bounds error in -splice.
  * Created Manhattan Interpolate method for -sparse-color.
  * Don't round up for JPEG image resolution.
  * Read the whole image @ image.jp2[0] or an individual
    tile @ image.jp2[1], image.jp2[2].
  * The -caption option no longer fails for filenames with @ prefix.
  * Honor $XDG_CONFIG_HOME and $XDG_CACHE_HOME.
  * Added extra checks to avoid out of bounds error when parsing the 8bim
    profile
  * Fixed size of memory allocation in RLE coder to avoid segfault.
  * The -colorspace gray option no long leaves a ghostly shadow.
  * Preservin.
  * Limit -fx recursive to avoid stack overflow.
  * Don't set image colorspace to gray for -alpha copy option.
  * GetImageType() no longer has side-effects to match behavior of IMv7.
  * Swap pixels for -spread command-line option.
  * Fix ModulusAdd & ModulusSubstract for HDRI compositing.
  * Added "-set colorspace:auto-grayscale false" that will prevent automatic
    conversion to grayscale inside coders that support grayscale.
  * Fixed -list weight and the options for -weight.
  * Added fontFamily, fontStyle, fontWeight and textUnderColor to the Image
    class of Magick++.
  * Fixed reading Photoshop layers of LSB TIFF files.
* Mon Jul 27 2015 sbrabec@suse.com
- Update to 6.9.1-10:
  * New version 6.9.1-10, SVN revision 19269.
  * coders/magick.c: added "-define h:format=FMT" and
    "-define magick:format=FMT" options. FMT can be any output format
    supported by ImageMagick except "H" or "MAGICK". If this define is
    omitted, the encoder uses GIF by default for pseudoclass images and
    PNM for directclass images, as previously.  Made "MAGICK" (read-write)
    and "H" (write-only) visible in the format list.
  * Removed incorrect EOF check in the DDS reader (reference
    http://www.imagemagick.org/discourse-server/viewtopic.php?f=3&t=28065).
  * Fixed undefined behaviors (reference
    http://www.imagemagick.org/discourse-server/viewtopic.php?f=3&t=28067).
  * Return exception message for unknown image properties.
  * Color shift removed when reading transparent gray images (reference
    http://www.imagemagick.org/discourse-server/viewtopic.php?f=3&t=28081)
* Thu Jul 23 2015 jweberhofer@weberhofer.at
- Removed duplicates
- Only libMagickCore and ImageMagick-doc contains the LICENSE file. Other
  libraries do not longer contain it, as they always require libMagickCore
  to be instaleld.
- Moved documentation to the ImageMagick-doc package.
- Removed executable bits from perl documentation-examples
- Added configurations for:
  * graphviz
  * lcms2 (Little CMS 2 color management)
  * jbig
  * openjp2 (JPEG 2000)
  * openexr
  * webp
- update to 6.9.1-9
  * Fixed issue with radial gradient in MVG (reference
    http://www.imagemagick.org/discourse-server/viewtopic.php?f=3&t=27995).
- update to 6.9.1-8
  * New version 6.9.1-8, SVN revision 19167.
  * Correct install location of the Magick++ headers (reference
    https://github.com/ImageMagick/ImageMagick/pull/17/commits).
  * Different gif cropping behavior between versions (reference
    http://www.imagemagick.org/discourse-server/viewtopic.php?f=3&t=28013).
  * Cannot read properly simple psd file (reference
    http://www.imagemagick.org/discourse-server/viewtopic.php?f=3&t=28002).
- update to 6.9.1-7
  * Fixed and escaped output of the json coder. (reference
    http://www.imagemagick.org/discourse-server/viewtopic.php?f=3&p=27894).
  * Support BPG image format (respects -quality option).
  * A bordered transparent image now remains transparent (reference
    http://www.imagemagick.org/discourse-server/viewtopic.php?f=5&t=27937).
  * The -update option behavior restored (reference
    http://www.imagemagick.org/discourse-server/viewtopic.php?f=1&t=27939).
* Wed Jul  1 2015 jweberhofer@weberhofer.at
- update to 6.9.1-6
  * Cache cloning on disk optimized with sendfile() (if available).
  * Add an additional check for end-of-file for the RLE coder (reference
    http://www.imagemagick.org/discourse-server/viewforum.php?f=3&t=27870).
  * Respect resource limits in AVS coder.
  * Reverted change to 6.9.1-3 that skipped palette-building.
- update to 6.9.1 returns proper XML (reference
    http://www.imagemagick.org/discourse-server/viewtopic.php?f=3&t=27751).
  * Support writing EXR files with different color types (reference
    http://www.imagemagick.org/discourse-server/viewtopic.php?f=2&t=27759).
  * Prefer PKG_CHECK_MODULES() when searching for delegate libraries.
  * Throw exception if frame option bevel exceeds to the image width / height.
  * Resolve undefined behaviors (reference
    http://www.imagemagick.org/discourse-server/viewtopic.php?f=3&t=27811).
- update to 6.9.1-4
  * Support 'restrict' keyword under Windows.
  * Added support for reading a user supplied layer mask in PSD files.
  * Added support for reading photoshop layers in TIFF files.
- update to 6.9.1-3
  * Fixed transparency issue with 16-bit tga files (reference
    http://www.imagemagick.org/discourse-server/viewtopic.php?f=3&t=27469).
  * Fixed writing label and comment in tiff images (reference
    http://www.imagemagick.org/discourse-server/viewtopic.php?f=3&t=25516).
  * Jpeg images no longer have pixels per inch as a default value for density
    units when the density is not set (reference
    http://www.imagemagick.org/discourse-server/viewtopic.php?f=3&t=27589).
  * Added support for setting the font color with -fill to the pango coder.
  * Fixed bug with "-define png:format=x" in png.c, introduced in version
    6.8.9-0, that caused the define to be ignored.
  * Replaced some dead code in ReadJNGImage with an assert().
  * Avoid palette-building when writing a grayscale PNG (reference
    http://www.imagemagick.org/discourse-server/viewtopic.php?f=3&t=27580).
  * Support -define compose:clamp=false option (reference
    http://www.imagemagick.org/discourse-server/viewtopic.php?f=3&t=26946).
  * Don't extend any user supplied image buffer in SeekBlob() (bug report
    from a.chernij@corp...).
  * Improved reproducible builds (reference
    https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=783933).
  * Draw a rectangle of width & height of 1 (reference
    http://www.imagemagick.org/discourse-server/viewtopic.php?f=3&t=24874).
- update to 6.9.1-2
  * Avoid using a NULL alpha_image or color_image in the JNG decoder.
  * Fix JPEG-2000 transparency on write (reference
    http://www.imagemagick.org/discourse-server/viewtopic.php?f=3&t=27304).
  * Identify now identifies PSD (reference
    http://www.imagemagick.org/discourse-server/viewtopic.php?f=3&t=26948).
  * Speed up writing to TGA (reference
    http://www.imagemagick.org/discourse-server/viewtopic.php?f=3&t=27369).
  * Reduce draw epsilon to increase mathematical stability.
  * Fixed UTF8 issue when determining the current working directory
    on Windows (reference
    http://www.imagemagick.org/discourse-server/viewtopic.php?f=3&t=27295).
* Mon May 11 2015 pgajdos@suse.com
- update to 6.9.1-1
  * Skip empty frames when comparing layers.
  * Grayscale DPX image files are no longer skewed.
  * Fix integer overflow when scaling a 1-bit sample to Q64.
  * Account for differences in image size when comparing two images.
  * Set an upper ceiling compression with -quality and jpeg:extent.
* Mon Mar  2 2015 pgajdos@suse.com
- update to 6.9.0-9
  * Writing histograms / mpeg working again.
  * The -linear-stretch option worked for Q16 but not Q32.
* Thu Feb 26 2015 pgajdos@suse.com
- update to 6.9.0-7
  * Line strokes appeared too thin.
  * Keep text in caption area.
  * A transient bug for the write MSL element.
  * Fixed infinite loop in HDR reader.
  * In the PNG codec, check status wherever a function returns it.
  * Check lengths of  sanity checks.
  etc. see ChangeLog
* Fri Jan 16 2015 pgajdos@suse.com
- update to 6.9.0-3
  * Don't read beyond the end of a tEXt keyword when checking for
    Raw profile.
  * Fixed enabling alpha in 32-bit BMP files.
  * Added support for writing 16-bit TGA files.
  * Improved performance of dds.
  * Fix ImageMagick crashes while read EXIF from TIFF.
  * Don't handle a "previous" image in the PNG or JNG decoder.
  * Don't override gamma with 1.0 when reading a grayscale PNG
    image.
  * Update progress monitor for every PNG row instead of every pass.
  * Reject input PNG with dimensions larger than specified with
  - limit width and -limit height.
  * etc., see ChangeLog
* Mon Dec 15 2014 pgajdos@suse.com
- do not use -march/-mtune [bnc#904545]
* Tue Nov 18 2014 pgajdos@suse.com
- update to 6.9.0-0
  * Check for zero-sized rendered SVG image.
  * EXIF directory offsets must be greater than 0.
  * Accept morphology kernels from files.
  * Don't optimize JPEG compression by default.
  * etc. see ChangeLog
* Thu Oct 30 2014 pgajdos@suse.com
- update to 6.8.9-8
  * Added sixel coder.
  * Fixed buffer overflow in PCX and DCM coder.
  * Added support for reading/writing the tIME chunk in the PNG coder.
  * Added eps:fit-page option to the PS coder to set -dEPSFitPage.
  * Support xyY colorspace.
  * Reduce noise while preserving edges with the -kuwahara option.
  * Off-by-one count when parsing an 8BIM profile.
  * OpenCL no longer benchmarks are run on every initialization.
  * Don't clone a 0x0 image.
* Mon Sep 22 2014 pgajdos@suse.com
- update to 6.8.9-8
  * JPEG library version >= 80 is thread safe
  * Added support for some legacy dds formats
* Wed Sep 10 2014 pgajdos@suse.com
- updated to 6.8.9-7
  * Fix off by one buglet when extracting profiles 8BIM.
  * Fixed bug when reading 1 bit PSD.
  * Fixed fill-rule in SVG clip path.
  * Added support for R5G6B5, RGB5A1 and RGBA4 dds files.
  * Write LAB pixels as percentages in the TXT image format.
  * Throw exception when image morphology differs when comparing.
  * Remove mogrify backup file.
  * Read WEBP images from STDIN.
* Mon Sep  8 2014 coolo@suse.com
- fix baselibs.conf requires for ImageMagick++
* Fri Aug 29 2014 coolo@suse.com
- fix license for spdx 1.2
* Fri Jul 18 2014 pgajdos@suse.com
- build against librsvg again
* Fri Jul 18 2014 pgajdos@suse.com
- updated to 6.8.9-5
  * Use -define profile:skip=icc, for example, to skip color profiles on read.
  * Do not let libpng16 check ICC/sRGB profiles in non-debug runs; we do it
    ourselves anyway. Avoids emitting "known incorrect profile" warnings.
    For strict profile checking and warning, use "-debug coder".
  * Disabled OpenCL acceleration when image has a 'mask' or 'clip-mask'.
* Wed Jun 25 2014 pgajdos@suse.com
- updated to 6.8.9-4
  * Support RMS argument for -evaluate-sequence and -statistic options.
  * Pipe image to display program no longer reports an exception.
  * Check that profile is non-NULL in coders/tiff.c.
* Tue Jun 10 2014 opensuse@dstoecker.de
- update to 6.8.9-3
  * Quiet warning about unused variable "skip_to_iend" in coders/png.c.
  * Fixed creation of SVG from 8bim clip path.
  * The -version option returns 0 status
  * The inline coder can now read from standard input
  * Add '=' character to the santize whitelist.
* Sat May 31 2014 opensuse@dstoecker.de
- update to 6.8.9-2
  * Fixed some bugs in the PNG codec discovered by coverity analysis.
  * The -fx equality operator returns a proper boolean result now.
  * Permit spaces in the gradient color specification.
  * Fix IdentifyImagrsed.
  * Remove Makefile race condition where two targets attempt to install
    magick-baseconfig.h
  * Fix memory leak in BlobToStringInfo().
  * In certain cases, -adaptive-sharpen failed to sharpen
  * Bump major Magick++ library version.
  * Added support for writing RLE compressed TGA files.
  * Improved performance of parsing the xmp profile.
  * Fixed detecting transparency in PSD files.
* Sat May 31 2014 coolo@suse.com
- remove autotrace dependency again - it's not compiled in and
  autotrace's last release is 10 years old and we don't want to
  promote it, better drop it
* Tue May 27 2014 opensuse@dstoecker.de
- update to 6.8.9
  * Fixed bug with the PNG00 subformat when the original format was PNG32.
  * The "-strip" option now only removes profiles and comments from PNG
    output.  Previously the background, density, and other metadata were
    also discarded.
  * Support new -hough-lines option.
  * Support new -mean-shift option.
  * identify -units without argument no longer faults (reference
    http://www.imagemagick.org/discourse-server/viewtopic.php?f=3&t=25542).
  * Require OpenJP2 version 2.1.0 (opj_stream_set_user_data() method signature
    change between 2.0.0 and 2.1.0).
* Sat May 24 2014 mailaender@opensuse.org
- Fixed the SLE build
- Added missing dependencies:
  * autotrace
  * dejavu-fonts
  * fftw3
  * ghostscript
  * libjbig
  * liblqr
  * mupdf
  * p7zip
  * xdg-utils
  * zip
* Thu Apr 24 2014 dmueller@suse.com
- remove dependency on gpg-offline (blocks rebuilds and
  tarball integrity is checked by source-validator anyway)
* Mon Mar  3 2014 pgajdos@suse.com
- directories in libMagickCore depends on %%{clibver} and
  %%{quantum_depth} [bnc#866442]
* Thu Feb 27 2014 pgajdos@suse.com
- fix baselibs
* Wed Feb 26 2014 opensuse@dstoecker.de
- update to 6.8.8-7
- remove disable_mat_test.patch (fixed upstream)
* Tue Feb 18 2014 pgajdos@suse.com
- updated to 6.8.8-6:
  * build against openjpeg2
  * identify -define identify:locate=maximum locates the position of the
    maximum value
  * Fix case where an image moment might have a mass of 0 or a Hu moment might
    be 0.
  * Enhance the TXT coder to read RGB percent values, e.g. 10.008%%.
  * etc. see ChangeLog
* Thu Feb 13 2014 pgajdos@suse.com
- modified patches [bnc#843673]:
  * disable_mat_test.patch -- rather than disable the test,
    use upstream solution (increase threshold for mean error)
  - - use this patch also for s390, s390x
* Wed Jan  8 2014 pgajdos@suse.com
- updated to 6.8.8-1:
  * Support points argument for draw MSL element.
  * The -page option now correctly sets the image page offset.
  * The -evaluate-sequence sum returns a proper alpha channel now.
  * etc. see ChangeLog
* Wed Jan  8 2014 coolo@suse.com
- really disable parallel build, don't just have a comment about it
* Wed Dec 18 2013 pgajdos@suse.com
- updated to 6.8.7-10:
  * fix crash when using -resize with GPU acceleration
* Mon Dec  9 2013 pgajdos@suse.com
- updated to 6.8.7-9:
  * fixed bug in coders/png.c that caused -define png:color-type=0
    to fail
  * fixed bug in automatic selection of OpenCL device
  * simplified interface to initialize the OpenCL environment
  * Fix possible memory corruption when writing PSD image
  * etc. see ChangeLog
* Mon Oct  7 2013 tom.mbrt@googlemail.com
- added openexr-devel as build requirement to enable openexr support
* Thu Oct  3 2013 pgajdos@suse.com
- use fdupes -s [bnc#841472]
* Wed Oct  2 2013 dvaleev@suse.com
- disable mat tests for powerpc bnc#843673 (disable_mat_test.patch)
* Wed Oct  2 2013 pgajdos@suse.com
- docuselibs.conf for previous change
* Mon Sep 30 2013 pgajdos@suse.com
- setting quantum depth to 16 [bnc#840825]
* Mon Sep 30 2013 pgajdos@suse.com
- fix build (find doesn't support -perm +mode)
* Thu Sep  5 2013 pgajdos@suse.com
- updated to 6.8.6-9
  * Fixed infinite loop with jpeg:extent.
  * Fixed performance issue when converting jpeg to png.
  * Added "-define bmp:format=bmp2|bmp3|bmp4" option.
  * etc. see ChangeLog
* Tue Aug  6 2013 pgajdos@suse.com
- updated to 6.8.6-7
  * Fix memory leak in CloneImageArtifacts and CloneImageProfiles.
  * JPEG ICC color profile requires null after ICC tag
  * etc.
- employ gpg-offline
* Mon Jun 17 2013 pgajdos@suse.com
- use AllCompliance instead of X11Compliance to cover also 'None'
  [bnc#825151]
  * adjusted no-XPMCompliance.patch
* Mon Jun  3 2013 pgajdos@suse.com
- mark no-XPMCompliance.patch as suse specific
  http://www.imagemagick.org/discourse-server/viewtopic.php?f=3&t=23462
* Thu May 23 2013 pgajdos@suse.com
- workaround: fix reading xpm which uses symbolic color names which
  are said to be not XPMCompliant
  * http://www.imagemagick.org/discourse-server/viewtopic.php?f=3&t=23462
* Tue May 21 2013 pgajdos@suse.com
- update to 6.8.5-7:
  * fixes reading XPM
* Mon May 13 2013 pgajdos@suse.com
- update to 6.8.5-6:
  * fixed 'Sometimes an sRGB image is masquerading as grayscale'
  * fixed 'The stream utility no longer faults when exporting float pixels'
  * Labels no longer overflow
  * Change the sample JPEG quantization table xml to something that works
    really well with 2x2 Chroma subsampling around quality 75.
  * Eliminate whitespace from image properties that hold PNG chunk data.
  * etc. see ChangeLog
- remove fix-wand.pc.patch, the issue is fixed upstream
- remove test-signatures.patch, the issue is fixed upstream
* Sun Apr  7 2013 coolo@suse.com
- add ImageMagick-6.8.4.0-fix-wand.pc.patch to fix build of e.g.
  emacs and xine-lib, who rely on pkg-config --libs Wand returning
  actually MagickWand and not MagickCore (looks like a copy&paste
  error of upstream)
* Fri Mar 29 2013 pgajdos@suse.com
- update to 6.8.4-0:
  * dropped ImageMagick-6.8.2.4-revert-r9087-montage-signatures.patch,
    issue is almost fixed -> new test-signatures.patch,
    see followups in
    http://www.imagemagick.org/discourse-server/viewtopic.php?f=2&t=22479
  * created rpath.patch
  * created dont-build-in-install.patch
- upstream changes
  * Do not write zero-length TIFF tags
  * Do not split words for caption
  * The -blur, -guassian-blur, and -sharpen are now convenience methods
    for -morphology convolve.
  * etc. see ChangeLog
* Sun Mar 24 2013 coolo@suse.com
- fix baselibs.conf
* Wed Feb 20 2013 pgajdos@suse.com
- use versioned /etc/ImageMagick* to allow parallel installation
  of libMagickCore
* Wed Feb  6 2013 vjt@openssl.it
- name library packages after the new -QN library names (thanks dstoecker)
- depend on newer libtiff
* Wed Feb  6 2013 vjt@openssl.it
- fix missed variable expansion
* Wed Feb  6 2013 vjt@openssl.it
- use a quantum depth of 8 for our package, as we do not require
  that amount of precision, and we prefer faster conversions with
  less heap usage.
* Wed Feb  6 2013 vjt@openssl.it
- updated to 6.8.2.4
  * Update libver to 7
  * Dropped upstreamed ImageMagick-uninitialized-memory.patch
  * Added ImageMagick-6.8.2.4-revert-r9087-montage-signatures.patch
    Related to GhostScript. Discussion:
    http://www.imagemagick.org/discourse-server/viewtopic.php?f=2&t=22479&p=95023
  * Add support for -QN library and .pc names, that express the
    pixel quantum deptxplicit spec variable for it
  * BuildRequire autoconf >= 2.69
* Tue Jan 15 2013 pgajdos@suse.com
- fix wrong mean-error output:
  http://www.imagemagick.org/discourse-server/viewtopic.php?f=3&t=22586
  * dropped disable-matlab-test.patch
  * added ImageMagick-uninitialized-memory.patch
* Thu Jan 10 2013 meissner@suse.com
- do not disable checking altogether.
- disable-matlab-test.patch: disable the 1 MATLAB testcase that fails.
* Thu Jan 10 2013 mrdocs@opensuse.org
- disable check for the moment, it breaks on Factory and 12.1, but
  12.2
* Tue Jan  8 2013 schuetzm@gmx.net
- enable support for Pango markup
  * this allows rendering formatted text with the pango:"..." syntax
    see http://www.imagemagick.org/Usage/text/#pango for details
  * to actually use this, libpango needs to be installed
* Tue Aug  7 2012 pgajdos@suse.com
- updated to 6.7.8.8:
  * Added 2d named convolution kernel Binomial (for Fred Wienhaus)
  * Clean up sigmoidal-contrast.
  * Use ConcatenateString() for multi-block GIF comments.
  * Caption no longer chops off text (reference
    http://www.imagemagick.org/discourse-server/viewtopic.php?f=3&t=21558).
  * Support LUV colorspace.
  * Support HCL colorspace.
  * Don't transform the composite image colorspace, set it instead.
  * Interpret -border 5%% as 5%% of width and 5%% of height (reference
    http://www.imagemagick.org/discourse-server/viewtopic.php?f=3&t=21537).
  * Don't normalize zero-sum kernels (reference
    http://www.imagemagick.org/discourse-server/viewtopic.php?f=3&t=21584).
  * Transform grayscale to linear RGB if fill color is non-gray (reference
    http://www.imagemagick.org/discourse-server/viewtopic.php?f=3&t=21586).
  etc. see ChangeLog
* Wed May 16 2012 pgajdos@suse.com
- updated to 6.7.6.9:
  * Don't write an invalid PNG sRGB chunk when rendering intent is undefined.
  * EXR images are in the linear RGB colorspace with a gamma of 1.0.
  * Correct annotation offset for right-to-left labels.
  * The -level 100x0%% now produces the equivalent of -negate.
  * etc., see ChangeLog
* Tue Mar 27 2012 pgajdos@suse.com
- cleanup the package
- updated to 6.7.6.1: fixes
  * CVE-2012-0247 [bnc#746880]
  * CVE-2012-0248 [bnc#746880]
  * CVE-2012-1185 [bnc#752879]
  * CVE-2012-1186 [bnc#752879]
* Fri Mar  9 2012 giecrilj@stegny.2a.pl
- moved the libtool archives to the main package
- separated the bulk documentation
- added a regression %%check for the locale comma crash
* Tue Feb 14 2012 cfarrell@suse.com
- license update: SUSE-ImageMagick
  Use SUSE- proprietary prefix until SPDX upstream accepts ImageMagick as
  license (e.g. like Fedora)
* Thu Jan 19 2012 pgajdos@suse.com
- ImageMagick-devel requires libbz2-devel [bnc#741947]
* Thu Jan 19 2012 pgajdos@suse.com
- update to 6.7.4.7:
  * Fixed -black-threshold and -white-threshold so they work properly with
    the -channels option
  * Promote image depths 9-15 to 16 to avoid crashing in the PNG
    encoder
  * Fix problems with JNG encoder "quality"
  * Fix memory leak in JP2 coder
  * Use maximum bounds when rendering PDF
  * etc. see ChangeLog
* Tue Jan 17 2012 crrodriguez@opensuse.org
- Add explicit libbz2-devel BuildRequires
- Support LZMA
- Use libcms2 now.
- Cleanup huge dependency bloat in -devel package, this
  will likely cause build fails on dependant packages
  the solution is to fix your BuildRequires.
* Mon Oct 31 2011 pgajdos@suse.com
- update to 6.7.3.3:
  * removed upstreamed scene.patch
* Tue Oct 18 2011 pgajdos@suse.com
- build against librsvg as recommended upstream [bnc#724222]
* Sat Oct 15 2011 coolo@suse.com
- ads@suse.com
- fixed [bnc#717871] -- imagemagick display wrong order
  * scene.patch
* Tue Sep 20 2011 pgajdos@suse.com
- update to 6.7.2.7:
  * Fix memory leak in text annotation.
  * The "-strip" option was excluding the PNG tRNS chunk.
  * Caption now wraps properly for Chinese text.
  * The PNG encoder would sometimes fail to respect the -define
    PNG:color-type option when the incoming image was PseudoClass.
  * Properly handled continued JPEG embedded profiles.
  * Revert -colorspace sRGB option patch.
  * Revert -type PaletteMatte option patch.
  * etc. see ChangeLog.
- obsoletes reason-error-message.patch
* Sat Sep 17 2011 jengelh@medozas.de
- Remove redundant tags/sections from specfile
* Fri Sep 16 2011 jengelh@medozas.de
- Fix baselibs: add missing requires to ImageMagick-devel
- Remove redundant tags/sections
* Wed Sep  7 2011 pgajdos@suse.com
- fixed wrong error messages [bnc#673303]
* Fri Jul 29 2011 pgajdos@novell.com
- update to 6.7.1.0:
  * Defend against corrupt PSD resource blocks.
  * Properly allocate points when render text with large font size.
  * Added support for Z_RLE strategy in the png compressor, using
  - quality 98 or 99.
  * Handle "-quality 97" properly in the png encoder, i.e., use intrapixel
    filtering when writing a MNG file and no filtering when writing a PNG file.
  * Added "-define PNG:compression-level|strategy|filter=value" options to
    the PNG encoder.  If these options are used, they take precedence over
    the -quality option.
  * Use zlib default compression strategy instead of Z_RLE and Z_FIXED
    strategies when linking with zlib versions (prior to 1.2.0 and 1.2.2.2,
    respectively) that don't support them.
- switch on WEBP support -- require libwebp-devel to build
* Mon Jun 20 2011 pgajdos@novell.com
- updated to 6.7.0.8:
  * added Initial implementation of Cylinder to/from Plane 3D Distorts
    Includes deritive (scaled lookup), and anti-alised horizon (validity)
    Currently can NOT handle extractions from full 360 cylinder panoramas.
  * Fix transient error for composite over operator.
  * Fix one-off bug in option parser.
  * etc., see ChangeLog
- adjusted inc-struct.diff
* Fri May 27 2011 coolo@novell.com
- fix requires of -devel package
* Thu May 26 2011 coolo@novell.com
- remove the -fuse-linker-plugin option, it's default in gcc 4.6
  and only confuses scripts
* Tue May 24 2011 dimstar@opensuse.org
- Require ImageMagick from -devel subpackage: Packages that depend
  on the -devel package very likely use the tools too.
* Tue May 17 2011 pgajdos@suse.cz
- updated to 6.6.9.9:
  * The -scale option nows considers the alpha channel when scaling.
  * Don't use comma as a separator for stroked tex.
  * Fix transient bug for HSL to RGB and back.
  * Fixed PNG8 reduction to work with an image that reduces to 256 colors
    plus transparency, by merging the two darkest red colors.
  * etc., see ChangeLog
* Sun May  8 2011 giecrilj@stegny.2a.pl
- created ImageMagick-devel-32bit for cross-compiling
* Thu Apr 21 2011 giecrilj@stegny.2a.pl
- updated to 6.6.9.5: fixes [Bug 682238]
  * macroized and cleaned up scripts
  * added conditions for optional components
  * updated file lists for upstream
  * cleaned up the include tree in devel (patch)
* Mon Apr 11 2011 pgajdos@suse.cz
- updated to 6.6.8.9: fixes [bnc#682238]
  * config files moved to /etc/ImageMagick*
  * see ChangeLog for more details
* Wed Feb 23 2011 pgajdos@suse.cz
- updated to 6.6.7.9: fixes [bnc#673789]
  * removed survive-exif.patch
* Mon Feb 21 2011 jw@novell.com
- added patch for crash reading png w [bnc#671047]
* Mon Dec  6 2010 coolo@novell.com
- fix build for factory
* Mon Nov 15 2010 pgajdos@suse.cz
- updated to 6.6.5-8: don't read config files from $CWD
  [bnc#653572]
* Thu Nov  4 2010 pgajdos@suse.cz
- updated to 6.6.5-5:
  * Revised PNG palette optimization
  * Added some debug logging in coders/png.c.
  * More precise blur values for Lanczos2Sharp and LanczosSharp.
  * Added location of first Mitchell crossing (=8/7) to the filters data
    structure.
  * Added Lanczos2D* filters now named Lanczos2*
  * Reorganization of AcquireFilter() to make it work better
  * Clearer EWA filters (LanczosSharp etc) comments.
  * Added LanczosSharp  (3-lobe Lanczos with sharpening)
  * Filter sharpening factors are also always applied regardless of usage.
  * CubicBC filter formulas simplified by constant folding. In
    particular, P1 coefficient (always zero) removed from coeff.
  * Revert the Robidoux filter to a Keys cubic with C=(108 sqrt 2-29)/398
    (as already specified in the documentation).
  * Ignore PS bounding box offsets if -page is set.
  * Add support for -evaluate exp.
* Fri Oct 15 2010 pgajdos@novell.com
- updated to 6.6.5-0:
  * Added "filter:sigma" expert setting defining the 'sigma' for the Gaussian
    filter only.  This is similar in action to 'blur' but only for Gaussians,
    and does not modify the filters support, allowing you to set a very small
    sigma, without the function 'missing' all pixels.
  * Patch for  DrawableRotation() and DrawableTranslation()
  * The webp format requires the webpconv delegate program (experimental).
  * Replaced "Robidoux" with Cubic 'Keys' filter that is near equivelent to
    the previous sharped "Lanczos2D" filter. (C=0.31089212245300069)
    This also is very similer to a Mitchell filter but specifically designed
    for EWA use and is the new default filter for Distorting Images.
  * Added new filter 'Lanczos2D' a 2-lobe Lanczos as defined by
    Andreas Gustafsson in his thesis  "Interactive Image Warping" (page 24)
    http://www.gson.org/thesis/warping-thesis.pdf
  * Added filter "Robidoux" which is a slightly sharpened version of the
    "Lanczos2D" filter (blur=0.958033808) specifically designed to be less
    'blurry' for horizontal and vertical lines in no-op distortions.
  * Add support for "pattern:vertical2" and "pattern:horizontal2".
  * Add support for "pattern:vertical3" and "pattern:horizontal3".
  * Properly handle PSD layers with negative offsets.
  * Added sqrt(2) bluring default for Gaussian Filter if used as
    a Cylindrical EWA filter.  This resulted removing the last aliasing
    issue that was present in tests for Gaussian EWA resampling. Of course
    it is still a very blury filter for default use in EWA.
  * Adjusted Variable Mapping Blur Composition so user arguments actual
    relate properly to the sigma of the blur for a maximum mapping value.
  * Fix horizon anti-alising for output-scaled perspective distortions.
  * 'Bessel' filter is now offically and more accuritally named 'Jinc'
    however 'Bessel' while not visible as a filter option can still be used
    as an internal alias for 'Jinc'.
  * Fix memory assertion with --enable-embeddable (reference
    http://www.imagemagick.org/discourse-server/viewtopic.php?f=3&t=17201).
  * Don't permit access to pixels when pinging an image (reference
    http://www.imagemagick.org/discourse-server/viewtopic.php?f=3&t=17194).
* Tue Oct  5 2010 pgajdos@novell.com
- updated to 6.6.4-8:
  * Automatically set the quantum depth to 16 for HDRI.
  * IPTC profile not always wrapped properlyf SincPolynomial to SincFast for easier user understanding.
    Ditto for LanczosChebyshev to LanzcosFast.
  * Switch default resize filters to using the faster SincPolynomial
    filter by default internally.  However 'Sinc' will still use the
    Trigonometric function, and can be used to assign the trig version
    of Sinc() to filters using the filter expert options.
  * The default filter for 'distort' was found to be a very blurry inaccurate
    filter function.  It was removed and replaced with a correct Gaussian
    filter (as used by resize)
  * Added a switch so that "-interpolate filter" will force the use of
    a cylindrical filter for ALL pixels in distorted images.  That is you can
    use that switch to use a cylindrical filter even for images that are
    being enlarged by the distortion.  However EWA is still currently using
    a fixed 2.0 sampling radius.  This switch complements the use of "-filter
    point" which turns off EWA filters in favor of interpolation for all
    pixels in a distorted image.  BOTH switches should not be used together.
  * A bug in the support radius of the EWA resampling function was found,
    now that correctly defined resize filters are being used. Suddenly Normal
    Gaussian distortions are not so blurry, and tests with distortions of
    the 'Rings' image show extremely good and clear results, with only minimal
    blurring.  The filter 'blur' expert option can be used to adjust this
    further.
  * Don't negate the geometry offset for the -extent option.
  * The RGBO format is now listed as a supported format.
  * Added the Nicolas Robidoux and Chantal Racette  Lanczos resize filter
    function as "LanczosChebyshev" as faster alternative to Lanczos.
  * Re-code Nicolas Robidoux and Chantal Racette Polynomial Approximation of
    the Sinc Trigonometric resize filter, as a proper filter to allow
    direct comparision and speed testing of the filter.
  * Expanded the "-set option:filter:verbose 1" output, so as to also include
    the actual functions and other values that were used to create the filter.
* Tue Sep  7 2010 pgajdos@suse.cz
- updated to 6.6.4-0:
  * Repair a few incorrect LocaleNCompare() calls (ttf.c, ps.c).
  * Path no longer closed if join style is round (reference
    http://www.imagemagick.org/discourse-server/viewtopic.php?f=3&t=16943).
  * Add case for BGRQuantum to GetQuantumExtent().
  * Support no compression on PCX write.
  * Fixed bug in the raw BGRA coders (reference
    http://www.imagemagick.org/discourse-server/viewtopic.php?f=3&t=16880).
  * Fix off-by-one error in the PSD coders.
  * Nicolas Robidoux with the assistance of Chantal Racette contribute an
    approximation of the sinc function over the interval [-3,3].
  * Eliminate a small memory leak in LevelizeImageChannel() (reference
    http://www.imagemagick.org/discourse-server/viewtopic.php?f=3&t=16951).
  * Recognize -fx logtwo (reference
    http://www.imagemagick.org/discourse-server/viewtopic.php?f=3&t=16958).
* Tue Aug 24 2010 pgajdos@suse.cz
- updated to 6.6.3-9:
  * Eliminate useless message about assuming zero delay when writing
    a single-frame MNG, and changed it from Error to Warning when
    writing a multiple-frame MNG.
  * Only use the first alpha channel in PSD image.
  * Only use XPM complying colors for XPM images (e.g. green is rgb(0,255,0)).
  * Eliminate bogus "invalid colormap index" when pinging ICO images.
  * Support -set density / units.
  * Properly map PNG intent to image->rendering_intent
  * The orient option sometimes improperly set "undefined"   * Only list orientation options for the -list orientation option (reference
    http://www.imagemagick.org/discourse-server/viewtopic.php?f=3&t=16801).
  * Return proper standard deviation for combined channels (reference
    http://www.imagemagick.org/discourse-server/viewtopic.php?f=3&t=16786).
  * Handle transparency properly for the PSD image format.
  * Emit a warning if the PNG encoder can't satisfy the color type and
    bit depth requested with a "-define" directive.
  * The -fx 2e+6/1e+5 argument no longer returns the wrong results (reference
    http://www.imagemagick.org/discourse-server/viewtopic.php?f=3&t=16833).
  * Add -subimage-search option to the compare utility.
  * Throw exception if image size differs for the compare program but the
  - subimage-search option is not specified.
* Mon Aug  2 2010 coolo@novell.com
- update baselibs.conf
* Thu Jul 29 2010 pgajdos@suse.cz
- updated to 6.6.3-1:
  * obsoletes units.patch
  * obsoletes grayscale-tiff-jpeg.patch
* Tue Jun 22 2010 pgajdos@suse.cz
- fixed jpeg compression of grayscale tif format [bnc#615223]
* Mon May 10 2010 aj@suse.de
- Do not compile in build time but use mtime of changes file instead.
  This allows build-compare to identify that no changes have happened.
* Mon Apr 26 2010 pgajdos@suse.cz
- fixed units in the output [bnc#598714]
  * units.patch
* Wed Apr  7 2010 ro@suse.de
- update baselibs.conf
* Tue Apr  6 2010 pgajdos@suse.cz
- updated to version 6.6.1-0:
  * Fixed bug in equal-size tile cropping, when image has a page offset.
  * The -recolor 4x4 matrix is now interpretted properly (previously it
    summed rather attenuating the alpha channel).
  * Support writing 1-bit PSD images.
  * Support LCMS 2.0.
  * Improved WMF support under Windows.
  * The new coders/png.c was failing to read a 1-bit paletted image properly.
  * Finished eliminating the deprecated direct references to members of
    the png_info structure. ImageMagick can now be built with libpng-1.5.
  * Respect the -density option when rendering a Postscript or PDF image.
  * Distort barrel no longer complains when 3 arguments are given (reference
    http://www.imagemagick.org/discourse-server/viewtopic.php?f=3&t=15883).
  * Support -direction left-to-right option for rendering text
  * coders/png.c: Eliminated support of libpng versions older than 1.0.12.
  * Relocated the new, misplaced png_get_rowbytes() call.
  * Updated setjmp/longjmp/jmpbuf usage to work with libpng-1.5.
  * Add support for monochrome PSD images.
  * VignetteImage() no longer crashes when x and y arguments are both greater
    than half the width (x) and height (y) of the image.
  * Eliminated some of the deprecated direct references to members of
    the png_info structure.  This must be finished before we can build
    with libpng-1.5.
  * The animate program no longer loops twice when -loop 1 is specified.
  * The caption format would sometimes hang when the text was not UTF-8.
  * Don't gamma correct log to linear color conversion unless the -gamma is
    specified (reference
    http://www.imagemagick.org/discourse-server/viewtopic.php?f=1&t=15799).
  * Detect CMYKProcessColor AI tag.
  * Delete image from command line cache for -write option.
  * Add support for the Adobe Large Document format.
  * Recognize -remap option for the mogrify utility.
  * The default Helvetica font is not always available, check for
    Century Schoolbook too (reference
    http://www.imagemagick.org/discourse-server/viewtopic.php?f=2&t=15780).
* Mon Mar 15 2010 pgajdos@suse.cz
- updated to version 6.6.0-5:
  * e the jinc() functio  so that the main peak is of amplitude of 1.
  * Resampling filter must respect the image virtual pixel method.
  * The -evaluate-sequence option behaves like -evaluate except it operates
    on a sequence of images.
  * Add support for the Adobe Large Document format.
  * Add support for the -maximum and -minimum options.
  * Check to see if ICON image width /height exceeds that of the image canvas.
  * Set the DPX descriptor to Luma only if the image type is not TrueColor.
  * Add support for -fx airy(), j0(), j1(), jinc(), and sinc() (reference
    http://www.imagemagick.org/discourse-server/viewtopic.php?f=2&t=15685).
  * Don't embed an XMP profile in an EPS image for now.
  * Insufficient image data in EPT is a warning rather than an error.
  * Respect -type TrueColor when writing gray DPX images.
  * Fix problem reading 10-bit grayscale DPX images when scanline length is
    not a multiple of 3.
  * BMP has an alpha channel, it was treated as an opacity channel.
  * Write 10-bit grayscale DPX images properly.
  * Detect PDF ICCBased colorspace.
  * Finalized -set option:convolve:scale  kernel normalize/scale option
  * TransformImage() resets the image blob when called in the PICT decoder;
    use SetImageExtent() instead.
  * Support PSD RLE compression.
  * The jpeg:extent define sometimes exceeded the specified limit.
  * Resolve "too many open files"  (reference
    http://www.imagemagick.org/discourse-server/viewtopic.php?f=3&t=15546).
  * Added Correlate method which does a Convolve without reflecting the kernel.
  * Initialize grayscale colormap for PSD images.
  * Addition Third-level Subtractive Morphology Methods:
    EdgeIn, EdgeOut, Edge, TopHat, BottomHat
  * Ensuring original kernels passed to morphology are cloned before being
    modifified for use by specific methods (EG: convolve scale/normalize)
  * display -immutable to display transparent image without a checkboard.
  * Make -define png:color-type less persnickity about what it will accept.
  * added use of -precision in 'showkernel' output of -morphology
  * correct use of a 'reflected kernel' for 'Convolve' 'Dilate' and
    'Distance' Morphology primatives. This does not have a performance hit,
    though is only truely applicable when the kernel is asymmetric.  Note that
    'Erode' does not use a 'reflected' kernel, so that 'Open' and 'Close'
    operations work properly.  This 'reflected usage is defined by online
    morphology lecture notes (Google for "EECE Binary Morphology")
  * Added convolve kernel scaling setting "-set option:convolve:scale N"
    If undefined morphology convolve does not do any scaling or normalization
    of the convolution kernel.  A value of 0.0 causes normalization for both
    zero and non-zero (added weights) kernel types.
  * Speed up reading the PSD image format.
  * Add the -precision option.  Use it to set the maximum number of significant
    digits to be printed.
  * Add -features option to the identify program to display channel features.
  * Add -unique option to the identify program to display channel features.
  * Add support for compact floating point (i.e. -depth 16 -define
    quantum:format=floating-point).
  * Transparent images no longer flicker on certain system when using the
    display program.
  * Permit interactive resizing with the display program.
  * Support heterogeneous distributed processing, see
    http://www.imagemagick.org/script/architecture.php#distributed.
  * Fix semaphore assertion when reading a corrupt image with Magick++.
  * Add support for -bri
  * Added Kernel Generator to generate kernels from user strings, which
    allows the generation in many built in kernels for both Convolution
    and other Morphological methods.  New Kernels currently include..
    Convolution: Gaussian, Blur, Comet
    Morphological: Rectangle, Square, Diamond, Disk, Plus
    Distance: Chebyshev, Manhatten, Knight, Euclidean
    And both old and new (rectangular) user defined kernel specifications
    including the use of 'nan' to represent elements which are not part
    of the kernel definition.  List built-in kernel types use "-list kernel"
  * Added -morphology {method}[:{iteration}] {kernel_string}
    Initial methods includes no only the basic morphology methods: Dilate,
    Erode, Open, Close; and a pixel color preserving 'Intensity' version, but
    also the special methods: Convolve, and Distance.  Of course the
    appropriate kernel should be provided for each specific method.
  * Add OpenCL-enabled filter (e.g.  convert image.png -process
    "convolve '-1, -1, -1, -1, 9, -1, -1, -1, -1'" image.jpg).
  * Added StringTo...() processing functions
* Mon Feb 15 2010 pgajdos@suse.cz
- don't remove *.la files, see [bnc#579798]
* Tue Feb  9 2010 prusnak@suse.cz
- build -doc subpackage as noarch
- spec cleanup
* Mon Jan 11 2010 pgajdos@suse.cz
- updated to 6.5.8-9, which fixes [bnc#565014]
* Wed Jan  6 2010 jengelh@medozas.de
- package baselibs.conf
* Mon Nov 23 2009 pgajdos@suse.cz
- updated to 6.5.7-9 (See ChangeLog)
* Tue Nov  3 2009 coolo@novell.com
- updated patches to apply with fuzz=0
* Mon Aug 24 2009 pgajdos@suse.cz
- splitted out doc package, see [bnc#533439]
* Tue Aug  4 2009 pgajdos@suse.cz
- updated to version 6.5.4-8 (See ChangeLog)
* Thu Jul 30 2009 ro@suse.de
- update baselibs.conf to complete previous change
* Fri Jun  5 2009 nadvornik@suse.cz
- updated to 6.5.3-2:
  * shared library version increased from 1 to 2
  * subpackages renamed accordingly
  * includes a fix for bnc#507728
* Fri Jan 23 2009 nadvornik@suse.cz
- backported fix for race condition [bnc#465967]
* Fri Dec  5 2008 nadvornik@suse.cz
- fixed fontconfig detection [bnc#441874]
* Mon Dec  1 2008 ro@suse.de
- add libMagicWand1 to baselibs.conf (for libxine1)
* Tue Oct  7 2008 thoenig@suse.de
- add baselibs.conf (libMagickCore1) required by libfprint0-32bit
* Wed Sep 10 2008 nadvornik@suse.cz
- update to 6.4.3-6, see ChangeLog for details
* Wed Apr  9 2008 nadvornik@suse.cz
- update to 6.4.0-4, see ChangeLog for details
  * mostly bugfixes
* Mon Apr  7 2008 schwab@suse.de
- Fix PRNG.
* Sat Mar 29 2008 coolo@suse.de
- fix requires
* Wed Mar 26 2008 nadvornik@suse.cz
- updated to 6.3.9-7, see ChangeLog for details
  * renamed shared library subpackages:
    libMagick10 -> libMagickCore1
    libWand10 -> libMagickWand1
    libMagick++10 -> libMagick++1
  * read EXIF data in TIFF images
  * add -encipher / -decipher options to the command-line utilities
  * many bugfixes and improvements
* Mon Dec  3 2007 nadvornik@suse.cz
- fixed BuildRequires
* Fri Nov 30 2007 nadvornik@suse.cz
- updated to 6.3.7-2, see ChangeLog for details
  * fixes conflicts in header files [#340485]
* Mon Oct  8 2007 pth@suse.de
- Add libMagick10 to Requires of perl-PerlMagick (#331611)
* Tue Sep 25 2007 nadvornik@suse.cz
- updated to 6.3.5-10: fixes CVE-2007-4985, CVE-2007-4986,
  CVE-2007-4987, CVE-2007-4988 [#327021]
* Fri Aug  3 2007 coolo@suse.de
- fix provides for ImageMagick-Magick++ (#293401)
* Sat Jul 28 2007 coolo@suse.de
- remove requires on ImageMagick-Magick++
* Wed Jul 25 2007 nadvornik@suse.cz
- updated to 6.3.5-3,,
  created ImageMagick-extra with full set of requirements
- adjusted to Shared Library Policy:
  * created libMagick10 and libWand10
  * renamed ImageMagick-Magick++ -> libMagick++10
  * renamed ImageMagick-Magick++-devel -> libMagick++-devel
* Thu Apr 19 2007 nadvornik@suse.cz
- updated to 6.3.3-8, see ChangeLog for details
- fixed various crashes on malformed input, including
  CVE-2007-1797 and CVE-2007-1667 [#258253]
- do not build static libs
- adjusted BuildRequires for libjasper-devel
* Tue Feb 27 2007 dmueller@suse.de
- adjust BuildRequires: libexif -> libexif-devel
* Mon Feb 19 2007 mvaner@suse.cz
- Array boundaries fix in bezier path (#243280)
  - bezier-array.patch
* Mon Oct 30 2006 nadvornik@suse.cz
- fixed overflows in dcm and palm codecs CVE-2006-5456 [#215685]
* Wed Oct 18 2006 postadal@suse.cz
- disabled -fstack-protector for %%suse_version <= 1000
* Tue Oct 17 2006 nadvornik@suse.cz
- updated to 1.3.0-0
  * enhanced -fx
  * many bugfixes, see ChangeLog
* Thu Jul 13 2006 nadvornik@suse.cz
- updated to 1.2.8-1
  * security fixes merged upstream
  * fixed compilation with new libpng
  * many other fixes
* Wed Mar 15 2006 nadvornik@suse.cz
- fixed rpath in perl module
* Fri Feb  3 2006 nadvornik@suse.cz
- better fix for format string vulnerability
  CVE-2006-0082 [#141390]
- fixed shell metacharacters in file names passed into delegates
  CVE-2005-4601 [#141999]
- added version numbers to devel subpackage requirements
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Mon Jan 16 2006 meissner@suse.de
- Use -fstack-protector.
* Tue Dec 20 2005 nadvornik@suse.cz
- updated to 6.2.5
* Wed Sep 21 2005 nadvornik@suse.cz
- updated to 6.2.4
* Sat Sep 17 2005 postadal@suse.cz
- parallelize build
* Wed Sep  7 2005 nadvornik@suse.cz
- fixed URL in man pages [#115568]
* Thu Jul 21 2005 nadvornik@suse.cz
- moved .la files back to main package, they are needed for runtime
* Fri Jul 15 2005 nadvornik@suse.cz
- updated to 6.2.3
- fixed incorrect char type usage [#95086]
* Tue May  3 2005 nadvornik@suse.cz
- updated to 6.2.2, fixes crash in PNM reader [#80428]
* Wed Mar  9 2005 nadvornik@suse.cz
- fixed format string vulnerability [#67273]
* Wed Mar  2 2005 nadvornik@suse.cz
- linked PerlMagick correcly
- added xorg-x11-devel to requires of devel subpackage
* Sat Jan 22 2005 ro@suse.de
- fix libltdl removal on lib64
* Tue Jan 18 2005 nadvornik@suse.cz
- updated to 6.1.8
  * fixed .psd file read overflow (CAN-2005-0005) [#49839]
* Mon Nov  1 2004 nadvornik@suse.cz
- fixed integer overflow in EXIF handling [#47745]
* Tue Sep 14 2004 nadvornik@suse.cz
- branched new subpackage ImageMagick-Magick++-devel [#45245]
* Tue Sep 14 2004 nadvornik@suse.cz
- removed Requires: ImageMagick-devel from ImageMagick-Magick++ [#45245]
* Tue Sep  7 2004 nadvornik@suse.cz
- updated to 6.0.7
  * fixed possible miscompilation of included headers
  * fixed PerlMagick's Profile crash [#44710]
  * other bugfixes
* Tue Aug 31 2004 nadvornik@suse.cz
- updated to 6.0.6-2:
  * fixed decoding runlength-encoded BMP [#44081]
  * enabled LZW compression
* Mon Aug  9 2004 ro@suse.de
- fix build with current automake
* Mon Jun 28 2004 nadvornik@suse.cz
- updated to 6.0.2
* Fri Mar 26 2004 nadvornik@suse.cz
- adjusted default fonts
* Fri Feb  6 2004 nadvornik@suse.cz
- update to 5.5.7-16
- added run_ldconfig macro
- build as user
* Tue Sep  9 2003 nadvornik@suse.cz
- fixed annotate function [29748]
* Mon Sep  8 2003 nadvornik@suse.cz
- fixed reading of tiff images [#25552]
* Thu Aug 28 2003 nadvornik@suse.cz
- fixed output from Magiar@suse.cz
- require the perl version we build with
* Tue Jul 29 2003 nadvornik@suse.cz
- lib64 fixed
- filelist fixed
* Fri Jul 25 2003 nadvornik@suse.cz
- updated to 5.5.7-10
- used perl_process_packlist
* Mon Feb 10 2003 nadvornik@suse.cz
- updated to 5.5.4-4:
  - fixed bug [#23111]
- copied ltdl sources from libtool package
* Thu Dec 19 2002 adrian@suse.de
- add liblcms-devel to #neededforbuild
* Thu Nov 21 2002 nadvornik@suse.cz
- updated to 5.5.1
* Wed Nov 20 2002 ro@suse.de
- fix build with latest automake
* Fri Nov  1 2002 nadvornik@suse.cz
- fixed detection of lpr [#21187]
- fixed to compile with new libjasper
* Tue Sep  3 2002 nadvornik@suse.cz
- do not try to detect supported ghostscript devices [#18424]
* Thu Aug 29 2002 nadvornik@suse.cz
- fixed typo in delegates.mgk
* Sat Aug 10 2002 kukuk@suse.de
- Fix filelist for threaded perl
* Fri Jul 26 2002 adrian@suse.de
- fix neededforbuild
* Fri Jul 26 2002 nadvornik@suse.cz
- update to 5.4.7-4
* Tue Jul  2 2002 nadvornik@suse.cz
- update to 5.4.7
* Fri May  3 2002 meissner@suse.de
- %%_lib fixes
* Wed Mar  6 2002 nadvornik@suse.cz
- added symlink index.html->ImageMagick.html in doc directory
* Mon Feb  4 2002 nadvornik@suse.cz
- update to 5.4.2-3, xtp updated to 5.4.3
* Thu Jan 31 2002 ro@suse.de
- changed neededforbuild <libpng> to <libpng-devel-packages>
* Thu Jan 17 2002 nadvornik@suse.cz
- html files installed correctly
* Tue Jan 15 2002 nadvornik@suse.cz
- update to 5.4.2:
  - new scripting language utility, conjure
* Mon Dec  3 2001 nadvornik@suse.cz
- update to 5.4.1:
  - better SVG support
  - changed default background color to none
  - eliminated the libMagick.so dependancy on libtiff, libpng, libjpeg
  - coders/wmf.c updated for libwmf 0.2
* Thu Oct 18 2001 nadvornik@suse.cz
- update to 5.4.0:
  - Text drawing now handles UTF8-encoding
  - Added a MATLAB encoder
  - Uses SHA instead of MD5 for image signatures
* Fri Aug 24 2001 nadvornik@suse.cz
- update to 5.3.8:
  - Added a new method SetImageClipMask().
  - Added @ to the image geometry specification. Use it to specify
    the square-root of the maximum area in pixels of an image
  - many bugfixes
* Tue Aug 21 2001 nadvornik@suse.cz
- removed wv-devel from neededforbuild, it is no longer needed
- fixed segfault in svg converting
- fixed doc installation
* Wed Aug 15 2001 nadvornik@suse.cz
- compiled with libjasper
* Tue Jul 24 2001 nadvornik@suse.cz
- update to 5.3.7
* Fri Jul 20 2001 kukuk@suse.de
- changed neededforbuild <gs_fonto> to <ghostscript-fonts-other>
- changed neededforbuild <gs_fonts> to <ghostscript-fonts-std>
- changed neededforbuild <gs_lib> to <ghostscript-library>
- changed neededforbuild <gs_serv> to <ghostscript-serv>
* Wed Jun 27 2001 nadvornik@suse.cz
- update to 5.3.6
- dropped ImageMagick-pictures subpackage
* Tue Jun 12 2001 nadvornik@suse.cz
- update to 5.3.5
- fixed to compile with new autoconf
* Tue Apr 17 2001 kukuk@suse.de
- Remove magickcpp_version macro
* Thu Apr  5 2001 nadvornik@suse.cz
- updated to 5.3.1
* Tue Mar 27 2001 ro@suse.de
- libtoolize main dir as well
* Mon Mar 26 2001 ro@suse.de
- libtoolize
* Fri Mar  9 2001 nadvornik@suse.cz
- updated to 5.3.0
- fixed neededforbuild
* Mon Feb 19 2001 nadvornik@suse.cz
- fixed filelist
* Tue Feb 13 2001 nadvornik@suse.cz
- update to 5.2.9
* Tue Dec 12 2000 nadvornik@suse.cz
- compiled with option --with-threads
* Tue Dec  5 2000 nadvornik@suse.cz
- update to 5.2.6
- now uses freetype2
* Thu Nov 16 2000 nadvornik@suse.cz
- update to 5.2.5
* Tue Nov 14 2000 nadvornik@suse.cz
- fixed writing transparent xpm files
* Wed magemag -> ImageMagick
-    magickd  -> ImageMagick-devel
-    magickpp -> ImageMagick-Magick++
-    plmagick -> perl-PerlMagick
-    impict   -> ImageMagick-pictures
* Wed Oct 18 2000 nadvornik@suse.cz
- update to 5.2.4
- compiled with --with-modules
* Mon Sep 18 2000 nadvornik@suse.cz
- fixed usage of suse_update_config
* Thu Sep 14 2000 nadvornik@suse.cz
- drop subpackage imfilm, removed povray from neededforbuild
- povray scripts are now in /usr/share/doc/imagemag/scenes
* Thu Sep 14 2000 nadvornik@suse.cz
- update to 5.2.3
- new subpackage magickd for includes and static libs
- changed prefix to /usr
- removed --without-largefiles
* Tue Aug 22 2000 ro@suse.de
- fixed perl path
* Thu Jun  8 2000 nadvornik@suse.cz
- update to latest source from ftp
- added source url
* Tue Jun  6 2000 nadvornik@suse.cz
- images, scenes -> /usr/share/ImageMagick
- doc -> %%{_defaultdocdir}/imagemag
* Mon Jun  5 2000 nadvornik@suse.cz
- used --without-largefiles
* Thu Jun  1 2000 nadvornik@suse.cz
- xtp updated to 5.2.0
* Mon May 29 2000 nadvornik@suse.cz
- updated to 5.2.0
* Fri May 19 2000 nadvornik@suse.cz
- used %%{_defaultdocdir}
- changed group
* Fri Apr 28 2000 nadvornik@suse.cz
- fixed to compile with xf86-4.0
* Mon Apr 10 2000 nadvornik@suse.cz
- added URL
* Fri Apr  7 2000 bk@suse.de
- added suse config update macro
* Thu Apr  6 2000 nadvornik@suse.cz
- update to 5.1.1
- added BuildRoot
* Wed Jan 19 2000 ro@suse.de
- fixed specfile
* Mon Jan  3 2000 ro@suse.de
- update to 5.1.0
* Mon Sep 27 1999 bs@suse.de
- fixed requirements for sub packages
* Mon Sep 13 1999 bs@suse.de
- ran old prepare_spec on spec file to switch to new prepare_spec.
* Wed Sep  1 1999 ro@suse.de
- update to 4.2.9
* Mon Jun 28 1999 ro@suse.de
- update to 4.2.7
* Wed May 19 1999 ro@suse.de
- fixed path in specfile
* Wed May 19 1999 ro@suse.de
- fixed specfile
* Tue May 18 1999 ro@suse.de
- update to 4.2.5
- new subpackage: magickpp (aka Magick++) a C++-API for libmagick
* Fri Feb 19 1999 ro@suse.de
- update to 4.2.0
* Mon Jan 18 1999 bs@suse.de
- set libraries to 755
* Wed Jan 13 1999 ro@suse.de
- update to 4.1.7 / PerlMagick 1.58
* Mon Dec 14 1998 ro@suse.de
- update to 4.1.6
- disabled unix98/ptys in configure.in
* Tue Dec  1 1998 ro@suse.de
- update to 4.1.5 / PerlMagick 1.53
* Tue Nov 17 1998 ro@suse.de
- update to 4.1.4
- switched to use configure instead of imake
* Mon Aug 17 1998 ro@suse.de
- update to 4.0.9
* Fri Aug 14 1998 ro@suse.de
- fixed online documentation
  /usr/doc/packages/ImageMagick/ImageMagick.html is start page
- added new subpackage PerlMagick "plmagick"
* Thu Aug 13 1998 ro@suse.de
- update to 4.0.8
  fixed default for printCommand in Display with a app-defaults file
* Mon Jun 29 1998 ro@suse.de
- update to version 4.0.7
  needs libpng-1.0.1 (and povray built with that version)
* Tue Apr  7 1998 ro@suse.de
- update to version 4.0.4
  added freetype support
  needs libpng-1.0.1 (and povray built with that version)
* Sun Mar  1 1998 ro@suse.de
- update to version 4.0.1
* Sun Nov 16 1997 ro@suse.de
- fixed Symlink /usr/doc/packages/ImageMagick
* Fri Nov 14 1997 ro@suse.de
- new version 3.9.2
* Tue Nov 11 1997 ro@suse.de
- imfilm and impict are built from same specfile
* Mon Nov  3 1997 ro@suse.de
- ready for autobuild


