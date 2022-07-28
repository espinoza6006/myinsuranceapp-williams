import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  stages: [
    { duration: '30s', target: 20 }, // simulates ramp up 20 users along 30s
    { duration: '1m30s', target: 10 }, // stays  20 users for 1,5 min
    { duration: '20s', target: 0 }, //ramp down to 0 users along 20s
  ],
};

export default function () {
  const res = http.get('https://httpbin.test.k6.io/'); // change by your own url
  check(res, { 'status was 200': (r) => r.status == 200 });
  sleep(1);
}