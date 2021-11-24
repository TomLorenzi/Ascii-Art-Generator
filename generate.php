<?php
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    // Get file from form and upload it to server
    $file = $_FILES['file'];
    $upload_dir = '/var/www/thomasdl/ascii/';
    $upload_file = $upload_dir . basename($file['name']);
    if (move_uploaded_file($file['tmp_name'], $upload_file)) {
        //echo "File is valid, and was successfully uploaded.\n";
    } else {
        //echo "Possible file upload attack!\n";
    }
    
    $size = $_POST['size'];
    if (empty($size)) {
        $size = 250;
    }
    $test = shell_exec("python3 /var/www/thomasdl/ascii/main.py /var/www/thomasdl/ascii/{$file['name']} $size");
    header("Location: https://thomasdl.fr/ascii/result.txt");
    die();
}
?>