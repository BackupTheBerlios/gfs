<!DOCTYPE HTML PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/TR/xhtml1">
<head>
<title>The GNOME for SuSE Project @ berlios.de</title>
<link type="text/css" rel="stylesheet" href="gfs.css">
</head>

<?php
putenv ("LANG=de");
bindtextdomain ("gfs", "./locale");
textdomain ("gfs");
?>

<body>

<!-- Top-Logo -->
<table border="0" cellpadding="0" cellspacing="0" width="100%">
<tr><td align="left"><img src="img/logo.gif" alt="GfS Logo"></td>
<td></td>
<td align="right" valign="top">
<a href="http://developer.berlios.de">
<img src="http://developer.berlios.de/bslogo.php?group_id=677" width="124" height="32" border="0" alt="BerliOS Logo"></a>
</td></tr>
</table>


<!-- Content -->
<table border="0" cellpadding="0" cellspacing="5">

<!-- Menu left -->
<tr><td valign="top" align="left">
<table border="0" cellpadding="4" cellspacing="0">
<?php

function menuItem($n) {
  echo '<tr><td class="menuItem"><a href="#" class="menuItem">'._($n).'</td></tr>';
}

function menuItemCurrent($n) {
  echo '<tr><td class="menuItemCurrent">'._($n).'</td></tr>';
}

menuItemCurrent('page 1');
menuItem('basic packages');
menuItem('gnome base');
menuItem('gnome core');
menuItem('gadgets');
menuItem('fifth toe');
menuItem('applications');
?>
</table>
</td>


<!-- current page content -->
<td valign="top">
Welcome to the Gnome for SuSE Project page.
<p>
03.03.2003&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;this site is still under construction
</p>
<p>
You can get the latest Gnome-2.2-RPM-Packages for SuSE 8.1 build for i686 via anonymous CVS
</p>

</td></tr>
</table>

</body>
