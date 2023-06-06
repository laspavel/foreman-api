import ForemanApi
rapi=ForemanApi.ForemanAPI('https://foreman.example.com/api/','apiuser','apipassword')
hosts=rapi.api_request(api_type='get',api_method='hosts/1')
# hosts=rapi.get.hosts(id=1)
print(hosts)
exit(0)