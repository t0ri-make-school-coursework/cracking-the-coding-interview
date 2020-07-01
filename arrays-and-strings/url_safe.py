## 1.3 Replace Spaces with "%20"
def replace_spaces(url):
    url = url.split()
    return '%20'.join(url)


if __name__ == "__main__":
    print(replace_spaces('make me url safe'))
