---
schema: qual/card@1
id: E-N7AOD
kind: problem
title: The fundamental group of a topological group is abelian
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Topological Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked against the located published solution: dbFin, "Section 52: Problem 7 Solution",
    https://dbfin.com/topology/munkres/chapter-9/section-52-the-fundamental-group/problem-7-solution/
    (read 2026-11-11; kept at tmp/sources/dbfin/section-52-the-fundamental-group/problem-7-solution.txt), and against Munkres, Topology (2000), Section 52
    Exercise 7, printed p. 335. dbFin answers all four parts. What was corrected: in part (c) dbFin's displayed computation of (f star e) tensor (e star g) reads f(s) on [0,1/2] and g(s) on [1/2,1], which forgets the reparametrisation; the correct values are f(2s) and g(2s-1), and the card has them. Part (d) is dbFin's argument by the interchange law, written out.
---

::: {.exercise}

Let $G$ be a topological group with operation $\cdot$ and identity element $x_0$.
Let $\Omega(G, x_0)$ denote the set of all loops in $G$ based at $x_0$.
If $f, g \in \Omega(G, x_0)$, let us define a loop $f \otimes g$ by the rule

$$
(f \otimes g)(s) = f(s) \cdot g(s).
$$

(a) Show that this operation makes the set $\Omega(G, x_0)$ into a group.

(b) Show that this operation induces a group operation $\otimes$ on $\pi_1(G, x_0)$.

(c) Show that the two group operations $*$ and $\otimes$ on $\pi_1(G, x_0)$ are the same.
[Hint: Compute $(f * e_{x_0}) \otimes (e_{x_0} * g)$.]

(d) Show that $\pi_1(G, x_0)$ is abelian.
:::

::: {.solution}
Let $e=x_0$ be the identity.

(a) Pointwise multiplication of loops is associative because multiplication in $G$ is associative. The constant loop $e_e$ is the identity, and
$$
f^{-1}(s)=f(s)^{-1}
$$
is a continuous loop and is the inverse of $f$. Thus $(\Omega(G,e),\otimes)$ is a group.

(b) If $f\simeq f'$ and $g\simeq g'$ through based homotopies $F,G$, then
$$
H(s,t)=F(s,t)G(s,t)
$$
is a based homotopy from $f\otimes g$ to $f'\otimes g'$. Hence
$$
[f]\otimes[g]=[f\otimes g]
$$
is well defined on $\pi_1(G,e)$.

(c) In $\pi_1(G,e)$, let $*$ denote ordinary loop concatenation. Since $f*e_e\simeq f$ and $e_e*g\simeq g$,
$$
[f]\otimes[g]=[f*e_e]\otimes[e_e*g].
$$
For $s\le1/2$, $((f*e_e)\otimes(e_e*g))(s)=f(2s)\cdot e=f(2s)$, and for $s\ge1/2$ it equals $e\cdot g(2s-1)=g(2s-1)$. So
$$
(f*e_e)\otimes(e_e*g)=f*g.
$$
Therefore
$$
[f]\otimes[g]=[f]*[g].
$$
So the two operations coincide.

(d) The operation $\otimes$ also satisfies the interchange law with concatenation:
$$
(a*b)\otimes(c*d)=(a\otimes c)*(b\otimes d).
$$
This holds pointwise for loops, hence for their classes. Write $1=[e_e]$, the identity for both operations. By part (c) and the interchange law,
$$
[f]*[g]
=[f]\otimes[g]
=(1*[f])\otimes([g]*1)
=(1\otimes[g])*([f]\otimes1)
=[g]*[f].
$$
Thus $\pi_1(G,e)$ is abelian.
:::
