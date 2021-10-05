def read_input():
    n_integers = int(input())
    integer_list = []
    for i in range(n_integers):
        integer_list.append(int(input()))
    return n_integers, integer_list

def solve_supermajority():
    list_size, list = read_input()
    majority_element = list[0]
    counter = 1
    for element in list[1:]:
        if counter == 0:
            counter = 1
            majority_element = element
        else:
            if element == majority_element:
                counter += 1
            else:
                counter -= 1
    final_count = 0
    for element in list[0:]:
        if element == majority_element:
            final_count += 1
    print(final_count > (2/3 * list_size))

solve_supermajority()