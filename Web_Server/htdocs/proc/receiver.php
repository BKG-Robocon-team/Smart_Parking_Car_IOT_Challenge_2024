<?php
    mysql_connect("localhost", "root", "") or die(mysql_error());
    mysql_select_db("cpms") or die(mysql_error());
   $name = $_POST['name']; //get posted data
    $phone = $_POST['phone'];  //escape string 
	$idno = $_POST['idno'];  //escape string 
	$plate = $_POST['plate'];  //escape string 

    $sql = "UPDATE users SET name = '$name', id_no = '$idno', plate_no = '$plate' WHERE phone = '$phone'";
       // $sql = "UPDATE content SET text = '$content' WHERE element_id = '2' ";


    if (mysql_query($sql))
    {
        echo 1;
    }

?>