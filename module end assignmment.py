feedback_data = {
    'S_No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Name': ['Ravi', 'Meera', 'Sam', 'Anu', 'Raj', 'Divya', 'Arjun', 'Kiran', 'Leela', 'Nisha'],
    'Feedback': [
        '  Very GOOD Service!!!',
        'poor support,  not happy  ',
        'GREAT experience! will come again.',
        'okay  okay...',
        '  not   BAD',
        'Excellent care, excellent staff!!',
        'good food and good ambience!',
        'Poor response and poor handling of issue',
        'Satisfied. But could be better.',
        'Good support... quick service.'
    ],
    'Rating': [5, 2, 5, 3, 2, 5, 4, 1, 3, 4]
}
n = int(input("How many more feedbacks do you want to add? "))

for i in range(n):
    name = input("Enter name: ")
    feedback = input("Enter feedback: ")
    rating = int(input("Enter rating (1-5): "))
    
    feedback_data["S_No"].append(len(feedback_data["S_No"]) + 1)
    feedback_data["Name"].append(name)
    feedback_data["Feedback"].append(feedback)
    feedback_data["Rating"].append(rating)

cleaned_feedbacks = []

for text in feedback_data['Feedback']:
    text = text.lower()
    text = text.replace('.', '').replace(',', '').replace('!', '').replace('?', '')
    text = ' '.join(text.split())
    cleaned_feedbacks.append(text)

feedback_data['Feedback'] = cleaned_feedbacks

print("\nCleaned Feedbacks:")
print(feedback_data['Feedback'])

def count_word_in_feedbacks(word):
    search_word = word.lower()
    count = 0
    for text in feedback_data['Feedback']:
        if search_word in text.split():
            count += 1
    return count

print("\n--- Word Count Insights ---")
print("Number of feedbacks containing 'good':", count_word_in_feedbacks("good"))
print("Number of feedbacks containing 'poor':", count_word_in_feedbacks("poor"))
print("Number of feedbacks containing 'excellent':", count_word_in_feedbacks("excellent"))

print("\n--- Final Summary & Insights ---")

print("\n1. Cleaned feedback_data:")
print(feedback_data)

avg_rating = sum(feedback_data['Rating']) / len(feedback_data['Rating'])
print(f"\n2. Average Rating: {avg_rating:.2f}")

longest_comment = max(feedback_data['Feedback'], key=lambda text: len(text.split()))
print(f"\n3. Longest Feedback: \"{longest_comment}\"")

unique_words = set()
for text in feedback_data['Feedback']:
    unique_words.update(text.split())
print(f"\n4. Unique Words List ({len(unique_words)} words):")
print(sorted(list(unique_words)))

print("\n--- Sorted Feedbacks by Rating (Highest to Lowest) ---")
zipped_data = list(zip(
    feedback_data['S_No'],
    feedback_data['Name'],
    feedback_data['Feedback'],
    feedback_data['Rating']
))
sorted_data = sorted(zipped_data, key=lambda x: x[3], reverse=True)

print(f"{'S_No':<6} | {'Name':<10} | {'Rating':<6} | {'Feedback'}")
print("-" * 65)
for s_no, name, text, rating in sorted_data:
    print(f"{s_no:<6} | {name:<10} | {rating:<6} | {text}")
