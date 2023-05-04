<?php
$dom=new DomDocument();
$dom->load("A2setB2.xml");
$mname=$dom->getElementsByTagName("movie_title");
$aname=$dom->getElementsByTagName("actor_name");

echo"Movie Details.<br>";
$cnt=count($mname);
for($i=0;$i<$cnt;$i++)
{
	echo"<h3>Movie Name:".$mname[$i]->textContent."<br>Actor Name:".$aname[$i]->textContent."<br></h3>";
}
?>

