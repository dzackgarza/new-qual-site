---
schema: qual/card@1
id: P-TRIV-VP10
kind: problem
title: Natural boundary conditions from a boundary term in the functional
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Variational Principle, Problem 10, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: problem
Consider the following problem

$$
\left\{ \begin{array} { l l } { \displaystyle F _ { f } - \frac { \partial } { \partial x } F _ { f x } - \frac { \partial } { \partial y } F _ { f y } = 0 , ( x , y ) \in D } \\ { F _ { f _ { x } } n _ { x } + F _ { f _ { y } } n _ { y } + = g ( s ) , x \in \partial D , } \end{array} \right.\tag{16}
$$

where $f = f ( x , y ) \in C ^ { 2 } ( \bar { D } ) , F = F [ f , f _ { x } , f _ { y } ] ( x , y ) \in C ^ { 2 } ( \mathbb { R } ^ { 3 } \times \bar { D } ) , g \in C ^ { 1 } ( \partial D )$ $\partial / \partial n$ denotes a normal derivative on $\partial D$, $\begin{array} { r } { f _ { x } \equiv \frac { \partial f } { \partial x } } \end{array}$ and $\begin{array} { r } { F _ { f } \equiv \frac { \partial F } { \partial f } } \end{array}$

(a) Show that the solutions to this equation are given by extrema of the functional

$$
J [ f ] = \iint _ { D } d x d y F - \int _ { \partial D } d s f g .\tag{17}
$$

(b) How must the functional above be modified to give the mixed boundary conditions on the function $f \colon$

$$
F _ { f _ { x } } n _ { x } + F _ { f _ { y } } n _ { y } + h ( s ) f = g ( s ) , \quad h \in C ^ { 1 } ( \partial D )\tag{18}
$$
:::
