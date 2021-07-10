<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width,initial-scale=1.0">
    <title>Login</title>
    <link rel="stylesheet" href="/public/css/screen.css">
    <link rel="stylesheet" href="/public/css/custom.css">
</head>

<body>
    <div class="container">
        <div id="header" class="span-24">
            <div class="span-12">
                <br>
                <h1>Retiws</h1>
            </div>

            <div class="span-12 last right-align">
                <br>
                <br>
                <a href="/">home</a> |
                <a href="/mentions">mentions</a>|
                <a href="/user">user</a> |
                <a href="/timeline">timeline</a> |
                <a href="/logout">logout</a>
            </div>
            <hr>
        </div>

        <div class="span-24">
            <div class="span-16">
                <div id="updateform" class="box">
                    <form action="/post" method="post">
                        what's on your mind?
                        <textarea name="content" id="" cols="70" rows="3"></textarea>
                        <br>
                        <input type="submit" value="Update">
                </div>

                <div id="posts" class="span-15">
                    <div class="post">
                        <strong>User</strong> hello world
                        <div class="date">2021年7月110日</div>
                    </div>
                </div>
            </div>
            <div class="span-7 last">
                <div class="box">
                    <h4>Follers:0</h4>
                    <ul class="user-list">
                        <li>user</li>
                    </ul>
                </div>

                <div class="box">
                    <h4>Follering:0</h4>
                    <ul class="user-list">
                        <li>user</li>
                    </ul>
                </div>
            </div>

        </div>

        <div class="span-24 last right-align">
            <hr> This site is by twiter by clone written by python and Redis.Copyright@ahao
        </div>
    </div>

</body>

</html>