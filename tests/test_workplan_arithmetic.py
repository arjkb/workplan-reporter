from workplan.entry import Entry
from workplan.workplan import WorkPlan

def test_subtraction_same_ongoing_entry_last_week():
    wp_prev = WorkPlan()
    wp_curr = WorkPlan()

    wp_prev.add_entries([
        Entry('AC Installation', 'Purchase - #AC-123', 'Ongoing', '2020-01-02', 'John Doe'),
    ])
    wp_curr.add_entries([
        Entry('AC Installation', 'Purchase - #AC-123', 'Ongoing', '2020-02-03', 'John Doe'),
    ])

    expected = (
        '\n\nOngoing'
        '\nAC Installation - Purchase - #AC-123 (ECD: 2020-02-03)'
    )
    actual = wp_curr - wp_prev
    assert f"{actual}" == expected

def test_subtraction_same_onhold_last_week():
    wp_prev = WorkPlan()
    wp_curr = WorkPlan()

    wp_prev.add_entries([
        Entry('Sound Proofing', 'Measure area - #SP-233', 'On Hold', '2020-03-06', 'John Doe'),
    ])
    wp_curr.add_entries([
        Entry('Sound Proofing', 'Measure area - #SP-233', 'On Hold', '2020-03-06', 'John Doe'),
    ])

    expected = ""
    actual = wp_curr - wp_prev
    assert f"{actual}" == expected

def test_subtraction_same_pending_last_week():
    # an ongoing item last week become dev-completed this week
    wp_prev = WorkPlan()
    wp_curr = WorkPlan()

    wp_prev.add_entries([
        Entry('Sound Proofing', 'Measure area - #SP-233', 'Pending', '2020-03-06', 'John Doe'),
    ])
    wp_curr.add_entries([
        Entry('Sound Proofing', 'Measure area - #SP-233', 'Pending', '2020-03-06', 'John Doe'),
    ])

    expected = (
        '\n\nUpcoming'
        '\nSound Proofing - Measure area - #SP-233'
    )
    actual = wp_curr - wp_prev
    assert f"{actual}" == expected

def test_subtraction_same_moved_to_next_sprint_last_week():
    # unlikely scenario
    wp_prev = WorkPlan()
    wp_curr = WorkPlan()

    wp_prev.add_entries([
        Entry('Sound Proofing', 'Measure area - #SP-233', 'Moved to next sprint', '2020-03-06', 'John Doe'),
    ])
    wp_curr.add_entries([
        Entry('Sound Proofing', 'Measure area - #SP-233', 'Moved to next sprint', '2020-03-06', 'John Doe'),
    ])

    expected = (
        '\n\nUpcoming'
        '\nSound Proofing - Measure area - #SP-233'
    )
    actual = wp_curr - wp_prev
    assert f"{actual}" == expected

def test_subtraction_same_completed_last_week():
    wp_prev = WorkPlan()
    wp_curr = WorkPlan()

    wp_prev.add_entries([
        Entry('Sound Proofing', 'Measure area - #SP-233', 'Completed', '2020-03-06', 'John Doe'),
    ])
    wp_curr.add_entries([
        Entry('Sound Proofing', 'Measure area - #SP-233', 'Completed', '2020-03-06', 'John Doe'),
    ])

    expected = ""
    actual = wp_curr - wp_prev
    assert f"{actual}" == expected

def test_subtraction_same_waiting_for_qa_last_week():
    wp_prev = WorkPlan()
    wp_curr = WorkPlan()

    wp_prev.add_entries([
        Entry('Sound Proofing', 'Measure area - #SP-233', 'Waiting for QA', '2020-03-06', 'John Doe'),
    ])
    wp_curr.add_entries([
        Entry('Sound Proofing', 'Measure area - #SP-233', 'Waiting for QA', '2020-03-06', 'John Doe'),
    ])

    expected = ""
    actual = wp_curr - wp_prev
    assert f"{actual}" == expected

def test_subtraction_same_dev_completed_last_week():
    # if an entry got dev-completed last week, do not include it in this week's report
    wp_prev = WorkPlan()
    wp_curr = WorkPlan()

    wp_prev.add_entries([
        Entry('AC Installation', 'Purchase - #AC-123', 'Dev Completed', '2020-01-02', 'John Doe'),
    ])
    wp_curr.add_entries([
        Entry('AC Installation', 'Purchase - #AC-123', 'Dev Completed', '2020-02-03', 'John Doe'),
    ])

    expected = ""
    actual = wp_curr - wp_prev
    assert f"{actual}" == expected

def test_subtraction_same_dev_completed_last_week_with_additional_dev_completed():
    wp_prev = WorkPlan()
    wp_curr = WorkPlan()

    wp_prev.add_entries([
        Entry('AC Installation', 'Purchase - #AC-123', 'Dev Completed', '2020-01-02', 'John Doe'),
    ])
    wp_curr.add_entries([
        Entry('AC Installation', 'Purchase - #AC-123', 'Dev Completed', '2020-02-03', 'John Doe'),
        Entry('House Cleaning', 'Wash curtains - #HS-566', 'Dev Completed', '2020-01-01', 'John Doe'),
    ])

    expected = (
        '\n\nDev Completed'
        '\nHouse Cleaning - Wash curtains - #HS-566'
    )
    actual = wp_curr - wp_prev
    assert f"{actual}" == expected

def test_subtraction_same_dev_completed_last_week_with_additional_ongoing():
    wp_prev = WorkPlan()
    wp_curr = WorkPlan()

    wp_prev.add_entries([
        Entry('AC Installation', 'Purchase - #AC-123', 'Dev Completed', '2020-01-02', 'John Doe'),
    ])
    wp_curr.add_entries([
        Entry('AC Installation', 'Purchase - #AC-123', 'Dev Completed', '2020-02-03', 'John Doe'),
        Entry('AC Installation', 'Install - #AC-124', 'Ongoing', '2020-03-05', 'John Doe'),
    ])

    expected = (
        '\n\nnOngoing'
        '\nAC Installation - Install - #AC-124 (ECD: 2020-03-05)'
    )
    actual = wp_curr - wp_prev
    assert f"{actual}" == expected

def test_subtraction_same_dev_completed_last_week_with_additional_dev_compeleted_and_ongoing():
    wp_prev = WorkPlan()
    wp_curr = WorkPlan()

    wp_prev.add_entries([
        Entry('AC Installation', 'Purchase - #AC-123', 'Dev Completed', '2020-01-02', 'John Doe'),
    ])
    wp_curr.add_entries([
        Entry('AC Installation', 'Purchase - #AC-123', 'Dev Completed', '2020-02-03', 'John Doe'),
        Entry('House Cleaning', 'Wash curtains - #HS-566', 'Dev Completed', '2020-01-01', 'John Doe'),
        Entry('AC Installation', 'Install - #AC-124', 'Ongoing', '2020-03-05', 'John Doe'),
    ])

    expected = (
        '\n\nDev Completed'
        '\nHouse Cleaning - Wash curtains - #HS-566'
        '\n\nnOngoing'
        '\nAC Installation - Install - #AC-124 (ECD: 2020-03-05)'
    )
    actual = wp_curr - wp_prev
    assert f"{actual}" == expected

def test_subtraction_ongoing_last_week_with_different_entries_this_week():
    # in new sprint, the things that were Ongoing last week would be dev-completed this week
    wp_prev = WorkPlan()
    wp_curr = WorkPlan()

    wp_prev.add_entries([
        Entry('AC Installation', 'Purchase - #AC-123', 'Ongoing', '2020-01-02', 'John Doe'),
    ])
    wp_curr.add_entries([
        Entry('House Cleaning', 'Wash curtains - #HS-566', 'Dev Completed', '2020-01-01', 'John Doe'),
        Entry('AC Installation', 'Install - #AC-124', 'Ongoing', '2020-03-05', 'John Doe'),
    ])

    expected = (
        '\n\nDev Completed'
        '\nAC Installation - Purchase - #AC-123'
        '\nHouse Cleaning - Wash curtains - #HS-566'
        '\n\nnOngoing'
        '\nAC Installation - Install - #AC-124 (ECD: 2020-03-05)'
    )
    actual = wp_curr - wp_prev
    assert f"{actual}" == expected

def test_subtraction_dev_completed_and_ongoing_last_week_with_different_entries_this_week():
    # in new sprint, dev-completed items from last sprint are to be discarded
    wp_prev = WorkPlan()
    wp_curr = WorkPlan()

    wp_prev.add_entries([
        Entry('AC Installation', 'Purchase - #AC-123', 'Dev Completed', '2020-01-02', 'John Doe'),
        Entry('Sound Proofing', 'Measure area - #SP-233', 'Ongoing', '2020-03-06', 'John Doe'),
    ])
    wp_curr.add_entries([
        Entry('House Cleaning', 'Wash curtains - #HS-566', 'Dev Completed', '2020-01-01', 'John Doe'),
        Entry('AC Installation', 'Install - #AC-124', 'Ongoing', '2020-03-05', 'John Doe'),
    ])

    expected = (
        '\n\nDev Completed'
        '\nSound Proofing - Measure area - #SP-233'
        '\nHouse Cleaning - Wash curtains - #HS-566'
        '\n\nnOngoing'
        '\nAC Installation - Install - #AC-124 (ECD: 2020-03-05)'
    )
    actual = wp_curr - wp_prev
    assert f"{actual}" == expected

def test_subtraction_ongoing_became_dev_completed():
    # an ongoing item last week become dev-completed this week
    wp_prev = WorkPlan()
    wp_curr = WorkPlan()

    wp_prev.add_entries([
        Entry('Sound Proofing', 'Measure area - #SP-233', 'Ongoing', '2020-03-06', 'John Doe'),
    ])
    wp_curr.add_entries([
        Entry('Sound Proofing', 'Measure area - #SP-233', 'Dev Completed', '2020-03-06', 'John Doe'),
    ])

    expected = (
        '\n\nDev Completed'
        '\nSound Proofing - Measure area - #SP-233'
    )
    actual = wp_curr - wp_prev
    assert f"{actual}" == expected
