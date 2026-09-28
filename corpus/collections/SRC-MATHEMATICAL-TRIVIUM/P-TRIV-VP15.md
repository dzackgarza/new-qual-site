---
schema: qual/card@1
id: P-TRIV-VP15
kind: problem
title: Derrick's theorem
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Variational Principle, Problem 15, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
”Derrick’s theorem” Consider the functional

$$
E [ \phi ] = \int d ^ { d } x \left( \frac { 1 } { 2 } K _ { a b } ( \phi ) \sum _ { i = 1 } ^ { d } \partial _ { i } \phi ^ { a } \partial _ { i } \phi ^ { b } + V ( \phi ) \right) ,\tag{20}
$$

where $\phi = \phi ( x _ { 1 } , . . . , x _ { d } ) \in C ^ { 2 } ( \mathbb { R } ^ { d } ) , K _ { a b } ( \phi )$ is a positive-definite matrix for any $\phi ,$ i.e.,

$$
K _ { a b } ( \phi ) \partial _ { i } \phi ^ { a } \partial _ { j } \phi ^ { b } \geqslant 0 ,\tag{21}
$$

where the equality implies $\phi = 0$ , and $V ( \phi ) \geqslant 0 , V ( \phi ) = 0 \Rightarrow \phi = 0$ Suppose $\phi _ { 0 } ( x )$ is a non-zero extremum of $E [ \phi ]$ . Consider the configurations of the form $\phi _ { \lambda } ( x ) = \phi _ { 0 } ( \lambda x )$ , obtaining from $\phi _ { 0 } ( x )$ by stretching the coordinates by a factor of λ.

(a) Show that $E ( \lambda ) \equiv E [ \phi _ { \lambda } ]$ must satisfy

$$
\left. \frac { d { E } } { d { \lambda } } \right| _ { \lambda = 1 } = 0 .\tag{22}
$$

(b) Using the notations

$$
\Gamma = \int d ^ { d } x \frac { 1 } { 2 } K _ { a b } ( \phi _ { 0 } ) \sum _ { i = 1 } ^ { d } \partial _ { i } \phi _ { 0 } ^ { a } \partial _ { i } \phi _ { 0 } ^ { b } , ~ \Pi = \int d ^ { d } x V ( \phi _ { 0 } ) ,\tag{23}
$$

show that the above relation implies

$$
( 2 - d ) \Gamma - d \Pi = 0 .\tag{24}
$$

(c) Give a conclusion about the existence of $\phi _ { 0 }$ , if

$$
( \mathrm { a } ) d > 2 \qquad \quad ( \mathrm { b } ) d = 2 \qquad \quad ( \mathrm { c } ) d = 1
$$
:::
