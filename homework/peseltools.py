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
    #pesel = 85051410071
    pesel = str(pesel)
    birth_year = pesel[0:2]
    birth_month = pesel[2:4]
    birth_day = pesel[4:6]

    MONTH_LEN = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    short_month = (birth_month == "04" or birth_month == "06" or birth_month == "09" or
                   birth_month == "11") and birth_day == "31"
    short_feb = birth_day == "29" or birth_day == "30" or birth_day == "31"

    if len(pesel) != 11:
        return False

    pesel_verification = 9 * int(pesel[0]) + 7 * int(pesel[1]) + 3 * int(pesel[2]) + 1 * int(pesel[3]) + \
                   9 * int(pesel[4]) + 7 * int(pesel[5]) + 3 * int(pesel[6]) + 1 * int(pesel[7]) + \
                   9 * int(pesel[8]) + 7 * int(pesel[9])

    pesel_verification = str(pesel_verification)

    if pesel_verification[2] != pesel[10]:
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


def extract_personal_data(pesel):
    """
    zwraca słownik o kluczach "birth_date": "data_ur" i "sex": "płeć" (male/female)
    jeśli do funkcji wrzucimy niepoprawny PESEL, powinna zwrócić wyjątek ValueError
    :param pesel:
    :return:
    """
    if (validate(pesel)) == False:
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
    weryfikuje czy jako numer PESEL wpisywane są cyfry
    Args:

    """
    number = None
    while number is None:
        try:
            number = int(input(prompt))
        except ValueError:
            print('PESEL może zawierać tylko cyfry.')
        return number