from django.http import HttpResponse

def page(request, page_num):
    if page_num == 1:
        prev_page = ""
        next_page = "/page/2"
    elif page_num == 5:
        prev_page = "/page/4"
        next_page = ""
    else:
        prev_page = f"/page/{page_num - 1}"
        next_page = f"/page/{page_num + 1}"

    html_content = f"""
    <html>
    <head>
        <title>Page {page_num}</title>
    </head>
    <body>
        <h1>This is page {page_num}</h1>
        <a href="{prev_page}">Previous</a>
        <a href="{next_page}">Next</a>
    </body>
    </html>
    """

    return HttpResponse(html_content)







