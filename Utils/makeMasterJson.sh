find /Users/eddycrowder/Development/python/capstone/data/output/elitemarket_json/ -type f | 
   while read file
   do
     cat $file >> /Users/eddycrowder/Development/python/capstone/data/output/data.json
   done
