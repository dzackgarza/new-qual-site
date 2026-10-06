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
Let \(f:\mathbb D\to\mathbb D\) be holomorphic.
Suppose there are distinct points \(p,q\in\mathbb D\) such that \(f(p)=p\) and \(f(q)=q\). Show that \(f(z)=z\) for every \(z\in\mathbb D\).
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

<1>1. The map
$$
g:\mathbb D\to\mathbb D
$$
is holomorphic and fixes $0$.

::: {.proof}
The maps
$$
\phi_p
\quad\text{and}\quad
\phi_p^{-1}
$$
are holomorphic automorphisms of the disk, so $g$ is a holomorphic self-map of $\mathbb D$. Since
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

<1>2. The nonzero point
$$
a
\coloneqq
\phi_p(q)
$$
is also fixed by $g$.

::: {.proof}
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

<1>3. Schwarz's lemma gives
$$
|g(z)|\le|z|
$$
for every
$$
z\in\mathbb D.
$$

::: {.proof}
Step <1>1 gives a holomorphic self-map of the unit disk fixing the origin. Schwarz's lemma applies.
:::

<1>4. Equality holds in Schwarz's lemma at the nonzero point $a$:
$$
|g(a)|=|a|.
$$

::: {.proof}
By step <1>2,
$$
g(a)=a.
$$
Taking absolute values gives the equality.
:::

<1>5. Therefore there is a real number $\theta$ such that
$$
g(z)=e^{i\theta}z
$$
for every $z\in\mathbb D$.

::: {.proof}
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

<1>6. In fact,
$$
\boxed{g(z)=z}
$$
for every $z\in\mathbb D$.

::: {.proof}
By step <1>2,
$$
g(a)=a
$$
with
$$
a\ne0.
$$
Substituting the formula from step <1>5 gives
$$
e^{i\theta}a=a.
$$
Hence
$$
e^{i\theta}=1,
$$
so $g$ is the identity.
:::

<1>7. Therefore
$$
\boxed{f(z)=z}
$$
for every $z\in\mathbb D$.

::: {.proof}
By definition,
$$
g
=
\phi_p\circ f\circ\phi_p^{-1}.
$$
Step <1>6 says $g=\operatorname{id}_{\mathbb D}$. Conjugating by $\phi_p^{-1}$ gives
$$
f
=
\phi_p^{-1}\circ g\circ\phi_p
=
\operatorname{id}_{\mathbb D}.
$$
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>7 is the required conclusion.
:::
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

<1>1. The map
$$
g:\mathbb D\to\mathbb D
$$
is holomorphic and satisfies
$$
g(0)=0.
$$

::: {.proof}
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

<1>2. The nonzero point
$$
w_0
\coloneqq
\phi_p(q)
$$
is fixed by $g$.

::: {.proof}
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

<1>3. Schwarz's lemma gives
$$
|g(w)|\le|w|
$$
for every
$$
w\in\mathbb D.
$$

::: {.proof}
Step <1>1 gives a holomorphic self-map of the disk fixing the origin.
:::

<1>4. Equality holds in Schwarz's estimate at the nonzero point $w_0$:
$$
|g(w_0)|=|w_0|.
$$

::: {.proof}
By step <1>2,
$$
g(w_0)=w_0.
$$
Taking absolute values gives the equality.
:::

<1>5. Hence
$$
g(w)=e^{i\theta}w
$$
for some $\theta\in\RR$.

::: {.proof}
The equality case in Schwarz's lemma says that if equality
$$
|g(w)|=|w|
$$
occurs at some nonzero point of the disk, then $g$ is a rotation.
:::

<1>6. In fact
$$
\boxed{g(w)=w}
$$
for every $w\in\mathbb D$.

::: {.proof}
By steps <1>2 and <1>5,
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

<1>7. Therefore
$$
\boxed{f(z)=z}
$$
for every $z\in\mathbb D$.

::: {.proof}
Since
$$
g
=
\phi_p\circ f\circ\phi_p^{-1}
$$
and $g$ is the identity by step <1>6,
$$
f
=
\phi_p^{-1}\circ g\circ\phi_p
=
\operatorname{id}_{\mathbb D}.
$$
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>7 is the required conclusion.
:::
:::
