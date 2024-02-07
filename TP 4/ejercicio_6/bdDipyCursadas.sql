-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 21-10-2022 a las 08:12:06
-- Versión del servidor: 10.4.24-MariaDB
-- Versión de PHP: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `bddipycursadas`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cohorte`
--

CREATE TABLE `cohorte` (
  `idCohorte` int(11) NOT NULL,
  `anio` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `cohorte`
--

INSERT INTO `cohorte` (`idCohorte`, `anio`) VALUES
(1, 2020),
(2, 2021),
(3, 2022);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `concursado`
--

CREATE TABLE `concursado` (
  `idCondC` int(11) NOT NULL,
  `descripcion` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `concursado`
--

INSERT INTO `concursado` (`idCondC`, `descripcion`) VALUES
(1, 'Cursando'),
(2, 'Recursando');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `condestudiante`
--

CREATE TABLE `condestudiante` (
  `idCondE` int(11) NOT NULL,
  `descripcion` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `condestudiante`
--

INSERT INTO `condestudiante` (`idCondE`, `descripcion`) VALUES
(1, 'Regular'),
(2, 'Abandono'),
(3, 'Libre');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estadotpf`
--

CREATE TABLE `estadotpf` (
  `idEstadoTPF` int(11) NOT NULL,
  `descripcion` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `estadotpf`
--

INSERT INTO `estadotpf` (`idEstadoTPF`, `descripcion`) VALUES
(1, 'Aprobado'),
(2, 'Desaprobado');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estudiante`
--

CREATE TABLE `estudiante` (
  `lu` int(11) NOT NULL,
  `dni` int(11) NOT NULL,
  `apellido` varchar(25) NOT NULL,
  `nombre` varchar(25) NOT NULL,
  `idLocalidad` int(11) NOT NULL,
  `fechaNac` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `estudiante`
--

INSERT INTO `estudiante` (`lu`, `dni`, `apellido`, `nombre`, `idLocalidad`, `fechaNac`) VALUES
(123, 40006580, 'Cruz Miguez', 'Pablo Andres', 8, '1997-12-27'),
(221520, 40911765, 'Velazquez', 'Cristian Daniel', 1, '1997-12-27');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estudiantec`
--

CREATE TABLE `estudiantec` (
  `idEstudiantesC` int(11) NOT NULL,
  `lu` int(11) NOT NULL,
  `idCohorte` int(11) NOT NULL,
  `idCondC` int(11) NOT NULL,
  `idCondE` int(11) NOT NULL,
  `idEstadoTPF` int(11) NOT NULL,
  `fechaAlta` datetime NOT NULL,
  `idUsuarioAlta` int(11) NOT NULL,
  `fechaMod` datetime NOT NULL,
  `idUsuarioMod` int(11) NOT NULL,
  `p1` int(11) NOT NULL,
  `rp1` int(11) NOT NULL,
  `p2` int(11) NOT NULL,
  `rp2` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `estudiantec`
--

INSERT INTO `estudiantec` (`idEstudiantesC`, `lu`, `idCohorte`, `idCondC`, `idCondE`, `idEstadoTPF`, `fechaAlta`, `idUsuarioAlta`, `fechaMod`, `idUsuarioMod`, `p1`, `rp1`, `p2`, `rp2`) VALUES
(1, 123, 3, 1, 1, 1, '2022-10-21 07:21:02', 4, '2022-10-21 07:21:02', 1, 53, 60, 70, -1),
(2, 221520, 3, 1, 1, 1, '2022-10-21 07:21:02', 5, '2022-10-21 07:21:02', 3, 44, 72, 60, -1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `localidad`
--

CREATE TABLE `localidad` (
  `idLocalidad` int(11) NOT NULL,
  `descripcion` varchar(25) NOT NULL,
  `idPais` int(11) NOT NULL,
  `idProvincia` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `localidad`
--

INSERT INTO `localidad` (`idLocalidad`, `descripcion`, `idPais`, `idProvincia`) VALUES
(1, 'Capital', 1, 1),
(2, 'Campo Quijano', 1, 1),
(3, 'Cerrillos', 1, 1),
(4, 'Rosario de Lerma', 1, 1),
(5, 'San Lorenzo', 1, 1),
(6, 'Vaqueros', 1, 1),
(7, 'La Caldera', 1, 1),
(8, 'Oran', 1, 1),
(9, 'Cafayate', 1, 1),
(10, 'San Salvador de Jujuy', 1, 2),
(11, 'San Miguel de Tucuman', 1, 3),
(12, 'Perico', 1, 2),
(13, 'Burracuyu', 1, 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pais`
--

CREATE TABLE `pais` (
  `idPais` int(11) NOT NULL,
  `descripcion` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `pais`
--

INSERT INTO `pais` (`idPais`, `descripcion`) VALUES
(1, 'Argentina'),
(2, 'Uruguay'),
(3, 'Bolivia'),
(4, 'Chile');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `provincias`
--

CREATE TABLE `provincias` (
  `idProvincias` int(11) NOT NULL,
  `descripcion` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `provincias`
--

INSERT INTO `provincias` (`idProvincias`, `descripcion`) VALUES
(1, 'Salta'),
(2, 'Jujuy'),
(3, 'Tucuman'),
(4, 'Santiago del Estero'),
(5, 'Chaco'),
(6, 'Formosa');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipousuario`
--

CREATE TABLE `tipousuario` (
  `idTipoUsuario` int(11) NOT NULL,
  `descripcion` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tipousuario`
--

INSERT INTO `tipousuario` (`idTipoUsuario`, `descripcion`) VALUES
(1, 'Profesor'),
(2, 'Ayudante');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `idUsuario` int(11) NOT NULL,
  `apellido` varchar(30) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `idTipoUsuario` int(11) NOT NULL,
  `password` varchar(15) NOT NULL,
  `fechaUAcceso` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`idUsuario`, `apellido`, `nombre`, `idTipoUsuario`, `password`, `fechaUAcceso`) VALUES
(1, 'Martinez', 'Cristian', 1, 'null', '2022-10-19 22:08:47'),
(3, 'Tuero', 'Jose Ignacio', 1, 'null', '2022-10-19 22:08:47'),
(4, 'Muñoz', 'Nicolas', 2, '1234', '2022-10-19 22:12:24'),
(5, 'Colque', 'Maria', 2, '1234', '2022-10-19 22:12:24'),
(6, 'Paz', 'Lucas', 2, '1234', '2022-10-19 22:12:24');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `cohorte`
--
ALTER TABLE `cohorte`
  ADD PRIMARY KEY (`idCohorte`);

--
-- Indices de la tabla `concursado`
--
ALTER TABLE `concursado`
  ADD PRIMARY KEY (`idCondC`);

--
-- Indices de la tabla `condestudiante`
--
ALTER TABLE `condestudiante`
  ADD PRIMARY KEY (`idCondE`);

--
-- Indices de la tabla `estadotpf`
--
ALTER TABLE `estadotpf`
  ADD PRIMARY KEY (`idEstadoTPF`);

--
-- Indices de la tabla `estudiante`
--
ALTER TABLE `estudiante`
  ADD PRIMARY KEY (`lu`),
  ADD KEY `idLocalidad` (`idLocalidad`);

--
-- Indices de la tabla `estudiantec`
--
ALTER TABLE `estudiantec`
  ADD PRIMARY KEY (`idEstudiantesC`),
  ADD KEY `lu` (`lu`),
  ADD KEY `idCohorte` (`idCohorte`),
  ADD KEY `idCondC` (`idCondC`),
  ADD KEY `idCondE` (`idCondE`),
  ADD KEY `idEstadoTPF` (`idEstadoTPF`),
  ADD KEY `idUsuarioAlta` (`idUsuarioAlta`),
  ADD KEY `idUsuarioMod` (`idUsuarioMod`);

--
-- Indices de la tabla `localidad`
--
ALTER TABLE `localidad`
  ADD PRIMARY KEY (`idLocalidad`),
  ADD KEY `idPais` (`idPais`),
  ADD KEY `idProvincia` (`idProvincia`);

--
-- Indices de la tabla `pais`
--
ALTER TABLE `pais`
  ADD PRIMARY KEY (`idPais`);

--
-- Indices de la tabla `provincias`
--
ALTER TABLE `provincias`
  ADD PRIMARY KEY (`idProvincias`);

--
-- Indices de la tabla `tipousuario`
--
ALTER TABLE `tipousuario`
  ADD PRIMARY KEY (`idTipoUsuario`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`idUsuario`),
  ADD KEY `idTipoUsuario` (`idTipoUsuario`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `cohorte`
--
ALTER TABLE `cohorte`
  MODIFY `idCohorte` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `concursado`
--
ALTER TABLE `concursado`
  MODIFY `idCondC` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `condestudiante`
--
ALTER TABLE `condestudiante`
  MODIFY `idCondE` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `estadotpf`
--
ALTER TABLE `estadotpf`
  MODIFY `idEstadoTPF` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `estudiantec`
--
ALTER TABLE `estudiantec`
  MODIFY `idEstudiantesC` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `localidad`
--
ALTER TABLE `localidad`
  MODIFY `idLocalidad` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT de la tabla `pais`
--
ALTER TABLE `pais`
  MODIFY `idPais` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `provincias`
--
ALTER TABLE `provincias`
  MODIFY `idProvincias` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `tipousuario`
--
ALTER TABLE `tipousuario`
  MODIFY `idTipoUsuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `idUsuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `estudiante`
--
ALTER TABLE `estudiante`
  ADD CONSTRAINT `Estudiante_ibfk_1` FOREIGN KEY (`idLocalidad`) REFERENCES `localidad` (`idLocalidad`);

--
-- Filtros para la tabla `estudiantec`
--
ALTER TABLE `estudiantec`
  ADD CONSTRAINT `estudiantec_ibfk_1` FOREIGN KEY (`lu`) REFERENCES `estudiante` (`lu`),
  ADD CONSTRAINT `estudiantec_ibfk_2` FOREIGN KEY (`idCohorte`) REFERENCES `cohorte` (`idCohorte`),
  ADD CONSTRAINT `estudiantec_ibfk_3` FOREIGN KEY (`idCondC`) REFERENCES `concursado` (`idCondC`),
  ADD CONSTRAINT `estudiantec_ibfk_4` FOREIGN KEY (`idCondE`) REFERENCES `condestudiante` (`idCondE`),
  ADD CONSTRAINT `estudiantec_ibfk_5` FOREIGN KEY (`idEstadoTPF`) REFERENCES `estadotpf` (`idEstadoTPF`),
  ADD CONSTRAINT `estudiantec_ibfk_6` FOREIGN KEY (`idUsuarioAlta`) REFERENCES `usuario` (`idUsuario`),
  ADD CONSTRAINT `estudiantec_ibfk_7` FOREIGN KEY (`idUsuarioMod`) REFERENCES `usuario` (`idUsuario`);

--
-- Filtros para la tabla `localidad`
--
ALTER TABLE `localidad`
  ADD CONSTRAINT `Localidad_ibfk_1` FOREIGN KEY (`idPais`) REFERENCES `pais` (`idPais`),
  ADD CONSTRAINT `Localidad_ibfk_2` FOREIGN KEY (`idProvincia`) REFERENCES `provincias` (`idProvincias`);

--
-- Filtros para la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD CONSTRAINT `Usuario_ibfk_1` FOREIGN KEY (`idTipoUsuario`) REFERENCES `tipousuario` (`idTipoUsuario`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
