class MdSource:
    def __init__(self, title, link, code):
        self.title = title
        self.link = link
        self.code = code

    def get_md_title(self):
        return "## " + self.title.split(". ")[1].strip("\n")

    def get_md_link(self):
        title = self.title.split(". ")[1].strip("\n")
        lnk_tale = self.link.split("/")[-2]
        return f"+ [{title}](#{lnk_tale})"

    def get_md_code(self):
        return f"```python\n{self.code}\n```\n"

    def get_md_task(self):
        return f"\n{self.get_md_title()}\n\n{self.link}\n\n{self.get_md_code()}"


def read_txt():
    with open("in.txt") as f:
        data = f.readlines()
    res = [data[0], data[1].strip("\n"), "".join(map(lambda x: x[8::], data[6::]))]
    return res


def read_md(filename):
    with open(f"{filename}", "r") as f:
        data = f.read()
    return data


def prepare_data_to_write(md_obj, data):
    links, tasks = '', ''
    if len(data) != 0:
        links, tasks = data.split("<!---->\n")

    links += md_obj.get_md_link()
    tasks += md_obj.get_md_task()
    tasks.strip('\n')

    return [links, tasks]


def write_to_file(filename, data):
    header = f"# {filename.split('.')[0].upper()}\n\n"
    with open(f"{filename}", "w") as f:
        if header not in data[0]:
            f.write(header)
        f.write(f"{data[0]}")
        f.write("\n<!---->\n")
        f.write(data[1])


def main():
    md = MdSource(*read_txt())
    s = read_md('lists.md')
    s = prepare_data_to_write(md, s)
    write_to_file('lists.md', s)


if __name__ == "__main__":
    main()
