---
schema: qual/card@1
id: P-KSRING17-036
kind: problem
title: Reducibility of $x^2+1$ over $\mathbb Z_p$ for $p\equiv 1 \pmod 4$
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 36 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Show that if p is a prime such that $p \equiv 1 { \bigl ( } { \mathrm { m o d ~ } } 4 { \bigr ) }$ , then $x ^ { 2 } + 1$ is not irreducible in $\mathbb { Z } _ { p } [ x ]$
:::

::: {.solution}
Write
$$
p=4m+1.
$$

<1>1. Wilson's theorem gives
$$
(p-1)!\equiv-1\pmod p.
$$

::: {.proof}
This is Wilson's theorem for the prime $p$.
:::

<1>2. One has
$$
(p-1)!
\equiv
(-1)^{(p-1)/2}
\left(
\left(\frac{p-1}{2}\right)!
\right)^2
\pmod p.
$$

::: {.proof}
Pair the factors
$$
1,2,\ldots,p-1
$$
as
$$
k
\quad\text{and}\quad
p-k
$$
for
$$
1\le k\le\frac{p-1}{2}.
$$
Then
$$
\begin{aligned}
(p-1)!
&=
\prod_{k=1}^{(p-1)/2}
k(p-k)\\
&\equiv
\prod_{k=1}^{(p-1)/2}
(-k^2)\\
&=
(-1)^{(p-1)/2}
\left(
\left(\frac{p-1}{2}\right)!
\right)^2
\pmod p.
\end{aligned}
$$
:::

<1>3. Since
$$
p\equiv1\pmod4,
$$
one has
$$
(-1)^{(p-1)/2}=1.
$$

::: {.proof}
The congruence
$$
p\equiv1\pmod4
$$
means
$$
p-1
$$
is divisible by $4$. Hence
$$
\frac{p-1}{2}
$$
is even.
:::

<1>4. The element
$$
a
\coloneqq
\left(\frac{p-1}{2}\right)!
\in
\FF_p
$$
satisfies
$$
a^2=-1.
$$

::: {.proof}
Combine steps <1>1--<1>3:
$$
-1
\equiv
(p-1)!
\equiv
a^2
\pmod p.
$$
Thus
$$
a^2+1=0
$$
in $\FF_p$.
:::

<1>5. Therefore
$$
x^2+1
$$
is reducible in
$$
\FF_p[x].
$$

::: {.proof}
By step <1>4,
$$
a
$$
is a root of
$$
x^2+1.
$$
Hence the factor theorem gives
$$
x^2+1
=
(x-a)(x+a)
$$
in $\FF_p[x]$.
Both factors have positive degree, so the polynomial is not irreducible.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required conclusion.
:::
:::
