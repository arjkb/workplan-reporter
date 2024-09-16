from workplan.entry import Entry
from workplan.workplan import WorkPlan

def test_print():
    wp = WorkPlan()
    wp.add_entries([
        Entry('AC Installation', 'Purchase - #AC-123', 'Dev Completed', '2020-01-01', 'John Doe'),
        Entry('House Cleaning', 'Wash curtains - #HS-566', 'Dev Completed', '2020-01-01', 'John Doe'),
        Entry('AC Installation', 'Install - #AC-124', 'Ongoing', '2020-03-05', 'John Doe'),
    ])
    
    expected = (
        '\n\nDev Completed'
        '\nAC Installation - Purchase - #AC-123'
        '\nHouse Cleaning - Wash curtains - #HS-566'
        '\n\nOngoing'
        '\nAC Installation - Install - #AC-124 (ECD: 2020-03-05)'
    )

    assert f"{wp}" == expected
