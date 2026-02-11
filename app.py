import random

def humanize(text):
    # 1. Smarter Word Swap (more options)
    replacements = {
        "furthermore": ["also", "and honestly,"],
        "consequently": ["so basically,", "as a result,"],
        "utilize": ["use", "go with"],
        "essential": ["key", "super important"],
        "demonstrates": ["shows", "really proves"],
    }
    
    for ai_word, student_options in replacements.items():
        # Randomly pick a replacement to increase "Perplexity"
        replacement = random.choice(student_options)
        text = text.replace(ai_word, replacement)

    # 2. Break the "Robotic" sentence structure
    # AI writes sentences of the same length. Let's break some in half.
    sentences = text.split(". ")
    new_sentences = []
    for s in sentences:
        if len(s.split()) > 15: # If the sentence is too long/robotic
            parts = s.split(", ")
            if len(parts) > 1:
                # Break it at the comma to create "Burstiness"
                new_sentences.append(parts[0])
                new_sentences.append("Basically, " + parts[1].lower())
            else:
                new_sentences.append(s)
        else:
            new_sentences.append(s)
            
    return ". ".join(new_sentences)
