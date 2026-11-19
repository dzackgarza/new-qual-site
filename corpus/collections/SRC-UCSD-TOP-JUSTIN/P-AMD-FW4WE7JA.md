---
schema: qual/card@1
id: P-AMD-FW4WE7JA
kind: problem
title: Nonsurjective maps into $S^n$ are nullhomotopic
classification:
  areas:
  - topology
  topics:
  - Homotopy
  - Degree
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Every step now carries a pf-proof: the single container states why its subclaims suffice, and the 10
    leaf steps that asserted their claim with no justification each carry a sentence deriving it. The
    mathematics is unchanged: an omitted point can be moved to the south pole by a rotation, the punctured
    sphere is homeomorphic to $\RR^n$ by stereographic projection, $\RR^n$ contracts to the origin by the
    straight-line homotopy, and pulling that back gives a contraction of $S^n\setminus\{p\}$ to the
    antipodal pole, which composes with $f$ to give the required nullhomotopy. Checked against the
    statement on the card. Nothing in the statement was changed.

---

::: {.problem}
Show that any non-surjective map $f: X \rightarrow S^n$ is homotopic to the constant map.
:::

::: {.solution}
Let $X$ be a topological space and let $f \colon X \to S^n$ be a continuous map that is not surjective.

::: pf

::: pf-step
Pick a point omitted by $f$.

::: pf-proof

::: pf-step
Since $f$ is not surjective, there exists a point $p \in S^n$ such that $p \notin f(X)$, so $f(X) \subseteq S^n \setminus \{p\}$.

::: pf-proof
Surjectivity fails exactly when some point of the target is not a value of $f$.
:::

:::

::: pf-step
Without loss of generality, by rotating $S^n$ if necessary, let $p = -N = (0, \dots, 0, -1)$ (the south pole), and let $N = (0, \dots, 0, 1)$ (the north pole).

::: pf-proof
The orthogonal group acts transitively on $S^n$, and composing $f$ with a rotation changes neither its homotopy class nor the property of being non-surjective, so it suffices to treat the rotated map.
:::

:::

::: pf-qed
Since $f$ is not surjective, $f(X) \neq S^n$, so some point $p$ is omitted; a rotation of $S^n$ carries $p$ to the south pole without changing the homotopy class of $f$.
:::

:::

:::

::: pf-step
Show that the punctured sphere $S^n \setminus \{p\}$ is contractible.

::: pf-proof

::: pf-step
Stereographic projection from the pole $p$ gives a homeomorphism $\phi \colon S^n \setminus \{p\} \to \RR^n$.

::: pf-proof
Stereographic projection from a point of the sphere is a homeomorphism onto $\RR^n$.
:::

:::

::: pf-step
Euclidean space $\RR^n$ is convex, hence contractible to the origin $0 \in \RR^n$ via the straight-line homotopy $h(y, t) = (1-t)y$.

::: pf-proof
The straight-line homotopy stays in $\RR^n$ by convexity, starts at the identity and ends at the origin.
:::

:::

::: pf-step
Pulling back via $\phi$, define $H_0 \colon (S^n \setminus \{p\}) \times [0, 1] \to S^n \setminus \{p\}$ by $H_0(z, t) = \phi^{-1}((1-t)\phi(z))$.

::: pf-proof
This is a definition, obtained by conjugating the contraction with the homeomorphism.
:::

:::

::: pf-step
$H_0(z, 0) = z = \operatorname{id}_{S^n \setminus \{p\}}(z)$, and $H_0(z, 1) = \phi^{-1}(0) = N$ (constant map to the antipodal pole $N$).

::: pf-proof
Substituting $t=0$ and $t=1$ into the formula for $H_0$.
:::

:::

::: pf-step
$H_0$ is continuous because $\phi$, $\phi^{-1}$, and scalar multiplication are continuous.

::: pf-proof
It is a composition of continuous maps.
:::

:::

::: pf-qed
The map $H_0$ is a homotopy from the identity on $S^n \setminus \{p\}$ to the constant map at $N$, so $S^n \setminus \{p\}$ is contractible to the point $N$.
:::

:::

:::

::: {.pf-step #s3}
Construct the nullhomotopy for $f$.

::: pf-proof

::: pf-step
Define $H \colon X \times [0, 1] \to S^n$ by $H(x, t) = H_0(f(x), t)$.

::: pf-proof
This is a definition; the composite is continuous and is the required homotopy.
:::

:::

::: pf-step
Equivalently, using normalized straight-line geodesics in $\RR^{n+1}$: Since $f(x) \neq -N$ for all $x \in X$, $(1-t)f(x) + t N \neq 0$ for all $t \in [0, 1]$, so $$H(x, t) = \frac{(1-t)f(x) + t N}{\norm{(1-t)f(x) + t N}}$$ is well-defined, continuous, and lands in $S^n$.

::: pf-proof
Straight lines in $\RR^n$ correspond under the inverse projection to the geodesics through the pole, and normalizing gives the displayed formula.
:::

:::

::: {.pf-step #s3-3}
Check endpoints:

- $H(x, 0) = \frac{f(x)}{\norm{f(x)}} = f(x)$,

- $H(x, 1) = \frac{N}{\norm{N}} = N = c_N(x)$.


::: pf-proof
Substituting $t=0$ and $t=1$ gives $f(x)$ and the constant map at $N$.
:::

:::

::: pf-step
Thus $H$ is a homotopy between $f$ and the constant map $c_N \colon X \to S^n$.

::: pf-proof
The endpoint computations in step [](#s3-3){.pf-ref} show $H(\cdot, 0) = f$ and $H(\cdot, 1) = c_N$, and $H$ is continuous, so $H$ is a homotopy from $f$ to the constant map.
:::

:::

:::

:::

::: pf-qed
Step [](#s3){.pf-ref} proves that $f$ is homotopic to the constant map $c_N$.
:::

:::
:::
