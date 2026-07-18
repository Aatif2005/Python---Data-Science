from pprint import pprint

with open("initialdata.txt", encoding='utf-8') as f:
    data = f.read()

chunks = data.split("\n\n")
chunks = [c for c in chunks if len(c) > 3]

def parse_chunk(chunk):
    chunk = chunk.strip()
    sep_chunk = chunk.split('\n')
    username = sep_chunk[0]
    no_of_posts = int(sep_chunk[1].split("post")[0].replace(",", "").strip())

    follower_str = sep_chunk[2].split("followers")[0].replace(",", "").strip()
    if "K" in sep_chunk[2]:
        no_of_followers = int(float(follower_str.replace("K", "")) * 1000)
    elif "M" in sep_chunk[2]:
        no_of_followers = int(float(follower_str.replace("M", "")) * 1000000)
    else:
        no_of_followers = int(follower_str)

    following_str = sep_chunk[3].split("following")[0].replace(",", "").strip()
    if "K" in sep_chunk[3]:
        no_of_following = int(float(following_str.replace("K", "")) * 1000)
    elif "M" in sep_chunk[3]:
        no_of_following = int(float(following_str.replace("M", "")) * 1000000)
    else:
        no_of_following = int(following_str)

    name = sep_chunk[4]
    if len(sep_chunk) >= 6:
        type_of_page = sep_chunk[5]
        bio = "\n".join(sep_chunk[6:])
    else:
        type_of_page = "Unknown"
        bio = ""
    return {
        "username": username,
        "no_of_posts": no_of_posts,
        "no_of_followers": no_of_followers,
        "no_of_following": no_of_following,
        "name": name,
        "type_of_page": type_of_page,
        "bio": bio
    }

all_chunks = []
for chunk in chunks:
    parsed_chunk = parse_chunk(chunk)
    all_chunks.append(parsed_chunk)

'''max_followers = 0
for chunk in all_chunks:
    if chunk['no_of_followers'] > max_followers:
        max_followers = chunk['no_of_followers']
        chunk_with_max_followers = chunk

pprint(chunk_with_max_followers)'''

'''max_following = 0
for chunk in all_chunks:
    if chunk['no_of_following'] > max_following:
        max_followers = chunk['no_of_following']
        chunk_with_max_following = chunk

pprint(chunk_with_max_following)'''

categories = set()
for chunk in all_chunks:
    categories.add(chunk['type_of_page'])
pprint(categories)
print(categories, len(categories))