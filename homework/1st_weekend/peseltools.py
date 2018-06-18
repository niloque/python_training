import calendar

def validate(pesel):

    """
    Checks if provided PESEL number is valid

    Args:
        pesel (string)
    Returns:
        if valid - True
        if not valid - Else
    """

    if len(pesel) != 11:
        return False

    pesel = str(pesel)
    birth_year = pesel[0:2]
    birth_month = pesel[2:4]
    birth_day = pesel[4:6]
    MONTH_LEN = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    check_digits = [9, 7, 3, 1, 9, 7, 3, 1, 9, 7]
    sum_check = 0
    for digit, value in enumerate(check_digits):
        sum_check += (int(pesel[digit])) * value
    sum_check = str(sum_check)

    if sum_check[2] != pesel[10]:
        return False

    if birth_month[0] == "0" or birth_month[0] == "1":
        full_year = 1900 + int(birth_year)
        if calendar.isleap(full_year):
            if birth_month == "02" and (int(birth_day) > 29 or int(birth_day) <= 0):
                return False
            elif birth_month != "02" and (MONTH_LEN[(int(birth_month) - 1)] < int(birth_day) or int(birth_day) <= 0):
                return False
        elif calendar.isleap(full_year) == False:
            if birth_month == "02" and (int(birth_day) > 28 or int(birth_day) <= 0):
                return False
            elif birth_month != "02" and (MONTH_LEN[(int(birth_month) - 1)] < int(birth_day) or int(birth_day) <= 0):
                return False

    elif birth_month[0] == "2" or birth_month[0] == "3":
        full_year = 2000 + int(birth_year)
        if calendar.isleap(full_year):
            if birth_month == "02" and (int(birth_day) > 29 or int(birth_day) <= 0):
                return False
            elif birth_month != "02" and (MONTH_LEN[(int(birth_month) - 1)] < int(birth_day) or int(birth_day) <= 0):
                return False
        elif calendar.isleap(full_year) == False:
            if birth_month == "02" and (int(birth_day) > 28 or int(birth_day) <= 0):
                return False
            elif birth_month != "02" and (MONTH_LEN[(int(birth_month) - 1)] < int(birth_day) or int(birth_day) <= 0):
                return False

    elif birth_month[0] == "4" or birth_month[0] == "5":
        full_year = 2100 + int(birth_year)
        if calendar.isleap(full_year):
            if birth_month == "02" and (int(birth_day) > 29 or int(birth_day) <= 0):
                return False
            elif birth_month != "02" and (MONTH_LEN[(int(birth_month) - 1)] < int(birth_day) or int(birth_day) <= 0):
                return False
        elif calendar.isleap(full_year) == False:
            if birth_month == "02" and (int(birth_day) > 28 or int(birth_day) <= 0):
                return False
            elif birth_month != "02" and (MONTH_LEN[(int(birth_month) - 1)] < int(birth_day) or int(birth_day) <= 0):
                return False

    elif birth_month[0] == "6" or birth_month[0] == "7":
        full_year = 2200 + int(birth_year)
        if calendar.isleap(full_year):
            if birth_month == "02" and (int(birth_day) > 29 or int(birth_day) <= 0):
                return False
            elif birth_month != "02" and (MONTH_LEN[(int(birth_month) - 1)] < int(birth_day) or int(birth_day) <= 0):
                return False
        elif calendar.isleap(full_year) == False:
            if birth_month == "02" and (int(birth_day) > 28 or int(birth_day) <= 0):
                return False
            elif birth_month != "02" and (MONTH_LEN[(int(birth_month) - 1)] < int(birth_day) or int(birth_day) <= 0):
                return False

    elif birth_month[0] == "8" or birth_month[0] == "9":
        full_year = 1800 + int(birth_year)
        if calendar.isleap(full_year):
            if birth_month == "02" and (int(birth_day) > 29 or int(birth_day) <= 0):
                return False
            elif birth_month != "02" and (MONTH_LEN[(int(birth_month) - 1)] < int(birth_day) or int(birth_day) <= 0):
                return False
        elif calendar.isleap(full_year) == False:
            if birth_month == "02" and (int(birth_day) > 28 or int(birth_day) <= 0):
                return False
            elif birth_month != "02" and (MONTH_LEN[(int(birth_month) - 1)] < int(birth_day) or int(birth_day) <= 0):
                return False
    return True

def extract_personal_data(pesel):
    """
    Displays dictionary with data stored in PESEL and informs if PESEL is invalid

    Args:
        pesel

    Returns:
        if valid - dictionary with keys: "birth_date" and "sex"
        if invalid - ValueError message
    """
    if validate(pesel) == False:
       raise ValueError("Numer PESEL jest niepoprawny.")

    pesel = str(pesel)
    birth_year = pesel[0:2]
    birth_month = pesel[2:4]
    birth_day = pesel[4:6]

    personal_info = {"birth_date": None, "sex": None}

    if birth_month[0] == "0" or birth_month[0] == "1":
        d_o_b = str(birth_day + "." + birth_month + "." + str(19) + birth_year)
        personal_info["birth_date"] = d_o_b
    elif birth_month[0] == "8" or birth_month[0] == "9":
        d_o_b = str(birth_day + "." + birth_month + "." + str(18) + birth_year)
        personal_info["birth_date"] = d_o_b
    elif birth_month[0] == "2" or birth_month[0] == "3":
        d_o_b = str(birth_day + "." + birth_month + "." + str(20) + birth_year)
        personal_info["birth_date"] = d_o_b
    elif birth_month[0] == "4" or birth_month[0] == "5":
        d_o_b = str(birth_day + "." + birth_month + "." + str(21) + birth_year)
        personal_info["birth_date"] = d_o_b
    elif birth_month[0] == "6" or birth_month[0] == "7":
        d_o_b = str(birth_day + "." + birth_month + "." + str(22) + birth_year)
        personal_info["birth_date"] = d_o_b

    if int(pesel[9]) % 2 == 0:
        personal_info["sex"] = "female"
    else:
        personal_info["sex"] = "male"
    return personal_info


def int_input(prompt):
    """
    Ensures that the input's type is integer.

    Args:
        prompt
    Returns:
        number - if int
        ValueError - if empty or string
    """
    number = None
    while number is None:
        try:
            number = int(input(prompt))
        except ValueError:
            print('PESEL może zawierać tylko cyfry.')
        return number