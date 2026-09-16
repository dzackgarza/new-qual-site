---
schema: qual/card@1
id: FT-VHK2H
kind: theorem
title: Hypotheses of Tonelli's and Fubini's theorems
prompts:
- What hypothesis does Tonelli need that Fubini does not?
classification:
  areas:
  - real-analysis
  topics:
  - Fubini-Tonelli
relations: []
review: draft
---

::: {.theorem}
Let $f$ be a [[D-DHFN4|Lebesgue measurable]] function on $\RR^n\times\RR^k$.

- **Tonelli.** If $f$ takes values in $[0,\infty]$, then $\int_{\RR^{n+k}}f$ equals both iterated integrals of $f$, as elements of $[0,\infty]$ ([[FT-4JRQX]]).

- **Fubini.** If $f\in L^1(\RR^{n+k})$, then $\int_{\RR^{n+k}}f$ equals both iterated integrals of $f$, whose inner integrals exist for almost every value of the outer variable ([[FT-T7OAO]]).
:::
