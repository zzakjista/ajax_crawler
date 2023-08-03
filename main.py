from session import Session
from parsing import parser
from options import args
from preprocessing import preprocessor
from save import save_file


def main(args):
    session = Session(args)
    session.go_main()
    parser_obj = parser(args,session)
    data = parser_obj.crawl_one_theme()
    preprocessor_obj = preprocessor(args,data)
    df = preprocessor_obj.preprocess()
    save_file_obj = save_file(args,df)
    save_file_obj.save()


if __name__ == "__main__":
    main(args)

