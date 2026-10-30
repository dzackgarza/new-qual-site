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
  note: Verified the coefficient-sum estimate for every $\abs{z}\ge R$ and the resulting reverse-triangle-inequality exclusion of zeros.
---

::: {.problem}
Let $c_0,c_1,\ldots,c_{n-1}$ be complex numbers.
Prove that all the zeroes of the polynomial
$$
z^n+c_{n-1}z^{n-1}+\cdots+c_1z+c_0
$$
lie in the open disc with center $0$ and radius
$$
1+\abs{c_{n-1}}+\cdots+\abs{c_1}+\abs{c_0}.
$$
:::

::: {.solution}

Set
$$
R\coloneqq1+\sum_{k=0}^{n-1}\abs{c_k}.
$$

::: pf

::: {.pf-step #s1-1}

If $\abs{z}\geq R$, then
$$
\sum_{k=0}^{n-1}\abs{c_k}\abs{z}^k<\abs{z}^n.
$$


::: pf-proof

Since $R\geq1$, the hypothesis $\abs{z}\geq R$ gives $\abs{z}\geq1$. Hence, for $0\leq k\leq n-1$,
$$
\abs{z}^k\leq\abs{z}^{n-1}.
$$
Therefore
$$
\sum_{k=0}^{n-1}\abs{c_k}\abs{z}^k
\leq
\left(\sum_{k=0}^{n-1}\abs{c_k}\right)\abs{z}^{n-1}
=(R-1)\abs{z}^{n-1}.
$$
Because $R\leq\abs{z}$,
$$
(R-1)\abs{z}^{n-1}
\leq
(\abs{z}-1)\abs{z}^{n-1}
<
\abs{z}^n.
$$
This proves the claim.

:::

:::

::: {.pf-step #s1-2}

The polynomial
$$
p(z)=z^n+c_{n-1}z^{n-1}+\cdots+c_1z+c_0
$$
has no zero with $\abs{z}\geq R$.


::: pf-proof

For $\abs{z}\geq R$, step [](#s1-1){.pf-ref} and the reverse triangle inequality give
$$
\begin{aligned}
\abs{p(z)}
&\geq
\abs{z}^n-\sum_{k=0}^{n-1}\abs{c_k}\abs{z}^k\\
&>0.
\end{aligned}
$$
Thus $p(z)\neq0$.

:::

:::

::: {.pf-step #s1-3}

Every zero $\zeta$ of $p$ satisfies
$$
\abs{\zeta}<
1+\abs{c_{n-1}}+\cdots+\abs{c_1}+\abs{c_0}.
$$


::: pf-proof

This is the contrapositive of step [](#s1-2){.pf-ref} together with the definition of $R$.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} is exactly the asserted open-disc bound.

:::

:::

:::
