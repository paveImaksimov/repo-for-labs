# TODO Найдите количество книг, которое можно разместить на дискете
disk = 1.44
size_simv = 4
count_of_page = 100
count_of_list = 50
count_of_simv = 25
disk_in_baits = disk * (1024 ** 2)
size_of_book = size_simv * count_of_simv * count_of_list * count_of_page
print("Количество книг, помещающихся на дискету:", int(disk_in_baits/size_of_book))
