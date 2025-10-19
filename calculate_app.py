import streamlit as st

# عنوان الصفحة
st.title("🧮 الآلة الحاسبة البسيطة - Streamlit")

# إدخال الأرقام من المستخدم
num1 = st.number_input("ادخل الرقم الأول:", format="%.2f")
num2 = st.number_input("ادخل الرقم الثاني:", format="%.2f")

# اختيار نوع العملية
operation = st.selectbox(
    "اختر نوع العملية:",
    ["جمع (+)", "طرح (-)", "ضرب (×)", "قسمة (÷)", "قسمة بدون كسور (//)"]
)

# زر لتنفيذ العملية
if st.button("احسب"):
    if operation == "جمع (+)":
        result = num1 + num2
        st.success(f"✅ الناتج: {result}")
    elif operation == "طرح (-)":
        result = num1 - num2
        st.success(f"✅ الناتج: {result}")
    elif operation == "ضرب (×)":
        result = num1 * num2
        st.success(f"✅ الناتج: {result}")
    elif operation == "قسمة (÷)":
        if num2 != 0:
            result = num1 / num2
            st.success(f"✅ الناتج: {result}")
        else:
            st.error("❌ خطأ: لا يمكن القسمة على صفر.")
    elif operation == "قسمة بدون كسور (//)":
        if num2 != 0:
            result = num1 // num2
            st.success(f"✅ الناتج: {result}")
        else:
            st.error("❌ خطأ: لا يمكن القسمة على صفر.")
