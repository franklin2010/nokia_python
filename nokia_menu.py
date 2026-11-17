print("\n1. Phone book\n2. Messages\n3. Chat\n4. Call register\n5. Tones\n6. Settings\n7. Call divert\n8. Music\n9. Games\n10. Calculator\n11. Reminders\n12. Clock\n13. Profiles\n14. Services\n15. SIM services")
choice = int(input("> "))
match choice:
    case 1:
        print("\n1. Search\n2. Service Nos.\n3. Add name\n4. Erase\n5. Edit\n6. Copy\n7. Assign tone\n8. Send b'card\n9. Options\n10. Speed dials\n11. Voice tags")
        choice = int(input("> "))
        match choice:
            case 1:
                print("Search selected")
            case 2:
                print("Service Nos. selected")
            case 3:
                print("Add name selected")
            case 4:
                print("Erase selected")
            case 5:
                print("Edit selected")
            case 6:
                print("Copy selected")
            case 7:
                print("Assign tone selected")
            case 8:
                print("Send b'card selected")
            case 9:
                print("\n1. Memory in use\n2. Type of view\n3. Memory status")
                choice = int(input("> "))
                match choice:
                    case 1:
                        print("Memory in use selected")
                    case 2:
                        print("Type of view selected")
                    case 3:
                        print("Memory status selected")
            case 10:
                print("Speed dials selected")
            case 11:
                print("Voice tags selected")
    case 2:
        print("\n1. Write messages\n2. Inbox\n3. Outbox\n4. Picture messages\n5. Templates\n6. Smileys\n7. Message settings\n8. Info service\n9. Voice mailbox number\n10. Service command editor")
        choice = int(input("> "))
        match choice:
            case 1:
                print("Write messages selected")
            case 2:
                print("Inbox selected")
            case 3:
                print("Outbox selected")
            case 4:
                print("Picture messages selected")
            case 5:
                print("Templates selected")
            case 6:
                print("Smileys selected")
            case 7:
                print("\n1. Set 1\n2. Common")
                choice = int(input("> "))
                match choice:
                    case 1:
                        print("\n1. Message centre number\n2. Messages sent as\n3. Message validity")
                        choice = int(input("> "))
                        match choice:
                            case 1:
                                print("Message centre number selected")
                            case 2:
                                print("Messages sent as selected")
                            case 3:
                                print("Message validity selected")
                    case 2:
                        print("\n1. Delivery reports\n2. Reply via same centre\n3. Character support")
                        choice = int(input("> "))
                        match choice:
                            case 1:
                                print("Delivery reports selected")
                            case 2:
                                print("Reply via same centre selected")
                            case 3:
                                print("Character support selected")
            case 8:
                print("Info service selected")
            case 9:
                print("Voice mailbox number selected")
            case 10:
                print("Service command editor selected")
    case 3:
        print("Chat selected")
    case 4:
        print("\n1. Missed calls\n2. Received calls\n3. Dialled numbers\n4. Erase recent call lists\n5. Show call duration\n6. Show call costs\n7. Call cost settings\n8. Prepaid credit")
        choice = int(input("> "))
        match choice:
            case 1:
                print("Missed calls selected")
            case 2:
                print("Received calls selected")
            case 3:
                print("Dialled numbers selected")
            case 4:
                print("Erase recent call lists selected")
            case 5:
                print("\n1. Last call duration\n2. All calls' duration\n3. Received calls' duration\n4. Dialled calls' duration\n5. Clear timers")
                choice = int(input("> "))
                match choice:
                    case 1:
                        print("Last call duration selected")
                    case 2:
                        print("All calls' duration selected")
                    case 3:
                        print("Received calls' duration selected")
                    case 4:
                        print("Dialled calls' duration selected")
                    case 5:
                        print("Clear timers selected")
            case 6:
                print("\n1. Last call cost\n2. All calls' cost\n3. Clear counters")
                choice = int(input("> "))
                match choice:
                    case 1:
                        print("Last call cost selected")
                    case 2:
                        print("All calls' cost selected")
                    case 3:
                        print("Clear counters selected")
            case 7:
                print("\n1. Call cost limit\n2. Show costs in")
                choice = int(input("> "))
                match choice:
                    case 1:
                        print("Call cost limit selected")
                    case 2:
                        print("Show costs in selected")
            case 8:
                print("Prepaid credit selected")
    case 5:
        print("\n1. Ringing tone\n2. Ringing volume\n3. Incoming call alert\n4. Message alert tone\n5. Keypad tones\n6. Warning tones\n7. Vibrating alert\n8. Screen saver")
        choice = int(input("> "))
        match choice:
            case 1:
                print("Ringing tone selected")
            case 2:
                print("Ringing volume selected")
            case 3:
                print("Incoming call alert selected")
            case 4:
                print("Message alert tone selected")
            case 5:
                print("Keypad tones selected")
            case 6:
                print("Warning tones selected")
            case 7:
                print("Vibrating alert selected")
            case 8:
                print("Screen saver selected")
    case 6:
        print("\n1. Call settings\n2. Phone settings\n3. Security settings\n4. Restore factory settings")
        choice = int(input("> "))
        match choice:
            case 1:
                print("\n1. Automatic redial\n2. Speed dialling\n3. Call waiting options\n4. Own number sending\n5. Phone line in use\n6. Automatic answer")
                choice = int(input("> "))
                match choice:
                    case 1:
                        print("Automatic redial selected")
                    case 2:
                        print("Speed dialling selected")
                    case 3:
                        print("Call waiting options selected")
                    case 4:
                        print("Own number sending selected")
                    case 5:
                        print("Phone line in use selected")
                    case 6:
                        print("Automatic answer selected")
            case 2:
                print("\n1. Language\n2. Cell info display\n3. Welcome note\n4. Network selection\n5. Confirm SIM service actions")
                choice = int(input("> "))
                match choice:
                    case 1:
                        print("Language selected")
                    case 2:
                        print("Cell info display selected")
                    case 3:
                        print("Welcome note selected")
                    case 4:
                        print("Network selection selected")
                    case 5:
                        print("Confirm SIM service actions selected")
            case 3:
                print("\n1. PIN code request\n2. Call barring service\n3. Fixed dialling\n4. Closed user group\n5. Security level\n6. Change access codes")
                choice = int(input("> "))
                match choice:
                    case 1:
                        print("PIN code request selected")
                    case 2:
                        print("Call barring service selected")
                    case 3:
                        print("Fixed dialling selected")
                    case 4:
                        print("Closed user group selected")
                    case 5:
                        print("Security level selected")
                    case 6:
                        print("Change access codes selected")
            case 4:
                print("Restore factory settings selected")
    case 7:
        print("Call divert selected")
    case 8:
        print("\n1. Music player\n2. Radio\n3. Recorder\n4. Track list")
        choice = int(input("> "))
        match choice:
            case 1:
                print("Music player selected")
            case 2:
                print("Radio selected")
            case 3:
                print("Recorder selected")
            case 4:
                print("Track list selected")
    case 9:
        print("Games selected")
    case 10:
        print("Calculator selected")
    case 11:
        print("Reminders selected")
    case 12:
        print("\n1. Alarm clock\n2. Clock settings\n3. Date setting\n4. Stopwatch\n5. Countdown timer\n6. Auto update of date and time")
        choice = int(input("> "))
        match choice:
            case 1:
                print("Alarm clock selected")
            case 2:
                print("Clock settings selected")
            case 3:
                print("Date setting selected")
            case 4:
                print("Stopwatch selected")
            case 5:
                print("Countdown timer selected")
            case 6:
                print("Auto update of date and time selected")
    case 13:
        print("Profiles selected")
    case 14:
        print("Services selected")
    case 15:
        print("SIM services selected")
