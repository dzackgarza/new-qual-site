---
schema: qual/card@1
id: P-YTOGK
kind: problem
title: Hölder's inequality $\bigl\|\prod f_j\bigr\|_r\le\prod\|f_j\|_{p_j}$ when $\sum 1/p_j=1/r\le 1$
classification:
  areas:
  - real-analysis
  topics:
  - lp-spaces
  - norms
relations: []
review: draft
solved: true
---

::: problem
Suppose that
\[
1\leq p_j \leq \infty, && \sum_{j=1}^n {1\over p_j} = {1\over r} \leq 1
.\]

Show that if $f_j \in L^{p_j}$ for each $1\leq j \leq n$, then
\[
\prod f_j \in L^r, && \norm{ \prod f_j }_r \leq \prod \norm{f_j}_{p_j}
.\]
:::
::: {.solution}
> **AI-Generated Solution**

<1>1. Reduce to the case where all $p_j < \infty$.
    Proof: if some $p_j = \infty$, then $|f_j| \le \norm{f_j}_\infty$ a.e., so $\norm{\prod f_j}_r \le \norm{f_j}_\infty \norm{\prod_{k\ne j} f_k}_r$, reducing to the $(n-1)$-term case. Iterating, assume $1 \le p_j < \infty$.
<1>2. Set $q_j = p_j/r$; then $q_j \ge 1$ and $\sum_j 1/q_j = 1$.
    Proof: $\sum_j 1/p_j = 1/r \le 1$ gives $r \le p_j$ for each $j$ (as $1/p_j \le 1/r$), so $q_j = p_j/r \ge 1$; and $\sum_j \frac{1}{q_j} = \sum_j \frac{r}{p_j} = r \cdot \frac1r = 1$.
<1>3. Apply Hölder's inequality to the functions $|f_j|^r$ with exponents $q_j$.
    Proof: by the generalized (multiplicative) Hölder inequality — iterated from the two-factor case — <1>2 gives
    \[
    \int \prod_j |f_j|^r \le \prod_j \Big(\int |f_j|^{r q_j}\Big)^{1/q_j} = \prod_j \Big(\int |f_j|^{p_j}\Big)^{r/p_j} = \prod_j \norm{f_j}_{p_j}^r .
    \]
<1>4. Conclude.
    Proof: taking the $r$-th root in <1>3:
    \[
    \norm{\prod_j f_j}_r = \Big(\int \prod_j |f_j|^r\Big)^{1/r} \le \prod_j \norm{f_j}_{p_j} ,
    \]
    so $\prod f_j \in L^r$ with the claimed norm bound. (When $r = \infty$, i.e. $\sum 1/p_j = 0$, all $p_j = \infty$ and the product is bounded by $\prod \norm{f_j}_\infty$.)
<1>5. Q.E.D.
:::
