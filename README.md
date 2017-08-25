Outline
-------

Local setup should be:

1) Install ruby
2) gem install bundler
3) Ensure that `bundle` is on $PATH

Then the Makefile will use bundle install --path .bundled to install all gems
locally in the .bundle file (using Gemfile as specification).

The Makefile should take care of building the notes locally with `make` or
`make serve`.

Building should occur automatically in github when pushing to the master
branch.

* http://jmcglone.com/guides/github-pages/
* https://jekyllrb.com/docs/home/
* https://help.github.com/articles/about-github-pages-and-jekyll/
* https://help.github.com/categories/customizing-github-pages/
* https://help.github.com/articles/setting-up-your-github-pages-site-locally-with-jekyll/
* https://help.github.com/articles/using-jekyll-as-a-static-site-generator-with-github-pages/
