# Minimal Makefile for Sphinx documentation
# You can tinker with the rest of this file yourself, but don't touch the
# "boilerplate" shown.

SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SPHINXPROJ    = .
SOURCEDIR     = .
BUILDDIR      = _build

# Internal variables.
PAPER         =
CONFIG        =
CHECKPYDOC    =
WARNINGS      =

.PHONY: help clean html dirhtml singlehtml pickle json htmlhelp qthelp devhelp \
		latex latexpdf text man texinfo epub

help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

clean:
	@rm -rf "$(BUILDDIR)"

html:
	@$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

dirhtml:
	@$(SPHINXBUILD) -M dirhtml "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

singlehtml:
	@$(SPHINXBUILD) -M singlehtml "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

pickle:
	@$(SPHINXBUILD) -M pickle "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

json:
	@$(SPHINXBUILD) -M json "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

htmlhelp:
	@$(SPHINXBUILD) -M htmlhelp "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

qthelp:
	@$(SPHINXBUILD) -M qthelp "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

devhelp:
	@$(SPHINXBUILD) -M devhelp "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

latex:
	@$(SPHINXBUILD) -M latex "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

latexpdf:
	@$(SPHINXBUILD) -M latexpdf "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

text:
	@$(SPHINXBUILD) -M text "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

man:
	@$(SPHINXBUILD) -M man "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

texinfo:
	@$(SPHINXBUILD) -M texinfo "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

epub:
	@$(SPHINXBUILD) -M epub "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)