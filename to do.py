while True:
    user_action = input("Ekle, göster, düzenle, tamamla veya çık yazın: ").strip().lower()

    if user_action == "ekle":
        todo = input("Bir yapılacak iş girin: ") + "\n"
        
        try:
            with open("todos.txt", "a") as file:  # Append modunda açma
                file.write(todo)
        except FileNotFoundError:
            with open("todos.txt", "w") as file:  # Dosya yoksa oluştur
                file.write(todo)

    elif user_action == "göster":
        try:
            with open("todos.txt", "r") as file:
                todos = file.readlines()

            if todos:
                for index, item in enumerate(todos):
                    item = item.strip("\n")
                    print(f"{index + 1} - {item}")
            else:
                print("Yapılacak iş bulunamadı.")
        except FileNotFoundError:
            print("Henüz bir yapılacak listesi oluşturulmamış.")

    elif user_action == "düzenle":
        try:
            with open("todos.txt", "r") as file:
                todos = file.readlines()

            number = int(input("Düzenlenecek işin numarasını girin: ")) - 1

            if 0 <= number < len(todos):
                new_todo = input("Yeni yapılacak işi girin: ")
                todos[number] = new_todo + "\n"
                
                with open("todos.txt", "w") as file:
                    file.writelines(todos)
            else:
                print("Geçersiz numara.")
        except (FileNotFoundError, ValueError):
            print("Dosya bulunamadı ya da geçersiz bir giriş yapıldı.")

    elif user_action == "tamamla":
        try:
            with open("todos.txt", "r") as file:
                todos = file.readlines()

            number = int(input("Tamamlanan işin numarasını girin: ")) - 1

            if 0 <= number < len(todos):
                removed_todo = todos.pop(number).strip("\n")
                
                with open("todos.txt", "w") as file:
                    file.writelines(todos)
                    
                print(f"Yapılacak iş -{removed_todo}- listeden kaldırıldı.")
            else:
                print("Geçersiz numara.")
        except (FileNotFoundError, ValueError):
            print("Dosya bulunamadı ya da geçersiz bir giriş yapıldı.")

    elif user_action == "çık":
        print("Programdan çıkılıyor...")
        break

    else:
        print("Geçersiz işlem. Lütfen tekrar deneyin.")