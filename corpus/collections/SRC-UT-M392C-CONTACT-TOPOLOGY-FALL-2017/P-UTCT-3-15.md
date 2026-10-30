---
schema: qual/card@1
id: P-UTCT-3-15
kind: problem
title: Generic characteristic foliations satisfy the hypotheses of Giroux's dividing set theorem
classification:
  areas:
  - topology
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Exercise 3.15 of the retained George D. Torres notes from Bob Gompf's M392C Contact Topology course, Fall 2017.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Replaced the truncated statement with Exercise 3.15 and the hypotheses of Theorem 3.13 it refers to, from p. 25 of Gompf Contact Topology.pdf.
---

::: {.problem}
Let $F$ be a compact oriented surface with an oriented singular foliation $\mathcal{F}$.
For a closed leaf, the monodromy $\phi : I \to I$ along a normal interval is defined by following the foliation until it intersects the normal again; the leaf is *attractive* if $\phi'(0) < 1$ and *repellant* if $\phi'(0) > 1$.
Define
$$
K_+ = \{+ \text{ singular points}\} \cup \{\text{repellant closed leaves}\}, \qquad K_- = \{- \text{ singular points}\} \cup \{\text{attractive closed leaves}\}.
$$
Theorem 3.13 (Giroux et al.) assumes that $\partial F$ is a union of leaves and critical points and that:

1. Each leaf limits as $t \to \pm\infty$ to a singular point or closed leaf ($t$ is a parameter on the leaf).
2. Each singular point has nonzero divergence and each closed leaf is either repellant or attractive (i.e. $\phi'(0) \neq 1$).
3. No leaf runs from $K_-$ to $K_+$.
4. The collection of singular points of $\mathcal{F}$ has finitely many connected components which can be ordered so that each leaf between points of the same sign preserves that order.

Show that the hypotheses of Theorem 3.13 hold for a generic foliation of $F$.
:::

::: {.solution}

The relevant genericity statement is the Kupka--Smale/Peixoto theorem for
flows on compact surfaces, applied to a vector field defining the oriented
singular foliation.

::: pf

::: pf-step

Choose a smooth vector field
$$
v
$$
on $F$ whose oriented trajectories are the leaves of
$$
\mathcal F
$$
and whose zero set is the singular set of $\mathcal F$.


::: pf-proof

An oriented singular foliation on a surface is locally the kernel of a
nonzero $1$-form away from its singular points. After fixing a positive area
form $\omega$, write
$$
\iota_v\omega=\alpha,
$$
where $\ker\alpha=T\mathcal F$.
Then $v$ is tangent to the oriented leaves and vanishes exactly at the
singular points.

:::

:::

::: {.pf-step #s1-2}

After an arbitrarily small $C^\infty$ perturbation, every singular
point of $v$ is nondegenerate and satisfies
$$
\operatorname{div}_\omega v\ne0.
$$


::: pf-proof

Nondegeneracy of a zero means
$$
\det Dv(p)\ne0.
$$
By the standard transversality theorem, this is generic for zeros of vector
fields.

At such a zero,
$$
\operatorname{div}_\omega v(p)
$$
is the trace of the linearization in oriented local coordinates. The
additional condition
$$
\operatorname{tr}Dv(p)=0
$$
is one further scalar equation on the $1$-jet of $v$, hence is avoided by a
generic perturbation as well.

Thus a generic singularity is isolated and has nonzero divergence.

:::

:::

::: {.pf-step #s1-3}

A generic closed leaf is hyperbolic:
$$
\phi'(0)\ne1.
$$
Hence every closed leaf is either attractive or repellant.


::: pf-proof

For a closed orbit, choose a small transverse interval and its Poincaré return
map
$$
\phi:I\to I.
$$
The equation
$$
\phi'(0)=1
$$
is the degeneracy condition for the periodic orbit. The Kupka--Smale theorem
states that, for a residual set of vector fields, all periodic orbits are
hyperbolic, hence
$$
\phi'(0)\ne1.
$$
If
$$
\abs{\phi'(0)}<1
$$
the orbit is attractive; if
$$
\abs{\phi'(0)}>1
$$
it is repellant. In the oriented surface convention of the source, the
monodromy preserves transverse orientation, so
$$
\phi'(0)>0,
$$
and these conditions reduce to the source's inequalities
$$
\phi'(0)<1
\quad\text{or}\quad
\phi'(0)>1.
$$

:::

:::

::: {.pf-step #s1-4}

For a generic foliation on compact $F$, the nonwandering set consists
of finitely many singular points and hyperbolic closed leaves.


::: pf-proof

Peixoto's structural-stability theorem for flows on compact surfaces says
that Morse--Smale vector fields form an open dense set: their nonwandering
sets consist of finitely many hyperbolic equilibria and hyperbolic periodic
orbits, and all invariant manifolds meet transversely.

The same conclusion applies here after the generic perturbation in
steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

Every nonsingular nonclosed leaf has
$$
\alpha\text{-limit}
\quad\text{and}\quad
\omega\text{-limit}
$$
equal to a singular point or a closed leaf.


::: pf-proof

Let $\gamma$ be a leaf that is neither singular nor periodic.
Its forward and backward limit sets are nonempty compact invariant subsets
of the nonwandering set.

By step [](#s1-4){.pf-ref}, the nonwandering set is a finite union of isolated singular
points and periodic orbits. A connected limit set contained in such a finite
union must be one of those individual basic pieces.

Therefore
$$
\lim_{t\to+\infty}\gamma(t)
$$
and
$$
\lim_{t\to-\infty}\gamma(t)
$$
are each a singular point or a closed leaf, in the sense of convergence to
that invariant set.

:::

:::

::: {.pf-step #s1-6}

Thus hypothesis (1) of Theorem 3.13 holds generically.


::: pf-proof

This is exactly step [](#s1-5){.pf-ref}, together with the trivial cases of singular and
closed leaves themselves.

:::

:::

::: {.pf-step #s1-7}

Hypothesis (2) of Theorem 3.13 holds generically.


::: pf-proof

Step [](#s1-2){.pf-ref} gives nonzero divergence at every singular point, and step [](#s1-3){.pf-ref}
gives
$$
\phi'(0)\ne1
$$
for every closed leaf.

:::

:::

::: {.pf-step #s1-8}

A generic characteristic foliation has no leaf running from
$$
K_-
\quad\text{to}\quad
K_+.
$$


::: pf-proof

There are two possibilities.

First, an attractive closed leaf cannot be the backward limit of a distinct
leaf, and a repellant closed leaf cannot be the forward limit of a distinct
leaf. Thus no oriented trajectory can run from an attractive closed leaf in
$K_-$ to a repellant closed leaf in $K_+$.

For singular endpoints, recall the contact-sign convention from the previous
section of the source:
for a positive contact structure,
$$
\operatorname{sign}
\bigl(
\operatorname{div}_\omega v(p)
\bigr)
=
\operatorname{sign}(p).
$$
Thus positive elliptic singularities are sources and negative elliptic
singularities are sinks, so the forbidden direction is dynamically
impossible in the elliptic cases.

If a trajectory from a negative singular point to a positive singular point
involves saddle branches, it is a saddle connection. Stable and unstable
manifolds of hyperbolic singularities are $1$-dimensional. A connecting orbit
forces them to coincide along that orbit, hence their intersection is not
transverse. Kupka--Smale transversality excludes such saddle connections
generically.

Therefore no generic leaf runs from $K_-$ to $K_+$.

:::

:::

::: {.pf-step #s1-9}

The singular set of a generic foliation has finitely many connected
components.


::: pf-proof

By step [](#s1-2){.pf-ref}, every singular point is isolated. A closed discrete subset of
the compact surface $F$ is finite. Hence the singular set consists of
finitely many singleton connected components.

:::

:::

::: pf-step

Define a directed graph whose vertices are the singular points of one
fixed sign and whose directed edges are leaves joining two such singular
points in the direction of the flow. Generically this graph is finite and
acyclic.


::: pf-proof

Finiteness follows from step [](#s1-9){.pf-ref}.

A directed cycle would consist of a finite cyclic chain of separatrices
between hyperbolic singularities of the same sign. Each edge is a saddle
connection. As in step [](#s1-8){.pf-ref}, such a connection is a nontransverse
intersection of a stable and an unstable $1$-manifold, forbidden by the
Kupka--Smale condition.

Hence the directed graph has no directed cycle.

:::

:::

::: {.pf-step #s1-11}

Every finite acyclic directed graph admits a linear order of its
vertices in which every directed edge points forward.


::: pf-proof

This is the standard topological-sorting theorem for finite directed acyclic
graphs.

Inductively, an acyclic finite directed graph has a vertex with no incoming
edge. Place it first, delete it and all outgoing edges, and repeat.

:::

:::

::: {.pf-step #s1-12}

Hypothesis (4) of Theorem 3.13 holds generically.


::: pf-proof

By step [](#s1-9){.pf-ref} there are finitely many singular components.

Apply step [](#s1-11){.pf-ref} separately to the directed connection graphs of the positive
and negative singular points. The resulting order has the property that every
leaf joining two singular points of the same sign preserves the chosen order.
This is exactly hypothesis (4).

:::

:::

::: {.pf-step #s1-13}

The boundary condition in Theorem 3.13 is also generic relative to a
fixed boundary model.


::: pf-proof

If $F$ is closed, there is nothing to prove.

If $F$ has boundary and the perturbation is required to preserve a boundary
model, perform the Kupka--Smale/Peixoto perturbation in the interior, relative
to a collar of $\partial F$. The source assumes that collar has already been
chosen so that
$$
\partial F
$$
is a union of leaves and singular points. A relative transversality
perturbation leaves this boundary condition unchanged.

:::

:::

::: {.pf-step #s1-14}

Therefore all hypotheses of Theorem 3.13 hold for a generic
characteristic foliation of $F$.


::: pf-proof

Hypothesis (1) is step [](#s1-6){.pf-ref}.
Hypothesis (2) is step [](#s1-7){.pf-ref}.
Hypothesis (3) is step [](#s1-8){.pf-ref}.
Hypothesis (4) is step [](#s1-12){.pf-ref}.
The boundary condition is step [](#s1-13){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-14){.pf-ref} is precisely Exercise 3.15.

:::

:::

:::
