def main():
    animals = ["cow", "duck", "pig", "horse", "sheep"]
    sounds = ["moo", "quack", "oink", "neigh", "baa"]
    for i in range(5):
        print(lyrics(animals[i], sounds[i]))


def lyrics(animal, sound):
    s = f"Old MacDonald had a farm, ee-igh, ee-igh, oh!\n"
    s += f"And on that farm he had a {animal}, ee-igh, ee-igh, oh!\n"
    s += f"With a {sound}, {sound} here and a {sound}, {sound} there.\n"
    s += f"Here a {sound}, there a {sound}, everywhere a {sound}, {sound}.\n"
    s += f"Old MacDonald had a farm, ee-igh, ee-igh, oh!\n"
    return s


if __name__ == "__main__":
    main()
