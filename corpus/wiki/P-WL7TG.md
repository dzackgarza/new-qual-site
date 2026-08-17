---
schema: qual/card@1
id: P-WL7TG
kind: problem
title: If $b$ and $x$ are units, a $2\times 2$ product over a commutative ring that vanishes off the bottom-right corner is zero
classification:
  areas:
  - algebra
  topics:
  - matrices
  - rings
  - determinants
relations: []
review: draft
solved: true
---
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

:::{.solution}
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
  - Use that $b\in R\units$, left-multiply (1) by $b\inv$ to get $b\inv a x = y$
  - Substitute $y$ into (2) to get $cx = d(b\inv a x)$.
  - Since $x\in R\units$, right-multiply by $x\inv$ to get $c = db\inv a$ and thus $cu = db\inv a u$.
  - Summary:
  \[
  ax = by 
  &\implies b\inv ax = y \\
  &\implies cx = dy = d(b\inv a x) \\
  &\implies c = db\inv a \\
  &\implies cu = db\inv au 
  .\]

- Writing $dv$:
  - Left-multiply (3) by $b\inv$ to get $b\inv au = v$.
  - Left-multiply by $d$ to get $db\inv au = dv$
  - Summary:
  \[
  au = bv 
  &\implies b\inv a u = v \\
  &\implies db\inv au = dv
  .\]

- So 
\[
cu = db\inv a u = dv
.\]

:::
