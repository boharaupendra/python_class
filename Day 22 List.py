# 9. remove() - removes the value from the list if available otherwise will raise ValueError
national_parks = ["Bara-Parsa", "Koshi", "Shey-Phoksundo", "Shivapuri", "Sagarmatha"]
print("remove()")
print("Before:", national_parks)
national_parks.remove("Koshi")
print("After:", national_parks)
print("")

# if not available
# national_parks.remove("Kanchanjunga")
# will raise ValueError: list.remove(x): x not in list

# 10. reverse()
name_list = ["Bill", "Joseph", "Hari", "Narayan", "Misha", "Perisha"]
print("reverse()")
print("Before:", name_list)
name_list.reverse()
print("After:", name_list)
print("")

# 11. sort()
odd_list = [1, 3, 5, 7, 9]
even_list = [2, 4, 6, 8, 10]
random_list = [1, 33, 2, 12, 53, 54, 3, 166, 222, 32, 4, 123]

print("sort()")
print("Before ODD:", odd_list)
print("Before EVEN:", even_list)
print("Before RANDOM:", random_list)
print("")

odd_list.sort(reverse=False)
even_list.sort(reverse=False)
random_list.sort(reverse=False)
print("sort() ODD:", odd_list)
print("sort() EVEN:", even_list)
print("sort() RANDOM:", random_list)
print("")

print("flag reverse=True")
odd_list.sort(reverse=True)
even_list.sort(reverse=True)
random_list.sort(reverse=True)
print("sort(reverse=True) ODD:", odd_list)
print("sort(reverse=True) EVEN:", even_list)
print("sort(reverse=True) RANDOM:", random_list)

