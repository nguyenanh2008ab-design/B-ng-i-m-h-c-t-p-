
#1. Import thu vien

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#2. Tao du lieu sinh vien

data = {
    "Ho_ten": [
        "Nguyen An", "Tran Binh", "Le Cuong", "Pham Dung",
        "Hoang Giang", "Vu Hieu", "Do Khanh", "Bui Lan",
        "Ngo Minh", "Dang Nam"
    ],
    "Chuyen_can": [9, 8, 7, 10, 6, 8, 9, 7, 5, 8],
    "Giua_ky": [8, 7, 6, 9, 5, 8, 7, 6, 4, 9],
    "Cuoi_ky": [9, 8, 7, 10, 6, 9, 8, 7, 5, 8]
}

df = pd.DataFrame(data)

#3. Tinh diem tong ket

df["Tong_ket"] = (
    df["Chuyen_can"] * 0.2
    + df["Giua_ky"] * 0.3
    + df["Cuoi_ky"] * 0.5
).round(2)

#4. Xep loai

def xep_loai(diem):
    if diem >= 8.5:
        return "Gioi"
    elif diem >= 7:
        return "Kha"
    elif diem >= 5:
        return "Trung binh"
    else:
        return "Yeu"

df["Xep_loai"] = df["Tong_ket"].apply(xep_loai)

#5. Giao dien web

st.title("QUAN LY DIEM SINH VIEN")

st.subheader("Bang diem sinh vien")

st.dataframe(
    df.rename(columns={
        "Ho_ten": "Ho ten",
        "Chuyen_can": "Chuyen can",
        "Giua_ky": "Giua ky",
        "Cuoi_ky": "Cuoi ky",
        "Tong_ket": "Tong ket",
        "Xep_loai": "Xep loai"
    }),
    use_container_width=True
)

#6. Thong ke

st.subheader("Thong ke ket qua")

st.write("Diem trung binh cua lop:",
         round(df["Tong_ket"].mean(), 2))

sv_cao = df.loc[df["Tong_ket"].idxmax()]
sv_thap = df.loc[df["Tong_ket"].idxmin()]

st.write("Sinh vien cao nhat:",
         sv_cao["Ho_ten"],
         "-", sv_cao["Tong_ket"])

st.write("Sinh vien thap nhat:",
         sv_thap["Ho_ten"],
         "-", sv_thap["Tong_ket"])

st.write("So sinh vien dat:",
         int((df["Tong_ket"] >= 5).sum()))

#7. Chon sinh vien

st.subheader("Tra cuu sinh vien")

ten = st.selectbox(
    "Chon sinh vien",
    df["Ho_ten"]
)

sv = df[df["Ho_ten"] == ten].iloc[0]

st.write("Ho ten:", sv["Ho_ten"])
st.write("Chuyen can:", sv["Chuyen_can"])
st.write("Giua ky:", sv["Giua_ky"])
st.write("Cuoi ky:", sv["Cuoi_ky"])
st.write("Tong ket:", sv["Tong_ket"])
st.write("Xep loai:", sv["Xep_loai"])

#8. Ve bieu do

st.subheader("Bieu do diem tong ket")

fig, ax = plt.subplots(figsize=(10, 5))

ax.bar(df["Ho_ten"], df["Tong_ket"])
ax.set_xlabel("Ho ten sinh vien")
ax.set_ylabel("Diem tong ket")
ax.set_title("Diem tong ket cua 10 sinh vien")
ax.set_ylim(0, 10)

plt.xticks(rotation=45)
plt.tight_layout()

st.pyplot(fig)

#9. Thong tin nguoi tao

st.caption("Ho ten: [Nhap ho ten cua ban]")
st.caption("MSSV: [Nhap MSSV cua ban]")
