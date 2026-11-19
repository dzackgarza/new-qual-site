---
schema: qual/card@1
id: T-SMTHN
kind: theorem
title: Smith normal form of a matrix over a PID
slogan: 'Every matrix over a PID is equivalent to a diagonal one whose entries divide the next, and the diagonal is unique up to units.'
classification:
  areas:
  - algebra
  topics:
  - Smith Normal Form
  - Modules over PIDs
relations: []
review: draft
---

::: {.theorem}
Let $R$ be a [[D-HTIL5|principal ideal domain]] and $A\in \Mat(m\times n; R)$.
There are invertible matrices $P$ and $Q$ over $R$ such that $PAQ$ is diagonal, with diagonal entries $a_1\divides a_2\divides\cdots\divides a_r$ followed by zeros, and the $a_i$ are unique up to multiplication by units of $R$.
The entries are $a_i = d_i/d_{i-1}$, where $d_0=1$ and $d_i$ is a greatest common divisor of the $i\times i$ minors of $A$.
Two $m\times n$ matrices over $R$ are [[D-JRPTK|equivalent]] if and only if they have the same Smith normal form [@DF04, p. 479].
:::

::: {.remark}
The matrices $P$ and $Q$ are the products of the elementary row and column operations that clear the entries of $A$ below and to the right of each pivot in turn, so the form is computed by the same algorithm that computes a basis adapted to a submodule; the entries $a_i$ are the invariant factors of the [[PR-UVUS6|module]] $R^n/\im(A)$.
:::
