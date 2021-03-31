<?php
class R {
  public $str;
  public $next;

  public function __construct($str, $next) {
    $this->str = $str;
    $this->next= $next;
  }
}

$dict = [
  "k" => [["ക", 1], ["ഖ", 1]],
  "m" => [["മ", 1], ["ം", 0]]
];

$input = "kamalam";

$ch = "";
$pos = 0;

$partial_result = [];
$result = [];
$consonant = false;
$lastI = 0;

$i = 0;
$rid = 0;
while($i < strlen($input)) {
  $ch .= $input[$i];
  echo $ch;

  if (isset($dict[$ch])) {
    if (empty($result)) {
      foreach($dict[$ch] as $ml) {
        $ml_str = $dict[$ch][0];
        $partial_result[$rid] = new R($ml_str, null);
        $rid++;
      }
    } else {
      foreach(end($result) as $rID => $r) {
        foreach($dict[$ch] as $ml) {
          $ml_str .= $v . $ml[0];
        }
        $partial_result[$rID] = new R($ml_str, null);
      }
    }

    echo "Match found for $ch.\n";

    $i++;
  } else {
    if (empty($partial_result)) {
      echo "No match for $ch.\n";
      $i++;
    } else {
      foreach ($partial_result as $rID => $pr) {
        if (isset($result[$rID])) {
          $result[$rID] .= 
        }
      }
      $partial_result = [];
    }
    $ch = "";
  }
}

print_r($result);
