---
schema: qual/card@1
id: P-TRIV-LA38
kind: problem
title: Rotation--scaling--shear decomposition of $SL_2(\mathbb{R})$ matrices
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Linear Algebra, Problem 38, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: problem
Consider the matrix $A = \left[ \begin{array} { l l } { a } & { b } \\ { c } & { d } \end{array} \right] , a , b , c , d \in \mathbb { R }$ , det $A = 1$ . It transforms the basis vectors ${ \vec { e } } _ { 1 } = \left[ { \begin{array} { l } { 1 } \\ { 0 } \end{array} } \right] , { \vec { e } } _ { 2 } = \left[ { \begin{array} { l } { 0 } \\ { 1 } \end{array} } \right]$ into ${ \vec { g } } _ { 1 } = { \Big [ } { \frac { a } { c } } { \Big ] } , { \vec { g } } _ { 2 } = { \Big [ } { \frac { b } { d } } { \Big ] }$ . One can obtain a useful decomposition of A by making an inverse transformation in three steps.

(a) Construct the rotation matrix $R ^ { - 1 }$ that sends $\vec { g } _ { 1 }$ to $R ^ { - 1 } ( \vec { g } _ { 1 } ) \lVert \vec { e } _ { 1 }$ . How does it act on $\vec { g } _ { 2 } ?$

(b) Construct the diagonal matrix $P ^ { - 1 }$ such that det $P ^ { - 1 } = 1$ and $P ^ { - 1 } ( R ^ { - 1 } ( \vec { g } _ { 1 } ) ) =$ $\vec { e } _ { 1 }$ . Show that the components of $P ^ { - 1 } ( R ^ { - 1 } ( \vec { g } _ { 2 } ) )$ are ${ \binom { x } { 1 } } , x \in \mathbb { R }$

(c) Apply a shear transformation $T ^ { - 1 }$ that leaves $\vec { e } _ { 1 }$ invariant and sends $P ^ { - 1 } ( R ^ { - 1 } ( \vec { g } _ { 2 } ) )$ to $\vec { e } _ { 2 }$ Then, we have $T ^ { - 1 } P ^ { - 1 } R ^ { - 1 } A = E$ ,or $A = R P T$

(d) Show that this decomposition is unique.
:::
