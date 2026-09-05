# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: TrainingDeck
import copy

def dry_run_operation(operation_name, args, state, dry_run=True):
    """Simulates an operation without modifying the actual state.

    Args:
        operation_name: Name of the operation to simulate.
        args: Arguments needed for the operation.
        state: Current state dictionary.
        dry_run: If True, simulate; if False, actually perform the operation.

    Returns:
        Tuple of (success, result_or_error_message).
    """
    try:
        if operation_name == 'add_topic':
            new_topic = copy.deepcopy(args['topic'])
            topics = state.get('topics', [])
            if new_topic['name'] in [t['name'] for t in topics]:
                return False, f"Topic '{new_topic['name']}' already exists."
            topics.append(new_topic)
            return True, new_topic

        elif operation_name == 'add_exercise':
            new_exercise = copy.deepcopy(args['exercise'])
            exercise_id = new_exercise['id']
            exercises = state.get('exercises', [])
            if any(e['id'] == exercise_id for e in exercises):
                return False, f"Exercise '{exercise_id}' already exists."
            exercises.append(new_exercise)
            return True, new_exercise

        elif operation_name == 'add_check':
            new_check = copy.deepcopy(args['check'])
            checks = state.get('checks', [])
            if any(c['id'] == new_check['id'] for c in checks):
                return False, f"Check '{new_check['id']}' already exists."
            checks.append(new_check)
            return True, new_check

        elif operation_name == 'add_progress':
            new_progress = copy.deepcopy(args['progress'])
            progress_list = state.get('progress', [])
            if any(p['user_id'] == new_progress['user_id'] and p['exercise_id'] == new_progress['exercise_id'] for p in progress_list):
                return False, f"Progress record for user '{new_progress['user_id']}' on exercise '{new_progress['exercise_id']}' already exists."
            progress_list.append(new_progress)
            return True, new_progress

        else:
            return False, f"Unknown operation: {operation_name}"

    except Exception as e:
        return False, str(e)
