def show_welcome():
  print("\n💰 WELCOME TO BUDGET TRACKER 💰")
  print("-" * 40)

def get_budget_status(budget, spent):
  remaining = budget - spent
  percentage = (spent / budget) * 100
  print(f"\nBudget: ${budget: .2f}")
  print(f"Spent: ${spent: .2f}")
  print(f"Remaining: ${remaining: .2f} ({100 - percentage: .1f}% left)")
  if remaining > budget * 0.5:
    print("✓ Status: Good!")
  elif remaining > 0:
    print("⚠ Status: Be careful!")
  else:
    print("❌ Status: Over budget!")
  return remaining

def can_buy(item_price,remaining):
  if item_price > 0 and item_price <= remaining:
    return True
  else:
    return False

def calculate_discount(price,discount_percent):
  discount = price * (discount_percent / 100)
  final_pricec = price - discount
  print(f"original price: ${price: .2f}")
  print(f"discount: {discount_percent}% off (${discount: .2f})")
  print(f"final price: ${final_pricec: .2f}")
  return final_pricec
def main():
  show_welcome()
  budget = float(input("enter your weekly budget: $"))
  total_spent = 0.0
  purchase_count = 0
  keep_going = True
  while keep_going:
    remaining = get_budget_status(budget, total_spent)
    print("\n" + "=" * 40)
    print("Menu:")
    print("1. Add a purchase")
    print("2. Buy multiple items")
    print("3. Calculate discount")
    print("4. Quit")
    print("=" * 40)

    choice = input("Enter your choice(1-4): ")
    if choice == "1":
      print("\n ------ Add a purchase -----")
      item_name = input("Enter item name: ")
      item_price = float(input("item pirce: $"))
      if can_buy(item_price,remaining):
        confirm = input(f"Buy {item_name} for ${item_price:.2f}? (yes/no): ")
        if confirm.lower() == "yes":
          total_spent += item_price
          purchase_count += 1
          print(f"✓ Purchased {item_name}!")
        else:
          print("❌ Purchase canceled.")
      else:
        shortage = item_price - remaining
        print(f"❌ Can't afford! Need ${shortage:.2f} more.")
    elif choice == "2":
      print("\n ------ Buy multiple items -----")
      print("enter items (type done to finish)")
      item_count = 0
      cart_total = 0.0
      while True:
        item =input(f"\nitem #{item_count + 1} name (or 'done'):")
        if item.lower() == "done":
          break
        if item.strip() == "":
          print("Error: Item name cannot be empty.")
          continue
        price = float(input(f"price for {item}: $"))
        if price <= 0:
          print("Error: Price must be greater than zero.")
          continue
        cart_total += price
        item_count += 1
        print(f"✓ Added {item}")
      if item_count == 0:
        print("no items added.")
      else:
        print(f"\n📦 Cart: {item_count} items, Total: ${cart_total:.2f}")

        affordable = cart_total <= remaining
        reasonable = cart_total <= remaining * 0.7
        if affordable and reasonable:
          print("✓ Safe to buy!")
        elif affordable and not reasonable:
          print("⚠ You can afford it,but it's tight.")
        else:
          print("❌ Not affordable.")
        if affordable:
          confirm = input("proceed with purchase? (yes/no): ")
          if confirm.lower() == "yes":
            total_spent += cart_total
            purchase_count += item_count
            print("✓ Purchase complete!")
    elif choice == "3":
      print("\n ------ Calculate discount -----")
      original = float(input("original price: $"))
      discount = float(input("discount %: "))
      if discount < 0 or discount > 100:
        print("Invalid discount.")
        continue
      final = calculate_discount(original,discount)
      if can_buy(final,remaining):
        print("✓ You can afford this!")
      else:
        print("❌ still too expensive")
    elif choice == "4":

      keep_going = False
      print("\n Exiting...")
    else:
      print("❌ Invalid choice!")
  print("\n" + "=" * 40)
  print("final summary")
  print("=" * 40)
  print(f"Budget: ${budget:.2f}")
  print(f"Spent: ${total_spent:.2f}")
  print(f"Remaining: ${budget - total_spent:.2f}")
  print(f"Total Purchases: {purchase_count}")
  print("\n shopping behavior:")
  levels = ["Saver 💎", "Moderate 👍", "Spender 💸"]
  spent_percentage = (total_spent / budget) * 100
  if spent_percentage < 50:
    level_index = 0
  elif spent_percentage < 80:
    level_index = 1
  else:
    level_index = 2 # Changed from 0 to 2 for 'Spender 💸'
  for i in range(len(levels)):
    if i == level_index:
      print(f"✓ {levels[i]}")
    else:
      print(f"✗ {levels[i]}")
  print("\n" + "=" * 40)
  print("Thanks for using Budget Tacker!😊")
if __name__ == "__main__":
  main()