<div align="center">
  <img src="./docs/images/pagify.png" alt="Pagify Logo" width="350px"/>
</div>

<div align="center">

![GitHub Stars](https://img.shields.io/github/stars/Mohammad222PR/pagify?style=flat&logo=github)
![GitHub Forks](https://img.shields.io/github/forks/Mohammad222PR/pagify?style=flat&logo=github)
![GitHub Issues](https://img.shields.io/github/issues/Mohammad222PR/pagify?style=flat&logo=github)
![Python Version](https://img.shields.io/badge/python-3.7%2B-blue?style=flat&logo=python)
![MIT License](https://github.com/Mohammad222PR/pagify/blob/main/LICENSE?style=flat)
![Contributors](https://img.shields.io/github/contributors/Mohammad222PR/pagify?style=flat)
![GitHub Repo Size](https://img.shields.io/github/repo-size/Mohammad222PR/pagify?style=flat)
![Commit Activity](https://img.shields.io/github/commit-activity/m/Mohammad222PR/pagify?style=flat)
[![Downloads](https://static.pepy.tech/badge/pagify?style=flat)](https://pepy.tech/project/pagify)

</div>

## Overview

**[Pagify](https://pypi.org/project/pagify/)** is a Python package that provides a robust and flexible pagination system suitable for both simple and complex applications. Whether you need pagination for raw Python projects or integration into Django or similar frameworks, `pagify` delivers straightforward and adaptable solutions.

### 🌟 **Features**

- **Multiple Pagination Types**:
  - **Offset Pagination**: Ideal for classic numbered offset and limit scenarios.
  - **Cursor Pagination**: Efficiently handles large datasets by using cursor-based navigation.
  - **Page Number Pagination**: Simple page-based pagination for easy implementation.
- **Framework-Agnostic**: Can be used in any Python project, from minimal scripts to complex web frameworks.
- **Detailed Pagination Info**: Includes next, previous, and current page indicators.
- **JSON Response Formatting**: Consistent output formatting with built-in JSON helpers.
- **Customizable and Extensible**: Easily extend with custom serializers or formatters.

## 📚 **Documentation**

For detailed guides and examples, please refer to the [Complete Documentation](docs/index.md).

## 🛠️ **Usage**

Here's a quick example of how to use `pagify` in your Python application:

```python
from pagify.adapters.paginate import paginate_with_page_number

queryset = [{'id': i} for i in range(1, 101)]  # Example dataset
result = paginate_with_page_number(queryset, page=2, page_size=10)
print(result)
```

## 🤝 **Contribution**

We welcome contributions! If you'd like to report issues, suggest new features, or contribute code, feel free to open an issue or submit a pull request.

## 📄 **License**

`pagify` is licensed under the MIT License. Check the [LICENSE](LICENSE) file for more details.

<div align="center">

🔗 **[Visit the Pagify GitHub Repository](https://github.com/Mohammad222PR/pagify)**  
📄 **[Read the Full API Reference](docs/index.md)**

</div>
