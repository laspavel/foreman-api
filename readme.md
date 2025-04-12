# Foreman API – Python Client for Foreman

Foreman API is a lightweight Python client designed to interact with the Foreman RESTful API. It simplifies the process of automating tasks such as provisioning, configuration, and monitoring of servers managed by Foreman.​

## 📌 Features

* Simple and intuitive interface for making API requests​
* Support for GET, POST, PUT, and DELETE HTTP methods​
* Handles authentication seamlessly​
* Flexible parameter handling for various API endpoints​

## ⚙️ Requirements

* Python 3.8 or higher​
* Access to a Foreman instance with API credentials​

## 🚀 Installation

Clone the repository and include ForemanApi.py in your project:​

```bash
git clone https://github.com/laspavel/foreman-api.git
```

Alternatively, you can copy the ForemanApi.py file directly into your project directory.​

## 🧪 Usage Example
Here's a basic example of how to use the Foreman API client:​

```python
import ForemanApi

# Initialize the Foreman API client
rapi = ForemanApi.ForemanAPI('https://foreman.example.com/api/', 'apiuser', 'apipassword')

# Retrieve information about a specific host
host_info = rapi.api_request(api_type='get', api_method='hosts/1')

# Alternatively, using the shorthand method
# host_info = rapi.get.hosts(id=1)

print(host_info)
```

For more examples, refer to the example.py file included in the repository.​

## 📄 License

MIT License.​

## 🤝 Contributions

Suggestions and improvements are welcome! Feel free to open an issue or submit a pull request.

## 📬 Contact

Author: [laspavel](https://github.com/laspavel)

Feel free to reach out with questions or ideas.

---