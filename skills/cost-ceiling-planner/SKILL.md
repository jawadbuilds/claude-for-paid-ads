---
name: cost-ceiling-planner
description: Works backwards from the most a business can pay for one customer to the targets an ad campaign has to hit. Use before setting a budget, when asked "what should my CPA or CPL be", "can I afford ads", "is this campaign viable", or when a plan needs a hard limit.
metadata:
  origin: "Original to this kit."
---

# Cost ceiling planner

Most ad plans start from a budget and hope the results fit. This one starts from the limit and tells you, before any spend, whether the plan can work.

## Step 1: get the ceiling

Ask for the most the business can pay in ad spend to win **one paying customer** and still be fine. Ask for two numbers:

- **Target:** the cost they want
- **Maximum:** the most they can pay and still keep the profit they need

If they do not know, help them find it: price, minus the cost of delivering it, minus the profit they need. A profit the owner names comes off first, and what is left is the maximum. Give one maximum. Do not add a second, higher limit that ignores the profit they asked for. For a customer who buys more than once, use what one customer is worth over the time the owner is willing to wait to be paid back, and say which period you used. Treat the maximum as a hard limit, not a guide.

## Step 2: get the funnel

Collect the real rate for each step, from their own data where it exists:

| Step | Rate needed |
|---|---|
| Click to lead (or sign-up, add to basket) | % of clicks |
| Lead to customer | % of leads |
| Cost per click | from the account, or the platform's forecast tool |

Mark every number as **measured** (from their data), **forecast** (from a platform tool) or **assumed**. Never mix them silently. Count customers from the owner's own records. If the ad platform's count differs, use the owner's and say so.

## Step 3: work backwards

```
Most you can pay per lead   = ceiling x (lead to customer rate)
Most you can pay per click  = most per lead x (click to lead rate)
```

Then compare the most you can pay per click with what a click really costs.

## Step 4: say plainly whether it fits

- **Fits:** real click cost is at or under the most you can pay. Give the targets to set.
- **Does not fit:** say by how much, and which step has to improve to close the gap. For example: "At today's click price the page must convert 2.5 times better, or the plan cannot reach the ceiling."
- **Cannot tell:** name the missing number.

Never propose a spend that cannot fit the ceiling without saying so.

## A worked example

An example tutor sells a course for 400. Delivering it costs 150 and they need 100 profit, so the most they can pay for one customer is 150.

- 1 lead in 5 becomes a customer, so the most they can pay for a lead is 150 x 0.20 = 30.
- 1 click in 20 becomes a lead, so the most they can pay for a click is 30 x 0.05 = 1.50.
- Clicks cost 2.40, so the plan does not fit. It fits if 1 click in 12.5 becomes a lead (2.40 / 30 = 8%), or if clicks cost 1.50.

## For a shop

A shop often thinks in return on ad spend (ROAS), the sales value that comes back for each unit spent on ads. The break-even ROAS is 1 divided by the margin. With a 40% margin after the cost of the goods and delivery, break-even is 1 / 0.40 = 2.5. Every 1 spent on ads must bring back 2.50 in sales just to stand still, so any target has to be above that.

## Output

```
Ceiling: [target] target, [maximum] maximum per customer

Step                Rate      Source      Most you can pay
Lead to customer    __%       measured    __ per lead
Click to lead       __%       assumed     __ per click
Real click cost     __        forecast

Verdict: fits / does not fit by __ / cannot tell
To make it fit: [the one change with the biggest effect]
Budget that gives a fair test: [enough for about 30 to 50 results at the target cost]
```

## Rules

- Use the business's own currency and say which it is.
- A small budget cannot test many things. If the budget buys fewer than about 30 results, recommend fewer campaigns, not thinner ones.
- Show the arithmetic. The person must be able to check it.
