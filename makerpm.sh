for a in $*
do
	case $a in
		*.spec)
			spec=$a
			;;
	esac
done

[[ -r $spec ]] || exit "no spec file"

if [[ ! -e ${HOME}/.rpmmacros ]]; then
  echo 'remember to have the correct rpmbuild in ~/.rpmmacros:'
  echo '%_topdir %(echo $HOME)/rpmbuild\'
fi

echo linting the spec file...
if [[ -x  /opt/testing/bin/rpmlint ]]; then /opt/testing/bin/rpmlint -i $spec; else echo please install rpmlint-mini; fi
echo linting finished
bn=$(basename $spec .spec)
rel=$(awk '/Release/ {print $NF}' $spec)
ver=$(awk '/Version/ {print $NF}' $spec)
rbr="${HOME}/devel/rpmbuild"
brb="${rbr}/BUILDROOT/${bn}-${ver}-${rel}.arm"
arch="noarch"
pkg="${rbr}/RPMS/${arch}/${bn}-${ver}-${rel}.${arch}.rpm"

#echo -n Ctrl-C to quit now.
#for i in {3..0}; do echo -ne "."; sleep 1; done
#echo

# make build root structure
mkdir -p ${rbr}/{BUILD,BUILDROOT,RPMS,SOURCES,SPECS,SRPMS} 2>/dev/null
rm -r ${brb}
# link spec file
if [ ! -e ${rbr}/SPECS/${bn}.spec ]; then
	ln -s ${spec} ${rbr}/SPECS/${bn}.spec
fi
echo all set up, trying build...
# build rpm, do not clean sources
cd ${rbr}
rpmbuild --buildroot=${brb} -bb ${rbr}/SPECS/${bn}.spec

echo done.

