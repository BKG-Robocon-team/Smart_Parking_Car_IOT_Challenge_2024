<?php

if ($_SERVER["REQUEST_METHOD"] == "GET") 
{
	date_default_timezone_set('Asia/Ho_Chi_Minh');

	$today = date('Y-m-d H:i:s');                 // March 10, 2001, 5:16 pm

	// Kết nối CSDL
	$conn = mysqli_connect('localhost', 'root', '', 'bai-do-xe-db');
	 
	// Kiểm tra kết nối
	if (!$conn) {
		die("Kết nối thất bại: " . mysqli_connect_error());
	}
	 
	$sql = "SELECT COUNT(*) FROM `thong_tin_ve_xe` WHERE trang_thai = '1';";
	$result = mysqli_query($conn, $sql);
	$num = mysqli_num_rows($result);		
	if ($result && $num > 0)
	{
		while ( $row = mysqli_fetch_assoc($result) ) 
		{
			echo $row['COUNT(*)'];
		}
			
	}else
	{
		echo "get data ERROR";
	}
	//UPDATE `dbo_sinhvien` SET `IdDevice` = '5551' WHERE `dbo_sinhvien`.`MaSV` = '1101865';
	
	
}
else 
{
	echo "Wrong API Key provided.";
}
?>