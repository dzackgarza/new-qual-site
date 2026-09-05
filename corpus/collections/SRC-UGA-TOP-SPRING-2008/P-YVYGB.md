---
schema: qual/card@1
id: P-YVYGB
kind: problem
title: 'The commutator cover of a genus-$2$ surface: regularity, deck transformations,
  and a loop lifting trivially'
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Group Actions
  - Surfaces
  - Fundamental Group
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked the statement against problem 5 of the official UGA Spring 2008 topology exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-05
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: >-
    Used normal-cover classification with C=[G,G]. Since C is characteristic,
    the cover is regular and Deck is G/C=G_ab=Z^4. The nontrivial commutator
    [a_1,b_1] lies in C and hence induces the identity deck transformation;
    its nontriviality is witnessed by a quotient of the surface group onto a
    free group. Compare Hatcher, Algebraic Topology, Proposition 1.39 and the
    genus-g surface presentation preceding Corollary 1.27.
---

::: problem
Let $S$ be the closed orientable surface of genus 2 and let $C$ be the commutator subgroup of $\pi_1 (S, \ast)$.
Let $\tilde S$ be the cover corresponding to $C$.
Is the covering map $\tilde S \to S$ regular?

> The term "normal" is sometimes used as a synonym for regular in this context.

What is the group of deck transformations?

Give an example of a nontrivial element of $\pi_1 (S, \ast)$ which lifts to a trivial deck transformation.
:::

::: {.solution}
Set
\[
G=\pi_1(S,*),
\qquad
C=[G,G].
\]

<1>1. The subgroup $C$ is normal in $G$.
::: {.proof}
The commutator subgroup of any group is characteristic.
Indeed, if
\[
\varphi:G\longrightarrow G
\]
is an automorphism, then
\[
\varphi([x,y])=[\varphi(x),\varphi(y)]
\]
for every $x,y\in G$.
Thus $\varphi(C)\subseteq C$; applying the same argument to $\varphi^{-1}$ gives equality.
Every characteristic subgroup is normal, so $C\trianglelefteq G$.
:::

<1>2. The covering
\[
p:\widetilde S\longrightarrow S
\]
corresponding to $C$ is regular.
::: {.proof}
For a connected covering of a connected, locally path-connected space, the covering is regular exactly when the corresponding subgroup of the fundamental group is normal.
By <1>1, the corresponding subgroup $C$ is normal in $G$.
Hence $p$ is regular.
:::

<1>3. The deck transformation group is
\[
\operatorname{Deck}(p)\cong G/C.
\]
::: {.proof}
For a regular covering corresponding to a normal subgroup $H\trianglelefteq\pi_1(S,*)$, the deck transformation group is canonically isomorphic to
\[
\pi_1(S,*)/H.
\]
Apply this with $H=C$.
:::

<1>4. One has
\[
G/C\cong\ZZ^4.
\]
::: {.proof}
For a closed orientable surface of genus $2$,
\[
G
\cong
\left\langle
a_1,b_1,a_2,b_2
\ \middle|\
[a_1,b_1][a_2,b_2]=1
\right\rangle.
\]
The quotient by $C=[G,G]$ is the abelianization $G_{\mathrm{ab}}$.
After abelianization, every commutator is trivial, so the displayed relator imposes no relation among the four generator classes.
Therefore
\[
G/C=G_{\mathrm{ab}}\cong\ZZ^4.
\]
:::

<1>5. The element
\[
\gamma=[a_1,b_1]
\]
is nontrivial in $G$.
::: {.proof}
Let $F(a,b)$ be the free group on $a,b$.
Define a map on the generators of the surface presentation by
\[
a_1\longmapsto a,
\qquad
b_1\longmapsto b,
\qquad
a_2\longmapsto b,
\qquad
b_2\longmapsto a.
\]
The surface relator maps to
\[
[a,b][b,a]
=[a,b][a,b]^{-1}
=1,
\]
so this assignment induces a homomorphism
\[
\psi:G\longrightarrow F(a,b).
\]
But
\[
\psi(\gamma)=[a,b]=aba^{-1}b^{-1},
\]
which is a nonempty reduced word in the free group and hence is not the identity.
Thus $\gamma\ne1$ in $G$.
:::

<1>6. The nontrivial element $\gamma=[a_1,b_1]$ induces the trivial deck transformation of $\widetilde S$.
::: {.proof}
By definition,
\[
\gamma\in[G,G]=C.
\]
Under the isomorphism in <1>3, the deck transformation associated to an element $g\in G$ depends only on its coset $gC$.
Thus
\[
\gamma C=C,
\]
the identity element of $G/C$, so $\gamma$ induces the identity deck transformation.

Equivalently, the lift of a loop representing $\gamma$ from a chosen point of the fiber is closed.
The associated deck transformation fixes that point, and a deck transformation of a connected cover that fixes one point is the identity.
:::

Therefore
\[
\boxed{p\text{ is regular},\qquad
\operatorname{Deck}(p)\cong\ZZ^4,\qquad
[a_1,b_1]\ne1\text{ acts trivially}.}
\]
:::
