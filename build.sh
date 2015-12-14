read -p "Get the dependencies? [y/n]" answer
if [[ $answer = y ]] ; then
  
  echo "installing dependecies"
  pwd
  ./dependecies.sh >> log.txt

fi

read -p "Checkout the software? [y/n]" answer
if [[ $answer = y ]] ; then
  
  echo "Checking out!"
  pwd
  ./checkout.sh >> log.txt

fi





