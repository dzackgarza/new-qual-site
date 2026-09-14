---
schema: qual/card@1
id: P-TRIV-DE21
kind: problem
title: 'Mathematical Trivium — Differential Equations problem 21'
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Differential Equations, Problem 21, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: problem
Consider Schrodinger equation for a quantum harmonic oscillator with small quartic perturbation

$$
\left( - \frac { 1 } { 2 } \frac { d ^ { 2 } } { d x ^ { 2 } } + \frac { x ^ { 2 } } { 2 } + \frac { g x ^ { 4 } } { 4 } \right) \psi ( x ) = E _ { 0 } ( g ) \psi ( x )\tag{30}
$$

and make the ansatz

$$
\psi ( x ) = e ^ { - x ^ { 2 } / 2 } \sum _ { n = 0 } ^ { \infty } \left( { \frac { g } { 4 } } \right) ^ { n } B _ { n } ( x ) \qquad { \mathrm { w i t h } } \quad B _ { 0 } ( x ) = 1\tag{31}
$$

$$
E _ { 0 } ( g ) = \sum _ { k = 0 } ^ { \infty } a _ { k } \left( \frac { g } { 4 } \right) ^ { k } .\tag{32}
$$

We already know that $\begin{array} { r } { a _ { 0 } = \frac { 1 } { 2 } } \end{array}$ from the unperturbed oscillator.
We want to find the first two corrections $a _ { 1 }$ 2 and $a _ { 2 }$

(a) Find a recurrence relation for $B _ { k } ( x )$ and $a _ { k }$

(b) Solve the relation by assuming $B _ { i } ( x ) = \sum _ { j = 1 } ^ { 2 i } x ^ { 2 j } ( - 1 ) ^ { i } B _ { i , j }$

(c) Considering different powers of $x ,$ find the following relations

$$
a _ { n } = ( - 1 ) ^ { n + 1 } B _ { n , 1 }\tag{33}
$$

$$
2 j B _ { n , j } = ( j + 1 ) ( 2 j + 1 ) B _ { n , j + 1 } + B _ { n - 1 , j - 2 } - \sum _ { k = 1 } ^ { n - 1 } B _ { n - k , 1 } B _ { k , j }\tag{34}
$$

(d) Find $a _ { 1 }$ and $a _ { 2 }$ . You can check that your result agrees with the usual per-1 2turbation theory.
:::
