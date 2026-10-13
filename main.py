import requests
response=requests.get("https://jsonplaceholder.typicode.com/posts")
x=response.json()
print(response.status_code)
for post in x:
    if post['id']<4:
        print(post['title'])