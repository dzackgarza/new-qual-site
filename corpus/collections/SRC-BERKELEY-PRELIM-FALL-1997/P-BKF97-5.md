---
schema: qual/card@1
id: P-BKF97-5
kind: problem
title: Two fixed points force a holomorphic disk self-map to be the identity
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 5 in the deterministic MinerU Flash extraction assets/attachments/Fall97_extracted.md.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-25
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-25
  note: >-
    Conjugated by a disk automorphism sending one fixed point to zero; the
    second fixed point gives equality at a nonzero point in Schwarz's lemma,
    forcing the conjugated map to be the identity.
---

::: {.problem}
Let
\[
\mathbb D=\{z\in\mathbb C:|z|<1\}.
\]
Suppose $f:\mathbb D\to\mathbb D$ is analytic and there exist distinct $a,b\in\mathbb D$ with
\[
f(a)=a,
\qquad
f(b)=b.
\]
Prove that $f(z)=z$ for every $z\in\mathbb D$.
:::

::: {.solution}
Define the disk automorphism
$$
\phi_a(z)
\coloneqq
\frac{z-a}{1-\overline a z}.
$$

<1>1. The map $\phi_a$ is a biholomorphic self-map of $\DD$ satisfying
$$
\phi_a(a)=0.
$$

::: {.proof}
This is the standard disk automorphism associated with $a\in\DD$. Direct
substitution gives $\phi_a(a)=0$, and its inverse is
$$
\phi_a^{-1}(w)
=
\frac{w+a}{1+\overline a w}.
$$
:::

<1>2. The map
$$
g
\coloneqq
\phi_a\circ f\circ\phi_a^{-1}
$$
is a holomorphic self-map of $\DD$ with
$$
g(0)=0.
$$

::: {.proof}
Each map in the composition is holomorphic from $\DD$ to itself. Moreover,
$$
\phi_a^{-1}(0)=a,
$$
so
$$
g(0)
=
\phi_a(f(a))
=
\phi_a(a)
=0.
$$
:::

<1>3. The point
$$
c\coloneqq\phi_a(b)
$$
is nonzero and satisfies
$$
g(c)=c.
$$

::: {.proof}
Since $a\neq b$ and $\phi_a$ is injective,
$$
c=\phi_a(b)\neq\phi_a(a)=0.
$$
Also
$$
\begin{aligned}
g(c)
&=
\phi_a\!\left(
f(\phi_a^{-1}(\phi_a(b)))
\right)\\
&=
\phi_a(f(b))\\
&=
\phi_a(b)\\
&=
c.
\end{aligned}
$$
:::

<1>4. The function $g$ is the identity on $\DD$.

::: {.proof}
By step <1>2, Schwarz's lemma applies:
$$
\abs{g(z)}\leq\abs z
$$
for every $z\in\DD$. Step <1>3 gives equality at the nonzero point $c$:
$$
\abs{g(c)}
=
\abs c.
$$
The equality case of Schwarz's lemma therefore gives
$$
g(z)=\lambda z
$$
for some constant $\lambda$ with $\abs\lambda=1$. Since
$$
g(c)=c
$$
and $c\neq0$, one has $\lambda=1$. Thus $g(z)=z$ on $\DD$.
:::

<1>5. The original map $f$ is the identity on $\DD$.

::: {.proof}
By step <1>4,
$$
\phi_a\circ f\circ\phi_a^{-1}
=
\operatorname{id}_{\DD}.
$$
Conjugating by $\phi_a^{-1}$ gives
$$
f
=
\operatorname{id}_{\DD}.
$$
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required conclusion.
:::
:::
