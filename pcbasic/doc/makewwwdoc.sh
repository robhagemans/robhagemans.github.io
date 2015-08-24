DOCLOC=../../../pc-basic/docsrc/
VERSION=$(cat ../../../pc-basic/pcbasic/data/version.txt)
cp $DOCLOC/doc.css ../style
(cat $DOCLOC/documentation.html; echo -e '<article>\n<h1 id="invocation">Invocation</h1>'; cat $DOCLOC/options.html $DOCLOC/examples.html; echo -e "</article>"; cat $DOCLOC/reference.html $DOCLOC/acknowledgements.html $DOCLOC/footer.html) > predoc.html
$DOCLOC/maketoc.py predoc.html > toc.html
(cat header.html; echo -e "<header>\n<h1>PC-BASIC $VERSION</h1>\n<p><small>Documentation compiled on $(date --utc).</small></p></header>"; cat toc.html predoc.html) > index.html
rm predoc.html toc.html
