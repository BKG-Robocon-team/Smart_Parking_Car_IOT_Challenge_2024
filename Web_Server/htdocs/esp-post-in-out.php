<?php

if ($_SERVER["REQUEST_METHOD"] == "GET") 
{
	date_default_timezone_set('Asia/Ho_Chi_Minh');

	$today = date('Y-m-d H:i:s');                 // March 10, 2001, 5:16 pm

	$rfid = $_GET["rfid"];
	
	// Kết nối CSDL
	$conn = mysqli_connect('localhost', 'root', '', 'bai-do-xe-db');
	 
	// Kiểm tra kết nối
	if (!$conn) {
		die("Kết nối thất bại: " . mysqli_connect_error());
	}
	 
    $check = "1";
	$sql = "select * from thong_tin_ve_xe where rfid ='".$rfid."'";
	//echo $sql;
	$result = mysqli_query($conn, $sql);
	$num = mysqli_num_rows($result);		
	if ($result && $num > 0)
	{
		while ( $row = mysqli_fetch_assoc($result) ) 
		{
			if(true)
			{
				if($row["trang_thai"]==0)
				{
					$check = "1";
				}
				else
				{
					$check = "0";
				}
			}			
		}
		$sql = "UPDATE `thong_tin_ve_xe` SET `trang_thai`='".$check."' WHERE `rfid`='".$rfid."'";
		echo $sql;
		$result = mysqli_query($conn, $sql);
		
	
		
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