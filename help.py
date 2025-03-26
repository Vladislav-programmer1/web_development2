import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("name", type=str)

    parser.parse_args()
    global_init(parser.name)

    session = db_session.create_session()
    query = session.query(User.id).filter(User.address == "module_1",
                                          User.speciality.notlike("engineer"),
                                          User.position.notlike("engineer"))
    print(*query, sep="\n")


if __name__ == "__main__":
    main()