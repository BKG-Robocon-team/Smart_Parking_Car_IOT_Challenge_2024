<?php

if ($_SERVER["REQUEST_METHOD"] == "GET") 
{
	date_default_timezone_set('Asia/Ho_Chi_Minh');

	$today = date('Y-m-d H:i:s');                 // March 10, 2001, 5:16 pm

	$temperature_1 = $_GET["t1"];
	$temperature_2 = $_GET["t2"];
	$temperature_3 = $_GET["t3"];
	$temperature_4 = $_GET["t4"];
	$temperature_5 = $_GET["t5"];
	
	
	// Kết nối CSDL
	$conn = mysqli_connect('localhost', 'root', '', 'bai-do-xe-db');
	 
	// Kiểm tra kết nối
	if (!$conn) {
		die("Kết nối thất bại: " . mysqli_connect_error());
	}
	 

	$sql = "UPDATE `thong_tin_diem_do` SET `nhiet_do`='".$temperature_1."' WHERE `id`='1'";
	$result = mysqli_query($conn, $sql);
	$sql = "UPDATE `thong_tin_diem_do` SET `nhiet_do`='".$temperature_2."' WHERE `id`='2'";
	$result = mysqli_query($conn, $sql);
	$sql = "UPDATE `thong_tin_diem_do` SET `nhiet_do`='".$temperature_3."' WHERE `id`='3'";
	$result = mysqli_query($conn, $sql);
	$sql = "UPDATE `thong_tin_diem_do` SET `nhiet_do`='".$temperature_4."' WHERE `id`='4'";
	$result = mysqli_query($conn, $sql);
	$sql = "UPDATE `thong_tin_diem_do` SET `nhiet_do`='".$temperature_5."' WHERE `id`='5'";
	$result = mysqli_query($conn, $sql);
	// ngắt kết nối
	mysqli_close($conn);
	;
	
}
else 
{
	echo "Wrong API Key provided.";
}
?>