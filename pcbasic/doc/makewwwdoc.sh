(cat ../../../pc-basic/docsrc/documentation.html; echo -e '<article>\n<h1 id="invocation">Invocation</h1>'; cat ../../../pc-basic/docsrc/options.html ../../../pc-basic/docsrc/examples.html; echo -e "</article>"; cat ../../../pc-basic/docsrc/reference.html ../../../pc-basic/docsrc/acknowledgements.html ../../../pc-basic/docsrc/footer.html) > predoc.html
../../../pc-basic/docsrc/maketoc.py predoc.html > toc.html
(cat header.html; echo -e "<header>\n<h1>PC-BASIC $(cat ../../../pc-basic/data/VERSION)</h1>\n<p><small>Documentation compiled on $(date --utc).</small></p></header>"; cat toc.html predoc.html) > index.html
rm predoc.html toc.html
