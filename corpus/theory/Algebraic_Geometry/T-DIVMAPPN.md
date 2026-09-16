---
schema: qual/card@1
id: T-DIVMAPPN
kind: theorem
title: The morphism to projective space attached to a linear system
classification:
  areas:
  - algebraic-geometry
  topics:
  - Linear Systems
  - Closed Immersions
  - Very Ample Divisors
relations:
- kind: uses
  target: D-DIVLINSYS
- kind: related-to
  target: T-D8TUX
review: draft
prompts:
- How does a linear system define a map to projective space?
- When is the map defined by a linear system a closed immersion?
- What does it mean for a linear system to separate points and tangent vectors?
---

::: {.theorem}
Let $X$ be a scheme over a ring $A$, $\mcl$ an invertible sheaf on $X$, and $s_0, \dots, s_n \in H^0(X, \mcl)$ sections that generate $\mcl$.
Then there is a unique $A$-morphism
\[
\varphi : X \to \PP^n_A, \qquad p \mapsto [s_0(p) : \cdots : s_n(p)] ,
\]
with $\mcl \cong \varphi^* \OO_{\PP^n}(1)$ and $s_i = \varphi^*(x_i)$ under this isomorphism.
Conversely, every $A$-morphism $\varphi : X \to \PP^n_A$ arises this way, from $\mcl = \varphi^*\OO(1)$ and $s_i = \varphi^*(x_i)$.
[@Har10a, Theorem II.7.1]
:::

::: {.proposition title="Linear systems with base points"}
Let $X$ be a $k$-scheme, $V \subseteq H^0(X, \mcl)$ a subspace with basis $s_0, \dots, s_n$, and $B = \bigcap_i V(s_i)$ its base locus.
The sections restricted to the open set $X \sm B$ generate $\mcl$ there, so they define a morphism $\varphi_V : X \sm B \to \PP^n_k$, which is $\PP V$ up to the choice of basis.
On the open set $D(s_i) \subseteq X \sm B$ where $s_i$ does not vanish, $\varphi_V$ maps into the standard chart $D(x_i)$ and is given by $x_j/x_i \mapsto s_j/s_i$.
:::

::: {.proposition title="Degrees on curves"}
Let $X$ be a nonsingular projective curve over $k = \bar k$ and $V \subseteq H^0(X, \mcl)$ base-point free.

- If $\dim V = 2$, the morphism $\varphi_V : X \to \PP^1$ is finite of degree $\deg \mcl$.

- If $\mcl$ is very ample and $V = H^0(X, \mcl)$, then $\varphi_V$ embeds $X$ as a curve of degree $\deg \mcl$ in $\PP^n$, and $\mcl \cong \varphi_V^* \OO(1)$.

[@Har10a, Proposition II.6.9, Theorem II.7.1]
:::

::: {.remark}
Erratum: the source states the degree of the pencil map without assuming $V$ base-point free.
If a two-dimensional $V$ has base points, the fixed part $F$ of the pencil is an effective divisor of positive degree, and the morphism $X \to \PP^1$ that $V$ induces has degree $\deg \mcl - \deg F$.
:::

::: {.theorem title="Closed immersion criterion"}
Let $X$ be a projective scheme over $k = \bar k$ and $V \subseteq H^0(X, \mcl)$ base-point free.
$\varphi_V$ is a closed immersion exactly when the system separates points and separates tangent vectors:

- for all closed points $p \neq q$ there is $D \in \abs{V}$ with $p \in \supp D$ and $q \notin \supp D$;

- for every closed point $p$ and every $0 \neq t \in T_p X$ there is $D \in \abs{V}$ with $p \in \supp D$ and $t \notin T_p(D)$, where $D$ is regarded as a closed subscheme.

[@Har10a, Proposition II.7.3]
:::

::: {.remark}
Base-point freeness is exactly what makes the formula define a point of $\PP^n$ at all: some coordinate must be nonzero.
The two separation conditions are then injectivity and injectivity on tangent spaces, which is what a closed immersion is.

The choice of $V$ matters, not just $\mcl$: taking the complete system gives the largest target, and a proper subspace gives a linear projection of that image.
The standard examples to have ready are $\abs{\OO_{\PP^1}(d)}$, which embeds $\PP^1$ as the rational normal curve in $\PP^d$, and $\abs{\OO_{\PP^n}(2)}$, which gives the Veronese.
On a curve the two separation conditions become the numerical statement about $\ell(D - p - q)$.
:::
