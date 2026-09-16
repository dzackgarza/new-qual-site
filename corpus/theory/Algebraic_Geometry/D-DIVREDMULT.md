---
schema: qual/card@1
id: D-DIVREDMULT
kind: definition
title: Reduced divisors, multiplicity at a point, and pullback of divisors
classification:
  areas:
  - algebraic-geometry
  topics:
  - Weil Divisors
  - Cartier Divisors
  - Multiplicity
relations:
- kind: uses
  target: D-5PQ5W
review: draft
prompts:
- What is a prime divisor? A reduced divisor?
- For a prime divisor $D$ and $p \in \supp D$, what is the multiplicity of $D$ at $p$?
- What is the pullback of a divisor?
- What are the minimal requirements on a scheme for a theory of Weil divisors?
---

::: {.definition title="Prime and reduced divisors"}
On a Noetherian integral separated scheme $X$ regular in codimension one, a \dfn{prime divisor} is a closed integral subscheme of codimension one.
These hypotheses are what the theory of Weil divisors needs: integrality supplies a function field, and regularity in codimension one makes each local ring at a prime divisor a discrete valuation ring, so every rational function has an order along it.
A Weil divisor $D = \sum_i n_i D_i$ with the $D_i$ distinct prime divisors is \dfn{effective} if all $n_i \geq 0$, and \dfn{reduced} if every $n_i \in \{0, 1\}$.
:::

::: {.definition title="Multiplicity at a point"}
Let $X$ be a smooth variety and $D$ an effective divisor with local equation $f \in \OO_{X,p}$ at a point $p$.
The \dfn{multiplicity} of $D$ at $p$ is the largest $m$ with $f \in \mfm_p^m$.
It is $0$ when $p \notin \supp D$, and $1$ exactly when $D$ is smooth at $p$.
:::

::: {.definition title="Pullback"}
Let $\phi \colon X \to Y$ be a morphism of integral schemes and $D$ a Cartier divisor on $Y$ with local equations $\{(U_i, f_i)\}$, such that $\phi(X) \not\subseteq \supp D$.
The \dfn{pullback} $\phi^* D$ is the Cartier divisor on $X$ with local equations $\{(\phi^{-1} U_i, f_i \circ \phi)\}$.
It satisfies $\OO_X(\phi^* D) \cong \phi^* \OO_Y(D)$, and it respects linear equivalence, so it induces $\phi^* \colon \Pic Y \to \Pic X$.
:::

::: {.example}
For the plane curve $D = V(y^2 - x^3)$ in $\AA^2$, the multiplicity at the origin is $2$, since $y^2 - x^3 \in \mfm^2 \setminus \mfm^3$, and the multiplicity is $1$ at every other point of $D$.
For the double cover $\phi \colon \AA^1 \to \AA^1$, $t \mapsto t^2$, the pullback of the divisor $[0]$ is $2[0]$.
:::
