def is_email_valid(address):
    try:
        name,url=address.split('@')
        website_name,extension=url.split('.')
    except ValueError:
        return False
    checker_name=name.replace('-','').replace('_','')
    if checker_name.isalnum() is False:
        return False
    if website_name.isalnum() is False:
        return False
    if extension.isalpha():
        if len(extension)>3:
            return False
        else:
            pass
    else:
        return False
    return True


if __name__=='__main__':
    n=int(input().strip())
    emails=[input() for _ in range(n)]
    lister=list(filter(is_email_valid,emails))
    print(lister.sort())
