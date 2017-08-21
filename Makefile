.PHONY: serve

all: serve

Gemfile.lock: Gemfile
	bundle install
	touch Gemfile.lock

serve: Gemfile.lock
	bundle exec jekyll serve
