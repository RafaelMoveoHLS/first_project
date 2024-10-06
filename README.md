# Flask Health Check App

This is a simple Flask-based web application that provides a health check route.

## Setup

1. Clone the repository:
   `git clone <repository_url>`
2. Navigate into the project directory:
    `cd <project_directory>`
3. Create and activate a virtual environment:
    `python3 -m venv venv`
    `source venv/bin/activate`
4. Install the dependencies:
    `pip install -r requirements.txt`
5. Run the application:
    `python app.py`
6. Access the health check endpoint:
    Open a browser or use a tool like curl to check the health status at:
    http://127.0.0.1:5000
    

## Testing
To run tests (after setting up pytest), use:
    `pytest`

## Project Structure
- `app.py`: The main application file with a simple health check route.
- `requirements.txt`: Dependencies for the project.
- `.gitignore`: Ensures ignored files/folders (e.g., __pycache__, venv/).
- `tests/test_main.py`: Test file for the health check route using pytest.