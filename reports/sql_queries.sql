SELECT
    scheme_name,
    fund_house,
    sharpe_ratio
FROM scheme_performance
ORDER BY sharpe_ratio DESC
LIMIT 10;



SELECT
    scheme_name,
    alpha
FROM scheme_performance
ORDER BY alpha DESC
LIMIT 10;



SELECT
    scheme_name,
    return_3yr_pct,
    benchmark_3yr_pct,
    (return_3yr_pct - benchmark_3yr_pct) AS excess_return
FROM scheme_performance
ORDER BY excess_return DESC;


SELECT
    age_group,
    COUNT(*) AS investors
FROM investor_transactions
GROUP BY age_group
ORDER BY investors DESC;




SELECT
    gender,
    COUNT(*) AS count
FROM investor_transactions
GROUP BY gender;



SELECT
    state,
    SUM(amount_inr) AS total_investment
FROM investor_transactions
GROUP BY state
ORDER BY total_investment DESC;




SELECT
    fund_house,
    AVG(return_3yr_pct) AS avg_return,
    AVG(sharpe_ratio) AS avg_sharpe
FROM scheme_performance
GROUP BY fund_house
ORDER BY avg_sharpe DESC;




-- Top 5 Funds by AUM

SELECT
    scheme_name,
    aum_crore
FROM scheme_performance
ORDER BY aum_crore DESC
LIMIT 5;


-- Expense Ratio Less Than 1%

SELECT
    scheme_name,
    expense_ratio_pct
FROM scheme_performance
WHERE expense_ratio_pct < 1;


-- High Risk Funds

SELECT
    scheme_name,
    risk_grade
FROM scheme_performance
WHERE risk_grade = 'High';
