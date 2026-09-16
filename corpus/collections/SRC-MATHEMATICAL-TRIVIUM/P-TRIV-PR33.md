---
schema: qual/card@1
id: P-TRIV-PR33
kind: problem
title: Borel's normal number theorem
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Probability, Problem 33, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: problem
Normal numbers

Let $x \in [ 0 , 1 )$ . Consider the infinite decimal notation for x:

$$
x = 0 . a _ { 1 } a _ { 2 } . . . , \ a _ { i } = 0 , 1 , . . . , 9 , \ i \in \mathbb { N } ,\tag{55}
$$

where for the numbers with finite amount of decimal places we complete the records with infinite series of 0s. Now select randomly one x. What can one say about the typical distribution of digits $0 , . . . , 9$ in $x ?$ To answer the question, consider the following sequence of approximations:

$$
\begin{array} { l } { { x _ { 0 } = 0 } } \\ { { x _ { 1 } = 0 . a _ { 1 } } } \\ { { . . . } } \\ { { x _ { n } = 0 . a _ { 1 } . . . a _ { n } } } \\ { { . . . } } \end{array}\tag{56}
$$

(a) Show that

$$
P \left( \operatorname* { l i m } _ { n \to \infty } \frac { 1 } { n } I _ { n } ( i ) = \frac { 1 } { 1 0 } \right) = 1 , \forall i ,\tag{57}
$$

where $I _ { n } ( i )$ gives the number of i digit in $x _ { n }$ . The result implies that almost all numbers contain equal (and infinite) amount of all 10 digits.
Such numbers are called normal.

(b) Check if the rational numbers are normal.

(c) Check if the following number is normal:

$$
x = 0 , 1 2 3 4 5 6 7 8 9 1 0 1 1 1 2 1 3 . . .\tag{58}
$$
:::
