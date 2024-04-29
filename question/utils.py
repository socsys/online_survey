# utils.py
import os

import pandas as pd

from .models import Question


def generate_question_and_stories(num_stories):
    # Read file paths from environment variables
    synthetic_csv_path = os.environ.get('SYNTHETIC_CSV_PATH')
    non_synthetic_csv_path = os.environ.get('NON_SYNTHETIC_CSV_PATH')

    # Read synthetic stories from CSV
    synthetic_stories_df = pd.read_csv(synthetic_csv_path)
    synthetic_stories = synthetic_stories_df.sample(num_stories - 1)

    # Read non-synthetic story from CSV
    non_synthetic_stories_df = pd.read_csv(non_synthetic_csv_path)
    non_synthetic_story = non_synthetic_stories_df.sample(1)

    question = Question.objects.create(
        question_content=f"Question about {num_stories} stories",
        synthetic_story_ids=synthetic_stories['id'].tolist(),
        non_synthetic_story_ids=[non_synthetic_story['id'].iloc[0]]
    )

    # Construct response data with story IDs mapped to their contents
    story_data = synthetic_stories[['id', 'content']].append(non_synthetic_story[['id', 'content']])
    story_data = story_data.set_index('id').to_dict(orient='index')

    response_data = {
        "question_id": question.id,
        "question_content": question.question_content,
        "stories": story_data
    }
