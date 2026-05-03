-- Query to collect business card performance metrics
-- Logic: 
-- event_id 1 = Views (displays)
-- event_id 2 = Clicks (interactions)

SELECT
    date,
    company_id[1] AS company_id,
    countIf(web_id, has(event_id, 1)) AS total_view,
    uniqExactIf(web_id, has(event_id, 1)) AS unique_view,
    countIf(web_id, has(event_id, 2)) AS total_click,
    uniqExactIf(web_id, has(event_id, 2)) AS unique_click,
    CASE
        WHEN has(event_id, 1) THEN 'Показ візитки'
        WHEN has(event_id, 2) AND click_action = 1 THEN 'Клік на заголовок'
        WHEN has(event_id, 2) AND click_action = 2 THEN 'Клік на зображення'
        WHEN has(event_id, 2) AND click_action = 3 THEN 'Клік на "Показати контакти"'
        WHEN has(event_id, 2) AND click_action = 4 THEN 'Клік на назву компанії'
        ELSE 'Інше'
      END AS click_action
FROM click.house
WHERE hasAny(event_id, [1, 2])
   AND date BETWEEN toDate(%(date_start)s) AND toDate(%(date_stop)s)
GROUP BY date, company_id, click_action
