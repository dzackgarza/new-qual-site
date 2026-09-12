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
Let \(e=x_0\) be the identity.

(a) Pointwise multiplication of loops is associative because multiplication in \(G\) is associative. The constant loop \(e_e\) is the identity, and
\[
f^{-1}(s)=f(s)^{-1}
\]
is a continuous loop and is the inverse of \(f\). Thus \((\Omega(G,e),\otimes)\) is a group.

(b) If \(f\simeq f'\) and \(g\simeq g'\) through based homotopies \(F,G\), then
\[
H(s,t)=F(s,t)G(s,t)
\]
is a based homotopy from \(f\otimes g\) to \(f'\otimes g'\). Hence
\[
[f]\otimes[g]=[f\otimes g]
\]
is well defined on \(\pi_1(G,e)\).

(c) In \(\pi_1(G,e)\), let \(*\) denote ordinary loop concatenation. Since \(f*e_e\simeq f\) and \(e_e*g\simeq g\),
\[
[f]\otimes[g]=[f*e_e]\otimes[e_e*g].
\]
Pointwise multiplication distributes over these two half-interval descriptions, and one checks directly that
\[
(f*e_e)\otimes(e_e*g)=f*g.
\]
Therefore
\[
[f]\otimes[g]=[f]*[g].
\]
So the two operations coincide.

(d) The operation \(\otimes\) also satisfies the interchange law with concatenation:
\[
(a*b)\otimes(c*d)=(a\otimes c)*(b\otimes d).
\]
Since \(*=\otimes\) on homotopy classes and both have the same identity, the Eckmann--Hilton calculation gives
\[
[f]*[g]
=([f]*1)\otimes(1*[g])
=(1*[g])\otimes([f]*1)
=[g]*[f].
\]
Thus \(\pi_1(G,e)\) is abelian.
:::
