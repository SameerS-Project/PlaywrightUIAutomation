# Playwright UI Automation Project

This is a UI automation framework built with **Playwright**, **Python**, and **Pytest**. The project demonstrates a scalable and maintainable testing structure using the **Page Object Model (POM)**, covering both static UI testing and real-world login flows.

## What It Tests

- Login flow with valid and invalid credentials on [LambdaTest E-Commerce Playground](https://ecommerce-playground.lambdatest.io/)
- UI functionality of the [TodoMVC React app](https://demo.playwright.dev/todomvc/#/)

## Project Structure
PlaywrightUIAutomation/
- Directories:
  - pages
  - tests
  - NOTE - each directory has its POM structured python file

## Getting Started
1. Clone the repo 
- git clone

- cd PlaywrightUIAutomation

2. Install dependencies 
- pip install -r requirements.txt

3. Running tests
- pytest (in terminal)

## Sample Test Cases
- Valid Login: Verifies the user is navigated to the My Account page

- Invalid Login: Checks for an error message on login failure

- Todo Entry: Adds a new todo item and confirms UI behavior


## Why This Project Matters
- Building test frameworks from scratch
- Applying QA best practices 
- Automating real-world UI scenarios
- Writing clean, scalable, and maintainable test code

## Author

- Sameer Siddiqui
- Aspiring QA Automation Engineer
- Project built as a practical showcase of UI Automation skills
