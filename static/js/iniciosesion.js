async function iniciarSesion() {
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    const response = await fetch("/auth/login", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email, contraseña: password })
    });

    const result = await response.json();

    if (response.ok) {
        // Redirigir a la ruta proporcionada por el servidor
        window.location.href = result.redireccion;
    } else {
        alert(result.mensaje || 'Error desconocido');
    }
}
