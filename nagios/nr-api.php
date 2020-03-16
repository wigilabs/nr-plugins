<?php
$fil = fopen ("/usr/local/nagios/var/status.dat", "r");
$labels=array();
        while ($item = fgets($fil))
             {
                $labels[] = $item;
             }
$enterprise = fopen("enterprise.txt","r");
$e=array();
        while ($i = fgets($enterprise))
             {
                $e[] = $i;
             }
$burn=0;
//Json
$data= '
     {
     "eventType":"NagiosReport",
     "'.substr($labels[111],21).'":"'.substr($labels[139],15).'",
     "LastCheckCurrentLoad":"'.substr($labels[143],12).'",
     "LastOkCurrentLoad":"'.substr($labels[135],13).'",
     "'.substr($labels[167],21).'":"'.substr($labels[195],15).'",
     "LastCheckCurrentUsers":"'.substr($labels[199],12).'",
     "LastOkCurrentUsers":"'.substr($labels[191],13).'",
     "'.substr($labels[223],21).'":"'.substr($labels[251],15).'",
     "LastCheckHTTP":"'.substr($labels[255],12).'",
     "LastOkHTTP":"'.substr($labels[247],13).'",
     "'.substr($labels[279],21).'":"'.substr($labels[307],15).'",
     "LastCheckPING":"'.substr($labels[311],12).'",
     "LastOkPING":"'.substr($labels[303],13).'",
     "'.substr($labels[335],21).'":"'.substr($labels[363],15).'",
     "LastCheckRootPartition":"'.substr($labels[367],12).'",
     "LastOkRootPartition":"'.substr($labels[359],13).'",
     "'.substr($labels[391],21).'":"'.substr($labels[419],15).'",
     "LastCheckSSH":"'.substr($labels[423],12).'",
     "LastOkSSH":"'.substr($labels[415],13).'",
     "'.substr($labels[447],21).'":"'.substr($labels[475],15).'",
     "LastCheckSwap":"'.substr($labels[479],12).'",
     "LastOkSwap":"'.substr($labels[471],13).'",
     "'.substr($labels[503],21).'":"'.substr($labels[531],15).'",
     "LastCheckTotalProcess":"'.substr($labels[535],12).'",
     "LastOkTotalProcess":"'.substr($labels[527],13).'"
        }
         ';
echo $data;
//$client_n=$e[0];
//$host="<DB_HOST>";
//$user="<USER>";
//$password="<PASSWORD>";
//$dbname="LIGHTNING_TEAM";
//$dbconnection=mysqli_connect($host,$user,$password,$dbname);
//$register = mysqli_query($dbconnection,"INSERT INTO TASKS(SEQ, MONITOR, CLIENT_NAME, DATA_STREAM, TIME_EVENT) VALUES(0, 'nagios', '$client_n', '$data', NOW());");
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL,"http://64.227.31.194:25612/nagios/Nagios;".$data);
curl_setopt($ch, CURLOPT_POST, 1);
//curl_setopt($ch, CURLOPT_POSTFIELDS,
//            "postvar1=value1&postvar2=value2&postvar3=value3");
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
$server_output = curl_exec($ch);
curl_close ($ch);
?>
