---
schema: qual/card@1
id: P-AGXMISCTSENPONEBUNDLE
kind: problem
title: A family of genus-zero curves over a curve is a $\PP^1$-bundle
classification:
  areas:
  - algebraic-geometry
  topics:
  - Tsen's Theorem
  - Projective Bundles
  - Cohomology and Base Change
relations:
- kind: uses
  target: T-COHBC
- kind: related-to
  target: D-VARSEVBRAUER
review: draft
---

::: {.problem}
Use Tsen's theorem to show that given a flat family $X\to Y$ with $Y$ a curve where the fibers smooth curves of genus 0, this determines a Zariski $\PP^1$-bundle iff there exists a relative degree 1 line bundle on $X$ over $Y$.
:::

::: {.solution}
Work over an algebraically closed field $k$, with $Y$ a smooth curve and $\pi \colon X \to Y$ flat and proper whose fibres are smooth projective curves of genus $0$.
Tsen's theorem: the function field $K = k(Y)$ is $C_1$, so every quadratic form in at least three variables over $K$ has a nontrivial zero.

<1>1. If $X \cong \PP(\mathcal{E})$ for a rank-$2$ vector bundle $\mathcal{E}$ on $Y$, then $X$ has a line bundle of relative degree $1$.

::: {.proof}
$\OO_{\PP(\mathcal{E})}(1)$ restricts to $\OO_{\PP^1}(1)$ on every fibre.
:::

<1>2. If $L$ is a line bundle on $X$ of degree $1$ on every fibre, then $X \cong \PP(\pi_* L)$ over $Y$.

<2>1. $\pi_* L$ is locally free of rank $2$, and its formation commutes with base change.

::: {.proof}
Each fibre $X_y \cong \PP^1$ and $L|_{X_y} \cong \OO_{\PP^1}(1)$, so $h^0(X_y, L_y) = 2$ and $h^1(X_y, L_y) = 0$ for all $y$.
Since $\pi$ is flat and proper and $Y$ is reduced, cohomology and base change gives both claims.
:::

<2>2. The evaluation map $\pi^* \pi_* L \to L$ is surjective and defines a $Y$-morphism $\phi \colon X \to \PP(\pi_* L)$ that is an isomorphism on every fibre.

::: {.proof}
By step <2>1 the restriction of the evaluation map to $X_y$ is the evaluation map of $\OO_{\PP^1}(1)$, which is surjective and whose induced morphism $\PP^1 \to \PP(H^0(\OO_{\PP^1}(1)))$ is an isomorphism.
Surjectivity of a map of coherent sheaves is checked on fibres by Nakayama's lemma.
:::

<2>3. $\phi$ is an isomorphism.

::: {.proof}
$X$ and $\PP(\pi_* L)$ are flat and proper over $Y$, and $\phi$ is an isomorphism on each fibre.
A $Y$-morphism of flat proper $Y$-schemes that is an isomorphism on every fibre is an isomorphism, by the fibrewise criterion of flatness together with properness.
:::

<2>4. Q.E.D.

::: {.proof}
Step <2>3.
:::

<1>3. $X$ has a line bundle of relative degree $1$, so the two conditions of the problem always hold.

<2>1. The generic fibre $X_K$ has a $K$-rational point.

::: {.proof}
$X_K$ is a smooth projective curve of genus $0$ over $K$, so its anticanonical embedding identifies it with a conic in $\PP^2_K$, the zero set of a ternary quadratic form.
By Tsen's theorem that form has a nontrivial zero over $K$.
:::

<2>2. $\pi$ has a section $\sigma \colon Y \to X$.

::: {.proof}
A $K$-point of $X_K$ is a rational map $Y \dashrightarrow X$ over $Y$; since $Y$ is a smooth curve and $\pi$ is proper, the valuative criterion extends it to a morphism $\sigma$ with $\pi \circ \sigma = \mathrm{id}_Y$.
:::

<2>3. $L = \OO_X(\sigma(Y))$ is a line bundle of relative degree $1$.

::: {.proof}
$X$ is smooth over $k$, since $\pi$ is flat with smooth fibres over the smooth curve $Y$, so the prime divisor $\sigma(Y)$ is Cartier.
The section meets each fibre $X_y$ in the single point $\sigma(y)$, transversally because $\pi \circ \sigma = \mathrm{id}_Y$, so $\deg L|_{X_y} = 1$.
:::

<2>4. Q.E.D.

::: {.proof}
Step <2>3.
:::

<1>4. Q.E.D.

::: {.proof}
Steps <1>1 and <1>2 prove the equivalence, and step <1>3, which uses Tsen's theorem, shows that every such family is a Zariski $\PP^1$-bundle.
:::
:::
