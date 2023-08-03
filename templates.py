def set_template(args):
    if args.template is None:
        return

    elif args.template.startswith('crawling'):
        args.id = "id"
        args.pw = "password"
        args.home_url = "https://member.newhosting.ssem.or.kr/dggb/mber/mberLogin/mberLogin.do?baseInfo=AkIceGbFU5Idy%2BRY55KdK0ueNP6Yn7reO1jUHhwrsLM%3D&afterUrl=daehyun.sen.es.kr"

        args.theme = "공지사항"
        args.letter_link = "https://daehyun.sen.es.kr/66653/subMenu.do"
        args.notice_link = "https://daehyun.sen.es.kr/66652/subMenu.do"
        args.bob_link = "https://daehyun.sen.es.kr/66654/subMenu.do"

        args.file_type = "json"