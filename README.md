# A-RoadMap-To-SDET

export PYTHONPATH=$PYTHONPATH:.
pytest

## Running Tests

1. **Create a virtual environment (recommended):**
	```sh
	python3 -m venv venv
	```

2. **Activate the virtual environment:**
	- On macOS/Linux:
	  ```sh
	  source venv/bin/activate
	  ```
	- On Windows (cmd):
	  ```sh
	  venv\Scripts\activate.bat
	  ```
	- On Windows (PowerShell):
	  ```sh
	  venv\Scripts\Activate.ps1
	  ```

3. **Install dependencies:**
	```sh
	pip install pytest
	```

4. **Run tests:**
	```sh
	pytest
	```

Pytest will automatically discover and run all test functions prefixed with `test_` in files named `test_*.py`.