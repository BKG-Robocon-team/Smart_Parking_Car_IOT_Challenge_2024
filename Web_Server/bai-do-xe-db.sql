-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1
-- Thời gian đã tạo: Th7 26, 2024 lúc 01:40 PM
-- Phiên bản máy phục vụ: 10.4.24-MariaDB
-- Phiên bản PHP: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Cơ sở dữ liệu: `bai-do-xe-db`
--

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `barrier_status`
--

CREATE TABLE `barrier_status` (
  `id` int(11) NOT NULL,
  `status` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Đang đổ dữ liệu cho bảng `barrier_status`
--

INSERT INTO `barrier_status` (`id`, `status`) VALUES
(1, 'closed');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `history_log`
--

CREATE TABLE `history_log` (
  `id` int(11) NOT NULL,
  `licence_plate` varchar(20) DEFAULT NULL,
  `timestamp` datetime DEFAULT NULL,
  `action` varchar(10) DEFAULT NULL,
  `parking_lot_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Đang đổ dữ liệu cho bảng `history_log`
--

INSERT INTO `history_log` (`id`, `licence_plate`, `timestamp`, `action`, `parking_lot_id`) VALUES
(1, '98B2-93240', '2024-07-25 00:10:54', 'entry', 1),
(2, '98B2-93240', '2024-07-25 00:11:22', 'exit', 1),
(3, '98B2-93240', '2024-07-25 00:19:28', 'entry', 1),
(4, '98B2-93240', '2024-07-25 00:25:17', 'exit', 0),
(5, '98B2-93240', '2024-07-25 20:20:09', 'entry', 0),
(6, '98B2-93240', '2024-07-25 20:20:23', 'exit', 0),
(7, '98B2-93240', '2024-07-25 20:20:34', 'entry', 0),
(8, '98B2-93240', '2024-07-25 20:20:47', 'exit', 0),
(9, '98B2-93240', '2024-07-25 20:28:29', 'entry', 0),
(10, '98B2-93240', '2024-07-25 20:28:43', 'exit', 0),
(11, '98B2-93240', '2024-07-25 20:29:40', 'entry', 0),
(12, '98B2-93240', '2024-07-26 11:34:33', 'entry', 0),
(13, '98B2-93240', '2024-07-26 11:39:06', 'exit', 0),
(14, '98B2-93240', '2024-07-26 11:45:54', 'entry', 0),
(15, '98B2-93240', '2024-07-26 11:46:17', 'entry', 0),
(16, '98B2-93240', '2024-07-26 11:48:53', 'entry', 0),
(17, '98B2-93240', '2024-07-26 11:49:46', 'entry', 0),
(18, '98B2-93240', '2024-07-26 11:50:49', 'exit', 0),
(19, '98B2-93240', '2024-07-26 11:51:00', 'entry', 0),
(20, '98B2-93240', '2024-07-26 11:55:28', 'exit', 0),
(21, '98B2-93240', '2024-07-26 11:59:52', 'entry', 0),
(22, '98B2-93240', '2024-07-26 11:59:59', 'exit', 0),
(23, '98B2-93240', '2024-07-26 12:02:05', 'entry', 0),
(24, '98B2-93240', '2024-07-26 12:02:11', 'exit', 0),
(25, '98B2-93240', '2024-07-26 12:02:29', 'entry', 0),
(26, '98B2-93240', '2024-07-26 12:02:36', 'exit', 0),
(27, '98B2-93240', '2024-07-26 12:02:46', 'entry', 0),
(28, '98B2-93240', '2024-07-26 12:02:54', 'exit', 0),
(29, '98B2-93240', '2024-07-26 12:05:52', 'entry', 0),
(30, '98B2-93240', '2024-07-26 12:17:13', 'exit', 0),
(31, '98B2-93240', '2024-07-26 12:24:02', 'entry', 0);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `parking_lot`
--

CREATE TABLE `parking_lot` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Đang đổ dữ liệu cho bảng `parking_lot`
--

INSERT INTO `parking_lot` (`id`, `name`) VALUES
(1, 'Bãi đỗ xe ngoài trời'),
(2, 'Bãi đỗ xe trong nhà');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `thong_tin_diem_do`
--

CREATE TABLE `thong_tin_diem_do` (
  `id` int(11) NOT NULL,
  `address` varchar(20) NOT NULL,
  `status` int(11) NOT NULL,
  `fire` float NOT NULL,
  `battery` int(11) NOT NULL,
  `last_update` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `parking_lot_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Đang đổ dữ liệu cho bảng `thong_tin_diem_do`
--

INSERT INTO `thong_tin_diem_do` (`id`, `address`, `status`, `fire`, `battery`, `last_update`, `parking_lot_id`) VALUES
(1, '0x68DB', 1, 0, 242, '2024-07-25 14:06:24', 1),
(2, '0xD43B', 1, 1, 242, '2024-07-25 14:06:38', 1),
(3, '0x999A', 0, 0, 242, '2024-07-24 17:22:46', 1),
(4, '', 1, 0, 0, '2024-07-26 11:33:45', 2),
(5, '', 1, 0, 0, '2024-07-26 11:33:49', 2),
(6, '', 1, 0, 0, '2024-07-26 11:33:28', 0),
(7, '', 1, 0, 0, '2024-07-26 11:33:27', 0);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `thong_tin_ve_xe`
--

CREATE TABLE `thong_tin_ve_xe` (
  `id` int(11) NOT NULL,
  `licence_plate` varchar(30) NOT NULL,
  `is_parking` int(11) NOT NULL,
  `booking_time` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `parking_time` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Đang đổ dữ liệu cho bảng `thong_tin_ve_xe`
--

INSERT INTO `thong_tin_ve_xe` (`id`, `licence_plate`, `is_parking`, `booking_time`, `parking_time`) VALUES
(1, '98B2-93240', 1, '2024-07-26 05:24:02', '2024-07-26 05:24:01');

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `barrier_status`
--
ALTER TABLE `barrier_status`
  ADD PRIMARY KEY (`id`);

--
-- Chỉ mục cho bảng `history_log`
--
ALTER TABLE `history_log`
  ADD PRIMARY KEY (`id`);

--
-- Chỉ mục cho bảng `parking_lot`
--
ALTER TABLE `parking_lot`
  ADD PRIMARY KEY (`id`);

--
-- Chỉ mục cho bảng `thong_tin_diem_do`
--
ALTER TABLE `thong_tin_diem_do`
  ADD PRIMARY KEY (`id`);

--
-- Chỉ mục cho bảng `thong_tin_ve_xe`
--
ALTER TABLE `thong_tin_ve_xe`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT cho các bảng đã đổ
--

--
-- AUTO_INCREMENT cho bảng `barrier_status`
--
ALTER TABLE `barrier_status`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT cho bảng `history_log`
--
ALTER TABLE `history_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;

--
-- AUTO_INCREMENT cho bảng `parking_lot`
--
ALTER TABLE `parking_lot`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT cho bảng `thong_tin_diem_do`
--
ALTER TABLE `thong_tin_diem_do`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT cho bảng `thong_tin_ve_xe`
--
ALTER TABLE `thong_tin_ve_xe`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
