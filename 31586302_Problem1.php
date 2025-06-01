<?php
try {
    $mongo = new MongoDB\Driver\Manager("mongodb://localhost:27017");
    $sortField = ($_GET['sort'] === 'Symbol') ? 'Symbol' : 'Index';
    $query = new MongoDB\Driver\Query([], ['sort' => [$sortField => 1]]);
    $cursor = $mongo->executeQuery('stock_data.most_active', $query);
    
    echo '
    <html>
    <head>
        <title>Homework 9</title>
    </head>
    <body>
        <table border=1>
            <thead>
                <tr>
                    <th><a href="?sort=Index">Index</a></th>
                    <th><a href="?sort=Symbol">Symbol</a></th>
                    <th>Name</th>
                    <th>Price</th>
                    <th>Change</th>
                    <th>Volume</th>
                </tr>
            </thead>
            <tbody>';
    
    foreach ($cursor as $document) {
        echo '<tr>
                <td>'.htmlspecialchars($document->Index).'</td>
                <td>'.htmlspecialchars($document->Symbol).'</td>
                <td>'.htmlspecialchars($document->Name).'</td>
                <td>'.htmlspecialchars($document->Price).'</td>
                <td>'.htmlspecialchars($document->Change).'</td>
                <td>'.htmlspecialchars($document->Volume).'</td>
              </tr>';
    }
    
    echo '</tbody></table></body></html>';
    
} catch (Exception $e) {
    die('Error: ' . $e->getMessage());
}
?>
