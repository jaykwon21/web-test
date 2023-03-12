def calculate_grade(choice): # ,list):
    if choice == "grade":
        total_percent = 0
        grade = 0

        flag1 = True
        input1_list = []
        placeholder = 0
        category_input = input("type of category? (test, quiz, etc) ")
        percent_input1 = int(input("how much percent is this category worth? "))
        total_percent += percent_input1

        while flag1 == True:
            grade_input = input("enter grades. type 'stop' to stop. ")
            if grade_input == "stop":
                flag1 = False
            else:
                placeholder = int(grade_input)
                input1_list.append(placeholder)

        total1 = 0
        for i in input1_list:
            total1 = total1 + i
        print(category_input + " grade: " + str(total1/len(input1_list)))

        decimal_grade1 = ((total1/len(input1_list)) * ((percent_input1 / 100)))

        print("percentage: " + str(decimal_grade1))
        grade += decimal_grade1

        if total_percent > 100:
          print("can't exceed 100 percent.")




        flag2 = True
        input2_list = []
        placeholder = 0
        category_input2 = input("type of category? (test, quiz, etc) ")
        percent_input2 = int(input("how much percent is this category worth? "))
        total_percent += percent_input2
        while flag2 == True:
            grade_input2 = input("enter grades. type 'stop' to stop. ")
            if grade_input2 == "stop":
                flag2 = False
            else:
                placeholder = int(grade_input2)
                input2_list.append(placeholder)
        total2 = 0
        for i in input2_list:
            total2 = total2 + i
        print(category_input2 + " grade: " + str(total2/len(input2_list)))

        decimal_grade2 = ((total2/len(input2_list)) * ((percent_input2 / 100)))

        print("percentage: " + str(decimal_grade2))
        grade += decimal_grade2


        if total_percent > 100:
          print("can't exceed 100 percent.")




        final_exam_percentage = input("do you have a final exam percentage? ")
        if final_exam_percentage == "yes":
          flag3 = True
          input3_list = []
          placeholder = 0
          category_input3 = input("type of category? (test, quiz, etc) ")
          percent_input3 = int(input("how much percent is this category worth? "))
          total_percent += percent_input3

          while flag3 == True:
            grade_input3 = input("enter grades. type 'stop' to stop. ")
            if grade_input3 == "stop":
                flag3 = False
            else:
                placeholder = int(grade_input3)
                input3_list.append(placeholder)

          total3 = 0
          for i in input3_list:
              total3 = total3 + i
          print(category_input3 + " grade: " + str(total3/len(input3_list)))

          print(category_input3 + " grade: " + str(total3/len(input3_list)))

          decimal_grade3 = ((total3/len(input3_list)) * ((percent_input3 / 100)))

          print("percentage: " + str(decimal_grade3))
          grade += decimal_grade3


          if total_percent > 100:
            print("can't exceed 100 percent.")

          print("your current grade is: " + str(grade))
        
        else:
          print("your current grade is: " + str(grade))



          



calculate_grade("grade")