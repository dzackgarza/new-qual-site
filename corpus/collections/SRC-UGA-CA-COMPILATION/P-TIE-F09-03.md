---
schema: qual/card@1
id: P-TIE-F09-03
kind: problem
title: Lagrange inversion for $z-a-qf(z)=0$ via the residue theorem
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Fall 2009, question 3.
---

::: {.problem}
Suppose that $f$ is an analytic function in the region D which contains the point a. Let

$F ( z ) = z - a - q f ( z )$ where q is a complex parameter.

(1) Let $K \subset D$ be a circle with the center at point a and also we assume that $f ( z ) \neq 0$ for $z \in K$ . Prove that the function F has one and only one zero $z = w$ on the closed disc K whose boundary is the circle K if $| q | < \operatorname* { m i n } _ { z \in K } { \frac { | z - a | } { | f ( z ) | } }$

(2) Let G(z) be an analytic function on the disk K. Apply the residue theorem to prove that $\frac { G ( w ) } { F ^ { \prime } ( w ) } = \frac { 1 } { 2 \pi i } \int _ { K } \frac { G ( z ) } { F ( z ) } d z$ , where w is the zero from (1).

(3) $\mathrm { I f } ~ z \in { K }$ , prove that the function $\displaystyle \frac { 1 } { F ( z ) }$ can be represented as a convergent series with respect to q: ${ \frac { 1 } { F ( z ) } } = \sum _ { n = 0 } ^ { \infty } { \frac { ( q f ( z ) ) ^ { n } } { ( z - a ) ^ { n + 1 } } }$
:::
