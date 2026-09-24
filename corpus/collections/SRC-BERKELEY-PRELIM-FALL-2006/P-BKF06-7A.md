---
schema: qual/card@1
id: P-BKF06-7A
kind: problem
title: The equation $1+z+az^n=0$ has a root in $\lvert z\rvert\le2$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 7A of the retained Berkeley Fall 2006 preliminary-exam solution packet f06solution.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked both cases of the retained argument: Vieta's
    product formula when |1/a|<=2^n and Rouche's theorem with the reverse
    triangle inequality on |z|=2 when |1/a|>2^n.
---

::: {.problem}
Prove that for every $a\in\mathbb C$ and every integer $n\ge2$, the equation
\[
1+z+az^n=0
\]
has at least one root in the disk $|z|\le2$.
:::

::: {.solution}
<1>1. If $a=0$, the equation has the root $z=-1$.

::: {.proof}
When $a=0$, the equation is
$$
1+z=0,
$$
whose root $-1$ satisfies $\abs{-1}=1\le2$.
:::

<1>2. Suppose $a\ne0$ and set
$$
b=\frac1a.
$$
Then the original equation is equivalent to
$$
q(z)=z^n+bz+b=0.
$$

::: {.proof}
Multiplying
$$
1+z+az^n=0
$$
by the nonzero scalar $b=1/a$ gives
$$
b+bz+z^n=0,
$$
which is exactly $q(z)=0$.
:::

<1>3. If $\abs b\le2^n$, then $q$ has a root $z$ with
$\abs z\le2$.

::: {.proof}
Let $z_1,\ldots,z_n$ be the roots of the monic polynomial $q$,
counted with multiplicity. Vieta's formula gives
$$
\abs{z_1\cdots z_n}=\abs b.
$$
If every root satisfied $\abs{z_j}>2$, then
$$
\abs b
=
\prod_{j=1}^n\abs{z_j}
>
2^n,
$$
contrary to the hypothesis. Hence at least one root lies in
$\abs z\le2$.
:::

<1>4. If $\abs b>2^n$, then $q$ has a root in $\abs z<2$.

::: {.proof}
Write
$$
q(z)=g(z)+h(z),
\qquad
g(z)=b(1+z),
\qquad
h(z)=z^n.
$$
On the circle $\abs z=2$,
$$
\abs{h(z)}=2^n<\abs b.
$$
The reverse triangle inequality gives
$$
\abs{g(z)}
=
\abs b\,\abs{1+z}
\ge
\abs b(\abs z-1)
=
\abs b.
$$
Thus
$$
\abs{h(z)}<\abs{g(z)}
$$
on $\abs z=2$. By Rouché's theorem, $q=g+h$ and $g$ have the same
number of zeros in $\abs z<2$, counted with multiplicity. The
function $g(z)=b(1+z)$ has exactly one zero there, namely $z=-1$.
Therefore $q$ also has a zero in $\abs z<2$.
:::

<1>5. For every $a\in\CC$ and every integer $n\ge2$, the equation
has a root in $\abs z\le2$.

::: {.proof}
Step <1>1 handles $a=0$. If $a\ne0$, step <1>2 reduces the problem
to $q(z)=0$. The alternatives $\abs b\le2^n$ and $\abs b>2^n$ are
exhaustive, and steps <1>3 and <1>4 give the required root in the two
cases.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 proves the required conclusion.
:::
:::
