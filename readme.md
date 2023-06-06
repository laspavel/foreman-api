# foreman-api - Simple Foreman api client #

**Requirements:**
* python 3.8 (or higher)

**Example usage:**
```
import ForemanApi
rapi=ForemanApi.ForemanAPI('https://foreman.example.com/api/','apiuser','apipassword')
hosts=rapi.api_request(api_type='get',api_method='hosts/1')
# hosts=rapi.get.hosts(id=1)
print(hosts)
```

## License ##

MIT / BSD

## Author Information ##

This client was created in 2023 by [Pavel Lashkevych](https://laspavel.top/).
