---
schema: qual/card@1
id: P-3DTFZ
kind: problem
title: A map $S^2\to S^2$ of degree 2013
classification:
  areas:
  - topology
  topics:
  - Degree
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-04
  note: Checked the statement against the official UGA Spring 2013 topology exam DOCX and restored the source question mark.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-04
  note: Replaced the conflation of the Riemann-sphere power map with a suspension by an actual suspension construction and homological degree computation.
---

::: problem
Does there exist a map of degree 2013 from $S^2 \to S^2$?
:::

::: {.solution}
<1>1. Define
\[
g:S^1\to S^1,
\qquad
g(z)=z^{2013}.
\]
Then $g$ has degree $2013$.
::: {.proof}
With the standard parametrization
\[
S^1=\{e^{2\pi i t}:t\in\mathbb R/\mathbb Z\},
\]
the map $g$ is induced by
\[
t\longmapsto 2013t
\]
on $\mathbb R/\mathbb Z$.
Hence
\[
g_*:H_1(S^1;\mathbb Z)\to H_1(S^1;\mathbb Z)
\]
is multiplication by $2013$.
Thus $\deg g=2013$.
:::

<1>2. Suspend $g$ to obtain
\[
\Sigma g:\Sigma S^1\to\Sigma S^1.
\]
Using the standard homeomorphism $\Sigma S^1\cong S^2$, regard this as a map
\[
f:S^2\to S^2.
\]
::: {.proof}
The suspension functor sends a map $g:S^1\to S^1$ to the map
\[
\Sigma g([z,t])=[g(z),t].
\]
Since $\Sigma S^1$ is homeomorphic to $S^2$, this gives the required self-map of the sphere.
:::

<1>3. The map $f$ has degree $2013$.
::: {.proof}
The reduced-homology suspension isomorphism
\[
\sigma:\widetilde H_1(S^1;\mathbb Z)
\xrightarrow{\cong}
\widetilde H_2(\Sigma S^1;\mathbb Z)
\]
is natural.
Therefore
\[
(\Sigma g)_*\circ\sigma
=
\sigma\circ g_*.
\]
By <1>1, $g_*$ is multiplication by $2013$.
Since $\sigma$ is an isomorphism, the naturality identity implies that $(\Sigma g)_*$ is also multiplication by $2013$.
Hence
\[
\deg f=2013.
\]
Thus such a map exists.
:::
:::
