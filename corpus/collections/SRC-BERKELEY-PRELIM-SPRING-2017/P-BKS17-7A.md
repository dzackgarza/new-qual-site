---
schema: qual/card@1
id: P-BKS17-7A
kind: problem
title: Orthogonal matrices mapping one vector to another of equal norm
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored spaces around inline math and normalized LaTeX against Sp17_Exam_0.pdf page 8 problem 7A.
- event: source-checked
  by: chatgpt
  date: 2026-10-02
  note: Independently reviewed the supplied Berkeley Spring 2017 Householder-reflection solution. Its claim that $uu^T$ projects onto the hyperplane perpendicular to $x-y$ is reversed; $uu^T$ projects onto the normal line. The solution below verifies the construction directly.
- event: solution-written
  by: chatgpt
  date: 2026-10-02
- event: solution-reviewed
  by: chatgpt
  date: 2026-10-02
  note: Verified the equal-vector case, the Householder calculation when $x\neq y$, orthogonality, and norm preservation in the unequal-norm case.
---

::: {.problem}
Given two vectors $x$ and $y$ in $\RR^n$ with $\norm{x}_2 = \norm{y}_2$, construct an orthogonal matrix $Q$ such that $Qx = y$. Can there be such a matrix if $\norm{x}_2 \neq \norm{y}_2$?
:::

::: pf

::: pf-step

If $\|x\|_2=\|y\|_2$ and $x=y$, then the choice
$$
\boxed{Q=I}
$$
is orthogonal and satisfies $Qx=y$.


::: pf-proof

The identity matrix satisfies $I^TI=I$, and $Ix=x=y$.

:::

:::

::: pf-step

Suppose $\|x\|_2=\|y\|_2$ and $x\neq y$, and define
$$
u\coloneqq\frac{x-y}{\|x-y\|_2},
\qquad
\boxed{Q=I-2uu^T}.
$$
Then $u^Tu=1$.


::: pf-proof

Since $x\neq y$, the denominator is nonzero. Hence
$$
u^Tu
=
\frac{(x-y)^T(x-y)}{\|x-y\|_2^2}
=1.
$$

:::

:::

::: pf-step

The matrix $Q$ from step <1>2 is orthogonal.


::: pf-proof

Since $uu^T$ is symmetric and $u^Tu=1$ by step <1>2,
$$
\begin{aligned}
Q^TQ
&=(I-2uu^T)^2\\
&=I-4uu^T+4u(u^Tu)u^T\\
&=I.
\end{aligned}
$$
Thus $Q$ is orthogonal.

:::

:::

::: pf-step

Under the hypotheses of step <1>2,
$$
2uu^Tx=x-y.
$$


::: pf-proof

Because $\|x\|_2=\|y\|_2$,
$$
\begin{aligned}
\|x-y\|_2^2
&=(x-y)^T(x-y)\\
&=\|x\|_2^2+\|y\|_2^2-2x^Ty\\
&=2(\|x\|_2^2-x^Ty).
\end{aligned}
$$
Also
$$
(x-y)^Tx=\|x\|_2^2-y^Tx=\|x\|_2^2-x^Ty.
$$
Therefore
$$
\begin{aligned}
2uu^Tx
&=2\frac{(x-y)(x-y)^Tx}{\|x-y\|_2^2}\\
&=2\frac{(x-y)(\|x\|_2^2-x^Ty)}{2(\|x\|_2^2-x^Ty)}\\
&=x-y.
\end{aligned}
$$
The cancelled scalar is nonzero because, by the displayed norm identity, it equals $\|x-y\|_2^2/2>0$.

:::

:::

::: pf-step

The matrix $Q$ from step <1>2 satisfies $Qx=y$.


::: pf-proof

By step <1>4,
$$
Qx=(I-2uu^T)x=x-(x-y)=y.
$$

:::

:::

::: pf-step

If $\|x\|_2\neq\|y\|_2$, there is no orthogonal matrix $Q$ satisfying $Qx=y$.


::: pf-proof

If $Q$ were orthogonal and $Qx=y$, then
$$
\|y\|_2^2
=
\|Qx\|_2^2
=
x^TQ^TQx
=
x^Tx
=
\|x\|_2^2,
$$
contrary to the hypothesis.

:::

:::

::: pf-qed

Steps <1>1 and <1>2--<1>5 construct the required orthogonal matrix when the norms are equal, and step <1>6 proves impossibility when the norms are unequal.

:::

:::
