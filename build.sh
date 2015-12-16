read -p "Get the dependencies? [y/n]" answer
if [[ $answer = y ]] ; then
  
  echo "installing dependecies"
  pwd
  ./dependecies.sh >> buildlog.txt

fi

read -p "Unittest the software? [y/n]" answer
if [[ $answer = y ]] ; then
  
  echo "Unit testing!"
  ./unittest.sh > buildlog.txt

fi

read -p "Checkout the code quality of the software? [y/n]" answer
if [[ $answer = y ]] ; then
  
  echo "Checking quality!"
  pwd
  ./codequality.sh > buildlog.txt

fi

read -p "Checkout the software? [y/n]" answer
if [[ $answer = y ]] ; then
  
  echo "Checking out!"
  pwd
  ./checkout.sh > buildlog.txt

fi





