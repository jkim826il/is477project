import hashlib

with open("./raw_data/public_schools.csv", "r") as f3:
    bytes = f3.read().encode()
    hash = hashlib.sha256(bytes).hexdigest()
    print("SHA-256 Hash for public_schools.csv:", hash)
    assert(str(hash) == "1d4227cd7f2c64c2187bd2664eba67aac070757aecf64a41d24a731a279a5a69")
    print("SHA-256 Hash for public_schools.csv Matches.")

with open("./raw_data/postsecondary_schools.csv", "r") as f4:
    bytes = f4.read().encode()
    hash = hashlib.sha256(bytes).hexdigest()
    print("\nSHA-256 Hash for postsecondary_schools.csv:", hash)
    assert(str(hash) == "4002cd2eb1483edf7507adc536c9f46cc79edbdd5b31fb012af922db9eaf0385")
    print("SHA-256 Hash for postsecondary_schools.csv Matches.")

with open("./raw_data/census_data.csv", "r") as f5:
    bytes = f5.read().encode()
    hash = hashlib.sha256(bytes).hexdigest()
    print("\nSHA-256 Hash for census_data.csv:", hash)
    assert(str(hash) == "a39674919e049878153a6ad4f03a22f2398acd334b98e97654ccf6bada5ac700")
    print("SHA-256 Hash for census_data.csv Matches.")
    