import math


def parse_numbers(text):
    cleaned = text.replace(",", " ").strip()
    if not cleaned:
        raise ValueError("Числа не найдены. Укажите их через --numbers, --file или stdin.")
    numbers = []
    for token in cleaned.split():
        try:
            numbers.append(float(token))
        except ValueError as exc:
            raise ValueError(f"Некорректное число: {token}") from exc
    return numbers


def mean(numbers):
    if not numbers:
        raise ValueError("Пустая последовательность")
    return sum(numbers) / len(numbers)


def median(numbers):
    if not numbers:
        raise ValueError("Пустая последовательность")
    ordered = sorted(numbers)
    size = len(ordered)
    mid = size // 2
    if size % 2 == 1:
        return ordered[mid]
    return (ordered[mid - 1] + ordered[mid]) / 2


def normalize(numbers):
    if not numbers:
        raise ValueError("Пустая последовательность")
    low = min(numbers)
    high = max(numbers)
    if math.isclose(low, high):
        return [0.0 for _ in numbers]
    scale = high - low
    return [(value - low) / scale for value in numbers]


def format_report(numbers, include_normalized=False):
    report_lines = [
        "Отчет по статистике",
        f"Количество: {len(numbers)}",
        f"Минимум: {min(numbers)}",
        f"Максимум: {max(numbers)}",
        f"Среднее: {mean(numbers):.4f}",
        f"Медиана: {median(numbers):.4f}",
    ]
    if include_normalized:
        norm = normalize(numbers)
        report_lines.append("Нормализованные: " + ",".join(f"{n:.4f}" for n in norm))
    return "\n".join(report_lines)
