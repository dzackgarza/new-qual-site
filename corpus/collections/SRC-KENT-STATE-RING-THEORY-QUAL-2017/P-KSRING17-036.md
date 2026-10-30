---
schema: qual/card@1
id: P-KSRING17-036
kind: problem
title: Reducibility of $x^2+1$ over $\ZZ_p$ for $p\equiv 1 \pmod 4$
classification:
  areas: [algebra]
  topics:
  - Finite Fields
  - Irreducible Polynomials
  - Quadratic Residues
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 36 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Show that if $p$ is a prime such that $p \equiv 1 \pmod{4}$, then $x^{2} + 1$ is not irreducible in $\ZZ_{p}[x]$.
:::

::: {.solution}

Write
$$
p=4m+1.
$$

::: pf

::: {.pf-step #s1-1}

Wilson's theorem gives
$$
(p-1)!\equiv-1\pmod p.
$$


::: pf-proof

This is Wilson's theorem for the prime $p$.

:::

:::

::: {.pf-step #s1-2}

One has
$$
(p-1)!
\equiv
(-1)^{(p-1)/2}
\left(
\left(\frac{p-1}{2}\right)!
\right)^2
\pmod p.
$$


::: pf-proof

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

:::

::: {.pf-step #s1-3}

Since
$$
p\equiv1\pmod4,
$$
one has
$$
(-1)^{(p-1)/2}=1.
$$


::: pf-proof

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

:::

::: {.pf-step #s1-4}

The element
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


::: pf-proof

Combine steps [](#s1-1){.pf-ref} through [](#s1-3){.pf-ref}:
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

:::

::: {.pf-step #s1-5}

Therefore
$$
x^2+1
$$
is reducible in
$$
\FF_p[x].
$$


::: pf-proof

By step [](#s1-4){.pf-ref},
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

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the required conclusion.

:::

:::

:::
