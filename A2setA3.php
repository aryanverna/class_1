<?php
$str=<<<XML
<?xml version="1.0" encoding="UTF-8"?>
<bookinfo>
	<book>
		<bookno>1</bookno>
		<bookname>JAVA</bookname>
		<authorname>Balguru Swani</authorname>
		<price>250</price>
		<year>2006</year>
	</book>
	<book>
		<bookno>2</bookno>
		<bookname>C</bookname>
		<authorname>Denis Ritchie</authorname>
		<price>500</price>
		<year>1971</year>
	</book>
</bookinfo>
XML;
$fname="A2setA3.xml";
$fp=fopen($fname,"w");
fwrite($fp,$str);
fclose($fp);
echo "Created filename is:".$fname;
?>


