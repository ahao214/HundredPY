<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width,initial-scale=1.0">
    <title>Sign Up</title>
</head>

<body>
    <h2>Sign Up</h2>
    <hr>
    <form action="/signup" method="post">
        手机号：
        <input type="text" name="mobile" id="mobile"> 验证码：
        <input type="text" name="code" id="code">
        <input type="button" value="获取验证码" id="getcode">
        <input type="submit" value="注册">
    </form>
</body>

</html>