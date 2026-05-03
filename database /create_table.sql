create table company_business_card
(
    date         date,
    company_name text,
    click_action text,
    total_view   bigint,
    unique_view  bigint,
    total_click  bigint,
    unique_click bigint
);

comment on table company_business_card is 'company business card statistics';
