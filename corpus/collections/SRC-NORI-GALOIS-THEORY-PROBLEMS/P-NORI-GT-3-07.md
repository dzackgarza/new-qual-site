---
schema: qual/card@1
id: P-NORI-GT-3-07
kind: problem
title: Roots of cyclotomic polynomials in characteristic $p$
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against problem 3.7 of the retained Nori Galois Theory Problems PDF.
---

::: {.problem}
The cylotomic polynomials $\Phi _ { n } ( X ) \in \mathbb { Z } [ X ]$ defined for all natural numbers $n _ { \mathrm { : } }$ have the property

$$
X ^ { n } - 1 = \prod _ { d \mid n } \Phi _ { d } ( X )
$$

Let $n = n ^ { \prime } p ^ { k }$ with $p$ not dividing $n ^ { \prime } .$ . let $F$ be a field of characteristic $p$ such that $\mu _ { n ^ { \prime } } ( F )$ has order $n ^ { \prime }$ . Show that the roots of $\Phi _ { n } ( X )$ in $F$ are the primitive $n ^ { \prime } \mathrm { . }$ -th roots of unity, each of them occuring with multiplicity $\varphi ( p ^ { k } )$

Here $\varphi$ is Euler’s phi function.

$\varphi ( m )$ is the order of the group of units of the ring $\mathbb { Z } / m \mathbb { Z }$

Equivalently, $\varphi ( m )$ is the cardinality of the set of natural numbers $k \leq m$ such that $\operatorname { g . c . d . } ( k , m ) = 1$

$\varphi ( 1 ) = 1$ . If $p$ is a prime, then $\varphi ( p ^ { k } ) = p ^ { k - 1 } ( p - 1 ) { \mathrm { ~ i f ~ } } k > 0 .$
:::
