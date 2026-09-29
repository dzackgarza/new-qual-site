---
schema: qual/card@1
id: P-AGH32BIJNOTISO
kind: problem
title: A bijective bicontinuous morphism need not be an isomorphism
classification:
  areas:
  - algebraic-geometry
  topics:
  - Morphisms
  - Cuspidal Cubic
  - Frobenius
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: 'Compared both parts with Hartshorne I.3.2 and restored the chapter standing hypothesis that k is algebraically closed; without it, Frobenius need not be surjective. The proof checks bicontinuity directly from the Zariski topology and nonisomorphism from the induced coordinate-ring maps.'
- event: solution-written
  by: chatgpt
  date: 2026-09-17
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-17
  note: 'Checked each implication independently and against a published exercise solution: the set-theoretic inverse, closed-map argument, and coordinate-ring obstruction are valid. Part (b) uses algebraic closedness exactly for surjectivity.'
---

::: {.problem}
Let $k$ be algebraically closed.

A morphism whose underlying map of topological spaces is a homeomorphism need not be an isomorphism.

(a) Let $\phi: \AA^1 \to \AA^2$ be defined by $t \mapsto (t^2, t^3)$.
Show that $\phi$ is a bijective bicontinuous morphism of $\AA^1$ onto the curve $y^2 = x^3$, but that $\phi$ is not an isomorphism.

(b) Let the base field $k$ have characteristic $p > 0$, and define $\rho: \AA^1 \to \AA^1$ by $t \mapsto t^p$.
Show that $\rho$ is bijective and bicontinuous but not an isomorphism.
This is called the **Frobenius morphism**.
:::

::: {.solution}
For part (a), put $Y=Z(y^2-x^3)\subseteq\AA^2$ and write $A(Y)=k[x,y]/(y^2-x^3)$.

::: pf

::: {.pf-step #s1}

The map $\phi$ is a morphism from $\AA^1$ onto $Y$ and is bijective.

::: pf-proof

Its coordinate functions $t^2,t^3$ are polynomial, and
$$
(t^3)^2=(t^2)^3,
$$
so its image lies in $Y$.

Let $(a,b)\in Y$.
If $a=0$, then $b^2=a^3=0$, hence $(a,b)=(0,0)=\phi(0)$.
If $a\ne0$, put $t=b/a$.
Using $b^2=a^3$ gives
$$
t^2=\frac{b^2}{a^2}=a,
\qquad
t^3=t\,t^2=\frac{b}{a}a=b,
$$
so $(a,b)=\phi(t)$.
For a point of the form $\phi(t)$, this inverse returns $0$ when $t=0$ and returns $t^3/t^2=t$ when $t\ne0$.
It is therefore a two-sided set-theoretic inverse, proving injectivity and surjectivity.

:::

:::

::: {.pf-step #s2}

The bijection $\phi:\AA^1\to Y$ is bicontinuous.

::: pf-proof

Every morphism of varieties is continuous, so only continuity of the inverse remains.
The closed subsets of $\AA^1$ are $\AA^1$ itself and finite sets: a proper closed subset is the zero set of a nonzero polynomial in one variable, hence is finite.
Because $k$ is algebraically closed, every point of $Y$ is closed, so every finite subset of $Y$ is closed.
Thus $\phi$ sends every closed subset of $\AA^1$ to a closed subset of $Y$: the whole line maps to $Y$, and a finite set maps to a finite set.
Hence $\phi$ is a closed continuous bijection, so its inverse is continuous.

:::

:::

::: {.pf-step #s3}

The morphism $\phi$ is not an isomorphism, completing part (a).

::: pf-proof

The induced homomorphism on coordinate rings is
$$
\phi^*:A(Y)\longrightarrow k[t],
\qquad
x\longmapsto t^2,
\qquad
y\longmapsto t^3.
$$
Its image is the subring $k[t^2,t^3]$.
Every monomial of positive degree in this subring has exponent $2i+3j\ge2$, so no element of $k[t^2,t^3]$ has a nonzero $t^1$ coefficient.
In particular $t\notin k[t^2,t^3]$, and therefore $\phi^*$ is not surjective.
An isomorphism of affine varieties induces an isomorphism of coordinate rings, so $\phi$ cannot be an isomorphism.

Assume now that $\operatorname{char}k=p>0$ for part (b).

:::

:::

::: {.pf-step #s4}

The Frobenius morphism $\rho:\AA^1\to\AA^1$, $t\mapsto t^p$, is bijective and bicontinuous.

::: pf-proof

The map is a morphism because $t^p$ is a polynomial.
If $a^p=b^p$, then in characteristic $p$,
$$
(a-b)^p=a^p-b^p=0,
$$
so $a=b$; thus $\rho$ is injective.
For every $c\in k$, the polynomial $T^p-c$ has a root in the algebraically closed field $k$, so $c=t^p$ for some $t\in k$; hence $\rho$ is surjective.

As in step [](#s2){.pf-ref}, every proper closed subset of $\AA^1$ is finite.
The bijection $\rho$ therefore sends closed sets to closed sets, while every morphism is continuous.
Thus $\rho$ is a closed continuous bijection and hence a homeomorphism.

:::

:::

::: {.pf-step #s5}

The Frobenius morphism is not an isomorphism.

::: pf-proof

Its pullback on coordinate rings is
$$
\rho^*:k[u]\longrightarrow k[t],
\qquad
u\longmapsto t^p.
$$
The image is $k[t^p]$.
Every exponent occurring in a polynomial in $t^p$ is divisible by $p$, so $t\notin k[t^p]$.
Thus $\rho^*$ is not surjective and cannot be an isomorphism of coordinate rings.
Consequently $\rho$ is not an isomorphism of affine varieties.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref} prove part (a), and steps [](#s4){.pf-ref} and [](#s5){.pf-ref} prove part (b).

:::

:::

:::
