from typing import NamedTuple, TypeAlias

from calculator_utils.types import Matrix


class SolutionStep(NamedTuple):
    """Represents a step in the process of solving or calculating.

    Attributes:
        description (str): A description of the step.
        state (Matrix): The current state of the calculation.
    """

    description: str
    state: Matrix


Step: TypeAlias = SolutionStep
