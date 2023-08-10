from tkinter import *

window = Tk()
window.title("Roman Numerals Convert to Decimal")
window.minsize(500, 500)

myText = Label(text="Enter the Roman Numeral")
myText.config(pady=10)
myText.pack()

roman_num = Entry(width=40)
roman_num.pack()
roman_dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}



def clickedBtn():
    roman_str = roman_num.get()
    if roman_str == "":
        labelText("fill in the blank!")
    elif len(roman_str) == 1:
        if roman_str not in roman_dic.keys():
            labelText("Enter suitable character!")
            return
        labelText(f"{roman_str} = {roman_dic.get(roman_str)}")
    else:
        sum_list = []
        for i in range(len(roman_str) - 1):
            if roman_str[i] not in roman_dic.keys() or roman_str[i+1] not in roman_dic.keys():
                labelText("Enter suitable character!")
                return

            if roman_str[i] == roman_str[i + 1]:
                sum_list.append(roman_dic.get(roman_str[i]))
                if i == len(roman_str) - 2:
                    sum_list.append(roman_dic.get(roman_str[len(roman_str) - 1]))
            else:
                if roman_dic.get(roman_str[i]) > roman_dic.get(roman_str[i + 1]):
                    sum_list.append(roman_dic.get(roman_str[i]))
                    if i == len(roman_str) - 2:
                        sum_list.append(roman_dic.get(roman_str[len(roman_str) - 1]))
                else:
                    sum_list.append(roman_dic.get(roman_str[i + 1]) - roman_dic.get(roman_str[i]))
                    i += 1
        decimal_sum = 0
        for list_index in range(len(sum_list) - 1):
            if sum_list[list_index] < sum_list[list_index + 1]:
                labelText(f"{roman_str} is Not valid!")
                return
            decimal_sum += sum_list[list_index]
            if list_index == len(sum_list) - 2:
                decimal_sum += sum_list[list_index + 1]

        if decimal_sum > 5000:
            labelText("Enter a valid Roman Numeral or Integer from 1 to 4.999")
        elif len(sum_list) == 1:
            labelText(f"{roman_str} = {sum_list[0]}")
        else:
            print(sum_list)
            labelText(f"{roman_str} = {decimal_sum}")


cal_btn = Button(text="calculate")
cal_btn.config(padx=10, bg="blue", fg="white", command=clickedBtn)
cal_btn.pack()

label = Label()


def labelText(text):
    label.config(text=text)
    label.pack()


mainloop()
