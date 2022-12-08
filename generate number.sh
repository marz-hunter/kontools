#!/bin/bash
for i in {1..13}
do
   echo "curl -s 'https://api.whoxy.com/?key=[KEY]&reverse=whois&mode=micro&email=domains@apple.com&page=$i' | jq -r '.search_result[].domain_name'"
done
