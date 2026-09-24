---
schema: qual/card@1
id: P-BKF07-8B
kind: problem
title: Irreducible rational polynomials with all roots real
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
  note: Checked against the vendored UC Berkeley Fall 2007 preliminary-exam solution packet, which reproduces the problem statement with its solution.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the Eisenstein argument and the alternating-sign
    construction of n distinct real roots, specializing the source construction
    to spacing four.
---

::: {.problem}
Show that for every positive integer \(n\), there exists an irreducible polynomial over \(\mathbb Q\) of degree \(n\) all of whose roots are real.
:::

::: {.solution}
For $n\ge1$, define
$$
F_n(x)\coloneqq\prod_{k=1}^n(x-4k),
\qquad
G_n(x)\coloneqq F_n(x)+2.
$$

<1>1. The polynomial $G_n\in\ZZ[x]$ has degree $n$ and is
irreducible over $\QQ$.

::: {.proof}
The polynomial $F_n$ is monic of degree $n$. Every nonleading
coefficient of $F_n$ is divisible by $4$, because every elementary
symmetric polynomial of positive degree in $4,8,\ldots,4n$ is
divisible by $4$. Hence every nonleading coefficient of $G_n$ is
divisible by $2$.

The constant term of $G_n$ is
$$
2+(-4)^n n!,
$$
which is congruent to $2$ modulo $4$. Thus its constant term is not
divisible by $4$, while the leading coefficient is $1$ and is not
divisible by $2$. Eisenstein's criterion at the prime $2$ shows that
$G_n$ is irreducible over $\QQ$.
:::

<1>2. For $n=1$, the polynomial $G_1$ has one real root.

::: {.proof}
Here
$$
G_1(x)=2+(x-4)=x-2.
$$
Its unique root is $2$.
:::

<1>3. Suppose $n\ge2$. For $1\le j\le n-1$, set
$$
x_j\coloneqq4\left(j+\frac12\right)=4j+2.
$$
Then
$$
\operatorname{sgn}G_n(x_j)=(-1)^{n-j}.
$$

::: {.proof}
Directly,
$$
F_n(x_j)
=4^n\prod_{k=1}^n\left(j+\frac12-k\right).
$$
Exactly $n-j$ factors in the product are negative, so
$$
\operatorname{sgn}F_n(x_j)=(-1)^{n-j}.
$$
The two factors nearest zero have absolute value $1/2$, while every
other factor has absolute value at least $3/2$. Therefore
$$
\abs{F_n(x_j)}
\ge \frac{4^n}{4}
=4^{n-1}
>2.
$$
Since $G_n(x_j)=F_n(x_j)+2$, adding $2$ cannot change the sign, which
proves the claim.
:::

<1>4. For $n\ge2$, the polynomial $G_n$ has at least one real root in
each of the $n$ disjoint intervals
$$
(-\infty,x_1),\quad
(x_1,x_2),\quad\ldots,\quad
(x_{n-2},x_{n-1}),\quad
(x_{n-1},\infty).
$$

::: {.proof}
Step <1>3 shows that the signs at consecutive $x_j$ alternate, so the
intermediate value theorem gives a root in every interval
$(x_j,x_{j+1})$.

Because $G_n$ is monic of degree $n$,
$$
\lim_{x\to\infty}G_n(x)=+\infty,
\qquad
\operatorname{sgn}G_n(x)=(-1)^n
\quad\text{for all sufficiently negative }x.
$$
Step <1>3 gives
$\operatorname{sgn}G_n(x_1)=(-1)^{n-1}$ and
$\operatorname{sgn}G_n(x_{n-1})=-1$. Thus the intermediate value
theorem also gives a root in $(-\infty,x_1)$ and a root in
$(x_{n-1},\infty)$.
:::

<1>5. All $n$ roots of $G_n$ are real.

::: {.proof}
For $n=1$, this is step <1>2. For $n\ge2$, step <1>4 gives $n$
distinct real roots because the listed intervals are disjoint. Since
$G_n$ has degree $n$, it has no further roots over $\CC$.
:::

<1>6. For every positive integer $n$, the polynomial
$$
\boxed{G_n(x)=2+\prod_{k=1}^n(x-4k)}
$$
is irreducible over $\QQ$, has degree $n$, and has only real roots.

::: {.proof}
Irreducibility and degree are step <1>1, and reality of all roots is
step <1>5.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 supplies the required polynomial for every $n\ge1$.
:::
:::
