import time

class SimpleAIWriter:
    """
    Simulates an AI writer's performance improvement after a 'cold start' phase.
    This demonstrates how an AI system needs an initial set of data/interactions
    (like the '10 posts' mentioned in the article) to become effective.
    """
    def __init__(self, learning_threshold=10):
        self.post_count = 0
        self.learning_threshold = learning_threshold
        print(f"AI Writer initialized. Learning threshold: {self.learning_threshold} posts.")
        print("-" * 50)

    def generate_text(self, topic):
        self.post_count += 1
        print(f"Attempting to generate post #{self.post_count} on '{topic}'...")
        time.sleep(0.1) # Simulate processing time

        # This is where the article's core concept is illustrated:
        # The AI's output quality improves after a certain number of interactions.
        if self.post_count <= self.learning_threshold:
            # Before the threshold, output is generic, simulating poor initial performance.
            quality_description = " (Initial, generic draft)"
            content = f"Draft on '{topic}': This is a very basic outline. The AI needs more examples to learn context and style. Current understanding is limited."
        else:
            # After the threshold, output is more detailed, simulating improved learning.
            quality_description = " (Improved, detailed draft)"
            content = f"Detailed article draft on '{topic}': The AI has processed enough data to generate a more comprehensive and contextually relevant piece. It shows clear signs of learning and adaptation."

        print(f"Generated Post #{self.post_count}{quality_description}")
        print(f"Content: {content[:100]}...") # Show a snippet
        print("-" * 50)
        return content

# --- Main execution --- 
if __name__ == "__main__":
    ai_writer = SimpleAIWriter(learning_threshold=10) # The '10 posts' threshold from the article

    topics = [
        "Artificial Intelligence", "Machine Learning", "Natural Language Processing",
        "Data Science", "Deep Learning", "Neural Networks", "Computer Vision",
        "Reinforcement Learning", "Generative AI", "Ethical AI",
        "AI in Healthcare", "Future of AI", "AI and Society", "AI in Education",
        "Quantum Computing"
    ]

    # Simulate generating posts, exceeding the learning threshold
    for i, topic in enumerate(topics):
        if i >= 15: # Limit to 15 posts for brevity to show both phases clearly
            break
        ai_writer.generate_text(topic)
        time.sleep(0.5) # Pause between generations for readability

    print("\n--- Simulation Complete ---")
    print(f"The AI writer generated {ai_writer.post_count} posts.")
    print(f"Notice the change in output quality after post #{ai_writer.learning_threshold}.")
