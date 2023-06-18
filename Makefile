install-requirements:	
	@pip install --upgrade pip
	@pip3 install -r requirements.txt

run-quotes:
	@python3 python/quote_process.py

run-quotes-verbose:
	@python3 python/quote_process.py --verbose

run-authors:
	@python3 python/author_process.py

run-authors-verbose:
	@python3 python/author_process.py --verbose

run-merge:
	@python3 python/merge_quotes_and_authors.py
