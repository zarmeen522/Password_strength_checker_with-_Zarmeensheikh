import re
import streamlit as st

st.set_page_config(page_title="Password Strength Checker with Zarmeen Sheikh!" ,page_icon="", layout="centered",)

st.markdown("""
    <style>
        .stApp{
            background-image: url('https://i.pinimg.com/736x/a4/11/1b/a4111b7c99021dcd46a314c5c4216ecb.jpg');
            background-size: cover; 
            background-position: center; 
            background-repeat: no-repeat;   
            }
        .main{text-align: center;}      
            .stTextInput{width: 60%; height:30% ;!important; margin-left:25px; margin-right:10px; padding:8px; }
            .stButton button{ color:white; width: 30%; background-color: #4CAF50; margin-left:30px ; margin-right: 10px; display:block;  font-size: 18px;}
            .stButton button:hover{  color:white; background-color:#2E8B57 ;}
    </style>
""",
unsafe_allow_html=True)
st.title("Password Strength Checker! 🔐 ")
st.subheader("By Zarmeen Sheikh")
st.write("Enter your password below to check its strength!")

def check_password_strength(password):
    score=0
    feedback= []
    if len(password) >=9:
        score +=1
    else:
        feedback.append("❌Password should be at least 9 characters long!")
    if re.search(r"[A-Z]",password) and re.search(r"[a-z]", password):
            score +=1
    else:
         feedback.append("❌Password should contain **both uppercase(A-Z) and lowercase letters (a-z)**!")

    if re.search(r"\d", password):
         score +=1
    else:
         feedback.append("❌Password should contain **at least one digit(0-9)**!")

    if re.search(r"[!@#$%^&*()_+=-]",password):
              score +=1
    else:
          feedback.append("❌Password should contain at least one special character!")

    return score, feedback

password =st.text_input("Enter your password", type="password", help="Ensure your password is strong!", label_visibility="visible")



if st.button("Check Strength 🛡️"):
    if password:
        print(check_password_strength(password))
        score, feedback=check_password_strength(password)
        
        if  score == 4:
            st.success("**Strong Password!**✅ -Great job! 🧠")
        elif score == 3:
          st.info("**Medium Password!** ⚠️ -Consider adding more complexity.")
        elif score ==  2:
          st.warning("**Weak Password!** ❗ - Follow the suggestions to make it stronger 💡.")
        elif score ==1:
             st.warning("**Very Weak Password!**🚫")
        if feedback:
            with st.expander("Improve your password!"):
             for item in feedback:
                      st.write(item)
    




              
