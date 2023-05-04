<?php
$cnt=0;

if(!isset($_COOKIE['count']))
{
	$cnt=1;
	setcookie('count',$cnt);
}
else
{
	$cnt=$_COOKIE['count'];
	$cnt++;
	setcookie('count',$cnt);
}

echo "<h3>The web page has been accessed $cnt times";
?>
