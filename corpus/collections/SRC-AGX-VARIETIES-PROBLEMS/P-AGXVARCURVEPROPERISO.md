---
schema: qual/card@1
id: P-AGXVARCURVEPROPERISO
kind: problem
title: Birational morphisms between smooth projective curves are isomorphisms
classification:
  areas:
  - algebraic-geometry
  topics:
  - Curves
  - Properness
  - Isomorphisms
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-20
  note: >-
    Read Zaidenberg Theorem 8.6 and Exercise 8.7 in the recorded source.
    Exercise 8.7 asks for birational morphisms between smooth projective
    curves, not arbitrary proper morphisms.
- event: source-corrected
  by: chatgpt
  date: 2026-09-20
  note: >-
    Replaced the false imported proper-morphism statement by the source's
    birational-morphism statement and retitled the card accordingly.
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Checked normality of smooth curves, the Zariski-main connected-fiber
    argument, exclusion of positive-dimensional fibers, proper quasi-finite
    implies finite, and the affine proof that a finite birational morphism to
    a normal variety is an isomorphism.
---

::: {.problem}
Let $X$ and $Y$ be smooth projective curves over $\CC$. Show that every
birational morphism
$$
f:X\longrightarrow Y
$$
is an isomorphism.
:::

::: {.solution}
<1>1. Both $X$ and $Y$ are normal.

::: {.proof}
A smooth variety is regular, and every regular local ring is integrally
closed. Hence smooth varieties are normal.
:::

<1>2. Every fiber of $f$ consists of a single point.

::: {.proof}
By step <1>1, Theorem 8.6 of the source applies to the birational morphism
$$
f:X\longrightarrow Y.
$$
Zariski's Main Theorem there says that every fiber $f^{-1}(y)$ is connected,
and that a fiber which is not a singleton has positive dimension.

Suppose some fiber had positive dimension. It is a closed subset of the
irreducible curve $X$. Every proper closed subset of a curve has dimension
$0$, so a positive-dimensional fiber must equal $X$. Then $f$ would be
constant, contradicting birationality. Thus no fiber has positive dimension.
The source theorem therefore forces every fiber to be a singleton.
:::

<1>3. The morphism $f$ is finite.

::: {.proof}
Since $X$ and $Y$ are projective, $f$ is proper and of finite type. By step
<1>2 all fibers are finite, so $f$ is quasi-finite. A proper quasi-finite
morphism is finite. Hence $f$ is finite.
:::

<1>4. A finite birational morphism onto the normal variety $Y$ is an
isomorphism.

::: {.proof}
Let
$$
V=\Spec A\subseteq Y
$$
be affine. Since $f$ is finite,
$$
f^{-1}(V)=\Spec B
$$
for a finite $A$-algebra $B$.

Birationality identifies the function fields
$$
K(X)\cong K(Y)=K,
$$
and under this identification the inclusion induced by $f$ places
$$
A\subseteq B\subseteq K.
$$
Because $B$ is finite over $A$, every element of $B$ is integral over $A$.
By step <1>1, $Y$ is normal, so $A$ is integrally closed in its fraction
field $K$. Therefore
$$
B\subseteq A.
$$
Together with $A\subseteq B$, this gives
$$
A=B.
$$
Thus $f^{-1}(V)\to V$ is an isomorphism for every affine open $V\subseteq Y$.
These local isomorphisms show that $f$ is an isomorphism.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>3 makes $f$ finite, and step <1>4 uses birationality and normality of
$Y$ to conclude that $f$ is an isomorphism.
:::
:::
