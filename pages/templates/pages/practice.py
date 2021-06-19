# def about(request):
#     data = " "
#     with open('pages/templates/pages/about.txt') as f:
#         data = f.read()
#     file_data = data
#     return render(request, 'pages/about.html', {'file_data': file_data})

def about(files):
    data = " "
    with open(files, 'r') as f:
        data = f.read()
    return data

print(about("about.txt"))

