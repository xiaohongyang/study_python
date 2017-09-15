import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
import django

django.setup()
'''
'''


def main():
    from blog.models import Blog
    f = open("other/oldblog.txt", mode="r")
    lines = f.readlines()
    for line in lines:
        title, content = line.split('****')
        try:
            Blog.objects.get_or_create(title=title,content=content)
        except Exception:
            print(Exception.__context__)
    f.close()

if __name__ == "__main__":
    main();
    print("done")