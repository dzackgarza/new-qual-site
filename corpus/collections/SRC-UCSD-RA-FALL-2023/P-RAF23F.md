---
schema: qual/card@1
id: P-RAF23F
kind: problem
title: "$L^p$ characterization via distribution function and interpolation of weak-type bounds"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 6 of the official UCSD Fall 2023 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
(i) Prove that for $p \geq 1$, $f \in L^p$ if and only if $\sum_{-\infty}^{+\infty} \beta^{kp} \lambda_f(\beta^k) < \infty$ for all $\beta > 1$.
Here $\lambda_f(\alpha) = \mu(\{x : |f|(x) > \alpha\})$.

(ii) Assume that $T$ is a linear operator from $L^p$ into $L^{q_1}$ and $L^{q_2}$ with $1 < q_1 < q_2$ such that $\lambda_{Tf}(2^k) \leq (C_1 \|f\|_p / 2^k)^{q_1}$ for integers $k \leq 0$; and $\lambda_{Tf}(2^\ell) \leq (C_2 \|f\|_p / 2^\ell)^{q_2}$ for integers $\ell \geq 0$.
Prove that for any $q_1 < q < q_2$, $\|Tf\|_q \leq C_q \|f\|_p$.
Here $C_q$ depends on $q, q_1, q_2$ and $C_1, C_2$.
:::

::: {.solution}

For $\beta>1$ and a measurable $f$, write $S_\beta(f)\coloneqq\sum_{k\in\ZZ}\beta^{kp}\lambda_f(\beta^k)$.

::: pf

::: {.pf-step #part-i}

(i) For every $\beta>1$, $f\in L^p$ if and only if $S_\beta(f)<\infty$. Moreover, if $\abs{f}<\infty$ almost everywhere, then $\norm{f}_p^p\le(\beta^p-1)\,S_\beta(f)$.

::: pf-proof

Fix $\beta>1$.
If $E\coloneqq\{\abs{f}=\infty\}$ has positive measure, then $f\notin L^p$, and $\lambda_f(\beta^k)\ge\mu(E)>0$ for every $k$, so the terms $\beta^{kp}\lambda_f(\beta^k)$ with $k\ge0$ do not tend to $0$ and $S_\beta(f)=\infty$.
Both sides of the equivalence therefore fail, and we may assume $\mu(E)=0$.

Set $A_k\coloneqq\{x:\beta^k<\abs{f(x)}\le\beta^{k+1}\}$ for $k\in\ZZ$.
These sets are pairwise disjoint, and their union is $\{0<\abs{f}<\infty\}$, which differs from $\{\abs{f}>0\}$ by the null set $E$.
Since $\beta^{kp}<\abs{f}^p\le\beta^{(k+1)p}$ on $A_k$,
$$
\sum_{k}\beta^{kp}\mu(A_k)\le\norm{f}_p^p\le\beta^p\sum_{k}\beta^{kp}\mu(A_k).
$$
Also $\lambda_f(\beta^k)=\sum_{j\ge k}\mu(A_j)$, so exchanging the order of summation of nonnegative terms gives
$$
S_\beta(f)=\sum_j\mu(A_j)\sum_{k\le j}\beta^{kp}=\frac{\beta^p}{\beta^p-1}\sum_j\beta^{jp}\mu(A_j).
$$
The two displays together give
$$
\frac{\beta^p-1}{\beta^p}\,S_\beta(f)\le\norm{f}_p^p\le(\beta^p-1)\,S_\beta(f),
$$
so $\norm{f}_p<\infty$ exactly when $S_\beta(f)<\infty$.
Since $\beta>1$ was arbitrary, this holds for all $\beta>1$.

:::

:::

::: {.pf-step #normalize}

For part (ii) it suffices to find $C_q$ with $\norm{Th}_q\le C_q$ for every $h\in L^p$ with $\norm{h}_p=1$.

::: pf-proof

If $f=0$, then $Tf=0$ by linearity and the bound holds.
Otherwise $h\coloneqq f/\norm{f}_p$ has $\norm{h}_p=1$ and $Tf=\norm{f}_p\,Th$ by linearity, so $\norm{Tf}_q=\norm{f}_p\norm{Th}_q\le C_q\norm{f}_p$.

:::

:::

::: {.pf-step #low}

If $\norm{h}_p=1$, then $\sum_{k\le0}2^{kq}\lambda_{Th}(2^k)\le C_1^{q_1}\big(1-2^{-(q-q_1)}\big)^{-1}$.

::: pf-proof

For integers $k\le0$ the first weak-type hypothesis gives $\lambda_{Th}(2^k)\le C_1^{q_1}2^{-kq_1}$, so the sum is at most $C_1^{q_1}\sum_{k\le0}2^{k(q-q_1)}$.
Since $q>q_1$, this geometric series converges to the stated value.

:::

:::

::: {.pf-step #high}

If $\norm{h}_p=1$, then $\sum_{k\ge0}2^{kq}\lambda_{Th}(2^k)\le C_2^{q_2}\big(1-2^{-(q_2-q)}\big)^{-1}$.

::: pf-proof

For integers $k\ge0$ the second weak-type hypothesis gives $\lambda_{Th}(2^k)\le C_2^{q_2}2^{-kq_2}$, so the sum is at most $C_2^{q_2}\sum_{k\ge0}2^{-k(q_2-q)}$.
Since $q<q_2$, this geometric series converges to the stated value.

:::

:::

::: pf-step

(ii) $\boxed{\norm{Tf}_q\le C_q\norm{f}_p}$ with $C_q^q=(2^q-1)\Big(C_1^{q_1}\big(1-2^{-(q-q_1)}\big)^{-1}+C_2^{q_2}\big(1-2^{-(q_2-q)}\big)^{-1}\Big)$.

::: pf-proof

Let $\norm{h}_p=1$.
Since $Th\in L^{q_1}$, $\abs{Th}<\infty$ almost everywhere.
Steps [](#low){.pf-ref} and [](#high){.pf-ref} bound $\sum_{k\in\ZZ}2^{kq}\lambda_{Th}(2^k)$ by $C_q^q/(2^q-1)$.
Step [](#part-i){.pf-ref}, applied to $Th$ with exponent $q$ and $\beta=2$, gives $\norm{Th}_q^q\le(2^q-1)\sum_{k\in\ZZ}2^{kq}\lambda_{Th}(2^k)\le C_q^q$.
Step [](#normalize){.pf-ref} turns this bound into the claim.

:::

:::

:::

:::
