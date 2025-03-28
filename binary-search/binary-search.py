import streamlit as st
import random
import time

def native_search(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1

def binary_search(l, target):
    low, high = 0, len(l) - 1
    while low <= high:
        midpoint = (low + high) // 2
        if l[midpoint] == target:
            return midpoint
        elif target < l[midpoint]:
            high = midpoint - 1
        else:
            low = midpoint + 1
    return -1

st.title("Binary Search vs. Naive Search")

length = st.slider("Select list length", 10, 100000, 10000)
number_to_search = st.number_input("Enter a number to search", value=1, step=1)

if st.button("Search"):
    sorted_list = sorted(random.sample(range(-3*length, 3*length), length))
    
    trials = 5  # Multiple trials to get average time
    
    naive_time_total = 0
    binary_time_total = 0
    
    for _ in range(trials):
        start = time.perf_counter_ns()
        naive_result = native_search(sorted_list, number_to_search)
        naive_time_total += (time.perf_counter_ns() - start)
        
        start = time.perf_counter_ns()
        binary_result = binary_search(sorted_list, number_to_search)
        binary_time_total += (time.perf_counter_ns() - start)
    
    naive_time = naive_time_total / trials
    binary_time = binary_time_total / trials
    
    st.write(f"Naive Search Result: {naive_result} (Avg Time: {naive_time:.2f} nanoseconds)")
    st.write(f"Binary Search Result: {binary_result} (Avg Time: {binary_time:.2f} nanoseconds)")
    
    if naive_time > binary_time:
        st.write("Binary search is significantly faster!")
    else:
        st.write("Naive search performed well in this case.")
