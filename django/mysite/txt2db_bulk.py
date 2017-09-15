import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE","mysite.settings")
django.setup()

def main():
    from blog.models import Blog
    f = open("other/oldblog.txt", mode="r")
    lines = f.readlines()
    datas = []

    pks = 47
    for line in lines:
        pks +=1
        title, content = line.split('****')
        datas.append(Blog(title=title, content=content))

    f.close();

    if len(datas) > 0:
        Blog.objects.bulk_create(datas)


if __name__ == "__main__":
    main()
    print("done...")


