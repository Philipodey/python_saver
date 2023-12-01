def nokia_function():
    print(""""
          ******************
          1. PhoneBook
          2. Messages
          3. Chats
          4. Call register
          5. Tones
          6. Settings
          7. Call divert
          8. Games
          9. Calculator
          10. Reminders
          11. Clock
          12. Profiles
          13. Sim services
          *****************
          
    """)

    nokia = str(input("Select an option: "))
    if nokia == '1':
        print(phone_book())
    elif nokia == '2':
        print(messages())
    elif nokia == '3':
        print(chats())
    elif nokia == '4':
        print(call_register())
    elif nokia == '5':
        print(tones())
    elif nokia == '6':
        print(settings())
    elif nokia == '7':
        print(call_divert())
    elif nokia == '8':
        print(games())
    elif nokia == '9':
        print(calculator())
    elif nokia == '10':
        print(reminders())
    elif nokia == '11':
        print(clock())
    elif nokia == '12':
        print(sim_services())
    else:
        print("Invalid input")
        nokia_function()


def phone_book():
    print(""""
                      ***************
                      1. Search
                      2. Service Nos
                      3. Add name
                      4. Erase
                      5. Edit
                      6. Assign
                      7. Send b' card
                      8. Options
                      9. speed dials
                      10. Voice tags
                      11. Back to menu
                      ***************
                      """)
    phone_book_input = str(input("Select an option: "))
    if phone_book_input == '1':
        print("search")
    elif phone_book_input == '2':
        print("Service Nos")
    elif phone_book_input == '3':
        print("Erase")
    elif phone_book_input == '4':
        print("Edit")
    elif phone_book_input == '5':
        print("Assign tone")
    elif phone_book_input == '6':
        print("Assign tone")
    elif phone_book_input == '7':
        print("Send b' card ")
    elif phone_book_input == '8':
        print("Options")
        print(""""
                  **********************
                  1. Type of view
                  2. Memory status
                  3. Back to phoneBook
                  4. Back to menu
                  *********************
        """)
        option_input = str(input("Select an option: "))
        if option_input == '1':
            print("Type of view")
        elif option_input == '2':
            print("Memory status")
        elif option_input == '3':
            print(phone_book())
        elif option_input == '4':
            print(nokia_function())
        else:
            print("Invalid input!")
            print(phone_book())
    elif phone_book_input == '9':
        print("Speed dials")
    elif phone_book_input == '10':
        print("Voice tags")
    elif phone_book_input == '11':
        print(nokia_function())
    else:
        print("Invalid input")
        print(nokia_function())


def messages():
    print("Messages")
    print("""
             ****************************
             1. Write messages
             2. Inbox
             3. Outbox
             4. Picture messages
             5. Templates
             6. Smileys
             7. Messages settings
             8. Info service
             9. Voice mailbox number
             10. Service command editor
             11. Back to menu
             ***************************
    """)
    message = str(input("Select an option: "))
    if message == '1':
        print("Write messages")
    elif message == '2':
        print("Inbox")
    elif message == '3':
        print("Outbox")
    elif message == '4':
        print("Picture messages")
    elif message == '5':
        print("Templates")
    elif message == '6':
        print("Smileys")
    elif message == '7':
        print("Message settings")
        print(""""
                  **********************
                  1. Set
                  2. Common
                  3. Back to messages
                  4. Back to main menu
                  *********************
        """)
        message_settings = input("Select an option: ")
        if message_settings == '1':
            print("Set")
            print("""
                     *************************
                     1. Message centre number
                     2. Messages sent as
                     3. Message validity
                     4. BacK to Messages
                     5. Back to main menu
                     ************************
            """)
            set_input = input("Select an option: ")
            if set_input == '1':
                print("Message centre number")
            elif set_input == '2':
                print("Messages sent as")
            elif set_input == '3':
                print("Message validity")
            elif set_input == '4':
                print(messages())
            elif set_input == '5':
                print(nokia_function())
            else:
                print("INVALID NUMBER")
                print(messages())

        elif message_settings == '2':
            print("Common")
            print(""""
                      *************************
                      1. Delivery
                      2. Reply via same centre
                      3. Character support
                      4. Back to messages
                      5. Back to main menu
                      **************************
            """)
            common = int(input("Select an option: "))
            if common == '1':
                print("Delivery")
            elif common == '2':
                print("Reply via same centre")
            elif common == '3':
                print("Character support")
            elif common == '4':
                print(messages())
            elif common == '5':
                print(nokia_function())
            else:
                print("INVALID INPUT")
                print(messages())

        elif message_settings == '3':
            print(messages())
        elif message_settings == '4':
            print(nokia_function())
        else:
            print("INVALID INPUT")
            print(messages())
    elif message == '8':
        print("Info service")
    elif message == '9':
        print("Voice mailbox number")
    elif message == '10':
        print("service command editor")
    elif message == '11':
        print(nokia_function())
    else:
        print("INVALID NUMBER")
        print(nokia_function())


def chats():
    print("Chats")
    print("""
              *****************
              1. Back to menu
              *****************
    """)
    chat = input("Enter option: ")
    if chat == '1':
        print(nokia_function())
    else:
        print("INVALID INPUT")
        print(nokia_function())


def call_register():
    print("Call register")
    print(""""
              **************************
              1. Missed calls
              2. Received calls
              3. Dialled numbers
              4. Erase Show call duration
              5. Show call duration
              6. Show call cost
              7. Call cost settings
              8. Prepaid credit
              9. Back to menu
              **************************
    """)
    call_register_input = input("Select an option: ")
    if call_register_input == '1':
        print("Missed calls")
    elif call_register_input == '2':
        print("Received calls")
    elif call_register_input == '3':
        print("Dialled numbers")
    elif call_register_input == '4':
        print("Erase Show call duration")
    elif call_register_input == '5':
        print("Show call duration")
        print("""
                 *************************
                  1. Last call duration
                  2. All calls' duration
                  3. Received calls' duration
                  4. Dialled calls' duration
                  5. Clear timer
                  6. Back to call register
                  7. Back to menu
                                
                 *************************
        """)
        show_call_duration = input("Select an option: ")
        if show_call_duration == '1':
            print("Last call duration")
        elif show_call_duration == '2':
            print("All calls' duration")
        elif show_call_duration == '3':
            print("Received calls' duration")
        elif show_call_duration == '4':
            print("Dialled calls' duration")
        elif show_call_duration == '5':
            print("Clear timer")
        elif show_call_duration == '6':
            print(call_register())
        elif show_call_duration == '7':
            print(nokia_function())
        else:
            print("INVALID NUMBER")
            print(call_register())

    elif call_register_input == '6':
        print("Show call costs")
        print(""""
                  **********************
                  1. Last call cost
                  2. All calls' cost
                  3. Clear counters
                  4. Back to call register
                  5. Back to main menu
                  **********************
        """)
        call_cost = input("Select an option: ")
        if call_cost == '1':
            print("Last call cost")
        elif call_cost == '2':
            print("All calls' cost")
        elif call_cost == '3':
            print("Back to call register")
        elif call_cost == '4':
            print(call_register())
        elif call_cost == '5':
            print(nokia_function())
        else:
            print("INVALID INPUT")
            print(call_register())

    elif call_register_input == '7':
        print("Call cost settings")
        print(""""
                  ************************
                  1. Call cost limit
                  2. Show costs in
                  3. Back to call register
                  4. Back to menu
                  ************************
        """)
        cost_settings = input("Select an option: ")
        if cost_settings == '1':
            print("Call cost limit")
        elif cost_settings == '2':
            print("Show costs in")
        elif cost_settings == '3':
            print(call_register())
        elif cost_settings == '4':
            print(nokia_function())
        else:
            print("INVALID INPUT")
            print(call_register())

    elif call_register_input == '8':
        print("Prepaid credit")
    elif call_register_input == '9':
        print(nokia_function())
    else:
        print("INVALID INPUT")
        print(nokia_function())


def tones():
    print("Tones")
    print(""""
              ***************************
              1. Ringing tone
              2. Ringing volume
              3. Incoming call divert
              4. Composer
              5. Messages alert tone
              6. Keypad tones
              7. Warning and game tones
              8. Vibrating alert
              9. Screen saver
              10. Back to menu
              ************************* 
    """)
    tone = input("Select an option: ")
    if tone == '1':
        print("Ringing tone")
    elif tone == '2':
        print("Ringing volume")
    elif tone == '3':
        print("Incoming call divert")
    elif tone == '4':
        print("Composer")
    elif tone == '5':
        print("Messages alert tone")
    elif tone == '6':
        print("Keypad tones")
    elif tone == '7':
        print("Warning and game tones")
    elif tone == '8':
        print("Vibrating alert")
    elif tone == '9':
        print("Screen saver")
    elif tone == '10':
        print(nokia_function())
    else:
        print("INVALID NUMBER")
        print(nokia_function())


def settings():
    print("Settings")
    print(""""
              *****************************
              1. Call settings
              2. Phone settings
              3. Security settings
              4. Restore factory settings
              5. Back to menu
              ******************************
    """)
    settings_input = input("Select an option: ")
    if settings_input == '1':
        print("Call settings")
        print("""
                *****************************
                 1. Automatic redial
                 2. Speed dailling
                 3. call waiting options
                 4. Own number sending
                 5. Phone line in use
                 6. Automatic answer
                 7. Back to settings
                 8. Back to menu
                *******************************
        """)
        call_setting = input("Select an option: ")
        if call_setting == '1':
            print("Automatic redial")
        elif call_setting == '2':
            print("Speed dailling")
        elif call_setting == '3':
            print("call waiting options")
        elif call_setting == '4':
            print("Own number sending")
        elif call_setting == '5':
            print("Phone line in use")
        elif call_setting == '6':
            print("Automatic answer")
        elif call_setting == '7':
            print("Back to settings")
        elif call_setting == '8':
            print(nokia_function())
        else:
            print("INVALID NUMBER")
            print(nokia_function())
    elif settings_input == '2':
        print("Phone settings")
        print("""
                  *******************************
                  1. Language
                  2. Cell info display
                  3. Welcome note
                  4. Network selection
                  5. Lights
                  6. Confirm SIM service answer
                  7. Back to settings
                  8. back to menu
                  *******************************
        """)
        phone_settings = input("Select an option: ")
        if phone_settings == '1':
            print("Language")
        elif phone_settings == '2':
            print("Cell info display")
        elif phone_settings == '3':
            print("Welcome note")
        elif phone_settings == '4':
            print("Network selection")
        elif phone_settings == '5':
            print("Lights")
        elif phone_settings == '6':
            print("Confirm SIM service answer")
        elif phone_settings == '7':
            print(settings())
        elif phone_settings == '8':
            print(nokia_function())
        else:
            print("INVALID INPUT")
            print(settings())

    elif settings_input == '3':
        print("Security settings")

    elif settings_input == '4':
        print("Restore factory settings")
    elif settings_input == '5':
        print(nokia_function())
    else:
        print("INVALID INPUT")
        print(nokia_function())


def call_divert():
    print("Call divert")
    print("""
              ****************
              1. Back to menu
              ****************
    """)
    divert = input("Select an option: ")
    if divert == '1':
        print(nokia_function())
    else:
        print("INVALID INPUT")
        print(nokia_function())


def games():
    print("Games")
    print("""
             ****************
             1. Back to menu
             ***************
    """)
    game = input("Select an option: ")
    if game == '1':
        print(nokia_function())
    else:
        print("INVALID INPUT")
        print(nokia_function())


def calculator():
    print("Calculator")
    print("""
             ****************
             1. Back to menu
             ****************
    """)
    calculator_input = input("Select an option: ")
    if calculator_input == '1':
        print(nokia_function())
    else:
        print("INVALID INPUT")
        print(nokia_function())


def reminders():
    print("Reminders")
    print("""
             *****************
             1. Back to menu
             *****************
    """)
    reminder = input("Select an option: ")
    if reminder == '1':
        print(nokia_function())
    else:
        print("INVALID INPUT")
        print(nokia_function())


def clock():
    print("Clock")
    print("""
             *******************************
             1. Alarm clock
             2. Clock settings
             3. Date settings
             4. Stopwatch
             5. Countdown timer
             6. Auto update of date and time
             7. Back to menu 
             *********************************
    """)
    clock_input = input("Select an option: ")
    if clock_input == '1':
        print("Alarm clock")
    elif clock_input == '2':
        print("Clock settings")
    elif clock_input == '3':
        print("Date settings")
    elif clock_input == '4':
        print("Stopwatch")
    elif clock_input == '5':
        print("Countdown timer")
    elif clock_input == '6':
        print("Auto update of date and time")
    elif clock_input == '7':
        print(nokia_function())
    else:
        print("INVALID INPUT")
        print(nokia_function())


def profiles():
    print("Profiles")
    print("""
            ****************
            1. Back to menu
            ****************    
     """)
    profile = input("Select option: ")
    if profile == '1':
        print(nokia_function())
    else:
        print("INVALID INPUT")
        print(nokia_function())


def sim_services():
    print("SIM services")
    print("""
               ****************
               1. Back to menu
               ****************
    """)
    sim_service = input("Select option: ")
    if sim_service == '1':
        print(nokia_function())
    else:
        print("INVALID INPUT")
        print(nokia_function())


print(nokia_function())
