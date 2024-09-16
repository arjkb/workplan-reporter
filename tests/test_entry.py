from workplan.entry import Entry

def test_entry_print():
    cases = [
        (
            ('AC Installation', 'Purchase - #AC-123', 'Dev Completed', '2020-01-01', 'John Doe'),
            'AC Installation - Purchase - #AC-123'
        ),
        (
            ('AC Installation', 'Purchase - #AC-456', 'Ongoing', '2020-01-02', 'John Doe'),
            'AC Installation - Purchase - #AC-456 (ECD: 2020-01-02)'
        ),
        (
            ('AC Installation', 'Purchase - #AC-456', 'On Hold', '2020-01-02', 'John Doe'),
            'AC Installation - Purchase - #AC-456'
        ),
        (
            ('AC Installation', 'Purchase - #AC-456', 'Pending', '2020-01-02', 'John Doe'),
            'AC Installation - Purchase - #AC-456'
        ),
        (
            ('AC Installation', 'Purchase - #AC-456', 'Completed', '2020-01-02', 'John Doe'),
            'AC Installation - Purchase - #AC-456'
        ),
    ]

    for case, expected in cases:
        e = Entry(*case)
        assert f"{e}" == expected