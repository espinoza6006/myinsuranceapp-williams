# My Insurance App Load test

To run the tests:

### k6
    - k6 run sample-load-test.js

### Apache Benchmark
    - Move to bin directory in apache (eg D:\Program Files\xampp\apache\bin)
    - ab -n100 -c2 http://httpbin.test.k6.io/
      - This launch 100 requests with 20 simultaneous each time
