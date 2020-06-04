# CommitteeTotalsPacParty

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all_loans_received** | **float** |  | [optional] 
**allocated_federal_election_levin_share** | **float** |  | [optional] 
**cash_on_hand_beginning_period** | **float** |  | [optional] 
**committee_designation** | **str** | The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  | [optional] 
**committee_designation_full** | **str** | The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  | [optional] 
**committee_id** | **str** |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] 
**committee_name** | **str** | The name of the committee. If a committee changes its name,     the most recent name will be shown. Committee names are not unique. Use committee_id     for looking up records. | [optional] 
**committee_type** | **str** | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  | [optional] 
**committee_type_full** | **str** | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  | [optional] 
**contribution_refunds** | **float** |  | [optional] 
**contributions** | **float** | Contribution | [optional] 
**convention_exp** | **float** |  | [optional] 
**coordinated_expenditures_by_party_committee** | **float** |  | [optional] 
**coverage_end_date** | **datetime** |  | [optional] 
**coverage_start_date** | **datetime** |  | [optional] 
**cycle** | **int** |  Filter records to only those that are applicable to a given two-year period. This cycle follows the traditional House election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. The cycle begins with an odd year and is named for its ending, even year.  | [optional] 
**disbursements** | **float** | Disbursements | [optional] 
**exp_prior_years_subject_limits** | **float** |  | [optional] 
**exp_subject_limits** | **float** |  | [optional] 
**fed_candidate_committee_contributions** | **float** |  | [optional] 
**fed_candidate_contribution_refunds** | **float** |  | [optional] 
**fed_disbursements** | **float** |  | [optional] 
**fed_election_activity** | **float** |  | [optional] 
**fed_operating_expenditures** | **float** |  | [optional] 
**fed_receipts** | **float** |  | [optional] 
**federal_funds** | **float** |  | [optional] 
**independent_expenditures** | **float** |  | [optional] 
**individual_contributions** | **float** |  | [optional] 
**individual_itemized_contributions** | **float** | Individual itemized contributions are from individuals whose aggregate contributions total over $200 per individual per year. Be aware, some filers choose to itemize donations $200 or less. | [optional] 
**individual_unitemized_contributions** | **float** | Unitemized contributions are made individuals whose aggregate contributions total $200 or less per individual per year. Be aware, some filers choose to itemize donations $200 or less and in that case those donations will appear in the itemized total. | [optional] 
**itemized_convention_exp** | **float** |  | [optional] 
**itemized_other_disb** | **float** |  | [optional] 
**itemized_other_income** | **float** |  | [optional] 
**itemized_other_refunds** | **float** |  | [optional] 
**itemized_refunds_relating_convention_exp** | **float** |  | [optional] 
**last_beginning_image_number** | **str** |  | [optional] 
**last_cash_on_hand_end_period** | **float** |  | [optional] 
**last_debts_owed_by_committee** | **float** |  | [optional] 
**last_debts_owed_to_committee** | **float** |  | [optional] 
**last_report_type_full** | **str** |  | [optional] 
**last_report_year** | **int** |  | [optional] 
**loan_repayments_made** | **float** |  | [optional] 
**loan_repayments_received** | **float** |  | [optional] 
**loans_and_loan_repayments_made** | **float** |  | [optional] 
**loans_and_loan_repayments_received** | **float** |  | [optional] 
**loans_made** | **float** |  | [optional] 
**net_contributions** | **float** |  | [optional] 
**net_operating_expenditures** | **float** |  | [optional] 
**non_allocated_fed_election_activity** | **float** |  | [optional] 
**offsets_to_operating_expenditures** | **float** |  | [optional] 
**operating_expenditures** | **float** |  | [optional] 
**other_disbursements** | **float** |  | [optional] 
**other_fed_operating_expenditures** | **float** |  | [optional] 
**other_fed_receipts** | **float** |  | [optional] 
**other_political_committee_contributions** | **float** |  | [optional] 
**other_refunds** | **float** |  | [optional] 
**party_full** | **str** | Party affiliated with a candidate or committee | [optional] 
**pdf_url** | **str** |  | [optional] 
**political_party_committee_contributions** | **float** |  | [optional] 
**receipts** | **float** |  | [optional] 
**refunded_individual_contributions** | **float** |  | [optional] 
**refunded_other_political_committee_contributions** | **float** |  | [optional] 
**refunded_political_party_committee_contributions** | **float** |  | [optional] 
**refunds_relating_convention_exp** | **float** |  | [optional] 
**report_form** | **str** |  | [optional] 
**shared_fed_activity** | **float** |  | [optional] 
**shared_fed_activity_nonfed** | **float** |  | [optional] 
**shared_fed_operating_expenditures** | **float** |  | [optional] 
**shared_nonfed_operating_expenditures** | **float** |  | [optional] 
**total_exp_subject_limits** | **float** |  | [optional] 
**total_transfers** | **float** |  | [optional] 
**transaction_coverage_date** | **date** |  | [optional] 
**transfers_from_affiliated_party** | **float** |  | [optional] 
**transfers_from_nonfed_account** | **float** |  | [optional] 
**transfers_from_nonfed_levin** | **float** |  | [optional] 
**transfers_to_affiliated_committee** | **float** |  | [optional] 
**unitemized_convention_exp** | **float** |  | [optional] 
**unitemized_other_disb** | **float** |  | [optional] 
**unitemized_other_income** | **float** |  | [optional] 
**unitemized_other_refunds** | **float** |  | [optional] 
**unitemized_refunds_relating_convention_exp** | **float** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

