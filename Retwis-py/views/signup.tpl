<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width,initial-scale=1.0">
    <title>Signup</title>
</head>

<body>
    <h2>Retwis</h2>
    <hr>
    <form action="/signup" method="POST">
        用户名:
        <input type="text" name="username" id=""> 密码:
        <input type="text" name="password" id="">
        <button type="submit">注册</button>
    </form>
    <form action="/login" method="POST">
        用户名:
        <input type="text" name="username" id=""> 密码:
        <input type="text" name="password" id="">
        <button type="submit">登录</button>
    </form>
</body>

</html>