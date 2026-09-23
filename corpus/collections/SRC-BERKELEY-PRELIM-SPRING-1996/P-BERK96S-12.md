---
schema: qual/card@1
id: P-BERK96S-12
kind: problem
title: The range of $X\mapsto X+X^2$ contains a neighborhood of the zero matrix
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
- event: solution-written
  by: chatgpt
  date: 2026-09-23
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-23
  note: >-
    Verified that DF at the zero matrix is the identity and that the inverse
    function theorem gives a neighborhood of zero contained in the range.
---

::: {.problem}
Identify the real vector space $M_{2\times2}(\mathbb R)$ with $\mathbb R^4$ and define
\[
F:M_{2\times2}(\mathbb R)\to M_{2\times2}(\mathbb R),
\qquad
F(X)=X+X^2.
\]
Prove that the range of $F$ contains a neighborhood of the zero matrix.
:::

::: {.solution}
Regard $M_{2\times2}(\RR)$ as the real vector space $\RR^4$.

<1>1. The derivative of $F$ at the zero matrix is the identity map on
$M_{2\times2}(\RR)$.

::: {.proof}
For $H\in M_{2\times2}(\RR)$,
$$
\begin{aligned}
F(H)-F(0)
&=
H+H^2.
\end{aligned}
$$
Since
$$
\frac{\norm{H^2}}{\norm H}
\leq
\norm H
\longrightarrow0
\qquad(H\to0)
$$
for any submultiplicative matrix norm, the linear part is $H$. Hence
$$
DF_0(H)=H.
$$
Thus $DF_0$ is the identity and in particular is invertible.
:::

<1>2. There are neighborhoods $U$ and $V$ of the zero matrix such that
$$
F:U\longrightarrow V
$$
is a diffeomorphism.

::: {.proof}
The map $F$ is polynomial, hence continuously differentiable. By step <1>1,
its derivative at $0$ is invertible. The inverse function theorem therefore
gives neighborhoods $U$ of $0$ and $V$ of
$$
F(0)=0
$$
for which the displayed restriction is a diffeomorphism.
:::

<1>3. The range of $F$ contains a neighborhood of the zero matrix.

::: {.proof}
By step <1>2,
$$
V=F(U).
$$
Hence
$$
V\subseteq F\bigl(M_{2\times2}(\RR)\bigr),
$$
and $V$ is a neighborhood of $0$.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 is the required conclusion.
:::
:::
