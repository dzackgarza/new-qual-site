---
schema: qual/card@1
id: P-EXTME
kind: problem
title: Hungerford 7.2.4
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
  - Matrices
  - Rank and Nullity
relations: []
review: draft
solved: false
---

:::{.problem title="Hungerford 7.2.4"}
\envlist


1.  Show that a system of linear equations 
  \[
  a_{11} x_{1}+a_{12} x_{2} + &\cdots + a_{1 m} x_{m}=b_{1} \\ 
  & \vdots \\ 
  a_{n 1} x_{1}+a_{n 2} x_{2}+&\cdots+a_{n m} x_{m}=b_{n}
  \]
  has a simultaneous solution $\iff$ the corresponding matrix equation
  $AX = B$ has a solution, where
  $A = (a_{ij}), X = [x_1, \cdots, x_m]^t$, and
  $B = [b_1, \cdots , b_n]^t$.

2.  If $A_1, B_1$ are matrices obtained from $A, B$ respectively by
  performing the same sequence of elementary **row** operations, then
  $X$ is a solution of $AX=B$ $\iff$ $X$ is a solution of
  $A_1 X = B_1$.

3.  Let $C$ be the $n \times (m+1)$ matrix given by
\[
C = \left(\begin{array}{llll}{a_{11}} & {\cdots} & {a_{1 m}} & {b_{1}} \\ {} & {} & {} \\ {\cdot} & {} & {} \\ {a_{n 1}} & {\cdots} & {a_{n m}} & {b_{n}}\end{array}\right)
.\]
  Then $AX = B$ has a solution $\iff$
  $\mathrm{rank} A = \mathrm{rank} C$ and the solution is unique
  $\iff \mathrm{rank}(A) = m$.

  *Hint: use part 2.*

4.  If $B=0$, so the system $AX=B$ is homogeneous, then it has a
    nontrivial solution $\iff \mathrm{rank} A < m$ and in particular
    $n<m$.
:::

