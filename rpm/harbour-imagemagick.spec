# >> macros
#%%define debug_build    0
%define maj            7
%define mfr_version    %{maj}.0.10
%define mfr_revision   33
%define source_version %{mfr_version}-%{mfr_revision}
%define quantum_depth  16
%define clibver        7
%define libspec        -%{maj}_Q%{quantum_depth}HDRI
# delegation of video things:
Recommends:    ffmpeg-tools
# << macros
# >> setup
%setup -q -n ImageMagick-%{source_version}
# << setup
# >> build pre
# << build pre
# >> build post
# Do *NOT* use %%{?_smp_mflags}, this causes PerlMagick to be silently misbuild
# make
#make %{?_smp_mflags}
# lets try this from the macros
%{make_build}
# << build post
# >> install pre
make install DESTDIR=$RPM_BUILD_ROOT
# << install pre
# >> install post
# << install post
# >> files
# << files
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
