---
schema: qual/card@1
id: E-PER08-9.5
kind: problem
title: Octahedral axiom for mapping cones
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Completed from the retained Perutz Algebraic Topology I source and checked against the stated hypotheses.
---

::: {.problem}
(*) If a: A$\\ast$ $\\to$ B$\\ast$ and b$\\ast$ : B$\\ast$ $\\to$ C$\\ast$ are chain maps, what can we say about cone(b ◦ a)? Show how to arrange the six groups H$\\ast$(A), H$\\ast$(B), H$\\ast$(C), H$\\ast$(cone(a)), H$\\ast$(cone(b)) and H$\\ast$(cone(ba)) as the vertices of an octahedral diagram of maps.
Four of the faces should be commuting triangles, the other four exact triangles (i.e., long exact sequences visualised as triangles).
The last of these triangles is a long exact sequence · · · $\\to$ Hp(cone(a)) $\\to$ Hp(cone(ba)) $\\to$ Hp$^{-1}$(cone(b)) $\\to$ . . . . The hard part of the exercise is constructing this triangle and proving its exactness.
[Hint: define f : cone(a) $\\to$ cone(ba) by f(x, y) = (x, by). There is a natural inclusion i: cone(b) $\\to$ cone(f). Show that i is a chain-homotopy equivalence.] This exercise shows shows that the derived category of the abelian category of chain complexes satisfies Verdier’s ‘octahedral axiom’ for triangulated categories.
:::

::: {.solution}
Let $a:A\to B$ and $b:B\to C$ be chain maps.
There are the three standard exact triangles
\[
A\xrightarrow a B\to\operatorname{cone}(a)\to A[-1],
\]
\[
B\xrightarrow b C\to\operatorname{cone}(b)\to B[-1],
\]
and
\[
A\xrightarrow{ba}C\to\operatorname{cone}(ba)\to A[-1].
\]
The fourth exact triangle is the octahedral one
\[
\operatorname{cone}(a)\xrightarrow f\operatorname{cone}(ba)
\longrightarrow\operatorname{cone}(b)
\longrightarrow\operatorname{cone}(a)[-1].
\]

<1>1. Define the first map by
\[
f_n(x,y)=(x,b(y)),
\qquad (x,y)\in A_{n-1}\oplus B_n.
\]
::: {.proof}
A direct substitution in the cone differential, using $bd_B=d_Cb$, shows that $f$ is a chain map.
:::

<1>2. $\operatorname{cone}(f)$ is chain-homotopy equivalent to $\operatorname{cone}(b)$.
::: {.proof}
One has
\[
\operatorname{cone}(f)_n
=A_{n-2}\oplus B_{n-1}\oplus A_{n-1}\oplus C_n.
\]
The natural inclusion
\[
i:\operatorname{cone}(b)_n=B_{n-1}\oplus C_n\hookrightarrow\operatorname{cone}(f)_n,
\qquad i(u,v)=(0,u,0,v),
\]
is a chain map.
The two $A$-summands form a contractible mapping-cone pair for the identity of $A$; projecting away that contractible pair gives a chain map $r:\operatorname{cone}(f)\to\operatorname{cone}(b)$ with $ri=\mathrm{id}$, and the standard contraction of the identity cone gives $ir\simeq\mathrm{id}$.
Hence $i$ is a chain-homotopy equivalence.
:::

<1>3. The fourth triangle is exact on homology.
::: {.proof}
Apply the mapping-cone long exact sequence to $f$ and identify $H_*(\operatorname{cone}(f))$ with $H_*(\operatorname{cone}(b))$ using <1>2. We obtain
\[
\cdots\to H_n(\operatorname{cone}(a))\to H_n(\operatorname{cone}(ba))
\to H_n(\operatorname{cone}(b))\to H_{n-1}(\operatorname{cone}(a))\to\cdots.
\]
Together with the three standard cone triangles, these four exact triangles and the evident four commuting triangles arrange the six objects
\[
A,B,C,\operatorname{cone}(a),\operatorname{cone}(b),\operatorname{cone}(ba)
\]
as the vertices of the usual octahedron.
This is the octahedral diagram for the composable maps $a,b$.
:::
:::
