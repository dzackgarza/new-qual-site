---
schema: qual/card@1
id: P-AGH310SUBVARIETY
kind: problem
title: Subvarieties and the restriction of a morphism
classification:
  areas:
  - algebraic-geometry
  topics:
  - Subvarieties
  - Morphisms
  - Locally Closed Sets
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: 'Compared the full locally-closed setup and restriction claim with Hartshorne I.3.10. The proof uses the induced subvariety structure: regular functions locally have the same ambient quotient representatives, so the morphism pullback criterion restricts.'
- event: solution-written
  by: chatgpt
  date: 2026-09-17
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-17
  note: 'Checked continuity and the local regular-function argument against two independent published solution sources. No extension of a regular function across all of Y is assumed; only a local ambient representative is used.'
---

::: {.problem}
A subset of a topological space is **locally closed** if it is an open subset of its closure, equivalently if it is the intersection of an open set with a closed set.

If $X$ is a quasi-affine or quasi-projective variety and $Y \subseteq X$ is an irreducible locally closed subset, then $Y$ is itself quasi-affine, respectively quasi-projective, by virtue of being a locally closed subset of the same affine or projective space.
This is the **induced structure** on $Y$, and $Y$ is called a **subvariety** of $X$.

Now let $\phi: X \to Y$ be a morphism, and let $X' \subseteq X$ and $Y' \subseteq Y$ be irreducible locally closed subsets with $\phi(X') \subseteq Y'$.
Show that $\ro{\phi}{X'} : X' \to Y'$ is a morphism.
:::

::: {.solution}
Write
$$
\phi'=\ro{\phi}{X'}:X'\longrightarrow Y'.
$$

::: pf

::: {.pf-step #s1}

The map $\phi'$ is continuous for the induced topologies on $X'$ and $Y'$.

::: pf-proof

Let $C\subseteq Y'$ be closed.
Because $Y'$ has the subspace topology from $Y$, there is a closed subset $D\subseteq Y$ with
$$
C=Y'\cap D.
$$
Since $\phi(X')\subseteq Y'$,
$$
(\phi')^{-1}(C)=X'\cap\phi^{-1}(D).
$$
The set $\phi^{-1}(D)$ is closed in $X$ because $\phi$ is continuous, so its intersection with $X'$ is closed in $X'$.
Thus $\phi'$ is continuous.

:::

:::

::: {.pf-step #s2}

A regular function on an open subset of $Y'$ is, near each point, the restriction of a regular function on an open subset of $Y$.

::: pf-proof

Fix an open subset $V'\subseteq Y'$, a regular function $f$ on $V'$, and a point $Q\in V'$.
By the definition of a regular function on the induced quasi-affine or quasi-projective structure, after shrinking around $Q$ in $V'$, the function $f$ is represented by a quotient
$$
\frac{g}{h}
$$
of ambient polynomial functions, with $h$ nonzero there; in the projective case $g$ and $h$ are homogeneous of the same degree.
The same quotient is regular on the ambient open subset of $Y$ where $h\ne0$.
Intersecting that open subset with a sufficiently small ambient open neighborhood whose intersection with $Y'$ lies in $V'$ gives an open neighborhood $V\subseteq Y$ of $Q$ and a regular function $\widetilde f$ on $V$ whose restriction to a neighborhood of $Q$ in $Y'$ equals $f$.

:::

:::

::: {.pf-step #s3}

The pullback of every regular function by $\phi'$ is regular.

::: pf-proof

Let $V'\subseteq Y'$ be open, let $f\in\mco(V')$, and fix
$$
P\in(\phi')^{-1}(V').
$$
Put $Q=\phi'(P)$.
By step [](#s2){.pf-ref}, after shrinking around $Q$, choose an open neighborhood $V\subseteq Y$ and a regular function $\widetilde f$ on $V$ whose restriction to $Y'$ agrees with $f$ near $Q$.

Because $\phi$ is a morphism,
$$
\widetilde f\circ\phi
$$
is regular on $\phi^{-1}(V)$.
Restricting this regular function to the induced subvariety $X'$ gives a regular function near $P$, and there it equals
$$
f\circ\phi'.
$$
Thus $f\circ\phi'$ is regular in a neighborhood of every point of $(\phi')^{-1}(V')$.
Regularity is local, so it is regular on all of $(\phi')^{-1}(V')$.

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} proves continuity, and step [](#s3){.pf-ref} proves the regular-function pullback condition.
These are precisely the defining conditions for $\phi':X'\to Y'$ to be a morphism.

:::

:::

:::
