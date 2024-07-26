<?php
header('Content-Type: application/json');

// Thông tin kết nối cơ sở dữ liệu
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "bai-do-xe-db";

// Kết nối cơ sở dữ liệu
$conn = new mysqli($servername, $username, $password, $dbname);

// Kiểm tra kết nối
if ($conn->connect_error) {
    die("Kết nối thất bại: " . $conn->connect_error);
}

// Lấy trạng thái barrier
$sql = "SELECT status FROM barrier_status WHERE id=1";
$result = $conn->query($sql);

$response = array();
if ($result->num_rows > 0) {
    $row = $result->fetch_assoc();
    $response['status'] = $row['status'];
} else {
    $response['status'] = 'unknown';
}

echo json_encode($response);
$conn->close();
?>
