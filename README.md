# Playwright Python Pytest Automation Framework

A scalable UI test automation framework built using **Python, Playwright, and Pytest** for automating the SauceDemo application.

The framework follows the **Page Object Model (POM)** and includes data-driven testing, reusable fixtures, environment-based configuration, browser management, parallel execution, failure artifacts, Allure reporting, and GitHub Actions CI/CD.

The project is structured to demonstrate practical automation framework development, maintainability, reusability, and CI integration.

---

## Key Features

- Python + Playwright UI automation
- Pytest test framework
- Page Object Model (POM)
- Data-driven testing using JSON
- Reusable Pytest fixtures
- Centralized test data management
- Environment-based configuration
- QA, UAT, CI, and Production environments
- Browser Manager
- Chromium, Firefox, and WebKit support
- Parallel execution using Pytest-xdist
- Allure reporting
- HTML reporting
- Automatic screenshots on test failure
- Playwright trace collection
- Centralized logging
- Reusable authenticated session fixture
- Unit and end-to-end testing
- GitHub Actions CI/CD

---

## Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming language |
| Playwright | Browser automation |
| Pytest | Test execution |
| Pytest-xdist | Parallel execution |
| Allure | Test reporting |
| Pytest-HTML | HTML reporting |
| JSON | Test data management |
| Git | Version control |
| GitHub | Source code management |
| GitHub Actions | CI/CD |

---

## Framework Architecture

The framework follows a layered architecture to keep test logic, UI interactions, test data, configuration, and framework utilities separated.

Tests
  │
  ├── E2E Tests
  └── Unit Tests
        │
        ▼
Page Object Model
        │
        ▼
Base Page / Framework Utilities
        │
        ▼
Playwright
        │
        ▼
SauceDemo Application

---

## Test Coverage

The framework currently covers the major SauceDemo workflows.

**Authentication**
- Valid user login
- Multiple valid users
- Invalid credentials
- Locked-out user
- Login error validation
- Expected URL validation

**Inventory**
- Inventory page validation
- Add products to cart
- Multiple product scenarios
- Data-driven product testing
- Cart item count validation

**Shopping Cart**
- Add product to cart
- Open shopping cart
- Cart page validation
- Verify selected product exists in cart
- Verify product name is displayed
- Multiple product scenarios

**Checkout**
- Navigate from cart to checkout
- Checkout page validation
- Customer information entry
- Checkout overview validation
- Product validation in order summary
- Complete order
- Order confirmation validation
- Multiple customer datasets

**Framework**
- Browser launch validation
- Configuration Manager unit testing

---

## Data-Driven Testing

Test data is maintained separately from test implementation using JSON files.

test_data/
├── users.json
├── products.json
└── checkout.json

This allows the same test logic to execute against multiple datasets without duplicating test methods.

Examples include:
- Multiple login users
- Multiple products
- Multiple checkout customers

This approach improves test maintainability and makes it easier to extend test coverage.

---

## Environment Configuration

The framework supports environment-specific configuration.

Available environments include:
- QA
- UAT
- CI
- Production

Configuration files are maintained under:
- config/environments/

Tests can be executed against a specific environment using:
- pytest --env=qa

The same test suite can therefore be executed against different environments without modifying the test implementation.

---

## Installation

**Prerequisites**
- Python 3.x
- Git
- pip
- Playwright

**Clone the Repository**
- git clone git@github.com:pdharwal22/playwright-python-pytest-framework.git
- cd playwright-python-pytest-framework

**Create Virtual Environment**
- python -m venv .venv

**Activate Virtual Environment**

- macOS/Linux: source.venv/bin/activate
- Windows: .venv\Scripts\activate

**Install Dependencies**
- pip install -r requirements.txt

**Install Playwright Browsers**
- playwright install

---

## Running Tests

**Run Complete Test Suite**
- pytest

**Run Tests against QA**
- pytest --env=qa

**Run Smoke Tests**
- pytest -m smoke

**Run Regression Tests**
- pytest -m regression

**Run Tests in Parallel**
- pytest -n auto

**Run a specific Test File**
- pytest tests/e2e/test_login.py -v

---

## Reporting & Failure Handling

**HTML Report**

HTML reports are generated under:
- reports/html/

**Allure Reports**

Generate Allure results:
- pytest --alluredir=allure-results

View the Allure report:
- allure serve allure-results

**Failure Artifacts**

The framework automatically captures diagnostic artifacts when tests fail.

**Screenshots**
- reports/screenshots/

**Playwright Traces**
- reports/traces/

Failure screenshots and traces are also attached to the Allure report.

Playwright traces can be opened using:
- playwright show-trace reports/traces/<trace-file>.zip

These artifacts help investigate failed automation scenarios by providing browser actions, screenshots, DOM snapshots, and execution details.

**Logging**

The framework includes centralized logging for important test execution and framework events.

Logs can help with troubleshooting:
- Browser initialization
- Application navigation
- Login operations
- Product interactions
- Test execution
- Failure investigation

**Parallel Execution**

The framework supports parallel test execution using **pytest-xdist**.

- pytest -n auto

Each test uses isolated Playwright browser context to minimize test interference and support reliable parallel execution.

---

## CI/CD

The project uses **GitHub Actions** for continuous integration.

Workflow:
- .github/workflows/playwright-tests.yml

The CI workflow automatically:
- Checks out the repository
- Sets up Python
- Installs dependencies
- Installs Playwright browsers
- Executes the automated test suite
- Reports workflow status

The workflow is triggered through repository changes and is used to validate the framework automatically.

---

## Branch Strategy

The repository maintains separate branches to demonstrate different framework implementations.

| Branch | Purpose |
|------------|---------|
| main | Stable core Page Object Model implementation |
| develop | Active development and integration |
| feature/playwright-browser-manager | Browser Manager implementation and framework improvements |
| Business Flow feature branch | Separate Business Flow / Workflow Layer implementation |

The **POM implementation and Business Flow implementation are intentionally maintained separately** so both approaches can be referenced for future learning and architectural comparison.

---

## Design Principles

The framework focuses on:
- Separation of concerns
- Reusability
- Maintainability
- Data-driven testing
- Centralized configuration
- Reusable fixtures
- Scalable test organization
- Clear separation between test logic and UI - interaction logic
- CI/CD integration

---

## Project Status

The framework is currently functional and all implemented local and CI test scenarios are passing.

Implemented capabilities include:
- Page Object Model
- Data-driven testing
- JSON test data
- Reusable fixtures
- Authentication fixture
- Browser Manager
- Environment configuration
- Multiple environment support
- Allure reporting
- HTML reporting
- Failure screenshots
- Playwright traces
- Logging
- Parallel execution
- Unit testing
- End-to-end testing
- GitHub Actions CI/CD
- Authentication workflow
- Inventory workflow
- Shopping cart workflow
- Checkout workflow
- Business Flow implementation maintained separately

---

## Future Enhancements

Potential future improvements include:
- API automation integration
- WebSocket testing
- Expanded negative test coverage
- Docker-based execution
- Multi-browser CI matrix
- Additional reusable business workflows
- Enhanced CI artifact publishing

---

## Author

**Prateek Dharwal**

Automation Engineer focused on:
- Python
- Playwright
- Pytest
- UI Automation
- API Testing
- Test Framework Development
- CI/CD
- GitHub Actions

