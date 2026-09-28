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

<1>1. One has
$$
s=3x-4x^3.
$$

::: {.proof}
This is the triple-angle identity
$$
\sin(3u)=3\sin u-4\sin^3u
$$
with $u=\theta/3$.
:::

<1>2. One has
$$
F_\theta\subseteq E_\theta.
$$

::: {.proof}
By step <1>1,
$$
s=3x-4x^3\in\QQ(x)=E_\theta.
$$
Therefore
$$
F_\theta=\QQ(s)\subseteq E_\theta.
$$
:::

<1>3. The extension degree satisfies
$$
[E_\theta:F_\theta]\in\{1,2,3\}.
$$

::: {.proof}
Step <1>1 gives
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

<1>4. Degree $1$ occurs.

::: {.proof}
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

<1>5. Degree $2$ occurs.

::: {.proof}
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

<1>6. Degree $3$ occurs.

::: {.proof}
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

<1>7. The complete set of possibilities is
$$
\boxed{\{1,2,3\}}.
$$

::: {.proof}
Step <1>3 gives the only possible degrees, and steps <1>4--<1>6 show that
each of them occurs.
:::

<1>8. Q.E.D.

::: {.proof}
Steps <1>2 and <1>7 prove the two requested assertions.
:::
:::
