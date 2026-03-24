<?php
#https://www.fundaofwebit.com/post/how-to-create-password-hash-and-password-verify-in-php-mysql-with-example

if (!isset($_POST['email'], $_POST['password']) || 
    empty($_POST['email']) || 
    empty($_POST['password'])) {
    exit("Täida kõik väljad");
}

$email = $_POST['email'];
$password = $_POST['password'];

$paring = "SELECT password FROM users WHERE email='$email'";

$result = mysqli_query($yhendus, $paring);
$rida = mysqli_fetch_assoc($result);

if ($row && password_verify($password, $rida['password'])) {
    echo "OK";
    $_SESSION['email'] = $email;
    $_SESSION['role'] = $row['status']; // admin või user
} else {
    echo "Viga";
}

?>


#kontroll
<?php
session_start();

if (!isset($_SESSION['role']) || $_SESSION['role'] !== 'admin') {
    header("Location: login.php");
    exit;
}
?>




või 

<?php
session_start();

if (!isset($_SESSION['role'])) {
    header("Location: login.php");
    exit;
}
?>