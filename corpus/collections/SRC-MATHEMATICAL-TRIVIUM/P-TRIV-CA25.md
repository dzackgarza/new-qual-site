---
schema: qual/card@1
id: P-TRIV-CA25
kind: problem
title: 'Mathematical Trivium — Complex Analysis problem 25'
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis, Problem 25, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: problem
(a) Matsubara summation: in statistical mechanics, one often has to carry out summations over Matsubara frequencies.
These frequencies appear when the system is put at finite temperature, and the summation can be tedious to carry out.
We will consider the expectation value of the number of particles of a bosonic non-interacting gas.
Consider the function $h ( \omega _ { n } ) = - \frac { T } { i \omega _ { n } - \xi }$ Here $\omega _ { n }$ are called Matsubara frequencies.
In this case (the bosonic one) they are given by $\omega _ { n } = 2 \pi n T$

What we want to compute is $\begin{array} { r } { S \equiv \sum _ { n } h ( \omega _ { n } ) } \end{array}$ . To do so, we introduce an auxiliary function $\begin{array} { r } { g ( z ) = \frac { \beta } { e ^ { \beta z } - 1 } } \end{array}$ (setting $k _ { B } = 1 , \beta = T ^ { - 1 } )$ •

•Where are the poles of h? Where are those of $g \smash { ? }$

Consider now the function $g ( z ) h ( - i z )$ . Find a contour for which

$$
\frac { 1 } { 2 \pi i } \oint \mathrm { d } z g ( z ) h ( - i z ) = S .
$$

This contour encompasses an infinite number of poles.

•Since for large z the function decays fast enough the residue at infinity vanishes; inflate the contour and flip its orientation, so that it includes only a finite number of poles, in this case only one.

Carry out the integration.
You should find $- T \sum _ { n } { \frac { 1 } { i \omega _ { n } - \xi } } = { \frac { 1 } { e ^ { \beta \xi } - 1 } } ;$ as expected, this is the Bose distribution.

(b) Redo the previous exercise for fermions: the frequencies are $\omega _ { n } = ( 2 n { + } 1 ) \pi T$

It's convenient to pick $\begin{array} { r } { g ( z ) = \frac { \beta } { e ^ { \beta z } + 1 } } \end{array}$ . You should find

$$
T \sum _ { n } { \frac { 1 } { i \omega _ { n } - \xi } } = { \frac { 1 } { e ^ { \beta \xi } + 1 } }
$$
:::
