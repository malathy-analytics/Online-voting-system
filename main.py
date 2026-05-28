# Online Voting System in Python

# Dictionary to store candidates and votes
votes = {
    "Alice": 0,
    "Bob": 0,
    "Charlie": 0
}

# List to store voted users
voted_users = []

while True:
    print("\n🗳️ ===== ONLINE VOTING SYSTEM ===== 🗳️")
    print("1️⃣ Vote")
    print("2️⃣ Show Results")
    print("3️⃣ Exit")

    choice = input("👉 Enter your choice: ")

    # Voting Section
    if choice == "1":
        voter_id = input("🆔 Enter your Voter ID: ")

        # Check if user already voted
        if voter_id in voted_users:
            print("❌ You have already voted!")
        else:
            print("\n📋 Candidates List:")
            for candidate in votes:
                print("👉", candidate)

            selected_candidate = input("🗳️ Enter candidate name: ")

            # Check valid candidate
            if selected_candidate in votes:
                votes[selected_candidate] += 1
                voted_users.append(voter_id)
                print("✅ Vote cast successfully! 🎉")
            else:
                print("❌ Invalid candidate!")

    # Result Section
    elif choice == "2":
        print("\n📊 ===== VOTING RESULTS ===== 📊")

        for candidate, vote_count in votes.items():
            print(f"🏅 {candidate} : {vote_count} votes")

        # Find winner
        winner = max(votes, key=votes.get)
        print(f"\n🏆 Winner is: {winner} 🎉")

    # Exit
    elif choice == "3":
        print("\n🙏 Thank you for using the Online Voting System! 💖")
        print("👋 Have a great day! 😊")
        break

    else:
        print("⚠️ Invalid choice! Please try again.")
