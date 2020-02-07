%define debug_build    0
%define maj            7
%define mfr_version    %{maj}.0.9
%define mfr_revision   21
%define source_version %{mfr_version}-%{mfr_revision}

Name:           ImageMagick
Version:        %{mfr_version}.%{mfr_revision}
Release:        1
Summary:        Viewer and Converter for Images

Group:          Productivity/Graphics/Other
License:        ImageMagick
URL:            https://imagemagick.org/
Source0:        https://imagemagick.org/download/ImageMagick-%{mfr_version}-%{mfr_revision}.tar.xz

BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires: gcc
BuildRequires: libtool-ltdl-devel
#Requires:	

%description
ImageMagick is a software suite to create, edit, compose, or convert bitmap
images. 


%prep
#%setup -q
%setup -q -n ImageMagick-%{source_version}


%build
%configure \
  --disable-silent-rules \
  --enable-shared \
  --without-frozenpaths \
  --without-magick_plus_plus \
  --without-modules \
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
%doc



%changelog
* Fri Feb  7 13:46:29 CET 2020 <sailfish@nephros.org> 7.0.9
- initial creation of .spec file
