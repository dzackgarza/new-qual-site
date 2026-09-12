---
schema: qual/card@1
id: E-SMI-8000E-ED1
kind: problem
title: Every ideal in a Euclidean domain is principal
classification:
  areas:
  - algebra
  topics:
  - Euclidean Domains
  - Principal Ideal Domains
  - Ideals
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-11
  note: "Compared the statement and minimum-size hint with the local 8000e extraction, Euclidean-domains problem 1."
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Chose a nonzero ideal element of minimal Euclidean size, used division to force zero remainder, and identified a nonzero principal ideal with R because R is a domain."
---

::: {.exercise}
Assume $R$ is a Euclidean domain.
Prove every ideal $I$ in $R$ is principal, i.e. is a cyclic module.

[Hint: if $I$ contains nonzero elements, choose one $x$ of smallest size, and prove $x$ divides all the other elements of $I$.] Conclude that either $I = \{0\}$, or $I$ is isomorphic to $R$.
:::


::: solution
Let
$$
\delta:R\setminus\{0\}\longrightarrow\mathbb Z
$$
be a Euclidean size function.

<1>1. If $I\ne0$, choose a nonzero element $x\in I$ of minimal Euclidean size.
::: proof
The set
$$
\{\delta(y):0\ne y\in I\}
$$
is a nonempty subset of $\mathbb Z$ bounded below, so it has a least element.
Choose $0\ne x\in I$ attaining that minimum.
:::

<1>2. The element $x$ divides every element of $I$.
::: proof
Let $y\in I$. If $y=0$, the assertion is trivial. If $y\ne0$, Euclidean
division by $x$ gives
$$
y=qx+r
$$
with either $r=0$ or
$$
\delta(r)<\delta(x).
$$
Since $x,y\in I$ and $I$ is an ideal,
$$
r=y-qx\in I.
$$
If $r\ne0$, this contradicts the minimality of $\delta(x)$. Hence $r=0$ and
$$
y=qx.
$$
Thus every $y\in I$ lies in $(x)$.
:::

<1>3. Every ideal of $R$ is principal.
::: proof
Because $x\in I$, one has
$$
(x)\subseteq I.
$$
Step <1>2 gives the reverse inclusion, so
$$
I=(x).
$$
If $I=0$, then of course
$$
I=(0).
$$
Thus every ideal is principal.
:::

<1>4. A nonzero ideal is isomorphic to $R$ as an $R$-module.
::: proof
If $I=(x)$ with $x\ne0$, define
$$
\mu_x:R\longrightarrow I,
\qquad
r\longmapsto rx.
$$
This map is $R$-linear and surjective by definition of $(x)$. Since $R$ is a
domain and $x\ne0$,
$$
rx=0\Longrightarrow r=0,
$$
so $\mu_x$ is injective. Hence
$$
\boxed{I\cong R.}
$$
Therefore every ideal is either $0$ or an $R$-module isomorphic to $R$.
:::
:::
