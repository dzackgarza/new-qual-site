---
schema: qual/card@1
id: P-ALGS08H
kind: problem
title: "The center of a simple ring with identity is a field"
classification:
  areas:
  - algebra
  topics:
  - Ring Theory
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Compared with Problem 8 of the official UCSD Spring 2008 algebra qualifying exam.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Verified that a nonzero central element generates a nonzero two-sided ideal, hence all of R; its inverse in R is central, so every nonzero element of the center is invertible in the center.
---

::: problem
Show that the center of a simple ring with identity element is a field.
:::

::: {.solution}
<1>1. The center $Z(R)$ is a commutative subring of $R$ containing $1$.
::: {.proof}
By definition,
\[
Z(R)=\{z\in R:zr=rz\text{ for every }r\in R\}.
\]
It is closed under addition, subtraction, and multiplication, every two of its elements commute, and $1\in Z(R)$.
:::

<1>2. Every nonzero $z\in Z(R)$ is invertible in $R$.
::: {.proof}
Because $z$ is central,
\[
RzR=zR=Rz
\]
is a two-sided ideal of $R$.
It is nonzero because $z=z\cdot1$ belongs to it.
Since $R$ is simple,
\[
zR=R.
\]
Hence $1\in zR$, so there exists $w\in R$ such that
\[
zw=1.
\]
Centrality of $z$ gives
\[
wz=zw=1,
\]
so $w=z^{-1}$ in $R$.
:::

<1>3. The inverse $z^{-1}$ is again central.
::: {.proof}
Let $w=z^{-1}$ and let $r\in R$.
Using $zw=wz=1$ and $zr=rz$,
\[
rw=(wz)rw=w(zr)w=w(rz)w=wr(zw)=wr.
\]
Thus $rw=wr$ for every $r\in R$, so $w\in Z(R)$.
:::

<1>4. Therefore $Z(R)$ is a field.
::: {.proof}
By <1>1, $Z(R)$ is a commutative ring with identity.
By <1>2 and <1>3, every nonzero element of $Z(R)$ has its multiplicative inverse in $Z(R)$.
Hence $Z(R)$ is a field.
:::
:::
