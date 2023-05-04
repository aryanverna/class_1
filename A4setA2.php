<?php
$name=$_GET['name'];
$userNames=array('Rohit','Virat','Dhoni','Ashwin','Harbhajan');

if(in_array(ucfirst($name),$userNames))
	echo "Hello, Master\t".$name."!";
else if(trim($name==""))
	echo"Please tell me your name";
else
	echo $name."I don't know you";
?>
