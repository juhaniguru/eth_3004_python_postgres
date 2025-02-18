
from db import connect
from posts import get_all_posts, get_newest_post, get_newest_post_with_exc


if __name__ == '__main__':
    while True:
        _choice = input("Mitä haluat tehdä (0=lopeta, 1=listaa, 2=uusin postaus)? ")
        if _choice == "0":
            break
        elif _choice == "1":
            with connect() as conn:
                posts = get_all_posts(conn)
                print(posts)
                for post in posts:
                    print(post)
        elif _choice == "2":
            with connect() as conn:
                post = get_newest_post(conn)
                if post is None:
                    print("Riviä ei löydy")
                else:
                    print(post)
        elif _choice == "3":
            with connect() as conn:
                try:
                    post = get_newest_post_with_exc()
                except Exception as e:
                    print(e)

                