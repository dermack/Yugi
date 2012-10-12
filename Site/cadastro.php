<?php
	$con = mysql_connect('localhost', 'root', 'root') or die('Não foi possível conectar');

	mysql_select_db("yugi", $con);
	
	if($_SERVER["REQUEST_METHOD"] == "POST") {
		$nome = $_POST["nome"];
		$username = $_POST["login"];
		$senha = $_POST["password"];
		$email = $_POST["email"];
	}
	
	$sql = "INSERT INTO user (nome, username, passwd, email) Values ('$nome', '$username', PASSWORD('$senha'), '$email')" 
    if (@mysql_query($sql)){
		echo "<p> Cadastro efetuado com sucesso </p>"
	} else {
		if(mysql_errno() == 1062) {
                echo $erros[mysql_errno()];
                exit;
        } else {        
                echo "Erro nao foi possivel efetuar o cadastro";
                exit;
        }   
	}	
    @mysql_close()
?>