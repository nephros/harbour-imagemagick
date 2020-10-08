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
