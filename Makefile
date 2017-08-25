.PHONY: serve

all: serve

.bundled: Gemfile
	bundle install --path .bundle
	touch $@

serve: .bundled
	bundle exec jekyll serve
