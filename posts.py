def get_all_posts(conn):
    with conn.cursor() as cursor:
        cursor.execute('SELECT title, id, body FROM posts')
        # hakee kaikki
        posts = cursor.fetchall()
        # posts[0][1]
        return list(posts)

def get_newest_post(conn):
    with conn.cursor() as cursor:
        cursor.execute('SELECT id, title, body FROM posts ORDER BY id DESC LIMIT 1;')
        post = cursor.fetchone()
        return post

def get_newest_post_with_exc(conn):
    with conn.cursor() as cursor:
        cursor.execute('SELECT id, title, body FROM posts ORDER BY id DESC LIMIT 1;')
        post = cursor.fetchone()
        if post is None:
            raise Exception("Riviä ei löydy")
        return post




        
