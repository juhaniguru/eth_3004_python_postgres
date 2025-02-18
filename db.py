# connect

import contextlib

import psycopg2





@contextlib.contextmanager
def connect():
    conn = None
    try:
        # HUOM: tässä tietokanta ja käyttäjä, jonka loimme aiemmin
        conn = psycopg2.connect("postgresql://blog_db_user:password@localhost/blog_db2")
        # yieldia ei käydä tässä läpi tarkemmin. Sekin opetellaan toisella opintojaksolla
        # tässä riittää, että ajattelet yieldia returnin kaltaisena (palauttaa tietokantayhteyden sinne, missä
        # connect-funktiota kutsutaan)
        yield conn
    finally:
        if conn is not None:
            # suljetaan tietokantayhteys
            conn.close()

















