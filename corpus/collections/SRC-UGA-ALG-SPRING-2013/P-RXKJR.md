---
schema: qual/card@1
id: P-RXKJR
kind: problem
title: Jordan forms of a $5$-dimensional operator annihilated by $(x+1)^2$
classification:
  areas:
  - algebra
  topics:
  - Jordan Canonical Form
  - Minimal and Characteristic Polynomials
  - Eigenvalues and Eigenvectors
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: problem
Let $T: V\to V$ be a linear map from a 5-dimensional $\CC\dash$vector space to itself and suppose $f(T) = 0$ where $f(x) = x^2 + 2x + 1$.

a. Show that there does not exist any nonzero vector $v\in V$ such that $Tv = v$, but there *does* exist a nonzero vector $w\in V$ such that $T^2 w= w$.

b. Give all of the possible Jordan canonical forms of $T$.
:::

::: solution
Since
\[
f(T)=(T+I)^2=0,
\]
write $N=T+I$. Then $N^2=0$ and $T=-I+N$.

For (a), suppose $v\ne0$ and $Tv=v$. Then
\[
Nv=(T+I)v=2v.
\]
Applying $N$ again gives
\[
0=N^2v=2Nv=4v,
\]
which is impossible over $\mathbb C$. Hence no nonzero vector satisfies $Tv=v$.

Because $N^2=0$, we have $\operatorname{im}N\subseteq\ker N$. In particular $\ker N\ne0$: if $N=0$ this is clear, while if $N\ne0$, its nonzero image lies in the kernel. Choose $0\ne w\in\ker N$. Then $Tw=-w$, so
\[
T^2w=w.
\]

For (b), the relation $(T+I)^2=0$ says that the only eigenvalue is $-1$ and every Jordan block has size at most $2$. Since $\dim V=5$, the possible partitions of $5$ into parts of size at most $2$ are
\[
1+1+1+1+1,
\qquad
2+1+1+1,
\qquad
2+2+1.
\]
Hence the possible Jordan forms are
\[
[-1]^{\oplus5},
\qquad
J_2(-1)\oplus[-1]^{\oplus3},
\qquad
J_2(-1)\oplus J_2(-1)\oplus[-1].
\]
All three occur and are annihilated by $(x+1)^2$.
:::
