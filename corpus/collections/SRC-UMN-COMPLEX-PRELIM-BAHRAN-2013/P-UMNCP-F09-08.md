---
schema: qual/card@1
id: P-UMNCP-F09-08
kind: problem
title: Two interior fixed points force the identity
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
  note: Checked against Fall 2009, 8 as reproduced in Cihan Bahran's vendored 2013 University of Minnesota complex-prelim solution compilation.
---

::: {.problem}
Let \(f:\DD\to\DD\) be holomorphic.
Suppose there are distinct points \(p,q\in\DD\) such that \(f(p)=p\) and \(f(q)=q\). Show that \(f(z)=z\) for every \(z\in\DD\).
:::

::: {.solution}

Let
$$
\phi_p(z)
\coloneqq
\frac{z-p}{1-\overline p z},
$$
the disk automorphism sending $p$ to $0$, and define
$$
g
\coloneqq
\phi_p\circ f\circ\phi_p^{-1}.
$$

::: pf

::: {.pf-step #p1-s1-1}

The map
$$
g:\DD\to\DD
$$
is holomorphic and fixes $0$.


::: pf-proof

The maps
$$
\phi_p
\quad\text{and}\quad
\phi_p^{-1}
$$
are holomorphic automorphisms of the disk, so $g$ is a holomorphic self-map of $\DD$. Since
$$
f(p)=p,
$$
one has
$$
g(0)
=
\phi_p(f(p))
=0.
$$

:::

:::

::: {.pf-step #p1-s1-2}

The nonzero point
$$
a
\coloneqq
\phi_p(q)
$$
is also fixed by $g$.


::: pf-proof

Because
$$
p\ne q
$$
and $\phi_p$ is injective,
$$
a=\phi_p(q)\ne0.
$$
Using
$$
f(q)=q,
$$
we get
$$
\begin{aligned}
g(a)
&=
\phi_p\!\left(
f(\phi_p^{-1}(\phi_p(q)))
\right)\\
&=
\phi_p(f(q))\\
&=
\phi_p(q)\\
&=
a.
\end{aligned}
$$

:::

:::

::: pf-step

Schwarz's lemma gives
$$
|g(z)|\le|z|
$$
for every
$$
z\in\DD.
$$


::: pf-proof

Step [](#p1-s1-1){.pf-ref} gives a holomorphic self-map of the unit disk fixing the origin. Schwarz's lemma applies.

:::

:::

::: pf-step

Equality holds in Schwarz's lemma at the nonzero point $a$:
$$
|g(a)|=|a|.
$$


::: pf-proof

By step [](#p1-s1-2){.pf-ref},
$$
g(a)=a.
$$
Taking absolute values gives the equality.

:::

:::

::: {.pf-step #p1-s1-5}

Therefore there is a real number $\theta$ such that
$$
g(z)=e^{i\theta}z
$$
for every $z\in\DD$.


::: pf-proof

The equality case of Schwarz's lemma states that if a holomorphic self-map of the disk fixing $0$ satisfies
$$
|g(a)|=|a|
$$
at some
$$
a\ne0,
$$
then $g$ is a rotation.

:::

:::

::: {.pf-step #p1-s1-6}

In fact,
$$
\boxed{g(z)=z}
$$
for every $z\in\DD$.


::: pf-proof

By step [](#p1-s1-2){.pf-ref},
$$
g(a)=a
$$
with
$$
a\ne0.
$$
Substituting the formula from step [](#p1-s1-5){.pf-ref} gives
$$
e^{i\theta}a=a.
$$
Hence
$$
e^{i\theta}=1,
$$
so $g$ is the identity.

:::

:::

::: {.pf-step #p1-s1-7}

Therefore
$$
\boxed{f(z)=z}
$$
for every $z\in\DD$.


::: pf-proof

By definition,
$$
g
=
\phi_p\circ f\circ\phi_p^{-1}.
$$
Step [](#p1-s1-6){.pf-ref} says $g=\operatorname{id}_{\DD}$. Conjugating by $\phi_p^{-1}$ gives
$$
f
=
\phi_p^{-1}\circ g\circ\phi_p
=
\operatorname{id}_{\DD}.
$$

:::

:::

::: pf-qed

Step [](#p1-s1-7){.pf-ref} is the required conclusion.

:::

:::

Let
$$
\phi_p(z)
\coloneqq
\frac{z-p}{1-\overline p z},
$$
the disk automorphism sending $p$ to $0$, and define
$$
g
\coloneqq
\phi_p\circ f\circ\phi_p^{-1}.
$$

::: pf

::: {.pf-step #p2-s1-1}

The map
$$
g:\DD\to\DD
$$
is holomorphic and satisfies
$$
g(0)=0.
$$


::: pf-proof

The map $\phi_p$ is an automorphism of the unit disk, so the conjugate $g$ is a holomorphic self-map of the disk. Since
$$
f(p)=p
$$
and
$$
\phi_p(p)=0,
$$
one has
$$
g(0)
=
\phi_p(f(p))
=0.
$$

:::

:::

::: {.pf-step #p2-s1-2}

The nonzero point
$$
w_0
\coloneqq
\phi_p(q)
$$
is fixed by $g$.


::: pf-proof

Because $p\ne q$ and $\phi_p$ is injective,
$$
w_0\ne0.
$$
Moreover,
$$
\begin{aligned}
g(w_0)
&=
\phi_p
\left(
f(\phi_p^{-1}(\phi_p(q)))
\right)\\
&=
\phi_p(f(q))\\
&=
\phi_p(q)\\
&=
w_0.
\end{aligned}
$$

:::

:::

::: pf-step

Schwarz's lemma gives
$$
|g(w)|\le|w|
$$
for every
$$
w\in\DD.
$$


::: pf-proof

Step [](#p2-s1-1){.pf-ref} gives a holomorphic self-map of the disk fixing the origin.

:::

:::

::: pf-step

Equality holds in Schwarz's estimate at the nonzero point $w_0$:
$$
|g(w_0)|=|w_0|.
$$


::: pf-proof

By step [](#p2-s1-2){.pf-ref},
$$
g(w_0)=w_0.
$$
Taking absolute values gives the equality.

:::

:::

::: {.pf-step #p2-s1-5}

Hence
$$
g(w)=e^{i\theta}w
$$
for some $\theta\in\RR$.


::: pf-proof

The equality case in Schwarz's lemma says that if equality
$$
|g(w)|=|w|
$$
occurs at some nonzero point of the disk, then $g$ is a rotation.

:::

:::

::: {.pf-step #p2-s1-6}

In fact
$$
\boxed{g(w)=w}
$$
for every $w\in\DD$.


::: pf-proof

By steps [](#p2-s1-2){.pf-ref} and [](#p2-s1-5){.pf-ref},
$$
w_0
=
g(w_0)
=
e^{i\theta}w_0.
$$
Since $w_0\ne0$,
$$
e^{i\theta}=1.
$$
Thus $g$ is the identity.

:::

:::

::: {.pf-step #p2-s1-7}

Therefore
$$
\boxed{f(z)=z}
$$
for every $z\in\DD$.


::: pf-proof

Since
$$
g
=
\phi_p\circ f\circ\phi_p^{-1}
$$
and $g$ is the identity by step [](#p2-s1-6){.pf-ref},
$$
f
=
\phi_p^{-1}\circ g\circ\phi_p
=
\operatorname{id}_{\DD}.
$$

:::

:::

::: pf-qed

Step [](#p2-s1-7){.pf-ref} is the required conclusion.

:::

:::

:::
