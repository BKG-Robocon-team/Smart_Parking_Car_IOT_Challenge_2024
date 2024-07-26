<?php
header('Content-Type: application/json');

// Thông tin kết nối cơ sở dữ liệu
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "bai-do-xe-db";

// Tạo kết nối
$conn = new mysqli($servername, $username, $password, $dbname);

// Kiểm tra kết nối
if ($conn->connect_error) {
    die("Kết nối thất bại: " . $conn->connect_error);
}

// Truy vấn để tìm số lượng chỗ trống của từng bãi đỗ xe
$sql = "
    SELECT p.name AS parking_lot, COUNT(d.id) AS empty_spots
    FROM thong_tin_diem_do d
    JOIN parking_lot p ON d.parking_lot_id = p.id
    WHERE d.status = 0
    GROUP BY p.id, p.name
";

$result = $conn->query($sql);

$parking_data = array();
if ($result->num_rows > 0) {
    // Lấy dữ liệu và lưu vào mảng
    while($row = $result->fetch_assoc()) {
        $parking_data[] = array("parking_lot" => $row["parking_lot"], "empty_spots" => $row["empty_spots"]);
    }
}

echo json_encode($parking_data);

$conn->close();
?>
