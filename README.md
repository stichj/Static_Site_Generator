
# Static Site Generator

This  **Static Site Generator**  is a Python-based tool that converts markdown files into HTML pages. It includes a simple web server that serves the generated site locally. You can interact with the generated static site through your browser at  `localhost:8888`.

Developed as part of a coding bootcamp on  **[boot.dev](https://www.boot.dev/)**, this project demonstrates skills in Python, web development, static site generation, and testing.

## Tech Stack

-   **Python 3**
    
-   **Markdown**  – for content creation
    
-   **HTML/CSS**  – for generated static site structure and styling
    
-   **unittest**  – for automated testing

- **HTTP-Server** - for static site provisioning 
    

## Getting Started

### Prerequisites

Make sure you have  **Python 3**  installed. You can verify by running:
```bash
python3 --version
```

### Installation

Clone the repository:
```bash
git clone https://github.com/stichj/Static_Site_Generator.git
cd Static-Site-Generator
```

### Running the Static Site Generator

1. You can run the generator by running `main.sh`:
```
bash
./main.sh 
```
The script will automatically generate the HTML files and launch a local web server.

3.  Open your browser and visit:
http://localhost:8888

You will see the generated static website running locally. You can interact with the pages and see the content rendered from the markdown files.

### Configuration

The static markdown files are already contained in the `contents/` folder. The static CSS stylesheet and the images are contained in the `static/` and `static/images/` folders. You can replace them if you wish to generate your own static website. 
    

## Testing

The project is well-tested using Python's built-in  **unittest**  module. To run the tests, use the following command:

```bash
./test.sh
```

This will run all the unit tests defined in the  `tests`  directory to ensure the generator works as expected.


## Features

-   Converts  **markdown**  files into  **HTML**  pages.
    
-   Includes  **static assets**  like stylesheets and images.
    
-   Launches a  **local Python web server**  to serve the generated site on  `localhost:8888`.
    
-   Well-tested with  **unittest**  to ensure stability and correctness.
    
-   Simple and easy-to-use with both Python and shell script execution options.
