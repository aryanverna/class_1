<?php
session_start();
if($_SERVER['REQUEST_METHOD']=='GET')
{
?>
	<form method="POST" action="<?php echo $_SERVER['PHP_SELF']?>">
<h3>Enter UserName:<input type=text name=txt1><br>
Enter Password:<input type=password name=txt2><br>
<input type=submit value=LOGIN>
</form>
<?php
}
else if($_SERVER['REQUEST_METHOD']=='POST')
{
	$name=$_POST['txt1'];
	$pw=$_POST['txt2'];
	if($name==$pw && $_SESSION['cnt']<3)
		echo"<h3><a href='next.php'>NEXT FORM</a></h3><br>";
	else if($_SESSION['cnt']<3&& $name!=$pw)
	{
		echo"<h3>Wrong UserName And PassWord..........".++$_SESSION['cnt']."<br>";
		echo"<h3><a href=ass1setb1.php>BACK</a></h3>";
	}
	else
	{
		echo"<h3>SORRY!!!!!!!!!!!YOUR CHANCES ARE OVER";
		session_destroy();
	}
}
?>
