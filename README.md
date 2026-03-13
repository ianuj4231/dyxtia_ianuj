
steps 
1. install  docker descktop
2. install postman


3. open vs code or  cursor.

in terminal, paste `git clone https://github.com/ianuj4231/dyxtia_ianuj.git`


`cd dyxtia_ianuj`


`docker build -t imagedyxtia .`


 `docker run -p  8080:8080  imagedyxtia`  

then in postman
1. hit "POST" - `http://127.0.0.1:8080/analyze-file`
	


req body to be of json type:
		

{
"business_name": "ABC Transport Ltd",
"loan_amount_requested": 75000,
"transactions": [
{"date": "2024-01-02", "description": "Client Payment", "amount": 5200},
{"date": "2024-01-03", "description": "Office Rent", "amount": -2000},
{"date": "2024-01-05", "description": "Equipment Purchase", "amount": -750},
{"date": "2024-01-07", "description": "Client Payment", "amount": 6100},
{"date": "2024-01-10", "description": "Utilities", "amount": -400},
{"date": "2024-01-15", "description": "NSF Fee", "amount": -45}
]
}



2.  hit "GET"  `http://127.0.0.1:8080/health`

