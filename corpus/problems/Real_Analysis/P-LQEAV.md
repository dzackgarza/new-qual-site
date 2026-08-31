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
Show that for $0 < p < q \le \infty$,
$$
\|a\|_{\ell^q} \le \|a\|_{\ell^p}
$$
for any sequence $a = (a_j)_{j=1}^\infty \in \mathbb{C}^\mathbb{N}$, where $\|a\|_{\ell^\infty} := \sup_j |a_j|$ and $\|a\|_{\ell^r} := \left(\sum_{j=1}^\infty |a_j|^r\right)^{1/r}$ for $r < \infty$.
:::

::: solution
**Goal:** Prove the sequence norm inequality $\|a\|_{\ell^q} \le \|a\|_{\ell^p}$ for $0 < p < q \le \infty$.

<1>1. Case 1: $q = \infty$ (where $0 < p < \infty$).
::: {.proof}
<2>1. If $\|a\|_{\ell^p} = \infty$, the inequality $\|a\|_{\ell^\infty} \le \infty$ is immediate.
<2>2. Assume $\|a\|_{\ell^p} < \infty$. For every fixed index $k \ge 1$:
$$|a_k|^p \le \sum_{j=1}^\infty |a_j|^p = \|a\|_{\ell^p}^p.$$
<2>3. Taking the $(1/p)$-th power of both sides (since $t \mapsto t^{1/p}$ is strictly increasing on $[0, \infty)$):
$$|a_k| \le \|a\|_{\ell^p} \quad \text{for all } k \ge 1.$$
<2>4. Taking the supremum over all $k \ge 1$:
$$\|a\|_{\ell^\infty} = \sup_{k \ge 1} |a_k| \le \|a\|_{\ell^p}.$$
:::

<1>2. Case 2: $q < \infty$ (where $0 < p < q < \infty$).
::: {.proof}
<2>1. If $\|a\|_{\ell^p} = 0$, then $a_j = 0$ for all $j$, so $\|a\|_{\ell^q} = 0 = \|a\|_{\ell^p}$.
<2>2. If $\|a\|_{\ell^p} = \infty$, the inequality holds trivially.
<2>3. Assume $0 < \|a\|_{\ell^p} < \infty$. Define the normalized sequence $b = (b_j)_{j=1}^\infty$ by $b_j = \frac{a_j}{\|a\|_{\ell^p}}$.
<2>4. The normalized sequence satisfies
$$\|b\|_{\ell^p}^p = \sum_{j=1}^\infty |b_j|^p = \sum_{j=1}^\infty \frac{|a_j|^p}{\|a\|_{\ell^p}^p} = 1.$$
<2>5. In particular, for every index $j \ge 1$, $|b_j|^p \le \sum_{k=1}^\infty |b_k|^p = 1$, which implies $|b_j| \le 1$.
<2>6. Since $q > p > 0$ and $|b_j| \le 1$, the exponent comparison gives
$$|b_j|^q = |b_j|^{q-p} |b_j|^p \le 1^{q-p} |b_j|^p = |b_j|^p \quad \text{for every } j \ge 1.$$
<2>7. Summing over all $j \ge 1$:
$$\|b\|_{\ell^q}^q = \sum_{j=1}^\infty |b_j|^q \le \sum_{j=1}^\infty |b_j|^p = \|b\|_{\ell^p}^p = 1.$$
<2>8. Taking the $(1/q)$-th power gives $\|b\|_{\ell^q} \le 1^{1/q} = 1$.
<2>9. Multiplying both sides by the positive scalar $\|a\|_{\ell^p}$:
$$\|a\|_{\ell^q} = \|a\|_{\ell^p} \|b\|_{\ell^q} \le \|a\|_{\ell^p} \cdot 1 = \|a\|_{\ell^p}.$$
:::

<1>3. Conclusion:
::: {.proof}
The inequality $\|a\|_{\ell^q} \le \|a\|_{\ell^p}$ holds for all $0 < p < q \le \infty$.
:::
