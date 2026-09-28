---
schema: qual/card@1
id: P-BKF06-3A
kind: problem
title: Analytic continuation of $\sum\binom{2n}{n}z^n$ to $z=-2$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 3A of the retained Berkeley Fall 2006 preliminary-exam solution packet f06solution.pdf. The packet explicitly corrects the original target set from {3,-3} to {1/3,-1/3}.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the central-binomial generating function and the
    continuation argument. The proof globalizes the branch-free identity
    (1-4z)f(z)^2=1 on U, so no square-root branch on all of U is assumed.
---

::: {.problem}
Let $U$ be a connected open subset of $\mathbb C$ containing $-2$ and $0$.
Suppose $f:U\to\mathbb C$ is holomorphic and its Taylor expansion at $0$ is
\[
\sum_{n\ge0}\binom{2n}{n}z^n.
\]
Prove that
\[
f(-2)\in\left\{\frac13,-\frac13\right\}.
\]
:::

::: {.solution}
<1>1. In a neighborhood of $0$,
$$
f(z)=(1-4z)^{-1/2},
$$
where the branch is the one taking the value $1$ at $0$.

::: {.proof}
For $\abs z<1/4$, the generalized binomial series gives
$$
(1-4z)^{-1/2}
=
\sum_{n=0}^\infty
\binom{-1/2}{n}(-4z)^n.
$$
For $n=0$ the coefficient identity is immediate. For every $n\ge1$,
$$
\begin{aligned}
\binom{-1/2}{n}(-4)^n
&=
\frac{1\cdot3\cdots(2n-1)}{2^n n!}\,4^n
\\
&=
\frac{2^n(2n-1)!!}{n!}
\\
&=
\frac{(2n)!}{(n!)^2}
\\
&=
\binom{2n}{n}.
\end{aligned}
$$
Thus
$$
(1-4z)^{-1/2}
=
\sum_{n=0}^\infty\binom{2n}{n}z^n
$$
near $0$. This is exactly the Taylor series of $f$ there, so the two
holomorphic functions agree on some neighborhood of $0$.
:::

<1>2. The holomorphic function
$$
G(z)=(1-4z)f(z)^2-1
$$
vanishes identically on $U$.

::: {.proof}
The function $G$ is holomorphic on all of $U$. By step <1>1, on a
nonempty neighborhood of $0$ one has
$$
f(z)^2=(1-4z)^{-1},
$$
and hence $G(z)=0$ there. Since $U$ is connected, the identity theorem
implies
$$
G\equiv0
$$
on $U$.
:::

<1>3. At $z=-2$,
$$
f(-2)^2=\frac19.
$$

::: {.proof}
Step <1>2 gives
$$
(1-4z)f(z)^2=1
$$
for every $z\in U$. Since $-2\in U$,
$$
9f(-2)^2=1,
$$
which is the claimed identity.
:::

<1>4. Therefore
$$
\boxed{
f(-2)\in
\left\{
\frac13,-\frac13
\right\}
}.
$$

::: {.proof}
The only complex numbers whose square is $1/9$ are $1/3$ and $-1/3$,
so the conclusion follows from step <1>3.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required conclusion.
:::
:::

::: {.remark}
Erratum: the exam paper prints the set as $\{3,-3\}$. By the identity $(1-4z)f(z)^2=1$ on $U$, $f(-2)^2=1/9$, so the correct set is $\{1/3,-1/3\}$.
:::
