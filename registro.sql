-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 11-12-2021 a las 04:23:54
-- Versión del servidor: 10.4.22-MariaDB
-- Versión de PHP: 8.0.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `registro`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `datos`
--

CREATE TABLE `datos` (
  `id` int(9) NOT NULL,
  `nombre` varchar(40) NOT NULL,
  `email` varchar(40) NOT NULL,
  `contraseña` varchar(20) NOT NULL,
  `fecha_na` varchar(20) NOT NULL,
  `saldo` varchar(20) NOT NULL,
  `numCuenta` int(8) NOT NULL,
  `Nip` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `datos`
--

INSERT INTO `datos` (`id`, `nombre`, `email`, `contraseña`, `fecha_na`, `saldo`, `numCuenta`, `Nip`) VALUES
(1, 'luis', 'lmoreno12@ucol.mx', 'luis1234', '10/08/2001', '1100', 20166536, 6536),
(3, 'Gabo', 'gportillo@ucol.mx', 'gabo1234', '2021-12-01', '1260', 12121212, 6655),
(4, 'juls', 'juls@ucol.mx', 'julio1234', '2021-12-01', '100', 54652332, 8987),
(5, 'cedeño', 'ccedeno@ucol.mx', 'carlos', '2021-12-01', '100', 45878799, 2234),
(17, 'pedro', 'pedro@gmail.com', '1234', '2021-12-01', '100', 12349879, 8978),
(18, 'juan', 'juan@ucol.mx', '1234', '2021-12-01', '100', 36369898, 7784),
(19, 'joto', 'joto@gmail.com', '1234', '2021-12-01', '0', 0, 0),
(20, 'miguel', 'miguel@gmail.com', '1234', '2021-12-01', '100', 85637417, 5993),
(21, 'cesar', 'cesar@gmail.com', '1234', '2021-12-01', '100', 53511178, 1072),
(22, 'carlos cedeño', 'carlos@ucol.mx', 'juleslachupa', '1999-11-05', '8790', 74004802, 7123),
(23, 'roberto', 'lgaklvez1@ucol.mx', '1qazxsw2', '2021-12-08', '200', 76907391, 1212);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `datos`
--
ALTER TABLE `datos`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `datos`
--
ALTER TABLE `datos`
  MODIFY `id` int(9) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
