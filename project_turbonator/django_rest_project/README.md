This Django Rest framework is an API implementation to read employee details.

GET Function -
OUTPUT in JSON FORMAT:

[{"id":1,"firstname":"POIU","lastname":"mnbv","emp_id":1},{"id":2,"firstname":"ABCD","lastname":"xyz","emp_id":2}]

POST Function -
{
  "id": 4,
  "firstname": "LKJH",
  "lastname": "asdf",
  "emp_id": 3
}
OUTCome:
[{"id":1,"firstname":"POIU","lastname":"mnbv","emp_id":1},{"id":2,"firstname":"ABCD","lastname":"xyz","emp_id":2},{"id":3,"firstname":"LKJH","lastname":"asdf","emp_id":3},{"id":4,"firstname":"LKJH","lastname":"asdf","emp_id":3}]
