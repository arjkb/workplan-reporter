from workplan.entry import Entry
from workplan.workplan import WorkPlan

def test_print_dev_completed_ongoing():
    wp = WorkPlan()
    wp.add_entries([
        Entry('AC Installation', 'Purchase - #AC-123', 'Dev Completed', '2020-01-01', 'John Doe'),
        Entry('House Cleaning', 'Wash curtains - #HS-566', 'Dev Completed', '2020-01-01', 'John Doe'),
        Entry('Sound Proofing', 'Measure area - #SP-233', 'Waiting for QA', '2020-03-06', 'John Doe'),
        Entry('Bathroom', 'Install shower - #BR-754', 'Completed', '2020-03-06', 'John Doe'),
        Entry('AC Installation', 'Install - #AC-124', 'Ongoing', '2020-03-05', 'John Doe'),
    ])
    expected = (
        '\n\nDev Completed'
        '\nAC Installation - Purchase - #AC-123'
        '\nHouse Cleaning - Wash curtains - #HS-566'
        '\nSound Proofing - Measure area - #SP-233'
        '\nBathroom - Install shower - #BR-754'
        '\n\nOngoing'
        '\nAC Installation - Install - #AC-124 (ECD: 2020-03-05)'
    )
    assert f"{wp}" == expected

def test_print_ongoing():
    wp = WorkPlan()
    wp.add_entries([
        Entry('AC Installation', 'Purchase - #AC-123', 'Ongoing', '2020-01-01', 'John Doe'),
        Entry('House Cleaning', 'Wash curtains - #HS-566', 'Ongoing', '2020-02-04', 'John Doe'),
        Entry('AC Installation', 'Install - #AC-124', 'Ongoing', '2020-03-05', 'John Doe'),
    ])
    expected = (
        '\n\nOngoing'
        '\nAC Installation - Purchase - #AC-123 (ECD: 2020-01-01)'
        '\nHouse Cleaning - Wash curtains - #HS-566 (ECD: 2020-02-04)'
        '\nAC Installation - Install - #AC-124 (ECD: 2020-03-05)'
    )
    assert f"{wp}" == expected

def test_print_pending_upcoming():
    wp = WorkPlan()
    wp.add_entries([
        Entry('AC Installation', 'Purchase - #AC-123', 'Pending', '2020-01-01', 'John Doe'),
        Entry('House Cleaning', 'Wash curtains - #HS-566', 'Moved to next sprint', '2020-01-01', 'John Doe'),
        Entry('AC Installation', 'Install - #AC-124', 'Moved to next sprint', '2020-03-05', 'John Doe'),
    ])
    expected = (
        '\n\nUpcoming'
        '\nAC Installation - Purchase - #AC-123'
        '\nHouse Cleaning - Wash curtains - #HS-566'
        '\nAC Installation - Install - #AC-124'
    )
    assert f"{wp}" == expected

def test_print_none():
    wp = WorkPlan()
    expected = ""
    assert f"{wp}" == expected
