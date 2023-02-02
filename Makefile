test:
	python3 -m unittest discover -s tests -p "test_*.py"

coverage:
	coverage run --source=devicemonitor -m unittest discover -s tests -p "test_*.py"
	coverage report -m