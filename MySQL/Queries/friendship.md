# MySQL Queries

SELECT *
FROM friendships;

SELECT *
FROM users;

SELECT users.id, users.first_name, users.last_name, friendships.friend_id, user2.first_name as friend_first_name, user2.last_name as friend_last_name
FROM users
LEFT JOIN friendships ON friendships.user_id = users.id
LEFT JOIN users as user2 ON friendships.friend_id = user2.id;
