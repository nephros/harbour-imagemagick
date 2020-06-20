#!/usr/bin/env bash
if [[ ! -d $1 ]] ; then
echo "$1 not a dir, must point to a dir (e.g. ../../rpmbuild/BUILD/ImageMagick-7.0.10-1/images), exit."
exit 1
fi
tmp=$(mktemp -d -t imtest_XXXXXX)
revfmt=png

for inp in $1/*
  do
	[[ -f $inp ]] || continue
	echo ${inp##*/}
	for fmt in pdf bmp png gif tiff jpg xbm xpm tga ps pnm pgx
  	do
		convert $inp -resize x240 $tmp/out.${fmt} || echo "${inp##*/} to $fmt failed."
		#convert $tmp/out.${fmt} $tmp/reverse${fmt}.$revfmt || echo "$fmt reverse to $revfmt failed." 
  	done
		#convert $inp -resize x240 $tmp/${inp##*/}resized_out.jpg || echo "${inp##*/} resize failed."
  done
echo conversion runs done. Enter to continue.
read dummy
file $tmp/*
echo \'file\' results shown above. Enter to continue.
read dummy
echo =================================
convert -version
echo =================================
rm -r $tmp
echo cleaning up
echo all done.
