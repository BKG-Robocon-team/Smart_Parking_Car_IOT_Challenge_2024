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

// Cập nhật trạng thái barrier
$sql = "UPDATE barrier_status SET status='closed' WHERE id=1";

$response = array();
if ($conn->query($sql) === TRUE) {
    $response['status'] = 'success';
    $response['message'] = 'Barrier closed successfully';
} else {
    $response['status'] = 'error';
    $response['message'] = 'Failed to close the barrier';
}

echo json_encode($response);
$conn->close();
?>
