---
schema: qual/card@1
id: E-SMI-8000E-ED9
kind: problem
title: Factorization length bounded by the size function
classification:
  areas:
  - algebra
  topics:
  - Euclidean Domains
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-11
  note: "Compared the strongly-Euclidean definition and factorization-length request with the local 8000e extraction, Euclidean-domains problem 9."
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Used strict size decrease on nonunit factors to obtain irreducible factorization by induction, then bounded its length from the strictly increasing integer sizes of successive partial products."
---

::: {.exercise}
Prove that if $a$ is a nonzero, nonunit element of a strongly Euclidean domain, then $a$ can be factored into at most $\abs{a}$ irreducible elements.

[A domain is called "strongly Euclidean" if it is a Euclidean domain with a size function $\abs{\cdot}$ satisfying $\abs{ab} = \abs{a}$ if $b$ is a unit, and $\abs{a} < \abs{ab}$ and $\abs{b} > 0$ if $b$ is not a unit.]
:::


::: {.solution}
Write $\delta(a)=\lvert a\rvert$ for the strongly Euclidean size.

<1>1. Every nonzero nonunit factors into finitely many irreducibles.
::: {.proof}
We use induction on the positive integer $\delta(a)$. Since $a$ is a nonunit,
the strong Euclidean hypothesis gives
$$
\delta(a)>0.
$$
If $a$ is irreducible, there is nothing to prove.

If $a$ is reducible, write
$$
a=bc
$$
with both $b$ and $c$ nonunits. Because $c$ is a nonunit,
$$
\delta(b)<\delta(bc)=\delta(a).
$$
Similarly, because $b$ is a nonunit,
$$
\delta(c)<\delta(cb)=\delta(a).
$$
Thus both $b$ and $c$ have strictly smaller positive size. By induction each
factors into finitely many irreducibles, and multiplying those factorizations
gives one for $a$.
:::

<1>2. In any irreducible factorization of $a$, the sizes of successive partial products strictly increase.
::: {.proof}
Let
$$
a=p_1p_2\cdots p_r
$$
be a factorization into irreducibles. Every irreducible is a nonunit. Define
$$
q_j=p_1p_2\cdots p_j.
$$
For $1\le j<r$, the factor $p_{j+1}$ is a nonunit, so strong Euclideanity gives
$$
\delta(q_j)<\delta(q_jp_{j+1})=\delta(q_{j+1}).
$$
Also $p_1$ is a nonunit, so
$$
\delta(q_1)=\delta(p_1)>0.
$$
Hence
$$
0<\delta(q_1)<\delta(q_2)<\cdots<\delta(q_r)=\delta(a).
$$
:::

<1>3. Bound the number of irreducible factors by $\lvert a\rvert$.
::: {.proof}
The numbers
$$
\delta(q_1),\ldots,\delta(q_r)
$$
are $r$ distinct positive integers, all at most $\delta(a)$. There are only
$\delta(a)$ positive integers from $1$ through $\delta(a)$. Therefore
$$
r\le\delta(a)=\lvert a\rvert.
$$
Thus $a$ admits a factorization into at most
$$
\boxed{\lvert a\rvert}
$$
irreducible elements.
:::
:::
