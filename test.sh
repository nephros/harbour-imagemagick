#!/usr/bin/env bash
if [[ ! -d $1 ]] ; then
echo $1 not a dir, must point to a dir with images, exit.
exit 1
fi
tmp=$( mktemp -d )
mkdir -p $tmp
for inp in $1/tests/*miff
  do
	for fmt in pdf bmp png gif tiff jpg 
  	do
		convert $inp $tmp/out.${fmt} && echo "${inp##*/} to $fmt ok."
		convert $tmp/out.${fmt} $tmp/re${fmt}.png && echo "$fmt reverse ok." 
  	done
		convert $inp -resize x240 $tmp/out.jpg && echo "${inp##*/} resize ok."
  done
file $tmp/*
convert -version
rm -r $tmp
