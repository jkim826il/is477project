#### Postsecondary Schools (postsecondary_schools.csv)

- Every postsecondary school has a name
- Every postsecondary school has a unique "UNITID"
- Several postsecondary schools (11) are missing "STREET" Addresses. Those that are missing are labeled with an "M"
- A few postsecondary schools (4) are missing "STFIP", "CNTY", "NMCNTY", and "LOCALE". They are marked with a "N". They are also missing many other values.
- There are (297) schools missing "CBSA". These schools are also missing "NMCBSA", "CSA", and "NMCSA". Their "CBSATYPE" is set to 0.
- There are several postsecondary schools with suspect "STREET" addresses (other than the ones that are missing). The University of Montevallo as a street address of "Station 6001," which is not its actual street address, as an example. Reid State Technical College has its street address as "100 and Hwy 83," which sounds like an intersection, not its actual address.
- Schools with a "N" in their "CBSA" likely means that the postsecondary institution is not located within a CBSA. As an example, the University of West Alabama is located in Livingston, AL. Sumter County, which contains Livingston, is not in a CBSA.

#### Public Schools (public_schools.csv)

- Suffers from similar issues as Postsecondary Schools

#### Census Data

- Does not appear to have missing values. I will do a more detailed check before merging the datasets.