import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Tasty Treats", layout="centered")
# a is a key inside st.session_state
if "a" not in st.session_state:               #session_state is a method store and rememeber values across interactions 
    st.session_state.a= False

if not st.session_state.a:
    st.title("🍽️ Welcome to Tasty Treats!")
    st.subheader("Delicious food delivered fast and fresh.")
    col1,col2,col3=  st.columns([1,2,1])
    with col2:
       st.image(r"C:\Users\AKSHAYA\Downloads\premium_photo-1661883237884-263e8de8869b.jpg",width=700)
       if st.button("Start Ordering"):
              st.session_state.a= True
 
  
 

# Stop app if exit clicked

              
              
# Main app(after button click)
if st.session_state.a:
    with st.sidebar:
        menu=option_menu(
            menu_title=" 🍔 Tasty Treats",
            options=["Home","Menu","Cats","Orders","About"],
            icons=["house","list","cart","clock","info-circle"],
            default_index=0
            
        )
    if menu == "Home":
       

            # Home Page Title and Subtitle
      st.title("🍴 Welcome to Tasty Treats!")
      st.subheader("Satisfy your cravings with just a few clicks.")
      st.image(r"C:\Users\AKSHAYA\Downloads\download.jpg",width=500)


  
# Intro Text
      st.markdown("""
Welcome to **Tasty Treats**, your one-stop food ordering app.  
Enjoy a wide selection of meals delivered right to your doorstep.  

---

### 👇 Why Choose Us?

- 🍲 Fresh & hot meals prepared on order  
- 🚴 Fast delivery within your area  
- 🎉 Exciting daily offers & discounts  
- 📱 Easy online ordering interface  
- 💬 Live order tracking and support  

---

### 🔔 Start Your Order Now!
Use the sidebar to:
- Explore the Menu
- Place Your Order
- View Order History
- Learn About Us
- Contact Support
""")
    if menu=="Menu":

        st.title("🍽️ Our Menu")
        st.markdown("## Welcome to Tasty Treats Menu Page!")
        st.write("Below are some delicious items you can order:")
        

# Initialize cart if not exists

# First time: cart_items is missing → if condition is True → create it.

# After that: cart_items is already created → if condition is False → skip.
        if "cart_items" not in st.session_state:   #cart item st.session state illana if true aagi oru empty list create pannum
            st.session_state.cart_items = []

# Item 1
        st.image(r"C:\Users\AKSHAYA\Downloads\images.jpg", width=300)
        st.subheader("🍔 Cheesy Burger")
        st.write("Price: ₹120")
        # If you have multiple widgets of the same type (like multiple st.number_inputs or st.text_inputs), you must set a key, or Streamlit will throw an error like:
        qty1 = st.number_input("Enter quantity for Cheesy Burger", min_value=1, max_value=10, key="burger_qty")  #burger_qty is my variable 
        if st.button("Add Cheesy Burger to Cart"):
                # append() is a built-in Python list method.
                st.session_state.cart_items.append({"name": "Cheesy Burger", "price": 120, "qty": qty1})
                st.success(f"{qty1} Cheesy Burger(s) added to cart.")

        st.markdown("---")

# Item 2
        st.image(r"C:\Users\AKSHAYA\Downloads\download (1).jpg", width=300)
        st.subheader("🍕 Margherita Pizza")
        st.write("Price: ₹180")
        qty2 = st.number_input("Enter quantity for Pizza", min_value=1, max_value=10, key="pizza_qty")
        if st.button("Add Pizza to Cart"):
             st.session_state.cart_items.append({"name": "Pizza", "price": 180, "qty": qty2})
             st.success(f"{qty2} Pizza(s) added to cart.")
             

        st.markdown("---")

# Item 3
        st.image("https://media.istockphoto.com/id/1292637257/photo/veg-hakka-noodles-a-popular-oriental-dish-made-with-noodles-and-vegetables-served-over-a.jpg?s=612x612&w=0&k=20&c=ckgGtleqsGxEMEW0ZlOR9eM8ii_R3A1apAMo8xa2Cr4=", width=300)
        st.subheader("🍜 Veg Noodles")
        st.write("Price: ₹100")
        qty3 = st.number_input("Enter quantity for Noodles", min_value=1, max_value=10, key="noodles_qty")
        if st.button("Add Noodles to Cart"):
                st.session_state.cart_items.append({"name": "Veg Noodles", "price": 100, "qty": qty3})
                st.success(f"{qty3} Noodle(s) added to cart.")

        st.markdown("---")

        st.info("🎉 Today's Offer: Get free delivery on orders over ₹300!")
        
    if menu=="Cats": 
        st.title("🛒 Your Cart")

# get is not a variable — it is a method (function) used to safely access data from a dictionary-like object (st.session_state).

# "cart_items" is the key where your list of ordered items is stored.
        cart = st.session_state.get("cart_items", [])

        if cart:
          total = 0
          for item in cart:
               item_total = item["qty"] * item["price"]
               total += item_total
               st.write(f"- {item['qty']} × {item['name']} = ₹{item_total}")

               st.markdown("---")
 
          if total >= 300:
                st.success("🎉 Congratulations! You get FREE delivery on orders over ₹300.")
                delivery = 0
          else:
             delivery = 30
             st.warning("🚚 ₹30 delivery charge (order below ₹300)")

          grand_total = total + delivery
          st.markdown(f"### 🧾 Total Bill: ₹{grand_total}")
        else:
          st.info("Your cart is currently empty.")


    if menu=="Orders":
      
        st.title("📦 Your Orders")

# Simulate a simple order confirmation
        if "cart_items" in st.session_state and st.session_state.cart_items:
             st.success("✅ Your recent order has been placed successfully!")

             st.markdown("### 🗒️ Order Details:")
             total = 0
             for item in st.session_state.cart_items:
                item_total = item["price"] * item["qty"]
                total += item_total
                st.write(f"- {item['qty']} × {item['name']} = ₹{item_total}")
    
                st.markdown(f"**Total Paid:** ₹{total}")
    
                st.info("📅 Expected Delivery: Within 30 minutes")
        else:
           st.warning("You haven't placed any orders yet.")
           
        if st.button("🚪 Exit App"):
           st.success("Thank you for using Tasty Treats! 👋")
           for key in st.session_state.keys():
                 del st.session_state[key]
                 st.stop()  # This ends the script

     
  
    if menu=="About":
      

              st.title("ℹ️ About Tasty Treats")

              st.markdown("""
Welcome to **Tasty Treats**, your favorite online food ordering app!  
We deliver delicious, freshly prepared food right to your doorstep — fast, hot, and tasty.  

---

### 🚀 Features:
- 🧾 Simple and clean ordering experience  
- 🛍️ Real-time cart and order tracking  
- 💳 Secure and easy payments  
- 🤝 Friendly customer support  

---

### 👨‍🍳 Built by:
- **Developer**: Akshaya  
- **Version**: 1.0  
- **Email**: [tastytreats@example.com](mailto:tastytreats@example.com)

📍 Based in Madurai, Tamil Nadu
""")

