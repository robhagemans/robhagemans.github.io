BASE=../../../pc-basic/
DOCSRCLOC=$BASE/docsrc/
DOCLOC=$BASE/doc
VERSION=$(cat $BASE/pcbasic/data/version.txt)
pushd $DOCSRCLOC
./makedoc.sh www/pcbasic/doc/header.html www/pcbasic/doc/index.html
popd
cp $DOCLOC/doc.css ../style
