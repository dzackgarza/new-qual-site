---
schema: qual/card@1
id: P-CALCPT3-14
kind: problem
title: "Years for the dollar to fall to one millionth of its value at a five-year halving time"
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-10-30
  note: "Transcribed from Question 14 of assets/attachments/calculus_practice_test3.pdf and checked against its MinerU Flash extraction; they agree where the extraction is legible."
---

::: {.problem}
At a $15$ percent annual inflation rate, the value of the dollar would decrease by approximately one-half every $5$ years.
At this inflation rate, in approximately how many years would the dollar be worth $\frac{1}{1{,}000{,}000}$ of its present value?

(A) $25$
(B) $50$
(C) $75$
(D) $100$
(E) $125$
:::

::: {.solution}
Model the value after $t$ years as $V(t)=V_0\,2^{-t/5}$, the value halving every $5$ years.

::: pf

::: {.pf-step #halvings}
The value reaches $\frac{1}{1{,}000{,}000}V_0$ after $n=\frac{6}{\log_{10}2}\approx 19.9$ halvings.

::: pf-proof
The equation $2^{-n}=10^{-6}$ gives $n\log_{10}2=6$, and $\log_{10}2\approx 0.301$, so $n\approx 6/0.301\approx 19.9$.
Equivalently, $2^{20}=1{,}048{,}576\approx 10^6$.
:::

:::

::: pf-step
The time is approximately $\boxed{100}$ years, choice (D).

::: pf-proof
By step [](#halvings){.pf-ref}, about $20$ halvings are needed, and each takes $5$ years, so $t=5n\approx 99.7\approx 100$.
:::

:::

:::

:::
