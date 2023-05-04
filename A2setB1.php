<?php
$xml=Simplexml_load_file("A2setA3.xml");
foreach($xml->book as $book)
{
	echo"<h3>Book no:$book->bookno<br>";
	echo"Book name: $book->bookname<br>";
	echo"Author name:$book->authorname<br>";
	echo"Price:$book->price<br>";
	echo"Year:$book->year<br>";
}
?>
