---
schema: qual/card@1
id: P-BKS13-4B
kind: problem
title: Cauchy estimate for derivatives on a compact subset
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-25
  note: Compared the authored statement with page 4 of the retained Spring 2013 solution PDF and independently reviewed the Cauchy derivative estimate.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the uniform radius argument, the limit r->D, and the U=C case via Liouville's theorem.
---

::: {.problem}
Let $U$ be an open subset of $\CC$.
Let $K$ be a closed bounded subset of $\CC$ that is contained in $U$.
Put
$$
D=\min_{p\in K,\ q\notin U}|p-q|.
$$
That is, $D$ is the closest distance between $K$ and $\CC\setminus U$.
(If $U=\CC$, then we put $D=\infty$.)

Suppose that $f$ is an analytic function on $U$ so that for all $z\in U$, we have $|f(z)|\le M$.
Here $M$ is a fixed positive number.
Find an explicit number $C<\infty$, depending on $M$ and $D$, so that for all $z_0\in K$ we have $|f'(z_0)|\le C$.
Justify your answer.
:::

::: {.solution}

::: pf

::: pf-step

If $U\neq\CC$, then
$$
D>0.
$$

::: pf-proof

The set $K$ is closed and bounded in $\CC$, hence compact. The complement
$$
\CC\setminus U
$$
is closed and disjoint from $K$. A compact set and a disjoint closed set
in a metric space have positive distance. Thus the stated distance $D$ is
positive.

:::

:::

::: {.pf-step #s2}

Fix
$$
z_0\in K
$$
and
$$
0<r<D.
$$
Then the closed disk
$$
\overline{B(z_0,r)}
$$
is contained in $U$.

::: pf-proof

If some point $w$ of the closed disk lay outside $U$, then
$$
\abs{z_0-w}
\leq
r
<
D,
$$
contradicting the definition of $D$ as the distance from $K$ to
$\CC\setminus U$.

:::

:::

::: {.pf-step #s3}

Under the hypotheses of step [](#s2){.pf-ref},
$$
\abs{f'(z_0)}
\leq
\frac{M}{r}.
$$

::: pf-proof

By Cauchy's integral formula for derivatives,
$$
f'(z_0)
=
\frac{1}{2\pi i}
\int_{\abs{z-z_0}=r}
\frac{f(z)}{(z-z_0)^2}\,dz.
$$
On the circle,
$$
\abs{f(z)}\leq M
\qquad\text{and}\qquad
\abs{z-z_0}=r.
$$
Its length is $2\pi r$, so
$$
\abs{f'(z_0)}
\leq
\frac{1}{2\pi}
\frac{M}{r^2}
(2\pi r)
=
\frac{M}{r}.
$$

:::

:::

::: {.pf-step #s4}

If $U\neq\CC$, then for every $z_0\in K$,
$$
\abs{f'(z_0)}
\leq
\frac{M}{D}.
$$

::: pf-proof

Step [](#s3){.pf-ref} holds for every
$$
0<r<D.
$$
Letting $r\to D^-$ gives the claimed bound.

:::

:::

::: {.pf-step #s5}

If $U=\CC$, then
$$
f'(z)=0
$$
for every $z\in\CC$.

::: pf-proof

The function $f$ is a bounded entire function. Liouville's theorem implies
that $f$ is constant, hence its derivative vanishes identically.

:::

:::

::: {.pf-step #s6}

An explicit valid choice is
$$
\boxed{
C=
\begin{cases}
M/D,&D<\infty,\\
0,&D=\infty.
\end{cases}
}
$$

::: pf-proof

If $D<\infty$, the definition of the problem gives $U\neq\CC$, and step
[](#s4){.pf-ref} applies. If $D=\infty$, then $U=\CC$ by the stated convention, and
step [](#s5){.pf-ref} applies.

:::

:::

::: pf-qed

Step [](#s6){.pf-ref} supplies the required uniform derivative bound.

:::

:::

:::
