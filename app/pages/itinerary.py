import streamlit as st
from backend.recommender import recommend_places

def show():
    st.header("AI Smart Itinerary ✈️")

    city = st.text_input("Enter City", "Manali")
    nights = st.number_input("Nights", min_value=1, max_value=15, value=1)
    budget = st.selectbox("Budget", ["Low", "Medium", "High"])
    traveler = st.selectbox("Traveller Type", ["Explorer", "Foodie", "Shopaholic"])

    if st.button("Generate Itinerary"):
        st.info("Generating AI-based itinerary...")

        query = f"{traveler} places to visit in {city} for a {nights}-night {budget} budget trip"

        results = recommend_places(city, query, top_k=5)

        if not results:
            st.error("No data found for that city.")
            return

        # Show itinerary summary
        st.success(f"Itinerary for {city.title()} — {nights} nights, {budget}, {traveler}")

        st.write("### Day 1:")
        for r in results:
            st.markdown(f"""
            - **{r['name']}**  
              ⭐ Rating: {r.get('rating', 'N/A')}  
              📍 Distance: {r.get('distance', 'N/A')}  
              📝 {r['description']}  
            """)

        # For more days in future:
        # Day 2, Day 3 will be added based on stay duration
