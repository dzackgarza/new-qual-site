---
schema: qual/card@1
id: P-PIVLV
kind: problem
title: $L^q\subseteq L^p$ for $p<q$ implies no sets of arbitrarily large finite measure
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
  - Measure Theory
relations: []
review: draft
---

::: problem
Let $(X, \mathcal{M}, \mu)$ be a measure space and $0 < p < q< \infty$.
Prove that if $L^q(X) \subseteq L^p(X)$, then $X$ does not contain sets of arbitrarily large finite measure.
:::

::: {.solution}
> **AI-Generated Solution**

<1>1. We prove the contrapositive: if $X$ contains sets of arbitrarily large finite measure, then $L^q \not\subseteq L^p$.
Proof: first build pairwise disjoint measurable $E_n$ with $2^n \le \mu(E_n) < \infty$: inductively, choose a measurable $B_n$ with $\mu(B_n) \ge 2^n + \sum_{k<n} \mu(E_k)$ (possible since arbitrarily large finite sets exist), and set $E_n = B_n \setminus \cup_{k<n} E_k$; then $\mu(E_n) \ge \mu(B_n) - \sum_{k<n}\mu(E_k) \ge 2^n$.
<1>2. Define $f = \sum_n \mu(E_n)^{-1/p}\chi_{E_n}$.
<1>3. $f \in L^q$.
Proof: $\int f^q = \sum_n \mu(E_n)^{1 - q/p} \le \sum_n (2^n)^{1-q/p} < \infty$, since $q/p > 1$ makes the geometric series converge.
<1>4. $f \notin L^p$.
Proof: $\int f^p = \sum_n \mu(E_n)^{-1}\mu(E_n) = \sum_n 1 = \infty$.
<1>5. Hence $L^q \not\subseteq L^p$, contradicting the hypothesis.
Proof: <1>3 and <1>4 exhibit $f \in L^q \setminus L^p$.
<1>6. Q.E.D.
:::
