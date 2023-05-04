<?php
session_start();
$basic=$_GET['basic'];
$da=$_GET['da'];
$hra=$_GET['hra'];
echo "<h1>Employee Details</h1><br><br>";
echo "Employee No:$_SESSION[eno]<br>";
echo "Employee Name:$_SESSION[ename]<br>";
echo "Employee Address:$_SESSION[addr]<br><br>";
$total=$basic+$da+$hra;
echo "Basic:$basic<br>";
echo "DA:$da<br>";
echo "HRA:$hra<br><br>";
echo "Total:$total";
?>

