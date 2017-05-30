import read

#def remove_subdomains(s):
#    s = str(s).split(".")[-2:]
#    return ".".join(s)

if __name__ == "__main__":
    data = read.load_data()
#    data["url_main_domain"] = data["url"].apply(remove_subdomains)
    domains = data["url"].value_counts()
    count = 0
    for name, row in domains.items():
        count += 1
        print("{0}: {1}".format(name, row))
        if count == 100:
            break
