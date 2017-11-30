gunicorn -c /opt/anagrams/gunicorn.config application:app

while true; do 
  echo "heartbeat"
  sleep 20
done