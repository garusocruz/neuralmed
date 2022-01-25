clean:
	find . -name "*.pyc" -delete
	find . -name "*.pyo" -delete
	rm -f .coverage
	rm -f pylint.out

run_cypher: clean
	export FLASK_DEBUG=False
	flask run

run_pandora: clean
	ls
	export FLASK_DEBUG=False
	flask run