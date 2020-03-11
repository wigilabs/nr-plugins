<?php
$fil = fopen ("/usr/local/nagios/var/status.dat", "r");
$labels=array();
        while ($item = fgets($fil))
             {
                $labels[] = $item;
             }

$burn=0;
//Json
 echo '
     {
     "eventType":"NagiosReport",
     "'.substr($labels[111],21).'":"'.substr($labels[139],15).'",
     "DateCurrentLoad":"'.substr($labels[159],13).'",
     "LastCheckCurrentLoad":"'.substr($labels[143],12).'",
     "LastOkCurrentLoad":"'.substr($labels[135],13).'",
     "'.substr($labels[167],21).'":"'.substr($labels[195],15).'",
     "DateCurrentUsers":"'.substr($labels[215],13).'",
     "LastCheckCurrentUsers":"'.substr($labels[199],12).'",
     "LastOkCurrentUsers":"'.substr($labels[191],13).'",
     "'.substr($labels[223],21).'":"'.substr($labels[251],15).'",
     "DateHTTP":"'.substr($labels[271],13).'",
     "LastCheckHTTP":"'.substr($labels[255],12).'",
     "LastOkHTTP":"'.substr($labels[247],13).'",
     "'.substr($labels[279],21).'":"'.substr($labels[307],15).'",
     "DatePING":"'.substr($labels[327],13).'",
     "LastCheckPING":"'.substr($labels[311],12).'",
     "LastOkPING":"'.substr($labels[303],13).'",
     "'.substr($labels[335],21).'":"'.substr($labels[363],15).'",
     "DateRootPartition":"'.substr($labels[383],13).'",
     "LastCheckRootPartition":"'.substr($labels[367],12).'",
     "LastOkRootPartition":"'.substr($labels[359],13).'",
     "'.substr($labels[391],21).'":"'.substr($labels[419],15).'",
     "DateSSH":"'.substr($labels[439],13).'",
     "LastCheckSSH":"'.substr($labels[423],12).'",
     "LastOkSSH":"'.substr($labels[415],13).'",
     "'.substr($labels[447],21).'":"'.substr($labels[475],15).'",
     "DateSwap":"'.substr($labels[495],13).'",
     "LastCheckSwap":"'.substr($labels[479],12).'",
     "LastOkSwap":"'.substr($labels[471],13).'",
     "'.substr($labels[503],21).'":"'.substr($labels[531],15).'",
     "DateTotalProcess":"'.substr($labels[551],13).'",
     "LastCheckTotalProcess":"'.substr($labels[535],12).'",
     "LastOkTotalProcess":"'.substr($labels[527],13).'"
        }
         ';
?>
