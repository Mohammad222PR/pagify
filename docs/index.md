# Pagify

Welcome to the **Pagify** documentation! This package provides an easy-to-use solution for handling pagination in Python applications, supporting a wide range of projects from basic scripts to complex frameworks.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [API Reference](#api-reference)
- [Contributing](#contributing)
- [License](#license)

---

## Introduction

The **Pagify** package is a versatile and efficient tool for implementing pagination in Python applications. It supports multiple pagination types to cater to different needs, making it suitable for use with plain Python, Django, Flask, or any other Python-based frameworks. 

### Key Features

- **Framework-Agnostic**: Compatible with raw Python applications, Django projects, and more.
- **Multiple Pagination Methods**: Supports offset, cursor, and page number pagination for diverse use cases.
- **Detailed Metadata**: Provides comprehensive pagination details such as next, previous, and current pages.
- **Easy-to-Use**: Straightforward API for rapid integration.
- **Customizable**: Easily extendable for advanced use cases.

---

## Installation

To install the **Pagify** package, run the following command:

### Install the Pagify Package

Install Pagify from PyPI using pip:

```bash
pip install pagify
```

---

## Usage

For complete guides, detailed examples, and advanced use cases, refer to the [usage documentation](usage.md). This section covers everything from basic usage to customization for different pagination strategies.

### Quick Start

Here's a brief overview to get you started quickly:

1. **Import and Setup**: Import the appropriate pagination method from `pagify.adapters`.
2. **Apply Pagination**: Use the method on your dataset or query results.
3. **Format Responses**: Utilize the provided functions for standardized JSON response formatting.

Example:

```python
from pagify.adapters.paginate import paginate_with_page_number

data = [{'id': i} for i in range(1, 101)]  # Sample dataset
result = paginate_with_page_number(data, page=2, page_size=10)
print(result)
```

---

## API Reference

For a detailed breakdown of classes, methods, and available parameters, please refer to the [API reference](api_reference.md). This will guide you through the full potential of Pagify and provide insights into all features.

### Quick Links

- **Pagination Adapters**: Overview of adapters for various pagination types.
- **Helper Functions**: Details of utility functions for formatting responses.
- **Error Handling**: Learn how to manage common issues when implementing pagination.

---

## Contributing

We welcome contributions to **Pagify**! If you'd like to contribute, follow these steps:

1. **Fork the Repository**: Create a copy of the project on your GitHub account.
2. **Make Changes**: Implement your improvements or new features.
3. **Submit a Pull Request**: Share your work with the community.

For detailed contribution guidelines, see the `CONTRIBUTING.md` file in the repository.

---

## License

This project is licensed under the MIT License. For more information, see the [LICENSE](LICENSE) file. This permits free use, modification, and distribution while maintaining the package's open-source nature.

