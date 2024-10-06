from status import status
from workplan.entry import Entry

def test_entry_print():
    cases = [
        (
            ('AC Installation', 'Purchase - #AC-123', status.Status.DEV_COMPLETED, '2020-01-01', 'John Doe'),
            'AC Installation - Purchase - #AC-123'
        ),
        (
            ('AC Installation', 'Purchase - #AC-456', status.Status.ONGOING, '2020-01-02', 'John Doe'),
            'AC Installation - Purchase - #AC-456 (ECD: 2020-01-02)'
        ),
        (
            ('AC Installation', 'Purchase - #AC-456', status.Status.ON_HOLD, '2020-01-02', 'John Doe'),
            'AC Installation - Purchase - #AC-456'
        ),
        (
            ('AC Installation', 'Purchase - #AC-456', status.Status.PENDING, '2020-01-02', 'John Doe'),
            'AC Installation - Purchase - #AC-456'
        ),
        (
            ('AC Installation', 'Purchase - #AC-456', status.Status.COMPLETED, '2020-01-02', 'John Doe'),
            'AC Installation - Purchase - #AC-456'
        ),
    ]

    for case, expected in cases:
        e = Entry(*case)
        assert f"{e}" == expected