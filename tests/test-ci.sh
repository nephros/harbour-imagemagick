#!/usr/bin/env bash
SRCURI="https://github.com/ImageMagick/ImageMagick"
git clone --quiet --depth 1 ${SRCURI} ~/test-data || exit 100
tmp=$(mktemp -d -t imtest_XXXXXX)
revfmt=png
cvt=convert
for inp in ~/test-data/images/*
do
	[[ -f $inp ]] || continue
	echo ${inp##*/}
	for fmt in pdf bmp png gif tiff jpg xbm xpm tga ps pnm pgx djvu
	do
		$cvt $inp -resize x240 $tmp/out.${fmt} || echo "${inp##*/} to $fmt failed."
	done
done
echo =================================
echo conversion runs done.
echo =================================
file $tmp/*
echo =================================
echo \'file\' results shown above.
echo =================================
convert -version
echo =================================
echo cleaning up
rm -r $tmp
echo all done.
