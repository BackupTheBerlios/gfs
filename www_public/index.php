<?php ?>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/TR/xhtml1">
<head>
<title>The GNOME for SuSE Project @ berlios.de</title>
<link type="text/css" rel="stylesheet" href="gfs.css">
</head>

<?php

$language=($HTTP_GET_VARS["language"]);

if ($language=="") $language='English';

include('functions');

include('locale/English');
include('locale/'.$language);
?>


<body>

<!-- Top-Logo -->
<table border="0" cellpadding="0" cellspacing="0" width="100%">
	<tr>
		<td align="left" rowspan="2"><img src="img/logo.gif" alt="GfS Logo"></td>
		<td align="right" valign="top">
			<a href="http://developer.berlios.de">
			<img src="http://developer.berlios.de/bslogo.php?group_id=677" width="124" height="32" border="0" alt="BerliOS Logo"></a>
		</td>
	</tr>
	<tr class="chooseLanguage">
		<td>
			<form method="get">
				<?php echo $textLanguage ?>:&nbsp;
				<select size="1" name="language">
					<option <?php if ($language=="Deutsch") echo 'selected="selected"' ?>>Deutsch</option>
					<option <?php if ($language=="English") echo 'selected="selected"' ?>>English</option>
				</select>
				&nbsp;<button type="submit"><?php echo $buttonChange ?></button>&nbsp;
			</form>		
		</td>
	</tr>
</table>


<!-- Content -->
<table border="0" cellpadding="0" cellspacing="5">

<!-- Menu left -->
<tr><td valign="top" align="left">
<table class="mainMenu">
<?php


menuItemCurrent($textPage1);
menuItem($textDocumentation,$language);
menuItem($textBasicPackages,$language);
menuItem($textGnomeCore,$language);
menuItem($textGnomeExtra,$language);
menuItem($text5thToe,$language);
menuItem($text3rdParty,$language);
menuItem($textNonGnome,$language);
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
You can get the latest Gnome SPECS for SuSE via anonymous CVS
</p>

</td></tr>
</table>

</body>
