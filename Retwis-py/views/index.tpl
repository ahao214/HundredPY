% include('shared/header.tpl',username=username)

<div class="span-24">
    <div class="span-16">
        <div id="updateform" class="box">
            <form action="/post" method="post">
                {{username}},what's on your mind?
                <textarea name="content" id="" cols="70" rows="3"></textarea>
                <br>
                <input type="submit" value="Update">
        </div>

        <div id="posts" class="span-15">
            % for id,post in posts.items():
            <div class="post">
                <strong>{{post['username']}}</strong> {{post['content']}}
                <div class="date">{{post['posttime']}}</div>
            </div>
            % end
        </div>
    </div>
    <div class="span-7 last">
        <div class="box">
            <h4>Followers:{{followers_num}}</h4>
            <ul class="user-list">
                % for user in followers:
                <li>{{user}}</li>
                % end
            </ul>
        </div>

        <div class="box">
            <h4>Following:{{following_num}}</h4>
            <ul class="user-list">
                % for user in following:
                <li>{{user}}</li>
                % end
            </ul>
        </div>
    </div>

</div>

% include('shared/footer.tpl')