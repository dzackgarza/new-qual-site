---
schema: qual/card@1
id: P-WL7TG
kind: problem
title: If $b$ and $x$ are units, a $2\times 2$ product over a commutative ring that
  vanishes off the bottom-right corner is zero
classification:
  areas:
  - algebra
  topics:
  - Matrices
  - Rings
  - Determinants
relations: []
review: draft
---

::: {.problem}
Let
\[
M=\left(\begin{array}{ll}{a} & {b} \\ {c} & {d}\end{array}\right)
\quad \text{and} \quad
N=\left(\begin{array}{cc}{x} & {u} \\ {-y} & {-v}\end{array}\right)
\]

over a commutative ring $R$, where $b$ and $x$ are units of $R$.
Prove that
\[
M N=\left(\begin{array}{ll}{0} & {0} \\ {0} & {*}\end{array}\right)
\implies MN = 0
.\]
:::

::: {.solution}
\envlist

- Multiply everything out to get
\[
\matt{ax-by}{au-bv}{cx-dy}{cu-dv}
,\]
  so it suffices to show $cu=dv$ given
  \[
  ax &= by \\
  cx &= dy \\
  au &= bv
  .\]

- Writing $cu$:

  - Use that $b\in \unitsof{R}$, left-multiply (1) by $\inverseof{b}$ to get $\inverseof{b} a x = y$

  - Substitute $y$ into (2) to get $cx = d(\inverseof{b} a x)$.

  - Since $x\in \unitsof{R}$, right-multiply by $\inverseof{x}$ to get $c = d\inverseof{b} a$ and thus $cu = d\inverseof{b} a u$.

  - Summary:
  \[
  ax = by 
  &\implies \inverseof{b} ax = y \\
  &\implies cx = dy = d(\inverseof{b} a x) \\
  &\implies c = d\inverseof{b} a \\
  &\implies cu = d\inverseof{b} au 
  .\]

- Writing $dv$:

  - Left-multiply (3) by $\inverseof{b}$ to get $\inverseof{b} au = v$.

  - Left-multiply by $d$ to get $d\inverseof{b} au = dv$

  - Summary:
  \[
  au = bv 
  &\implies \inverseof{b} a u = v \\
  &\implies d\inverseof{b} au = dv
  .\]

- So 
\[
cu = d\inverseof{b} a u = dv
.\]

:::
