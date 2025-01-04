# Department of Electronics - Quaid-i-Azam University Website

This project is a university assignment to develop an interactive and detailed website for the Department of Electronics at Quaid-i-Azam University, Islamabad.

## Project Overview

The website is designed to provide information about the Department of Electronics, including its faculty, research areas, programs offered, and contact information. It features a dynamic and responsive design with interactive elements like:

*   Moving headlines (marquee)
*   Animated cards
*   Interactive tabs for "About" section
*   Toggleable content in cards
*   Dark and Light theme switcher

## Technologies Used

*   **Frontend:**
    *   HTML5
    *   CSS3 (with CSS variables for theming)
    *   JavaScript (ES6+)
*   **Backend:**
    *   Python 3
    *   Flask (web framework)
*   **Templating Engine:**
    *   Jinja2 (comes with Flask)

## Project Structure

The project follows a standard Flask application structure:
Website {Project}/
├── app.py         # Main Flask application file (Backend)
├── static/        # Static assets (Frontend)
│   ├── css/
│   │   └── style.css  # CSS styles for the website
│   ├── images/    # Images used in the website (QAU logo, faculty, research, etc.)
│   │   ├── DSC_0016.jpeg

│   │   ├── DSC_0159.jpeg

│   │   ├── electronics.jpeg
│   │   ├── New Thumbnail Icons-13.png
│   │   └── qau_logo.jpg
│   └── js/
│       └── script.js  # JavaScript for interactivity
└── templates/     # Jinja2 templates
└── index.html   # Main HTML template
├── requirements.txt  # Project dependencies
└── README.md        # Project documentation

## Getting Started

### Prerequisites

*   Python 3.6 or higher
*   pip (Python package installer)

### Installation

1.  **Clone the repository (if applicable):**
    ```bash
    git clone <repository_url>
    cd Website\ \{Project\}
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python3 -m venv venv
    ```

3.  **Activate the virtual environment:**
    *   **On Windows:**
        ```bash
        venv\Scripts\activate
        ```
    *   **On macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

4.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

1.  **Start the Flask development server:**
    ```bash
    python app.py
    ```

2.  **Access the website in your browser:**
    Open your web browser and go to `http://127.0.0.1:5000/` (or the address indicated in the console output).

## Features

*   **Homepage:**
    *   Displays a welcome message with a moving headline.
    *   Provides an overview of the department.
    *   Presents sections for Faculty, Research, and Programs.
*   **Faculty:**
    *   Lists faculty members with their pictures, areas of expertise, and contact details.
    *   Cards are animated on hover and have toggleable content to show more/less information.
*   **Research:**
    *   Highlights research areas with descriptions and principal investigators.
    *   Uses a similar card layout as the Faculty section.
*   **Programs:**
    *   Details the BS, MS, MPhil, and PhD programs in Electronics offered by the department.
*   **Contact:**
    *   Provides a contact form to send messages to the department.
*   **Theme Switcher:**
    *   Allows users to toggle between a light and dark theme for the website. The chosen theme preference is saved using local storage.

## Customization

*   **Data:** Replace the sample data in `app.py` with actual data for faculty, research areas, and programs.
*   **Images:** Add relevant images to the `static/images` folder and update the paths in `app.py` and `index.html`. You can also rename the existing images (`DSC_0016.jpeg`, `DSC_0159.jpeg`) to more descriptive names if needed.
*   **Styling:** Modify the `style.css` file to change the website's appearance. You can easily adjust colors by changing the CSS variables for the light and dark themes.
*   **Content:** Update the `index.html` file to change the text content on the website.

## Contributing

(If you plan to make this project open source, add guidelines here on how others can contribute to the project. This might include information on how to report bugs, submit pull requests, and coding style conventions.)

## License

(Add a license for your project if you want to make it open-source. Common licenses are MIT, Apache 2.0, or GPLv3. If you are not sure, you can leave this section out for now.)

## Acknowledgements

*   Department of Electronics, Quaid-i-Azam University
