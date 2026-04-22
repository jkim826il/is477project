import hashlib

with open("./raw_data/public_schools.csv", "r") as f3:
    bytes = f3.read().encode()
    hash = hashlib.sha256(bytes).hexdigest()
    print("SHA-256 Hash for public_schools.csv:", hash)
    assert(str(hash) == "b28adb4dea2dd84c0d3becd965b720785fc24b40faf1f2bbbb180e9b94b98ad8")
    print("SHA-256 Hash for public_schools.csv Matches.")

with open("./raw_data/postsecondary_schools.csv", "r") as f4:
    bytes = f4.read().encode()
    hash = hashlib.sha256(bytes).hexdigest()
    print("\nSHA-256 Hash for postsecondary_schools.csv:", hash)
    assert(str(hash) == "07130531f7585aac23421385c3e68173dd85cf446ff0e2b011f9d5dd3a27c572")
    print("SHA-256 Hash for postsecondary_schools.csv Matches.")

with open("./raw_data/census_data.csv", "r") as f5:
    bytes = f5.read().encode()
    hash = hashlib.sha256(bytes).hexdigest()
    print("\nSHA-256 Hash for census_data.csv:", hash)
    assert(str(hash) == "a39674919e049878153a6ad4f03a22f2398acd334b98e97654ccf6bada5ac700")
    print("SHA-256 Hash for census_data.csv Matches.")
    