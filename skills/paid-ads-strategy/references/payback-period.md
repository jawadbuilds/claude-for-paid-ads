# Payback period budgeting

This file is for subscription businesses, where a customer pays every month and you want to know how long it takes to earn back what it cost to win them. Most small businesses sell one-off purchases, lessons or local services. If that is you, use `cost-ceiling-planner` instead, which works from the most you can pay for one result.

Terms used below:

- **CAC** (customer acquisition cost): what it costs, in total, to win one new customer.
- **ARPU** (average revenue per user): the average amount one customer pays you per month.
- **Gross margin**: the share of each payment left after the direct cost of serving the customer, written as a fraction (0.8 means 80%).
- **Churn**: the share of customers who cancel in a period.

The question this file answers: can I afford this channel? Advertising works best when money in comes back as more money out, on a clock you can name. Payback period is how you set that clock.

## Why not rely on LTV:CAC alone

LTV is lifetime value, the total a customer is expected to pay over their time with you. A blended LTV:CAC ratio can hide when cash comes back, and payback period shows it. Four reasons:

1. **It assumes every customer eventually leaves.** That is a modelling choice, and it can under-value a base of customers who stay for years.
2. **It assumes churn is evenly spread.** In many subscription businesses more customers cancel in the first months than later. One vendor reports this pattern in its own data, so check your own cohorts before assuming it. A blended average smooths that early drop and hides the real risk.
3. **It hides differences between plans.** A $9 a month plan and a $999 a month plan averaged into one number describe neither. The channels and payback that suit the $9 buyer are very different from the $999 buyer, but a blended "3:1, we're fine" can lead you to scale the wrong one.
4. **It ignores delay.** Free trials, free plans and long sales cycles mean money arrives weeks or months after the cost is spent. The ratio treats cost and revenue as simultaneous, and the gap in between is where cash runs out.

A healthy-looking ratio can sit on top of a channel that drains cash, because the ratio never asks when the money comes back.

## Payback period

**Revenue-only ratio = CAC / monthly ARPU.** To count the cost of serving customers, use **gross-margin payback = CAC / (monthly ARPU x gross margin)**. The revenue-only ratio assumes 100% gross margin. See [the CAC payback definition](https://chartmogul.com/saas-metrics/cac-payback/).

The result is in months, and it assumes steady monthly gross profit with no churn or payment delay. A target of 3 to 12 months is a rule of thumb, not a platform rule. Choose your own target from your cash runway, margins and measured cohort recovery. A shorter or longer ratio on its own does not justify changing spend.

Because it is worked per plan and per cohort rather than blended, it shows what a blended ratio hides.

### Worked example: same CAC, very different payback

Example: a channel costs $300 to win one customer (CAC = $300). The table is revenue-only, before serving costs and churn. It is a comparison, not permission to scale.

| Plan | ARPU (monthly) | Revenue-only ratio = CAC / ARPU | Verdict |
|------|---------------|----------------------|---------|
| Starter | $9 | 300 / 9 = **33.3 months** | Do not fund paid acquisition for this plan. It is 33.3 months before costs and churn, and longer once margin is included. |
| Pro | $99 | 300 / 99 = **3.0 months** | Check margin first. At 80% gross margin it is 3.8 months. At 20% it is 15.2 months, which is too slow to scale. |
| Enterprise | $999 | 300 / 999 = **0.3 months** | Scale, after confirming when cash is actually collected (annual invoices, 60-day payment terms). |

The same CAC does not mean the same affordability. At 20% gross margin the $99 plan takes 300 / (99 x 0.20) = **15.2 months** even before churn, despite its 3.0-month revenue-only ratio. Compare plans separately and check serving costs before approving spend.

Example in pounds: CAC is £240, a customer pays £30 a month, and gross margin is 70% (0.7). Monthly gross profit is 30 x 0.7 = £21, so gross-margin payback is 240 / 21 = **11.4 months** before churn. That is inside the 3 to 12 month rule of thumb, but only just, so check retention before spending more.

The practical move: work out recovery per plan or per cohort against measured margin, retention and cash timing. Use your target as a planning assumption to compare with runway, not as a rule that approves spend.

## Cohort recovery: account for when churn happens

`CAC / (ARPU x annual retention)` is not discounted payback. A single year-end retention percentage cannot show the monthly recovery path. Discounting for the time value of money needs an explicit discount rate, and retention describes how many customers stay, which is a different thing.

For a cohort (a group who all joined in the same period), find the first month where cumulative gross profit per original customer covers CAC:

```
Cumulative recovery through month n = sum(ARPU_t x gross_margin_t x retained_fraction_t)
```

Use measured retained revenue per original customer when you have it, and do not multiply by retention again. Include payment delay when you look at cash recovery. If the cohort you can see has not yet recovered CAC, say so rather than inventing a payback date.

Example: CAC $300, ARPU $99, 80% gross margin, so $79.20 gross profit per retained customer per month. Two cohorts both keep 70% of customers at month 12:

- Early loss: 70% retained in every month from 1 to 12. Gross profit per original customer is 79.20 x 0.70 = $55.44 a month. After 5 months that is $277.20, which is under $300. After 6 months it is $332.64. Recovery first crosses $300 in **month 6**.
- Late loss: 100% retained in months 1 to 11, then 70% at month 12. Gross profit is $79.20 a month. After 3 months that is $237.60, and after 4 months it is $316.80. Recovery crosses $300 in **month 4**.

The single-retention shortcut, 300 / (99 x 0.70), gives 4.3 months to both cohorts and ignores gross margin. Their real recovery differs by two months despite identical year-end retention.

## Using it as the channel gate

1. Work out CAC for the channel, all in: spend divided by new customers, including creative and management time.
2. Work out gross-margin payback and check the measured cohort recovery path, including when revenue is collected.
3. Compare recovery with your cash runway and your chosen target. Do not scale on a revenue-only ratio or an annual-retention multiplier.
4. Repeat monthly. CAC tends to rise as you scale, so the gate moves with it.

This pairs with the break-even cost per lead and per click maths in [b2b-paid-playbook.md](b2b-paid-playbook.md). Break-even tells you the most you can pay for a lead. Payback tells you how long your cash is tied up. You need both to scale without running dry.

---

*Source: Corey Haines, *Founding Marketing*, ch. 7 ("Spend budget where customers spend their time"). Payback targets and the early-churn pattern are practitioner or vendor reports: recalibrate against your own cohort data.*
