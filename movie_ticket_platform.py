print("welcome to ticket booking platform")
movies=["salaar", "mandadi", "pushpa", "radheshyam"]
seats=[50,50,50,50]
tickets_price=[200,100,150,180]
customer_details=[]
booking_history=[]
while True:
  print("1. Admin")
  print("2. user")
  print("3. exit")
  user_option=int(input("enter your choice: "))
  if user_option==1:
    admin_username=input("enter admin username: ")
    admin_password=input("enter admin password: ")
    if admin_username=='admin' and admin_password=='admin@47':
      while True:
        print("1.add a movie")
        print("2.remove a movie")
        print("3.add seats")
        print("4.view sales report")
        print("5.view booking history")
        print("6.exit")
        admin_choice=int(input("enter you choice: "))
        if admin_choice<=6 and admin_choice>0:
          if admin_choice==1:
            new_movie_name=input("enter the movie name: ")
            movies.append(new_movie_name)
            seats.append(50)
            tickets_price.append(150)
          elif admin_choice==2:
            remove_movie=input("enter the movie name want to remove: ")
            if remove_movie in movies:
              movie_index=movies.index(remove_movie)
              movies.pop(movie_index)
              seats.pop(movie_index)
              tickets_price.pop(movie_index)
            else:
              print("movie not found")
          elif admin_choice==3:
            movie_to_add_seats=input("enter the movie name: ")
            add_seats=int(input("enter how many seats need to added: "))
            if movie_to_add_seats in movies:
              movie_index=movies.index(movie_to_add_seats)
              seats[movie_index]=seats[movie_index]+add_seats
              print("seats added")
            else:
              print("movie not found")
          elif admin_choice==4:
            if len(booking_history)==0:
              print("booking history is empty")
            else:
              admin_sales_report=0
              for i in movies:
                admin_movie_wise_sales=0
                for j in booking_history:
                  if i==j[0]:
                    admin_sales_report=admin_sales_report+j[1]
                    admin_movie_wise_sales=admin_movie_wise_sales+j[1]
                    print(f"sales for {i} is {admin_movie_wise_sales}")
              print(f"total tickets sold: {admin_sales_report}")
          elif admin_choice == 5:
            if len(booking_history) == 0:
              print("booking history is empty")
            else:
              print("===== Booking History =====")
              for i in range(len(booking_history)):
                print(f"Movie: {booking_history[i][0]} | Tickets: {booking_history[i][1]}")
                print(f"customer name:{customer_details[i][0]} | customer_number:{customer_details[i][1]}")
          elif admin_choice==6:
            print("see you later")
            break
    else:
      print("incorrect paword")
      break
  if user_option==2:
    while True:
      print("="*20)
      print("1.Book tickets for a movie")
      print("2.Avaliable Seats")
      print("3.booking hitory")
      print("4.Exit")
      option=int(input("Enter the option: "))
      print("="*20)
      if option<=4 and option>0:
        if option==1:
          for i in range(len(movies)):
            print(f"{i+1} {movies[i]}")
          movie_option=int(input("Enter the movie choice: "))
          if movie_option<=len(movies) and movie_option>0:
            ticket_quantity=int(input("enter how many tickets you want: "))
            if ticket_quantity<=seats[movie_option-1] and ticket_quantity>0:
              customer_name=input("enter your name: ")
              customer_number=int(input("enter your mobile number: "))
              booking_history.append([movies[movie_option-1],ticket_quantity])
              seats[movie_option-1]=seats[movie_option-1]-ticket_quantity
              ticket_amount=tickets_price[movie_option-1]*ticket_quantity
              print(f"movie tickets successfully booked for {movies[movie_option-1]}")
              customer_details.append([customer_name,customer_number])
              print("Ticket price:", tickets_price[movie_option-1])
              print("Total tickets:", ticket_quantity)
              print("Total bill:", ticket_amount)
            else:
              print("Not enough seats avaliable.")
          else:
            print("invalid movie option")
        elif option==2:
          for i in range(len(movies)):
            print(f"Avaliable seats for {movies[i]}: {seats[i]}")
        elif option==3:
          if len(booking_history)==0:
            print("booking history is empty")
          else:
            sales_report=0
            for i in movies:
              movie_wise_booking=0
              for j in booking_history:
                if i==j[0]:
                  movie_wise_booking=movie_wise_booking+j[1]
                  print(f"Movie: {i} | Tickets: {j[1]}")
                  sales_report=sales_report+j[1]
                  print(f"movie wise tickets sold for {i} is {movie_wise_booking}")
            print("Total tickets sold:", sales_report)
        elif option==4:
          print("Thankyou for booking")
          break
    