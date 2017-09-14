# heroku-python-mecab-api


## API

- GET /parse
	- required parameter
		- `text`: input text 

- POST /parse
	- required parameter
		- `text`: input text
	
##### Response sample
```
$ curl 192.168.99.100:5000/parse?text=おはようございます | jq .

{
  "result": [
    "おはよう",
    "ござい",
    "ます",
    "\n"
  ]
}
```
		
## Run on local machine

1. Clone this repository

	```
	$ git clone git@github.com:tanakatsu/heroku-python-mecab-api.git
	```
	
1. Build image

	```
	$ docker-compose build
	```

1. Start container

	```
	$ docker-compose up -d
	```
	
1. Navigate your browser to `$(docker-machine ip your-machine-name):5000/`


## Deploy to Heroku

1. Clone this repository

	```
	$ git clone git@github.com:tanakatsu/heroku-python-mecab-api.git
	```
	
1. Create Heroku app

	```
	$ heroku create [your_app_name]
	```

1. Login to the registry
 
	```
	$ heroku container:login
	```

1. Build the image and push

	```
	$ heroku container:push web
	```

1. Open your web app in your browser

	```
	$ heroku open
	```
	
## License

MIT	