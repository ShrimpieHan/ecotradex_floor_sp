import streamlit as st
import math

# 地板数据结构
floor_data = {
    "comfort": {
        "6.5mm": 2.24
    },
    "classic": {
        "6.5mm": 2.01,
        "8mm": 1.79
    },
    "Premium": {
        "8mm": 1.74
    }
}

st.title("ECOTRADEX地板计算器")

# 输入选项
series = st.selectbox("请选择地板系列", list(floor_data.keys()))
thickness = st.selectbox("请选择厚度 (mm)", list(floor_data[series].keys()))
area = st.number_input("客户需要的面积（㎡）", min_value=0.0, step=0.1)

# 选择价格类型
price_type = st.radio("价格类型", ["零售价（不含GST）", "批发价（含GST）"])

if price_type == "零售价（不含GST）":
    price_input = st.number_input("请输入每㎡单价（不含GST）", min_value=0.0, step=0.1)
    include_gst = True
else:
    price_input = st.number_input("请输入每㎡单价（含GST）", min_value=0.0, step=0.1)
    include_gst = False

# 计算逻辑
if area > 0 and price_input > 0:
    per_pack_area = floor_data[series][thickness]
    num_packs = math.ceil(area / per_pack_area)
    total_area = num_packs * per_pack_area

    if include_gst:
        total_price = total_area * price_input * 1.15
        unit_price_with_gst = price_input * 1.15
        st.markdown("### 💰 计算结果（零售客户）")
        st.write(f"含税单价：**${unit_price_with_gst:.2f}/㎡**")
    else:
        total_price = total_area * price_input
        unit_price_no_gst = price_input / 1.15
        st.markdown("### 💰 计算结果（Builder 批发价）")
        st.write(f"不含税单价：**${unit_price_no_gst:.2f}/㎡**")

    # 输出结果
    st.write(f"📦 需要包数：**{num_packs} 包**")
    st.write(f"📐 实际提供面积：**{total_area:.2f} ㎡**")
    st.write(f"💵 含GST总价：**${total_price:.2f}**")
