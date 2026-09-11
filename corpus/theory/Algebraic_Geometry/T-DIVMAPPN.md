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
Let $\mcl$ be an invertible sheaf on $X$ and $V \subseteq H^0(X, \mcl)$ a base-point-free subspace with basis $s_0, \dots, s_n$.
Then
\[
\varphi_{\abs{V}} : X \to \PP^n, \qquad p \mapsto [s_0(p) : \cdots : s_n(p)]
\]
is a morphism with $\varphi^* \OO_{\PP^n}(1) \cong \mcl$, and every morphism to $\PP^n$ arises this way.
:::

::: {.theorem title="Closed immersion criterion"}
$\varphi_{\abs{V}}$ is a closed immersion exactly when the system separates points and separates tangent vectors:

- for all $p \neq q$ there is $D \in \abs{V}$ with $p \in \supp D$ and $q \notin \supp D$;

- for all $p$ and all $0 \neq t \in T_p X$ there is $D \in \abs{V}$ with $p \in \supp D$ and $t \notin T_p(\supp D)$.
:::

::: {.remark}
Base-point freeness is exactly what makes the formula define a point of $\PP^n$ at all: some coordinate must be nonzero.
The two separation conditions are then injectivity and injectivity on tangent spaces, which is what a closed immersion is.

The choice of $V$ matters, not just $\mcl$: taking the complete system gives the largest target, and a proper subspace gives a linear projection of that image.
The standard examples to have ready are $\abs{\OO_{\PP^1}(d)}$, which embeds $\PP^1$ as the rational normal curve in $\PP^d$, and $\abs{\OO_{\PP^n}(2)}$, which gives the Veronese.
On a curve the two separation conditions become the numerical statement about $\ell(D - p - q)$.
:::
