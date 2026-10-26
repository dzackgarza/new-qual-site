---
schema: qual/card@1
id: P-BKS19-4B
kind: problem
title: Bound on the zeros of a monic complex polynomial
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UC Berkeley Spring 2019 Graduate Preliminary Examination.
- event: source-checked
  by: chatgpt
  date: 2026-10-02
  note: Independently reviewed the supplied Berkeley Spring 2019 dominant-leading-term argument. It is correct; the solution below makes the strict inequality on the boundary of the stated disc explicit.
- event: solution-written
  by: chatgpt
  date: 2026-10-02
- event: solution-reviewed
  by: chatgpt
  date: 2026-10-02
  note: Verified the coefficient-sum estimate for every $|z|\ge R$ and the resulting reverse-triangle-inequality exclusion of zeros.
---

::: {.problem}
Let $c_0,c_1,\ldots,c_{n-1}$ be complex numbers.
Prove that all the zeroes of the polynomial
$$
z^n+c_{n-1}z^{n-1}+\cdots+c_1z+c_0
$$
lie in the open disc with center $0$ and radius
$$
1+|c_{n-1}|+\cdots+|c_1|+|c_0|.
$$
:::

Set
$$
R\coloneqq1+\sum_{k=0}^{n-1}|c_k|.
$$

::: pf

::: pf-step

If $|z|\geq R$, then
$$
\sum_{k=0}^{n-1}|c_k||z|^k<|z|^n.
$$


::: pf-proof

Since $R\geq1$, the hypothesis $|z|\geq R$ gives $|z|\geq1$. Hence, for $0\leq k\leq n-1$,
$$
|z|^k\leq|z|^{n-1}.
$$
Therefore
$$
\sum_{k=0}^{n-1}|c_k||z|^k
\leq
\left(\sum_{k=0}^{n-1}|c_k|\right)|z|^{n-1}
=(R-1)|z|^{n-1}.
$$
Because $R\leq|z|$,
$$
(R-1)|z|^{n-1}
\leq
(|z|-1)|z|^{n-1}
<
|z|^n.
$$
This proves the claim.

:::

:::

::: pf-step

The polynomial
$$
p(z)=z^n+c_{n-1}z^{n-1}+\cdots+c_1z+c_0
$$
has no zero with $|z|\geq R$.


::: pf-proof

For $|z|\geq R$, step <1>1 and the reverse triangle inequality give
$$
\begin{aligned}
|p(z)|
&\geq
|z|^n-\sum_{k=0}^{n-1}|c_k||z|^k\\
&>0.
\end{aligned}
$$
Thus $p(z)\neq0$.

:::

:::

::: pf-step

Every zero $\zeta$ of $p$ satisfies
$$
|\zeta|<
1+|c_{n-1}|+\cdots+|c_1|+|c_0|.
$$


::: pf-proof

This is the contrapositive of step <1>2 together with the definition of $R$.

:::

:::

::: pf-qed

Step <1>3 is exactly the asserted open-disc bound.

:::

:::
