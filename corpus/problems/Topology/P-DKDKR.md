---
schema: qual/card@1
id: P-DKDKR
kind: problem
title: Lift multiplication to the universal cover of a topological group
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-04
  note: Restored the hypotheses and task from topology_2005-2003, problem (10b).
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-04
---

::: problem
Let $G$ be a path-connected, locally path-connected topological group with identity $e$ and multiplication
\[
\mu:G\times G\to G.
\]
Let
\[
p:(H,e')\to(G,e)
\]
be a universal covering map.

Show that there is a continuous map
\[
\mu':H\times H\to H
\]
such that
\[
p\circ\mu'=\mu\circ(p\times p).
\]
:::

::: {.solution}
<1>1. The space $H\times H$ is path connected and simply connected.
::: {.proof}
The universal covering space $H$ is path connected and simply connected.
Products of path-connected spaces are path connected, and
\[
\pi_1(H\times H,(e',e'))
\cong
\pi_1(H,e')\times\pi_1(H,e')
=0.
\]
:::

<1>2. Define
\[
F\definedas\mu\circ(p\times p):H\times H\to G.
\]
Then
\[
F(e',e')=e.
\]
::: {.proof}
Since $p(e')=e$ and $e$ is the identity of $G$,
\[
F(e',e')
=\mu(p(e'),p(e'))
=\mu(e,e)
=e.
\]
:::

<1>3. The based map
\[
F:(H\times H,(e',e'))\to(G,e)
\]
has a unique lift
\[
\mu':(H\times H,(e',e'))\to(H,e')
\]
through $p$.
::: {.proof}
The covering-space lifting criterion says that a based map $F:(X,x_0)\to(G,e)$ lifts to $(H,e')$ if and only if
\[
F_*\pi_1(X,x_0)
\subseteq
p_*\pi_1(H,e').
\]
Here both groups are trivial: the left one by <1>1 and the right one because $H$ is simply connected.
Thus a lift exists.
Its value at the basepoint is prescribed to be $e'$, so uniqueness of based lifts gives uniqueness.
:::

<1>4. The lift $\mu'$ has the required compatibility with multiplication on $G$.
::: {.proof}
By the definition of a lift in <1>3,
\[
p\circ\mu'=F.
\]
Substitute the definition of $F$ from <1>2 to obtain
\[
p\circ\mu'=\mu\circ(p\times p).
\]
In particular,
\[
p(\mu'(a,b))=p(a)p(b)
\qquad(a,b\in H).
\]
Continuity of $\mu'$ is part of the lifting theorem, so no path-dependent definition of the product is required.
:::
:::
