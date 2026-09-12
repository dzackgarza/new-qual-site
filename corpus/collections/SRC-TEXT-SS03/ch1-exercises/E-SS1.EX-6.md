---
schema: qual/card@1
id: E-SS1.EX-6
kind: problem
title: "Connected components as equivalence classes"
classification:
  areas:
  - complex-analysis
  topics: ['Complex Numbers', 'Power Series', 'Cauchy-Riemann']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: exercise
6. Let Ω be an open set in C and $z \in \Omega$ . The connected component (or simply the component) of Ω containing z is the set $\mathcal { C } _ { z }$ of all points w in Ω that can be joined to z by a curve entirely contained in Ω.

(a) Check first that $\mathcal { C } _ { z }$ is open and connected.
Then, show that $w \in \mathcal { C } _ { z }$ defines an equivalence relation, that is: $\mathrm { ( i ) } \ z \in \mathcal { C } _ { z } \ , \ \mathrm { ( i i ) }$ $w \in \mathcal { C } _ { z }$ implies $z \in \mathcal { C } _ { w }$ , and (iii) if $w \in \mathcal { C } _ { z }$ and $z \in { \mathcal { C } } _ { \zeta }$ , then $w \in \mathcal { C } _ { \zeta }$

Thus Ω is the union of all its connected components, and two components are either disjoint or coincide.

(b) Show that Ω can have only countably many distinct connected components.

(c) Prove that if Ω is the complement of a compact set, then Ω has only one unbounded component.

[Hint: For (b), one would otherwise obtain an uncountable number of disjoint open balls. Now, each ball contains a point with rational coordinates. For (c), note that the complement of a large disc containing the compact set is connected.]
:::

::: solution
Let $\mathcal C_z$ be the set of points of $\Omega$ that can be joined to $z$ by a curve lying in $\Omega$.

For openness, take $w\in\mathcal C_z$. Since $\Omega$ is open, some disc $D(w,r)$ is contained in $\Omega$. Every $u\in D(w,r)$ can be joined to $w$ by the line segment in that disc, and concatenating this segment with a curve from $z$ to $w$ shows $u\in\mathcal C_z$. Hence $\mathcal C_z$ is open. It is path connected by definition, hence connected.

The relation $w\sim z$ defined by $w\in\mathcal C_z$ is reflexive (use the constant curve), symmetric (reverse a joining curve), and transitive (concatenate joining curves). Hence it is an equivalence relation. Its equivalence classes are exactly the connected components $\mathcal C_z$, so two components are either equal or disjoint and their union is $\Omega$.

For countability, every component is a nonempty open subset of $\mathbb C\cong\mathbb R^2$, hence contains a point of $\mathbb Q^2$. Distinct components are disjoint, so choosing one rational point from each component gives an injection from the set of components into the countable set $\mathbb Q^2$. Therefore there are at most countably many components.

Finally suppose $\Omega=\mathbb C\setminus K$ with $K$ compact. Choose $R>0$ such that $K\subset D(0,R)$. The exterior
\[
E=\{z:|z|>R\}
\]
is connected and lies in $\Omega$, so it is contained in a single component $U$ of $\Omega$. If $V$ is any unbounded component, then $V$ contains some point with modulus $>R$, hence meets $E\subset U$. Components that meet are equal, so $V=U$. Thus $\Omega$ has exactly one unbounded component.
:::
