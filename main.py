
# 簡易消費紀錄統計系統

# 建立消費紀錄 list
expenses = []

while True:
    print("\n--- 消費紀錄統計系統 ---")
    print("1. 新增消費")
    print("2. 顯示消費明細")
    print("3. 顯示統計")
    print("4. 退出系統")
    print("------------------------")

    choice = input("請選擇功能: ")

    # 1. 新增消費
    if choice == "1":
        item = input("請輸入消費項目: ")

        while True:
            amount_input = input("請輸入金額: ")
            amount_input = amount_input.strip()

            # 檢查金額格式
            number_check = amount_input.replace(".", "", 1)

            if amount_input != "" and number_check != "" and number_check.isascii() and number_check.isdigit():

                amount = float(amount_input)

                if amount > 0:
                    # 建立一筆消費資料
                    expense = {
                        "項目": item,
                        "金額": amount
                    }

                    expenses.append(expense)

                    print("新增成功。")
                    break
                else:
                    print("請輸入大於 0 的有效金額。")

            else:
                print("請輸入大於 0 的數字，可包含小數點。")

    # 2. 顯示消費明細
    elif choice == "2":

        if len(expenses) == 0:
            print("目前沒有消費紀錄。")

        else:
            print("\n--- 消費明細 ---")
            print("編號  項目          金額")
            print("------------------------")

            for i, expense in enumerate(expenses, 1):
                print(f"{i:>4}  {expense['項目']:<10} {expense['金額']:>7.2f}")

    # 3. 顯示統計
    elif choice == "3":

        if len(expenses) == 0:
            print("目前沒有消費紀錄。")

        else:
            count = len(expenses)
            total = 0

            # 計算總金額
            for expense in expenses:
                total = total + expense["金額"]

            # 計算平均金額
            average = total / count

            print("\n--- 消費統計 ---")
            print(f"消費筆數: {count}")
            print(f"總金額: {total:.2f} 元")
            print(f"平均每筆金額: {average:.2f} 元")

            # 判斷消費提醒
            if total < 300:
                print("消費提醒: 消費不多")

            elif total < 500:
                print("消費提醒: 注意控制消費")

            else:
                print("消費提醒: 已達提醒門檻")

    # 4. 退出系統
    elif choice == "4":
        print("系統已退出。")
        break

    # 輸入錯誤
    else:
        print("選項錯誤，請重新選擇。")
