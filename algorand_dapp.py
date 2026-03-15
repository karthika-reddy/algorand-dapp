from algokit_utils import Application
from algopy import ARC4Contract, arc4, GlobalState, UInt64, String


class AlgorandDApp(ARC4Contract):
    """
    A simple Algorand smart contract for the algorand-dapp project.
    Author: karthika-reddy
    """

    # Global state variables
    counter: GlobalState[UInt64]
    owner: GlobalState[String]

    def __init__(self) -> None:
        self.counter = GlobalState(UInt64(0))
        self.owner = GlobalState(String(""))

    @arc4.abimethod(create="require")
    def create(self, owner: String) -> None:
        """Initialize the contract with an owner."""
        self.owner.value = owner
        self.counter.value = UInt64(0)

    @arc4.abimethod
    def increment(self) -> UInt64:
        """Increment the counter by 1."""
        self.counter.value += UInt64(1)
        return self.counter.value

    @arc4.abimethod
    def get_counter(self) -> UInt64:
        """Return the current counter value."""
        return self.counter.value

    @arc4.abimethod
    def reset(self) -> None:
        """Reset the counter to 0."""
        self.counter.value = UInt64(0)
