A roadmap of things to do
=========================

* create a plugin to generated related articles box containing hyper links to
  related articles in the laytout. Interesting algorithms can be used to
  identify related articles.

* depends on `docutils` and `pygments`

* TOC to scroll down with page.

* if more that one article-content is detected for the same page-url, how to
  generate the HTML ? as list of individual articles ? or as tabbed version of
  articles ?

* `regen` option in generate sub-command is yet to be implemented.

* Cache templates while generating the target site.

* Merge support when using `create -f`. A 3-way merge is there, find a clean
  solution for this.

* for `pagd.myblog` layout,

  * Support asciidoc content parsing.
  * Facebook integration. There are aweful lot of ways to integrate a page with
    facebook. Do we really need them all ?


Release check-list 
------------------

- Sphinx doc quick-start, one time activity.
    sphinx-quickstart   # And follow the prompts.
    sphinx-apidoc -f -d 2 -T -o  docs/ pagd $(APIDOC_EXCLUDE_PATH)"

- Change the release version in ./CHANGELOG.rst, ./pagd/__init__.py

- Update ./CHANGELOG.rst for release changes and update README.rst to
  highlight important features.

- Update TODO.rst if any, because both CHANGELOG.rst and TODO.rst are referred
  by README.rst.

- copy ~/oss/magnific-popup-git/dist/
  {magnific-popup.css,jquery.magnific-popup.min.js}
  files to pagd/layouts/myblog/media/magnific-popup/ directory.

- Check whether release changelogs in CHANGELOG.rst have their release-timeline
  logged, atleast uptill the previous release.

- Update setup.py and MANIFEST.in for release

- Make sure that sphinxdoc/modules/ has all the modules that need to be
  documented.

- Enter virtual environment and upload the source into pypi.
        make upload

- Upload documentation zip.

- After making the release, taging the branch, increment the version number.

- Create a tag and push the tagged branch to
    github.com

