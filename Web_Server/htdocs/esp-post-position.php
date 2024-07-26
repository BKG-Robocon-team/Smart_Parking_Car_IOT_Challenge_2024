<?php

if ($_SERVER["REQUEST_METHOD"] == "GET") 
{
    date_default_timezone_set('Asia/Ho_Chi_Minh');

    $today = date('Y-m-d H:i:s'); // Lấy thời gian hiện tại

    $source_address = $_GET["source_address"];
    $status = $_GET["status"];
    $battery = $_GET["battery"];
    $fire = $_GET["fire"];
    
    // Kết nối CSDL
    $conn = mysqli_connect('localhost', 'root', '', 'bai-do-xe-db');
    
    // Kiểm tra kết nối
    if (!$conn) {
        die("Kết nối thất bại: " . mysqli_connect_error());
    }

    // Kiểm tra và cập nhật dữ liệu dựa trên source_address
    $sql = "UPDATE `thong_tin_diem_do` SET `status`='$status', `battery`='$battery', `fire`='$fire', `last_update`='$today' WHERE `source_address`='$source_address'";
    $result = mysqli_query($conn, $sql);

    if (mysqli_affected_rows($conn) == 0) {
        $sql = "INSERT INTO `thong_tin_diem_do` (`source_address`, `status`, `battery`, `fire`, `last_update`) VALUES ('$source_address', '$status', '$battery', '$fire', '$today')";
        $result = mysqli_query($conn, $sql);
    }

    // Ngắt kết nối
    mysqli_close($conn);
} 
else 
{
    echo "Wrong API Key provided.";
}
?>
