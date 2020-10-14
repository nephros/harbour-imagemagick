#BASE_DIR=/home/nephros/devel/sailfish/builder
BASE_DIR=$PWD
BUILDS_DIR=$BASE_DIR/builds
CACHE_DIR=/home/nephros/.cache/gitlab-runner-cache
mkdir -p $BUILDS_DIR

for sfv in 3.3.0.14 3.4.0.22; do
  for trg in armv7hl i486; do
    gitlab-runner -l warn exec docker --docker-volumes "$BUILDS_DIR/$sfv:/builds:rw" --docker-cache-dir $CACHE_DIR --env CI_PROJECT_NAMESPACE=imagemagick-sh --env TARGET=$trg --env SFOS_VERSION=$sfv .build-local | tee $BASE_DIR/build-${sfv}.log &
  done
done
wait
for sfv in 3.3.0.14 3.4.0.22; do
  find ../builder/builds/$sfv/*/*/output/ -type f -name "*.rpm"
done
if [[ $? = 0 ]]; then
echo Want to run tests now?
read dummy
case $dummy in
  y|Y)
  gitlab-runner -l warn exec docker --docker-volumes "$BUILDS_DIR:/builds:rw" --docker-cache-dir $CACHE_DIR .test-local | tee $BASE_DIR/last-test.log
  ;;
  *)
  echo ok, stop
  ;;
esac
fi
