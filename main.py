from rules import risk_simulation
import matplotlib.pyplot as plt

def get_input(prompt, min_val=0, max_val=100):
    while True:
        try:
            value = float(input(f"{prompt} ({min_val}-{max_val}): "))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"❌ Введіть значення в межах {min_val}-{max_val}.")
        except ValueError:
            print("❌ Некоректне значення. Спробуйте ще раз.")

def main():
    print("\n🔹 Розширена система оцінки ризиків у проектах 🔹\n")

    # Введення даних
    budget_value = get_input("Введіть рівень бюджету")
    deadline_value = get_input("Введіть рівень дедлайну")
    complexity_value = get_input("Введіть рівень складності")
    team_exp_value = get_input("Введіть досвід команди")
    uncertainty_value = get_input("Введіть рівень невизначеності")

    # Передача значень у нечітку систему
    risk_simulation.input['budget'] = budget_value
    risk_simulation.input['deadline'] = deadline_value
    risk_simulation.input['complexity'] = complexity_value
    risk_simulation.input['team_experience'] = team_exp_value
    risk_simulation.input['uncertainty'] = uncertainty_value

    # Обчислення ризику
    risk_simulation.compute()
    risk_level = risk_simulation.output['risk']

    # Виведення результату
    print(f"\n📌 Рівень ризику проекту: {risk_level:.2f} / 100")

    if risk_level < 20:
        print("✅ Ризик дуже низький. Успіх проєкту майже гарантований.")
    elif risk_level < 40:
        print("🟢 Ризик низький. Є мінімальні загрози.")
    elif risk_level < 60:
        print("🟡 Ризик середній. Варто бути уважним.")
    elif risk_level < 80:
        print("🔴 Ризик високий. Варто вжити заходів.")
    else:
        print("❌ Ризик дуже високий! Велика ймовірність проблем у проєкті.")

    # Візуалізація
    fig, ax = plt.subplots()
    ax.bar(["Risk Level"], [risk_level], color=['red' if risk_level > 80 else 'orange' if risk_level > 60 else 'yellow' if risk_level > 40 else 'green'])
    ax.set_ylim([0, 100])
    ax.set_ylabel("Рівень ризику (%)")
    ax.set_title("Візуалізація ризику проєкту")
    plt.show()

if __name__ == "__main__":
    main()



