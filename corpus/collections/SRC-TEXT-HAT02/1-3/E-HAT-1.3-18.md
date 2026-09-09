---
schema: qual/card@1
id: E-HAT-1.3-18
kind: problem
title: "Universal abelian covering space"
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 1.3, Exercise 18; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Identified the universal abelian cover with the commutator-subgroup cover and described the two- and three-generator cases as integer lattice Cayley graphs.
---

For a path-connected, locally path-connected, and semilocally simply-connected space $X$, call a path-connected covering space $\tilde{X} \to X$ abelian if it is normal and has abelian deck transformation group.
Show that $X$ has an abelian covering space that is a covering space of every other abelian covering space of $X$, and that such a "universal" abelian covering space is unique up to isomorphism.
Describe this covering space explicitly for $X = S^1 \vee S^1$ and $X = S^1 \vee S^1 \vee S^1$.

::: {.solution}
Let
\[
G=\pi_1(X,x_0).
\]

<1>1. A connected normal covering corresponding to a normal subgroup $H\triangleleft G$ is abelian exactly when
\[
[G,G]\subseteq H.
\]
::: {.proof}
For a connected normal covering with subgroup $H$, the deck transformation group is
\[
G/H.
\]
This quotient is abelian exactly when every commutator maps to the identity, equivalently when the commutator subgroup satisfies
\[
[G,G]\subseteq H.
\]
:::

<1>2. Let
\[
p_{\mathrm{ab}}:X_{\mathrm{ab}}\to X
\]
be the connected covering corresponding to the subgroup
\[
[G,G]\le G.
\]
Then $p_{\mathrm{ab}}$ is an abelian covering with deck group
\[
G/[G,G]=G_{\mathrm{ab}}.
\]
::: {.proof}
The commutator subgroup is normal.
By <1>1 its associated connected normal cover is abelian, and the standard normal-cover deck-group theorem identifies its deck group with the displayed quotient.
:::

<1>3. The cover $X_{\mathrm{ab}}$ covers every other connected abelian covering of $X$.
::: {.proof}
Let
\[
q:Y\to X
\]
be any connected abelian covering, corresponding to a subgroup $H\triangleleft G$.
By <1>1,
\[
[G,G]\subseteq H.
\]
The covering-space factorization criterion says that a connected cover for subgroup $K$ covers the connected cover for subgroup $H$ exactly when, after compatible basepoint choices,
\[
K\subseteq H.
\]
Taking $K=[G,G]$ gives a covering map
\[
X_{\mathrm{ab}}\to Y
\]
over $X$.
:::

<1>4. Any universal abelian covering is isomorphic to $X_{\mathrm{ab}}$.
::: {.proof}
Suppose
\[
q:U\to X
\]
is an abelian cover that covers every other abelian cover, and let its subgroup be $K$.
Since $U$ is abelian, <1>1 gives
\[
[G,G]\subseteq K.
\]
Since $U$ covers $X_{\mathrm{ab}}$, the factorization criterion gives
\[
K\subseteq [G,G].
\]
Thus
\[
K=[G,G].
\]
Connected coverings with the same subgroup are isomorphic over $X$ after basepoint choice, hence unbased as well.
:::

<1>5. For
\[
X=S^1\vee S^1,
\qquad
G=F(a,b),
\]
the universal abelian cover is the square lattice graph in $\mathbb R^2$.
::: {.proof}
The abelianization is
\[
F(a,b)_{\mathrm{ab}}\cong\mathbb Z^2.
\]
Use one vertex
\[
v_{(m,n)}
\]
for each $(m,n)\in\mathbb Z^2$.
Attach an oriented $a$-edge
\[
v_{(m,n)}\to v_{(m+1,n)}
\]
and an oriented $b$-edge
\[
v_{(m,n)}\to v_{(m,n+1)}.
\]
Map all $a$-edges to the first circle and all $b$-edges to the second.
This is the labelled Cayley covering graph of $\mathbb Z^2$.
Its deck transformations are the translations
\[
(m,n)\mapsto(m+p,n+q),
\qquad(p,q)\in\mathbb Z^2,
\]
so the deck group is $\mathbb Z^2$, and its subgroup is the kernel of
\[
F(a,b)\to\mathbb Z^2,
\]
namely $[F,F]$.
:::

<1>6. For
\[
X=S^1\vee S^1\vee S^1,
\qquad
G=F(a,b,c),
\]
the universal abelian cover is the cubic lattice graph in $\mathbb R^3$.
::: {.proof}
Now
\[
G_{\mathrm{ab}}\cong\mathbb Z^3.
\]
Put a vertex at every lattice point
\[
(m,n,p)\in\mathbb Z^3
\]
and join it by oriented $a$-, $b$-, and $c$-edges to the points obtained by adding the three standard basis vectors.
Map these edge families to the three wedge circles.
The deck group is the translation group $\mathbb Z^3$, and the corresponding subgroup is the commutator subgroup of $F(a,b,c)$.
:::

<1>7. Therefore the commutator-subgroup cover is the unique universal abelian covering, with the stated lattice models for the two examples.
::: {.proof}
Existence and universality are <1>2--<1>3, uniqueness is <1>4, and the explicit models are <1>5--<1>6.
:::
:::
