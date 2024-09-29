import csv

def calculate_bmi(weight, height):
    """
    計算BMI值
    :param weight: 體重（公斤）
    :param height: 身高（公尺）
    :return: BMI值
    """
    if height <= 0:
        raise ValueError("身高必須大於0")
    return weight / (height ** 2)

def main():
    try:
        weight = float(input("請輸入體重（公斤）："))
        height = float(input("請輸入身高（公尺）："))
        bmi = calculate_bmi(weight, height)
        print(f"你的BMI值是：{bmi:.2f}")
        
        if bmi < 18.5:
            category = "體重過輕"
        elif 18.5 <= bmi < 24.9:
            category = "體重正常"
        elif 25 <= bmi < 29.9:
            category = "體重過重"
        else:
            category = "肥胖"
        
        print(category)
        
        # 將結果寫入CSV檔案
        with open('bmi_results.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["體重(公斤)", "身高(公尺)", "BMI值", "分類"])
            writer.writerow([weight, height, f"{bmi:.2f}", category])
        
        print("結果已寫入bmi_results.csv")
        
    except ValueError as e:
        print(f"輸入錯誤：{e}")

if __name__ == "__main__":
    main()