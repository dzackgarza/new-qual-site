---
schema: qual/card@1
id: E-HAT-3.3-31
kind: problem
title: Boundary map sends fundamental class to fundamental class
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
  note: Checked against Hatcher, Algebraic Topology, Section 3.3, Exercise 31; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.3, Exercise 31; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the argument: at each boundary point the global class restricts to the local fundamental
    class of a half-ball, whose boundary is the local generator of the induced boundary
    orientation; a class with that property at every point is the fundamental class of
    $\partial M$. Read at the level of that characterisation.
- event: solution-written
  by: claude
  date: 2026-11-07
  note: >-
    The local half of this proof was a gesture — the image of the relative fundamental class in the
    local relative group was called the local fundamental class of the half-ball, and its local
    boundary the local generator, with no computation behind either claim. The solution now names the
    half-ball N and its flat part N', the two excisions that reduce the global statement to the pair
    (D^n, D^n-1), and the long exact sequence of the contractible pair that makes the boundary map an
    isomorphism there; and it says that M compact makes the boundary compact, so Lemma 3.27(a)
    applies with A equal to the boundary. Not checked: the global sign, which is the one fixed by
    Exercise 30's collar convention.
---

::: {.problem}
Show that if $M$ is a compact $R$-orientable $n$-manifold, then the boundary map $H_n(M, \partial M; R) \to H_{n-1}(\partial M; R)$ sends a fundamental class for $(M, \partial M)$ to a fundamental class for $\partial M$.
:::

::: {.solution}
Let
$$
[M,\partial M]\in H_n(M,\partial M;R)
$$
be a fundamental class, and let
$$
\delta:H_n(M,\partial M;R)\to H_{n-1}(\partial M;R)
$$
be the boundary homomorphism.

Fix $x\in\partial M$. Choose a closed half-ball $N\subset M$ around $x$ that meets $\partial M$ in the flat disk $N'=N\cap\partial M$ and lies in a single boundary chart $H=\{u\in\RR^n:|u|\le\varepsilon,\ u_n\ge0\}$, with $x$ at the centre of $N'$. Excision of the complementary part of $\partial M$ identifies $H_n(M,\partial M;R)\cong H_n(N,N';R)$ and $H_{n-1}(\partial M,\partial M-\{x\};R)\cong H_{n-1}(N',N'-\{x\};R)$, and under these identifications the boundary map of $(M,\partial M)$ becomes the boundary map of $(N,N')$. That pair is $(D^n,D^{n-1})$ up to a homeomorphism of pairs, and $N$ is contractible, so its long exact sequence consists of isomorphisms
$$
\partial:H_n(N,N';R)\longrightarrow H_{n-1}(N';R),\qquad H_{n-1}(N';R)\cong R .
$$
Hence $\partial$ carries the generator $\mu_N$ that is the image of $[M,\partial M]$ to a generator of $H_{n-1}(N';R)$, and therefore to a generator of the local group $H_{n-1}(\partial M,\partial M-\{x\};R)$; the generator is the one fixed in Exercise 30 by dividing the local orientation at $x$ by the collar direction.

Since this holds at every $x\in\partial M$, the class $\delta[M,\partial M]$ is a section of the orientation cover of $\partial M$ whose value at each point is a generator, and $M$ compact makes $\partial M$ compact, so Lemma 3.27(a) with $A=\partial M$ identifies it with the fundamental class: $\delta[M,\partial M]=[\partial M]$, up to the global sign convention for the induced orientation on $\partial M$.
:::
