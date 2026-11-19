---
schema: qual/card@1
id: E-HAT-3.3-5
kind: problem
title: Orientability of products
classification:
  areas:
  - topology
  topics:
  - Poincaré Duality
  - Manifolds
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.3, Exercise 5; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.3, Exercise 5; it matches the printed text. The card says 'nonempty manifolds', which the print leaves implicit.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read both directions: product charts with the product orientation in one direction, and in the
    other the restriction of the orientation system of $M\times N$ to $M\times\{y_0\}$, which is
    the tensor of the system of $M$ with a fixed copy of $\ZZ$.
- event: source-corrected
  by: claude
  date: 2026-11-07
  note: >-
    Statement restored to the printed sentence (Hatcher p.257 §3.3 Ex.5), which has no nonemptiness
    hypothesis; the earlier card silently added one. The printed "iff" is false as it stands, and the
    solution now says why: $M=\emptyset$ is vacuously orientable and $M\times N=\emptyset$ with it, so
    the converse needs both factors nonempty. The equivalence itself is unchanged. Not checked here:
    whether the local-orientation system of a product is the tensor of the two (the Künneth-type
    identification is cited, not rederived).
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps. The card's forward direction (both orientable implies the
    product orientable) is kept, with the local homology of a product now stated as its own step
    with the excision and Kunneth inputs named. The converse was written in the prose as
    "restricting the orientation system to M x {y_0} gives the orientation system of M tensored
    with a fixed rank-one group, so the system of M is trivial", which skips the restriction step;
    it is now: an open subset of an orientable manifold is orientable; M x V is open in M x N for
    a chart V of N and is homeomorphic to M x R^n; and M x R^n orientable implies M orientable
    because the orientation double cover of M x R^n is the orientation double cover of M times
    R^n, triviality gives it exactly two components, and the components of X x R^n are C x R^n
    for the components C of X, so the double cover of M has two components. The empty-factor case
    the prose mentions is now a step, since M x N = empty is vacuously orientable. Statement
    unchanged; no retained solution set covers this exercise.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    Notation repair after the corpus check reported raw TeX the page cannot show. The
    sentence naming the book's own treatment wrote `\S3.3`, a section sign written as a TeX
    command outside a math span, which the HTML writer drops; it now reads the character
    `§3.3`. Mathematics and wording unchanged.
---

::: {.problem}
Show that $M \times N$ is orientable iff $M$ and $N$ are both orientable.
:::

::: {.solution}
Orientability is taken in Hatcher's sense, an orientable $n$-manifold being one whose orientation double cover is trivial, equivalently one that carries a local orientation system $x\mapsto\mu_x\in H_n(M,M-\{x\};\ZZ)$; the local homology of a product is the tensor product of the local homologies of the factors, and that is the only input used besides the elementary behaviour of components of a product. The printed statement needs both factors nonempty: if $M=\emptyset$ then $M\times N=\emptyset$, which is vacuously orientable whatever $N$ is. The argument is this card's own: no retained solution set covers this exercise.

::: pf

::: {.pf-step #empty}
If $M$ or $N$ is empty then the conclusion holds, so assume both nonempty.

::: pf-proof
If $M=\emptyset$ then $M\times N=\emptyset$; the empty manifold has a unique (empty) orientation and is orientable, while the right-hand side of the equivalence is false as soon as $N\ne\emptyset$. So the equivalence is a statement about nonempty factors, which the rest of the proof assumes.
:::

:::


::: {.pf-step #local}
For $x\in M$ and $y\in N$ there is a natural isomorphism $H_{m+n}(M\times N,M\times N-\{(x,y)\};\ZZ)\cong H_m(M,M-\{x\};\ZZ)\otimes H_n(N,N-\{y\};\ZZ)$.

::: pf-proof
Choose coordinate balls $U\ni x$ and $V\ni y$ with $U$ homeomorphic to $\RR^m$ and $V$ to $\RR^n$, so that $U\times V$ is a neighbourhood of $(x,y)$ homeomorphic to $\RR^{m+n}$. By excision, the inclusions of pairs induce isomorphisms $H_*(U\times V,U\times V-\{(x,y)\})\cong H_*(M\times N,M\times N-\{(x,y)\})$ and $H_*(U,U-\{x\})\cong H_*(M,M-\{x\})$, $H_*(V,V-\{y\})\cong H_*(N,N-\{y\})$. The Künneth formula applied to the product pair $(U\times V,U\times V-\{(x,y)\})$ gives the tensor decomposition in degree $m+n$, the only degree in which both factors are nonzero, and the same decomposition is natural for inclusions of coordinate balls; this is the pairing $\mu_x\otimes\nu_y\mapsto\mu_x\times\nu_y$ used in Hatcher, §3.3.
:::

:::


::: {.pf-step #forward}
If $M$ and $N$ are orientable then $M\times N$ is orientable.

::: pf-proof
Let $x\mapsto\mu_x$ and $y\mapsto\nu_y$ be local orientation systems. For $(x,y)$ define $\mu_{(x,y)}$ to be the image of $\mu_x\otimes\nu_y$ under the isomorphism of step [](#local){.pf-ref}; it is a generator, because a tensor product of generators of infinite cyclic groups generates. The systems are locally constant, and the isomorphism of step [](#local){.pf-ref} is natural, so $(x,y)\mapsto\mu_{(x,y)}$ is locally constant as well: a local orientation system on $M\times N$. Hence $M\times N$ is orientable.
:::

:::


::: {.pf-step #open}
An open subset of an orientable manifold is orientable.

::: pf-proof
If $W\subseteq X$ is open and $x\mapsto\mu_x$ is a local orientation system on $X$, then $x\mapsto\mu_x$ restricted to $W$ is a local orientation system on the $n$-manifold $W$: each point of $W$ has a neighbourhood in $W$ on which the system is constant, because it has one in $X$. So $W$ is orientable.
:::

:::


::: {.pf-step #reduce}
If $M\times N$ is orientable and $V\subseteq N$ is a chart, then $M\times V$ is orientable, hence so is $M\times\RR^n$.

::: pf-proof
$M\times V$ is open in $M\times N$, so it is orientable by step [](#open){.pf-ref}. Choosing a homeomorphism $\psi\colon V\to\RR^n$ of the chart gives a homeomorphism $\mathrm{id}\times\psi\colon M\times V\to M\times\RR^n$; orientability is a homeomorphism invariant, since a homeomorphism carries local orientation systems to local orientation systems through the induced isomorphisms of local homology. So $M\times\RR^n$ is orientable.
:::

:::


::: {.pf-step #extract}
If $M\times\RR^n$ is orientable then $M$ is orientable.

::: pf-proof
Let $\widetilde M\to M$ be the orientation double cover, whose points are the pairs $(x,\mu)$ with $\mu$ a generator of $H_m(M,M-\{x\};\ZZ)$. By step [](#local){.pf-ref} with $\RR^n$ in place of $N$, a generator of $H_{m+n}(M\times\RR^n,M\times\RR^n-\{(x,t)\};\ZZ)$ corresponds to $\mu\otimes\nu_t$ with $\nu_t$ a fixed generator of $H_n(\RR^n,\RR^n-\{t\};\ZZ)$, and this correspondence is natural; so the orientation double cover of $M\times\RR^n$ is $\widetilde M\times\RR^n$, and $M\times\RR^n$ being orientable says exactly that this double cover is trivial, i.e. that $\widetilde M\times\RR^n$ has exactly two components. The components of a product $X\times\RR^n$ are the sets $C\times\RR^n$ with $C$ a component of $X$, since $\RR^n$ is connected; so $\widetilde M$ has exactly two components. A double cover whose total space has two components is trivial, hence the local orientation system of $M$ extends over $M$ and $M$ is orientable.
:::

:::


::: {.pf-step #conclusion}
$M\times N$ is orientable if and only if $M$ and $N$ are both orientable.

::: pf-proof
One implication is step [](#forward){.pf-ref}. For the other, suppose $M\times N$ is orientable; by steps [](#reduce){.pf-ref} and [](#extract){.pf-ref} $M$ is orientable, and the same argument with the factors exchanged, using a chart of $M$, gives that $N$ is orientable. Together with step [](#empty){.pf-ref} this covers the vacuous cases as well.
:::

:::

:::
:::
