from guardrails import Guard, OnFailAction
from guardrails.hub import CompetitorCheck, ToxicLanguage

guard = Guard().use_many(
    CompetitorCheck(["Microsoft", "Google"], on_fail=OnFailAction.EXCEPTION),
    ToxicLanguage(threshold=0.5, validation_method="sentence", on_fail=OnFailAction.EXCEPTION)
)

 # Both the guardrails pass

try:
    guard.validate(
        """Apple just released a new iPhone."""
    )  # Both the guardrails fail
except Exception as e:
    print(e)