<link rel="stylesheet" type="text/css" href="styles.css">

<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Database Search Tool</title>

    <link rel="stylesheet" type="text/css" href="styles.css">





</head>

<div class="square-border">

    <body>

        <h1>Database Search Tool</h1>

        <?php

        $operation = isset($_POST['operation']) ? $_POST['operation'] : '';

        $operation2 = isset($_POST['operation2']) ? $_POST['operation2'] : '';

        $searchtype = isset($_POST['search_type']) ? $_POST['search_type'] : 'exact';

        $tables = isset($_POST['tables']) ? $_POST['tables'] : 'Persons';

        $num1 = isset($_POST['num1']) ? $_POST['num1'] : '';

        $command1 = "python3 get_columns.py Persons";

        $columns1_json = shell_exec($command1);

        $columns1 = json_decode($columns1_json, true);

        $command2 = "python3 get_columns.py Persons2";

        $columns2_json = shell_exec($command2);

        $columns2 = json_decode($columns2_json, true);

        ?>

        <form action="" method="post" autocomplete="on">



            <label for="num1">DB search:</label>

            <input type="text" class="my-textbox" id="num1" name="num1" value="<?php echo htmlspecialchars($num1); ?>"><br>

            <div class="wrapper">

                <label for="operation">Field name:</label>

                <select class="my-select" id="operation" name="operation" style="<?php echo ($tables === 'Persons2') ? 'display: none;' : 'display: block;'; ?>">

                    <?php

                    if ($columns1) {

                        foreach ($columns1 as $column) {

                            $selected = ($operation == $column) ? 'selected' : '';

                            echo "<option value='" . htmlspecialchars($column) . "' " . $selected . ">" . htmlspecialchars($column) . "</option>";

                        }

                    }

                    ?>

                </select>

                <select class="my-select2" id="operation2" name="operation2" style="<?php echo ($tables === 'Persons') ? 'display: none;' : 'display: block;'; ?>">

                    <?php

                    if ($columns2) {

                        foreach ($columns2 as $column) {

                            $selected = ($operation2 == $column) ? 'selected' : '';

                            echo "<option value='" . htmlspecialchars($column) . "' " . $selected . ">" . htmlspecialchars($column) . "</option>";

                        }

                    }

                    ?>

                </select>

            </div><br>

            <label for="search_type">Search type: </label>

            <input type="radio" id="EXACT" name="search_type" value="exact" <?php if ($searchtype == 'exact') echo 'checked'; ?>>

            <label for="exact">Exact</label>

            <input type="radio" id="LIKE" name="search_type" value="like" <?php if ($searchtype == 'like') echo 'checked'; ?>>

            <label for="like">Like</label><br>

            <label for="Database">Tables: </label>

            <input type="radio" name="tables" value="Persons" id="personsRadio" <?php if ($tables == 'Persons') echo 'checked'; ?>>Persons

            <input type="radio" name="tables" value="Persons2" id="persons2Radio" <?php if ($tables == 'Persons2') echo 'checked'; ?>>Persons2

            <script>

                function showSelectList(Value) {

                    const selectList1 = document.getElementById('operation');

                    const selectList2 = document.getElementById('operation2');

                    if (Value === 'Persons') {

                        selectList1.style.display = 'block';

                        selectList2.style.display = 'none';

                    } else if (Value === 'Persons2') {

                        selectList1.style.display = 'none';

                        selectList2.style.display = 'block';

                    }

                }

                document.getElementById('personsRadio').addEventListener('change', function() {

                    showSelectList('Persons');

                });

                document.getElementById('persons2Radio').addEventListener('change', function() {

                    showSelectList('Persons2');

                });

            </script>

            <br>

            <button type="submit" class="gobutton" style="vertical-align:middle"><span>Run DB Search</span></button>

        </form>

</div>

</div>

<div class="output-container">

    <?php

    if ($_SERVER['REQUEST_METHOD'] === 'POST') {

        $command = "python3 script.py " . escapeshellarg($operation) . " " . escapeshellarg($operation2) . " " . escapeshellarg($searchtype) . " " . escapeshellarg($tables) . " " . escapeshellarg($num1);

        $output = shell_exec($command);

        echo "<pre>" . htmlspecialchars($output) . "</pre>";

    }

    ?>

</div>



</body>

</html>
