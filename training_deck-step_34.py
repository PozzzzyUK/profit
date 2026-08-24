# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: TrainingDeck
TEMPLATE_REGISTRY = {}

def register_template(name, fields):
    """Register a template with name and list of field specs."""
    TEMPLATE_REGISTRY[name] = fields

def create_from_template(name, **overrides):
    """Create a new record from a registered template, applying overrides."""
    if name not in TEMPLATE_REGISTRY:
        raise ValueError(f"Unknown template: {name}")
    fields = TEMPLATE_REGISTRY[name].copy()
    record = {k: v for k, v in fields.items()}
    record.update(overrides)
    return record
