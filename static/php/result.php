<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<?php
  
  $postContent = "";
  foreach ($_POST as $key => $value) {
    //do something
    $postContent =  $postContent . $key . ' = ' . $value . "\n" ;
  }
  mail("lionel.coquin@gmail.com", "MAIL SITE MARION-IMMO.LU", "$postContent");
  
?>
<html>
<header>
	<meta http-equiv="refresh" content="3;url=http://www.marion-immo.lu/" />
</header
<body>
<p>Merci de nous faire confiance. Nous allons vous contacter très rapidement</p>
</bodY>
</html>
