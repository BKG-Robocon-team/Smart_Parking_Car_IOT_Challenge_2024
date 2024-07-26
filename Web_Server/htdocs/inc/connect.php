<?php
/* Database config */
$db_host		= 'localhost';
$db_user		= 'root';
$db_pass		= '';
$db_database	= 'bai-do-xe-db'; 

/* End config */

$db = new PDO('mysql:host='.$db_host.';dbname='.$db_database, $db_user, $db_pass);
$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);


$servername = "localhost";
$username = "root";
$password = "";
$dbname = "bai-do-xe-db";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

//connection
mysqli_connect("localhost", "root", "") or die(mysql_error());
			mysqli_select_db($conn, "bai-do-xe-db") or die(mysql_error());
?>