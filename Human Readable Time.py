def make_readable(seconds):
    minutes = seconds // 60
    hours = minutes //60
    return f"{hours:02d}:{minutes % 60 :02d}:{seconds % 60 :02d}"


print(make_readable(359999))