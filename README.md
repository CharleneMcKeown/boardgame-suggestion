# BoardGameGeek Collection Viewer

This Python project is a web application that allows users to view their BoardGameGeek collection in a visually appealing format. It uses Flask for the backend and renders the collection using HTML templates.

## Features

- **User Collection Viewing**: Users can enter their BoardGameGeek username to view their game collection.
- **Responsive Design**: The collection is displayed in a grid format that adjusts to the screen size.

## Installation

Before running the application, you need to install the required dependencies. Ensure you have Python and pip installed on your system, then run:

```
pip install -r requirements.txt

```


## Running the Application

To start the web application, navigate to the `src` directory and run:
    
```
python main.py
```

This will start a local server. Open a web browser and go to `http://127.0.0.1:5000/` to view the application.

## Todo

- Add support for accepting user input for game type
- Add support for accepting player count input
- Add support for accepting game duration input
- Add support for randomizing a game based on user inputs