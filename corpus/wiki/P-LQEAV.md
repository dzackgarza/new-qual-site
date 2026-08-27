---
schema: qual/card@1
id: P-LQEAV
kind: problem
title: $\|a\|_{\ell^q}\le\|a\|_{\ell^p}$ for $0<p<q\le\infty$
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
  - Norms
  - Series of Numbers
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: problem
Show that for $0 < p < q \leq \infty$, $\norm{a}_{\ell^q} \leq \norm{a}_{\ell^p}$ over $\CC$, where $\norm{a}_{\infty } \da \sup_j \abs{a_j}$.
:::
::: {.solution}
<1>1. Case $q = \infty$: $\|a\|_\infty = \sup_j|a_j| \le \|a\|_p$.
Proof: $|a_j|^p \le \sum_j |a_j|^p = \|a\|_p^p$ for every $j$, so $\sup_j |a_j| \le \|a\|_p$.

<1>2. Case $q < \infty$ (so $0 < p < q$): for $a \in \ell^p$, $\|a\|_q \le \|a\|_p$.
<2>1. If $a = 0$ the claim is trivial; assume $\|a\|_p > 0$; WLOG $\|a\|_p = 1$ (homogeneity: both sides scale by the same factor).
Proof: $\|\lambda a\|_q = |\lambda|\|a\|_q$, same for $\|\cdot\|_p$.
<2>2. With $\|a\|_p = 1$: $|a_j| \le 1$ for all $j$, so $|a_j|^q \le |a_j|^p$.
Proof: $|a_j|^p \le \sum_k |a_k|^p = 1$.
<2>3. $\|a\|_q^q = \sum_j |a_j|^q \le \sum_j |a_j|^p = 1$, so $\|a\|_q \le 1 = \|a\|_p$.
Proof: <2>2 and the normalization.

<1>3. Q.E.D. Proof: <1>1 and <1>2 cover $q = \infty$ and $q < \infty$.
(This is the standard fact $\ell^p \subseteq \ell^q$ for $p < q$, with the norm inequality; it holds over $\CC$ since only moduli are used.)
:::
