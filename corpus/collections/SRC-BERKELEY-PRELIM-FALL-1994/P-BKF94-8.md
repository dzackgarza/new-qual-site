---
schema: qual/card@1
id: P-BKF94-8
kind: problem
title: Degree of $\mathbb Q(\sin(\theta/3))$ over $\mathbb Q(\sin\theta)$
classification:
  areas:
  - prelim
  topics:
  - Abstract Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-25
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-25
  note: >-
    Used the triple-angle identity to obtain a cubic equation over
    Q(sin theta), then exhibited theta=0, pi, and pi/6 for extension degrees
    1, 2, and 3.
---

::: {.problem}
For real $\theta$, let
\[
F_\theta=\mathbb Q(\sin\theta),\qquad E_\theta=\mathbb Q\!\left(\sin\frac\theta3\right).
\]
Show that $E_\theta$ is an extension of $F_\theta$ and determine all possibilities for $[E_\theta:F_\theta]$.
:::

::: {.solution}
Set
$$
x\coloneqq\sin\frac{\theta}{3},
\qquad
s\coloneqq\sin\theta.
$$

::: pf

::: {.pf-step #s1}

One has
$$
s=3x-4x^3.
$$

::: pf-proof

This is the triple-angle identity
$$
\sin(3u)=3\sin u-4\sin^3u
$$
with $u=\theta/3$.

:::

:::

::: {.pf-step #s2}

One has
$$
F_\theta\subseteq E_\theta.
$$

::: pf-proof

By step [](#s1){.pf-ref},
$$
s=3x-4x^3\in\QQ(x)=E_\theta.
$$
Therefore
$$
F_\theta=\QQ(s)\subseteq E_\theta.
$$

:::

:::

::: {.pf-step #s3}

The extension degree satisfies
$$
[E_\theta:F_\theta]\in\{1,2,3\}.
$$

::: pf-proof

Step [](#s1){.pf-ref} gives
$$
4x^3-3x+s=0.
$$
Thus $x$ is algebraic over $F_\theta=\QQ(s)$ and its minimal polynomial
divides a polynomial of degree $3$. Since
$$
E_\theta=F_\theta(x),
$$
the degree $[E_\theta:F_\theta]$ is the degree of that minimal polynomial,
so it is $1$, $2$, or $3$.

:::

:::

::: {.pf-step #s4}

Degree $1$ occurs.

::: pf-proof

Take $\theta=0$. Then
$$
\sin\theta=0
\qquad\text{and}\qquad
\sin\frac{\theta}{3}=0.
$$
Hence
$$
F_0=E_0=\QQ.
$$

:::

:::

::: {.pf-step #s5}

Degree $2$ occurs.

::: pf-proof

Take $\theta=\pi$. Then
$$
F_\pi
=
\QQ(\sin\pi)
=
\QQ,
$$
while
$$
E_\pi
=
\QQ\left(\sin\frac{\pi}{3}\right)
=
\QQ\left(\frac{\sqrt3}{2}\right)
=
\QQ(\sqrt3).
$$
Therefore
$$
[E_\pi:F_\pi]=2.
$$

:::

:::

::: {.pf-step #s6}

Degree $3$ occurs.

::: pf-proof

Take
$$
\theta=\frac{\pi}{6}.
$$
Then
$$
F_\theta
=
\QQ\left(\frac12\right)
=
\QQ.
$$
For
$$
x=\sin\frac{\pi}{18},
$$
the triple-angle relation gives
$$
8x^3-6x+1=0.
$$
By the rational root theorem, a rational root could only be one of
$$
\pm1,\quad
\pm\frac12,\quad
\pm\frac14,\quad
\pm\frac18.
$$
Direct substitution shows that none of these is a root. Hence the cubic
$$
8T^3-6T+1
$$
is irreducible over $\QQ$. Therefore
$$
[\QQ(x):\QQ]=3,
$$
so
$$
[E_\theta:F_\theta]=3.
$$

:::

:::

::: {.pf-step #s7}

The complete set of possibilities is
$$
\boxed{\{1,2,3\}}.
$$

::: pf-proof

Step [](#s3){.pf-ref} gives the only possible degrees, and steps [](#s4){.pf-ref}, [](#s5){.pf-ref} and [](#s6){.pf-ref} show that
each of them occurs.

:::

:::

::: pf-qed

Steps [](#s2){.pf-ref} and [](#s7){.pf-ref} prove the two requested assertions.

:::

:::

:::
