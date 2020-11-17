import redis

r = redis.Redis(host='172.26.0.104', port=6379,
                decode_responses=True)


def check_if_keys_exist():
    if r.exists("my_status") == False:
        r.set("my_status", "Good")

    if r.exists("my_description") == False:
        r.set("my_description",
              "My name is Maciej Fiedler. I am 15 years old and i like to programm. Besides programming I also do Ju-Jitsu, play Tennis andVideogames.")

    if r.exists("my_interests") == False:
        r.set("my_interests", "Backend Systems, Overwatch, Tennis, Physics, Ju-Jitsu, Design,Linux, Music, PCs, Minecraft, Learning Programming languages and technologies, New technologies(RISC-V, Quantum Computing etc.)")


check_if_keys_exist()
