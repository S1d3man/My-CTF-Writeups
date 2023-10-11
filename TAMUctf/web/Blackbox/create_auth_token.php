<?php
const SECRET_KEY = 'JYOFGX6w5ylmYXyHuMM2Rm7neHXLrBd2V0f5No3NlP8';
function generate_token(array $data) {
  $b64json = base64_encode(json_encode($data));
  $hmac = hash('md5', SECRET_KEY . $b64json);

  return $b64json . '.' . $hmac;
}
$data = array('username'=>'admin', 'user_key'=>'26ceb685f46e6d22', 'admin'=>true);
print(generate_token($data));

