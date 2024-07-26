 <?php 
 
if (session_status() == PHP_SESSION_NONE) {
    session_start();
	$connection = mysql_connect("localhost", "root", "");
	$db = mysql_select_db("cpms", $connection);
	$phone=$_SESSION['phone'];
	$query = mysql_query("select * from users where pl_booked='YES' AND phone='$phone'", $connection);
	$rows = mysql_num_rows($query);
	//echo $rows;
	$row=mysql_fetch_array($query);
	if ($rows == 1) {
	 header("Location: ../booked.php");
	}else{
	 header("Location: ../your_car.php");
		}
		
}