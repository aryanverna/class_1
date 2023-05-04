<?php
setcookie("msg",$_GET['mess']);
setcookie("size",$_GET['size']);
setcookie("color",$_GET['color']);
setcookie("bcolor",$_GET['bcolor']);
setcookie("style",$_GET['st']);

echo "Message is:".$_COOKIE['msg'];
echo "<br>";
echo "Style is:".$_COOKIE['style'];
echo "<br>";
echo "Size is:".$_COOKIE['size'];
echo "<br>";
echo "Color is:".$_COOKIE['color'];
echo "<br>";
echo "Background color is:".$_COOKIE['bcolor'];
echo "<br>";

echo "<form action=A1setA2_3.php method=get>";
echo "<input type=Submit value=Next>";
echo "</form>";

?>
