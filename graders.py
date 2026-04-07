def grade_easy(state):
    if state["cost"] < 1500:
        return 1.0
    return 0.0


def grade_medium(state):
    score = 0

    if state["cost"] < 1500:
        score += 0.5

    if state["response_time"] < 400:
        score += 0.5

    return score


def grade_hard(state):
    score = 0

    if state["cost"] < 1500:
        score += 0.3

    if state["response_time"] < 400:
        score += 0.3

    if state["cpu_usage"] < 80:
        score += 0.2

    if state["traffic"] > 300:
        score += 0.2

    return score