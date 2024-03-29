def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            dividend = my_list_1[i]
            divisor = my_list_2[i]
            result.append(dividend / divisor)
        except (IndexError, TypeError):
            if i >= len(my_list_1) or i >= len(my_list_2):
                print("out of range")
            else:
                print("wrong type")
            result.append(0)
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        finally:
            pass
    return result
