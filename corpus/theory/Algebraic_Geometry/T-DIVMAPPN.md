---
schema: qual/card@1
id: T-DIVMAPPN
kind: theorem
title: The morphism to projective space attached to a linear system
slogan: 'A base-point-free linear system is a map to projective space; it is an embedding exactly when it separates points and tangent vectors.'
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
The surjection
$$
\OO_X^{\oplus(n+1)}\longrightarrow\mcl,
\qquad
(a_0,\ldots,a_n)\longmapsto\sum_i a_i s_i,
$$
defines a unique $A$-morphism
$$
\varphi\colon X\longrightarrow\PP^n_A
$$
together with an isomorphism $\mcl\cong\varphi^*\OO_{\PP^n}(1)$ carrying $s_i$ to $\varphi^*(x_i)$.
Conversely, every $A$-morphism $\varphi : X \to \PP^n_A$ arises this way, from $\mcl = \varphi^*\OO(1)$ and $s_i = \varphi^*(x_i)$.
[@Har77, Theorem II.7.1]
:::

::: {.proposition title="Linear systems with base points"}
Let $X$ be a $k$-scheme, $V \subseteq H^0(X, \mcl)$ a subspace with basis $s_0, \dots, s_n$, and $B = \bigcap_i V(s_i)$ its base locus.
The sections restricted to the open set $X \sm B$ generate $\mcl$ there, so they define a morphism
$$
\varphi_V\colon X\sm B\longrightarrow\PP(V^\vee),
$$
identified with $\PP^n_k$ after choosing the displayed basis of $V$.
On the open set $D(s_i) \subseteq X \sm B$ where $s_i$ does not vanish, $\varphi_V$ maps into the standard chart $D(x_i)$ and is given by $x_j/x_i \mapsto s_j/s_i$.
:::

::: {.proposition title="Degrees on curves"}
Let $X$ be a nonsingular projective curve over an algebraically closed field $k$ and let $V \subseteq H^0(X, \mcl)$ be base-point free.

- If $\dim V = 2$, the morphism $\varphi_V : X \to \PP^1$ is finite of degree $\deg \mcl$.

- If $\mcl$ is very ample and $V = H^0(X, \mcl)$, then $\varphi_V$ embeds $X$ as a curve of degree $\deg \mcl$ in $\PP^n$, and $\mcl \cong \varphi_V^* \OO(1)$.

[@Har77, Proposition II.6.9, Theorem II.7.1]
:::

::: {.remark}
If a two-dimensional linear system has fixed divisor $F$, division by the canonical section of $\OO_X(F)$ identifies it with a base-point-free pencil in
$$
H^0\bigl(X,\mcl(-F)\bigr).
$$
The resulting morphism $X\to\PP^1$ has degree
$$
\deg\mcl-\deg F.
$$
:::

::: {.theorem title="Closed immersion criterion"}
Let $X$ be a projective variety over an algebraically closed field $k$ and let $V \subseteq H^0(X, \mcl)$ be base-point free.
$\varphi_V$ is a closed immersion exactly when the system separates points and separates tangent vectors:

- for all closed points $p \neq q$ there is $D \in \abs{V}$ with $p \in \supp D$ and $q \notin \supp D$;

- for every closed point $p$ and every $0 \neq t \in T_p X$ there is $D \in \abs{V}$ with $p \in \supp D$ and $t \notin T_p(D)$, where $D$ is regarded as a closed subscheme.

[@Har77, Proposition II.7.3]
:::

::: {.remark}
Base-point freeness is exactly what makes the formula define a point of $\PP^n$ at all: some coordinate must be nonzero.
The two separation conditions say that the associated morphism distinguishes closed points and first-order tangent directions; for a projective variety these are exactly the conditions in the closed-immersion criterion above.

The choice of $V$ matters, not just $\mcl$: the complete system maps to $\PP(H^0(X,\mcl)^\vee)$, and a base-point-free subspace $V$ gives the corresponding linear projection to $\PP(V^\vee)$.
Standard examples are $\abs{\OO_{\PP^1}(d)}$, which embeds $\PP^1$ as the rational normal curve in $\PP^d$, and $\abs{\OO_{\PP^n}(2)}$, which gives the Veronese embedding.
On a curve the two separation conditions become the numerical statement about $\ell(D - p - q)$.
:::
