from quartic import step, writer
from quartic.incubating import raw, FromBucket

@raw
def raw_dataset() -> "raw/input":
    return FromBucket("quartic-employees.csv", "Employees")

@step
def step1(test: "raw/input") -> "output":
    return writer("Something", "Something").json({})
