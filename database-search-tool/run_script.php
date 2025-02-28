
<link rel="stylesheet" type="text/css" href="styles.css">
<?php
    $num1 = $_POST['num1'];
    $operation = $_POST['operation'];
    $operation2 = $_POST['operation2'];
    $search_type = $_POST['search_type'];
    $tables = $_POST['tables'];
    
    $command = "python3 script.py $operation $operation2 $search_type $tables $num1 ";
    $output = shell_exec($command);
    echo $output;
?>
<br>
<div class="back-button">
    <form>
  <input type="hidden" name="previous_page" value="<?php echo $_SERVER['REQUEST_URI']; ?>">
  <a href="#" onclick="history.back()">Back</a>
</form>
</div>
