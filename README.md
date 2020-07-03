# djangotask
using rest service  developed application  which performs

1.if provied IFSC code, get branch details
2. if provided bank name and city, gets details of all branches of the bank in the city



urls which works for
1. Given a bank branch IFSC code, get branch details: 
http://127.0.0.1:8000/api/?ifsc=SBIN0010433

2. Given a bank name and city, gets details of all branches of the bank in the city:
http://127.0.0.1:8000/api/?bank=STATE%20BANK%20OF%20INDIA&city=MUMBAI
