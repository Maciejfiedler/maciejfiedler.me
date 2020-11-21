import redis

r = redis.Redis(host='172.26.0.104', port=6379,
                decode_responses=True)


def check_if_keys_exist():
    if not r.exists("my_status"):
        r.set("my_status", "Good")

    if not r.exists("my_description"):
        r.set("my_description",
              "My name is Maciej Fiedler. I am 15 years old and i like to programm. Besides programming I also do Ju-Jitsu, play Tennis and Videogames.")

    if not r.exists("my_interests"):
        r.set("my_interests", "Backend Systems, Overwatch, Tennis, Physics, Ju-Jitsu, Design, Linux, Music, PCs, Minecraft, Learning Programming languages and technologies, New technologies(RISC-V, Quantum Computing etc.)")


check_if_keys_exist()
