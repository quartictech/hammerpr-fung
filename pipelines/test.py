from quartic import step, writer
from quartic.incubating import raw, FromBucket

@raw
def raw_dataset() -> "raw/input":
    return FromBucket("quartic_employees.csv")

@step
def step1(test: "input") -> "output":
    return writer("Something", "Something").json({})
