from templates import set_template
import argparse

parser = argparse.ArgumentParser(description='RecPlay')

# template #
parser.add_argument('--template', type=str, default='None')

# session #
parser.add_argument('--id', type=str, default=None)
parser.add_argument('--pw', type=str, default=None)
parser.add_argument('--home_url', type=str, default=None)

# theme #
parser.add_argument('--theme', type=str, default='가정통신문',choices=['가정통신문','공지사항','학교급식'])

# link #
parser.add_argument('--letter_link', type=str, default=None)
parser.add_argument('--notice_link', type=str, default=None)
parser.add_argument('--bob_link', type=str, default=None)

# parsing #
parser.add_argument('--start_page', type=int, default=3)
parser.add_argument('--end_page', type=int, default=12)

parser.add_argument('--first_button', type=int, default=1)
parser.add_argument('--last_button', type=int, default=14)

parser.add_argument('--prev_button', type=int, default=2)
parser.add_argument('--next_button', type=int, default=13)

# save #
parser.add_argument('--save_path', type=str, default='data')
parser.add_argument('--file_type', type=str, default='csv')

# args = parser.parse_args(args=[])
args = parser.parse_args()
set_template(args)