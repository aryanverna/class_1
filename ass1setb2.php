<?php
session_start();
$_SESSION['eno']=$_GET['eno'];
$_SESSION['ename']=$_GET['ename'];
$_SESSION['addr']=$_GET['addr'];
?>
<html><body>
<form action=ass1setb2_3.php>
Enter basic:<input type=text name=basic><br><br>
Enter DA:<input type=text name=da><br><br>
Enter HRA:<input type=text name=hra><br><br>
<input type=submit name=Next>
</form>
</body></html>
