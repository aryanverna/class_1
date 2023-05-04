<?php
$q=$_GET["q"];
echo $q;
$conn=pg_connect("host=127.0.0.1 port=5432 user=postgres password=postgres dbname=teacher") or die("Could not connect");
$sql="select * from teacher where tname='$q'";
$result=pg_query($sql) or die("Incorrect query");

echo "<html><body><table border=1>";
echo "<tr><th>tno</th><th>Tname</th><th>qual</th><th>salary</th></tr>";

while($row=pg_fetch_row($result))
{
	echo"<tr><td>";
	echo $row[0];
	echo"</td><td>";
	echo $row[1];
	echo"</td><td>";
	echo $row[2];
	echo"</td><td>";
	echo $row[3];
	echo"</td></tr>";
}
?>

