---
schema: qual/card@1
id: P-BERK90S-06
kind: problem
title: A continuous moment curve whose values at any three distinct parameters form a basis
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: source-checked
  by: chatgpt
  date: 2026-09-22
  note: Compared Problem 6 with the retained MinerU Flash extraction of Spring90.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-22
---

::: {.problem}
Give an example of a continuous function
$$
v:\RR\to\RR^3
$$
such that $v(t_1),v(t_2),v(t_3)$ form a basis of $\RR^3$ whenever $t_1,t_2,t_3$ are distinct real numbers.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The function $v\colon\RR\to\RR^3$ given by
$$
v(t)=\boxed{(1,t,t^2)}
$$
is continuous.

::: pf-proof

Each coordinate function is a polynomial in $t$, hence is continuous on
$\RR$. Therefore $v$ is continuous as a map to $\RR^3$.

:::

:::

::: {.pf-step #s2}

For any distinct real numbers $t_1,t_2,t_3$, the vectors
$v(t_1),v(t_2),v(t_3)$ form a basis of $\RR^3$.

::: pf-proof

Fix distinct $t_1,t_2,t_3\in\RR$. The matrix whose columns are these
vectors in the standard coordinates is
$$
V\coloneqq
\begin{pmatrix}
1&1&1\\
t_1&t_2&t_3\\
t_1^2&t_2^2&t_3^2
\end{pmatrix}.
$$
Subtracting the first column from the second and third columns, and then
expanding along the first row, gives
$$
\begin{aligned}
\det V
&=\det\begin{pmatrix}
t_2-t_1&t_3-t_1\\
t_2^2-t_1^2&t_3^2-t_1^2
\end{pmatrix}\\
&=(t_2-t_1)(t_3-t_1)
\det\begin{pmatrix}1&1\\t_2+t_1&t_3+t_1\end{pmatrix}\\
&=(t_2-t_1)(t_3-t_1)(t_3-t_2).
\end{aligned}
$$
The parameters are pairwise distinct, so every factor is nonzero.
Thus $V$ is invertible, and its columns form a basis of $\RR^3$.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} verify continuity and the required basis property for
the displayed function.

:::

:::

:::
