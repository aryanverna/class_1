<?php
$res=fopen("contact.dat","r");
echo"<table border=1><br>";
echo"<br><b>Contact Details</b>";
while($data=fgets($res))
{
	$arr=explode(" ",$data);
	echo"<tr><td>$arr[0]</td><td>$arr[1]</td><td>$arr[2]</td><td>$arr[3]</td></tr>";
}
echo"</table>";
?>
