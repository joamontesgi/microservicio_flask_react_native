import React, { useState, useEffect } from 'react';
import { View, Text } from 'react-native';
import axios from 'axios';

const Usuarios = () => {
    const [usuarios, setUsuarios] = useState([]);

    useEffect(() => {
        const obtenerUsuarios = async () => {
            try {
                const response = await axios.get('http://192.168.0.12:5000/usuarios');
                setUsuarios(response.data);
            } catch (error) {
                console.error('Error al obtener usuarios:', error);
            }
        };
        obtenerUsuarios();
    }, []);

    return (
        <View>
            <Text>Listado de Usuarios:</Text>
            {usuarios.map((item) => (
                <View key={item[0]}>
                    <Text>{`Nombre: ${item[1]}, Edad: ${item[2]}`}</Text>
                </View>
            ))}
        </View>
    );
};

export default Usuarios;
