---
schema: qual/card@1
id: P-BKF84-2
kind: problem
title: Derivatives of $(A+tB)^k$ and $\operatorname{tr}(A+tB)^k$ at $t=0$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 2 of the deterministic MinerU Flash extraction. Flash drops the arrow in the limit; the card restores $t\to0$.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Checked the noncommutative telescoping identity for the matrix-power derivative and the cyclic-trace reduction of all $k$ terms.
---

::: {.problem}
Let $A,B$ be real $n\times n$ matrices and let $k$ be a positive integer. Find

1.
\[
\lim_{t\to0}\frac{(A+tB)^k-A^k}{t};
\]

2.
\[
\left.\frac d{dt}\operatorname{tr}(A+tB)^k\right|_{t=0}.
\]
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

For arbitrary square matrices $X,Y$ of the same size,
$$
X^k-Y^k
=
\sum_{j=0}^{k-1}
X^j(X-Y)Y^{k-1-j}.
$$

::: pf-proof

Expand the right-hand side:
$$
\begin{aligned}
\sum_{j=0}^{k-1}X^j(X-Y)Y^{k-1-j}
&=
\sum_{j=0}^{k-1}X^{j+1}Y^{k-1-j}
-
\sum_{j=0}^{k-1}X^jY^{k-j}.
\end{aligned}
$$
All intermediate terms cancel, leaving only $X^k-Y^k$. No
commutativity is used.

:::

:::

::: {.pf-step #s2}

The limit in Part (1) is
$$
\boxed{
\sum_{j=0}^{k-1}A^jBA^{k-1-j}
}.
$$

::: pf-proof

Apply step [](#s1){.pf-ref} with
$$
X=A+tB,
\qquad
Y=A.
$$
For $t\neq0$,
$$
\frac{(A+tB)^k-A^k}{t}
=
\sum_{j=0}^{k-1}
(A+tB)^jBA^{k-1-j}.
$$
Each summand depends continuously on $t$, so letting $t\to0$ gives
$$
\sum_{j=0}^{k-1}A^jBA^{k-1-j}.
$$

:::

:::

::: {.pf-step #s3}

The derivative in Part (2) is
$$
\boxed{
k\operatorname{tr}(BA^{k-1})
}.
$$

::: pf-proof

By linearity of trace and step [](#s2){.pf-ref},
$$
\left.
\frac d{dt}\operatorname{tr}(A+tB)^k
\right|_{t=0}
=
\sum_{j=0}^{k-1}
\operatorname{tr}\left(A^jBA^{k-1-j}\right).
$$
For every $j$, cyclicity of trace gives
$$
\operatorname{tr}\left(A^jBA^{k-1-j}\right)
=
\operatorname{tr}\left(BA^{k-1-j}A^j\right)
=
\operatorname{tr}(BA^{k-1}).
$$
There are $k$ summands, so the displayed formula follows.

:::

:::

::: pf-qed

Steps [](#s2){.pf-ref} and [](#s3){.pf-ref} give the two requested values.

:::

:::

:::
