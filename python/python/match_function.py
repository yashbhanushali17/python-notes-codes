def match_status(status):
    match status:
        case 200:
            return "pass "
        case 404:
            return "link broken"
        case  300:
            return "unavailable"
        case _:
            return "noneeeee!!!"
print(match_status(4657))