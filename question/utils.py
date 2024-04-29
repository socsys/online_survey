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
    synthetic_stories = synthetic_stories_df[synthetic_stories_df['Synthetic_Post'].str.len() > 50].sample(
        num_stories - 1)

    # Read non-synthetic story from CSV
    non_synthetic_stories_df = pd.read_csv(non_synthetic_csv_path)
    non_synthetic_story = non_synthetic_stories_df[non_synthetic_stories_df['original_post'].str.len() > 50].sample(1)

    # Construct synthetic stories dictionary
    synthetic_story_data = synthetic_stories.set_index('Id').to_dict(orient='index')
    synthetic_story_data = {k: v['Synthetic_Post'] for k, v in synthetic_story_data.items()}

    # Construct non-synthetic story dictionary
    non_synthetic_story_data = non_synthetic_story.set_index('Id').to_dict(orient='index')
    non_synthetic_story_data = {k: v['original_post'] for k, v in non_synthetic_story_data.items()}

    # Merge synthetic and non-synthetic story dictionaries
    story_data = {**synthetic_story_data, **non_synthetic_story_data}

    question = Question.objects.create(
        question_content=f"Question about {num_stories} stories",
        synthetic_story_ids=synthetic_stories['Id'].tolist(),
        non_synthetic_story_ids=[non_synthetic_story['Id'].iloc[0]]
    )

    response_data = {
        "question_id": question.id,
        "question_content": question.question_content,
        "stories": story_data
    }

    return response_data
