---
schema: qual/card@1
id: P-UMNCP-S12-04
kind: problem
title: A derivative cannot have a simple pole on a punctured disk
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Spring 2012, 4 as reproduced in Cihan Bahran's vendored 2013 University of Minnesota complex-prelim solution compilation.
---

::: {.problem}
Prove that there is no function $f$ analytic on the punctured disk $\DD\setminus\{0\}$ such that $f'$ has a simple pole at $0$.
:::

::: {.solution}

::: pf

::: pf-step

Since $f$ is analytic on the punctured disk, it has a Laurent expansion
$$
f(z)
=
\sum_{n=-\infty}^{\infty}
a_nz^n
$$
valid for
$$
0<\abs{z}<1.
$$


::: pf-proof

The punctured disk is an annulus centered at the origin, so Laurent's theorem applies.

:::

:::

::: pf-step

Differentiating term by term gives
$$
f'(z)
=
\sum_{n=-\infty}^{\infty}
n a_n z^{n-1}.
$$


::: pf-proof

Laurent series may be differentiated term by term on every compact subannulus
$$
r\le\abs{z}\le R
$$
with
$$
0<r<R<1.
$$
The differentiated series therefore represents $f'$ on the punctured disk.

:::

:::

::: {.pf-step #s1-3}

The coefficient of
$$
z^{-1}
$$
in the Laurent expansion of $f'$ is zero.


::: pf-proof

A term
$$
z^{-1}
$$
in
$$
n a_n z^{n-1}
$$
would require
$$
n-1=-1,
$$
hence
$$
n=0.
$$
But the corresponding coefficient is
$$
n a_n
=
0\cdot a_0
=0.
$$
Therefore
$$
\operatorname{Res}_{z=0}f'=0.
$$

:::

:::

::: {.pf-step #s1-4}

A function with a simple pole at $0$ has a nonzero
$$
z^{-1}
$$
coefficient in its Laurent expansion.


::: pf-proof

By definition, if a meromorphic function $g$ has a simple pole at $0$, then its Laurent expansion has the form
$$
g(z)
=
\frac{c_{-1}}z
+c_0+c_1z+\cdots,
$$
with
$$
c_{-1}\ne0.
$$
Equivalently, its residue at the pole is nonzero.

:::

:::

::: {.pf-step #s1-5}

Therefore $f'$ cannot have a simple pole at $0$.


::: pf-proof

Step [](#s1-3){.pf-ref} says that the $z^{-1}$ coefficient of $f'$ is zero. Step [](#s1-4){.pf-ref} says that a simple pole would require that coefficient to be nonzero. These conditions are incompatible.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} proves that no such analytic function $f$ exists.

:::

:::

:::
