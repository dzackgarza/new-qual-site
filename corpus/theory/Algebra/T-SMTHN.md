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
Two $m\times n$ matrices over $R$ are [[D-JRPTK|equivalent]] if and only if they have the same Smith normal form, since each is equivalent to its own normal form and that form is unique up to units.
:::

::: {.remark}
The matrices $P$ and $Q$ are the products of the elementary row and column operations that clear the entries of $A$ below and to the right of each pivot in turn, so the form is computed by the same algorithm that computes a basis adapted to a submodule; the entries $a_i$ are the invariant factors of the [[PR-UVUS6|module]] $R^n/\im(A)$. The theorem is the matrix form of the structure theorem for finitely generated modules over a PID [@DF04, Theorem 5]: apply that theorem to $R^n/\im(A)$ and lift the direct sum decomposition to bases of $R^n$ and $R^m$, which is what $P$ and $Q$ record.
:::

::: {.remark}
Dummit and Foote carry the case of the matrix $xI-A$ over $F[x]$: for $A$ an $n\times n$ matrix over a field $F$, the matrix $xI-A$ can be put in Smith normal form, with monic diagonal entries $a_1(x)\divides\cdots\divides a_m(x)$ of degree at least one that are the invariant factors of $A$ [@DF04, §12.2, Theorem 21], and the formula $a_i=d_i/d_{i-1}$ in terms of the greatest common divisors of the $i\times i$ minors of $xI-A$ is §12.3 Exercise 35 [@DF04].
Hungerford states the first half too: $xI_n-A$ is equivalent over $K[x]$ to a diagonal matrix with monic diagonal entries $f_1\divides\cdots\divides f_n$, and the entries $f_i$ that are not constants are the invariant factors of $A$ [@Hun74, chapter VII, §4, Proposition 4.9].
:::
