import streamlit as st
import pandas as pd
from datetime import datetime

# Настройка страницы
st.set_page_config(page_title="Мой Трекер Ухода", page_icon="🌿", layout="wide")

# Заголовок
st.title("🌿 Мой Трекер Ухода за Лицом")
st.subheader(f"📅 Сегодня: {datetime.now().strftime('%d %B %Y, %A')}")

# Вкладки
tab1, tab2, tab3 = st.tabs(["☀️ Утро", "🌙 Вечер", "📊 График активов"])

# === УТРО ===
with tab1:
    st.header("Утренняя рутина")
    st.info("💡 Не забудьте про массаж от отеков!")
    
    morning_steps = [
        "1. Лимфодренажный массаж (5-7 мин)",
        "2. Мягкое умывание гелем",
        "3. Тоник (восстановление pH)",
        "4. Сыворотка (Витамин С или Ниацинамид)",
        "5. Крем для глаз",
        "6. Увлажняющий крем",
        "7. SPF 50 (обязательно!)"
    ]
    
    for i, step in enumerate(morning_steps):
        st.checkbox(step, key=f"am_{i}")

# === ВЕЧЕР ===
with tab2:
    st.header("Вечерняя рутина")
    
    evening_steps = [
        "1. Гидрофильное масло (если был SPF)",
        "2. Мягкое умывание гелем",
        "3. Тоник",
        "4. АКТИВ (см. вкладку 'График активов')",
        "5. Крем для глаз",
        "6. Восстанавливающий крем (через 20 мин)"
    ]
    
    for i, step in enumerate(evening_steps):
        st.checkbox(step, key=f"pm_{i}")
    
    st.divider()
    st.markdown("### 📝 Заметки дня")
    notes = st.text_area("Как кожа себя чувствует сегодня?", height=100)
    if st.button("💾 Сохранить заметку"):
        if notes.strip():
            st.success("✅ Заметка сохранена!")
        else:
            st.warning("Напишите что-нибудь!")

# === ГРАФИК АКТИВОВ ===
with tab3:
    st.header("📅 График введения активов")
    
    week = st.number_input("Какая у вас сейчас неделя?", min_value=1, max_value=12, value=1)
    
    if week <= 2:
        status = "🌱 Адаптация"
        plan = "Только база. Ретинол и кислоты НЕ вводим. Ежедневный массаж!"
        color = "green"
    elif week <= 4:
        status = "🧪 Ввод ретинола"
        plan = "Ретинол 2 раза в неделю (Вт, Чт). Остальные дни — база."
        color = "orange"
    elif week <= 6:
        status = "⚡ Усиление"
        plan = "Ретинол через день + AHA-кислота 1 раз в неделю (Сб)."
        color = "orange"
    else:
        status = "🎯 Поддержание"
        plan = "Ретинол 3-4 раза в неделю + AHA 1-2 раза. Следите за реакцией."
        color = "blue"
    
    st.markdown(f"### Статус: **{status}**")
    st.markdown(f"**Задача на эту неделю:** {plan}")
    
    st.divider()
    st.markdown("### 📋 Таблица по дням")
    
    schedule_data = {
        "День": ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"],
        "Неделя 1-2": ["База", "База", "База", "База", "База", "Энзимы", "База"],
        "Неделя 3-4": ["База", "🔴 Ретинол", "База", "🔴 Ретинол", "База", "Энзимы", "База"],
        "Неделя 5-6": ["База", "🔴 Ретинол", "База", "🔴 Ретинол", "База", "🟡 AHA", "База"],
        "Неделя 7+": ["🔴 Ретинол", "База", "🔴 Ретинол", "База", "🔴 Ретинол", "🟡 AHA", "База"]
    }
    
    df = pd.DataFrame(schedule_data)
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.caption("🔴 = Ретинол | 🟡 = AHA-кислота | База = только тоник + крем")

# Боковая панель
st.sidebar.markdown("---")
st.sidebar.markdown("### 🌸 Привет, Ariza!")
st.sidebar.markdown("Помните: результат виден через 4-8 недель. Будьте терпеливы!")
st.sidebar.markdown("---")
st.sidebar.markdown("**Красные флаги:**\n- Сильное жжение\n- Покраснение > 3 дней\n- Шелушение\n\n→ Отмените актив, только база + восстановление.")
