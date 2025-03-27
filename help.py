import argparse
from sqlalchemy import select, func


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("name", type=str)

    parser.parse_args()
    global_init(parser.name)

    session = db_session.create_session()
    selected_colonists = session.query(User).filter(User.address == "module_1", User.age < 21)

    for colonist in selected_colonists:
        colonist.address = "module_3"
    session.commit()


if __name__ == "__main__":
    main()