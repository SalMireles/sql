<div id="top"></div>

<!--
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->



[![Flask][flask-shield]][flask-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/SalMireles/simple-booking-api">
    <img src="images/sam.jpg" alt="Logo" width="80" height="80">
  </a>


</div>



<!-- TABLE OF CONTENTS -->
<br></br>
<details>
  <summary>Table of Contents</summary>
  <ol>
      <li><a href="#about-the-project">About The Project</a></li>
      <li><a href="#roadmap">Roadmap</a></li>
    <li>
      <a href="#getting-started">Project Setup</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#usage">Usage</a></li>
      </ul>
    </li>
    <li><a href="#notes">Notes</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project 

Complete workthrough of the book SamsTeachYourself SQL in 10 Minutes.


<!-- ROADMAP -->
## Roadmap

- [x] Setup: Test Database w/ MySQL Workbench
- [ ] 01: Understanding SQL
- [ ] 02: Retrieving Data
- [ ] 03: Sorting Retrieved Data
- [ ] 04: Filtering Data
- [ ] 05: Advanced Dta Filtering
- [ ] 06: Using Wildcard Filtering
- [ ] 07: Creating Calculated Fields
- [ ] 08: Using Data Manipulation Functions
- [ ] 09: Grouping Data
- [ ] 10: Working with Subqueries
- [ ] 11: Joining Tables
- [ ] 12: Creating Advanced Joins
- [ ] 13: Combining Queries
- [ ] 14: Inserting Data
- [ ] 15: Updating and Deleting Data
- [ ] 16: Creating and Manipulating Tables
- [ ] 17: Using Views
- [ ] 18: Working with Stored Procedures
- [ ] 19: Managing Transaction Processing
- [ ] 20: Using Cursors
- [ ] 21: Understanding Advanced SQL Features

<!-- GETTING STARTED -->
## Project Setup

####Installation

* python 3.8.10 via pyenv
  ```sh
  pyenv install 3.8.10
  ```
* Clone the repo
   ```sh
   git clone https://github.com/SalMireles/sql
   ```

####Usage

1. Install packages
   ```sh
   make install
   ```
2. Boot the app
   ```sh
   make run
   ```
2. Run endpoint commands
   ```sh
   make get endpoint="<endpoint_name>" OR 
   curl -X GET http://127.0.0.1:8000/<endpoint_name>
   ```
   Examples:
   ```python
   make get endpoint=""
   make get endpoint="products"
   curl -X GET http://127.0.0.1:8000/products
   ```

<!-- Notes -->
## Notes

None

_For more examples, please refer to the [Documentation](https://example.com)_


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [SamsTeachYourself SQL in 10 Minutes](https://www.oreilly.com/library/view/sams-teach-yourself/9780135182925/)
* [Creating SQLite Test DB](https://www.quackit.com/sqlite/tutorial/create_a_relationship.cfm)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
<!-- https://github.com/Ileriayo/markdown-badges -->

[flask-shield]: https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white

[flask-url]: https://flask.palletsprojects.com/en/2.1.x/

