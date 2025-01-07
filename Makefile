.PHONY: docs doc

docs:
	$(MAKE) -C docs clean
	$(MAKE) -C docs html

doc:
	start "" chrome "file:///$(CURDIR)/docs/build/html/index.html"