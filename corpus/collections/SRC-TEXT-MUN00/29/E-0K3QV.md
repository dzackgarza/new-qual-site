---
schema: qual/card@1
id: E-0K3QV
kind: exercise
title: The one-point compactification of the minimal uncountable well-ordered set
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Order Topology
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Show that the one-point compactification of $S_\Omega$ is homeomorphic with $\overline{S}_\Omega$.
:::

::: solution
**Goal:** Prove that the one-point compactification $S_\Omega^*$ of the minimal uncountable well-ordered set $S_\Omega = [0, \Omega)$ is homeomorphic to $\overline{S}_\Omega = [0, \Omega]$ equipped with the order topology.

<1>1. Properties of $\overline{S}_\Omega$:
    1. $\overline{S}_\Omega = [0, \Omega]$ in the order topology is compact and Hausdorff.
    2. The subspace topology on $S_\Omega = [0, \Omega) \subset \overline{S}_\Omega$ is identical to the intrinsic order topology on $S_\Omega$.
    3. The remainder $\overline{S}_\Omega \setminus S_\Omega = \{\Omega\}$ is a single point.
    *Proof:*
    <2>1. Every well-ordered set with a largest element is compact in the order topology (Munkres Theorem 27.1), and every order topology is Hausdorff. Thus $\overline{S}_\Omega$ is compact Hausdorff.
    <2>2. Since $S_\Omega$ is an initial segment (convex set) in $\overline{S}_\Omega$, the subspace topology and the order topology on $S_\Omega$ coincide.

<1>2. Compact subsets of $S_\Omega$:
    A closed subset $C \subseteq S_\Omega$ is compact in $S_\Omega$ if and only if $C$ is bounded above by some $\alpha < \Omega$.
    *Proof:*
    <2>1. ($\impliedby$) If $C$ is closed and bounded by $\alpha < \Omega$, then $C$ is a closed subset of the compact interval $[0, \alpha]$, hence $C$ is compact.
    <2>2. ($\implies$) If $C$ is unbounded in $S_\Omega$, the collection of open rays $\{[0, \beta) : \beta \in S_\Omega\}$ forms an open cover of $C$ with no finite subcover (since the supremum of any finite set of elements in $S_\Omega$ is strictly less than $\Omega$). Thus $C$ cannot be compact.

<1>3. Construction of the bijection $f: S_\Omega^* \to \overline{S}_\Omega$:
    Define $f: S_\Omega^* \to \overline{S}_\Omega$ by:
    $$f(x) = x \quad \text{for } x \in S_\Omega, \qquad f(\infty) = \Omega.$$
    $f$ is clearly a bijection.

<1>4. $f$ is a homeomorphism:
    *Proof:*
    <2>1. For $x \in S_\Omega$, a local neighborhood basis at $x$ in $S_\Omega^*$ consists of open intervals $(a, b) \subseteq S_\Omega$ containing $x$. In $\overline{S}_\Omega$, open intervals $(a, b)$ with $b < \Omega$ form the exact same local neighborhood basis at $x$.
    <2>2. A neighborhood basis of $\infty$ in $S_\Omega^*$ consists of sets of the form $(S_\Omega \setminus [0, \alpha]) \cup \{\infty\} = (\alpha, \Omega) \cup \{\infty\}$ for $\alpha < \Omega$ (by <1>2).
    <2>3. Under $f$, the image of $(\alpha, \Omega) \cup \{\infty\}$ is $(\alpha, \Omega) \cup \{\Omega\} = (\alpha, \Omega]$, which is precisely the standard basic open neighborhood of $\Omega$ in $\overline{S}_\Omega$.
    <2>4. Therefore $f$ is an open continuous bijection, so $f$ is a homeomorphism. Q.E.D.
:::
