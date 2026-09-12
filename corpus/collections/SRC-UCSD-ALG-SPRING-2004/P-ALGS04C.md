---
schema: qual/card@1
id: P-ALGS04C
kind: problem
title: "Construction of a nonabelian group of order 75"
classification:
  areas:
  - algebra
  topics:
  - Group Theory
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-09
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
Construct a nonabelian group of order $75 = 5^2 \cdot 3$.
:::

::: {.solution}
<1>1. Let \(V=\mathbf F_5^2\), written additively, and define
\[
A=\begin{pmatrix}0&-1\\1&-1\end{pmatrix}\in \operatorname{GL}_2(\mathbf F_5).
\]
Then \(A\) has order \(3\).
::: {.proof}
A direct computation gives
\[
A^2=\begin{pmatrix}-1&1\\-1&0\end{pmatrix}
\]
and therefore
\[
A^3=I.
\]
Also \(A\ne I\), so its order is exactly \(3\).
:::

<1>2. Let \(C_3=\langle t\rangle\) act on \(V\) by
\[
t\cdot v=Av.
\]
Form the semidirect product
\[
G:=V\rtimes_A C_3.
\]
Then \(|G|=75\).
::: {.proof}
The additive group \(V\) has order \(5^2=25\), and \(|C_3|=3\). Hence
\[
|G|=|V|\,|C_3|=25\cdot3=75.
\]
:::

<1>3. The group \(G\) is nonabelian.
::: {.proof}
Because \(A\ne I\), choose \(v\in V\) with \(Av\ne v\); for example \(v=(1,0)\), for which
\[
Av=(0,1)\ne(1,0).
\]
In the semidirect product,
\[
tvt^{-1}=Av\ne v.
\]
Thus \(t\) and \(v\) do not commute, so \(G\) is nonabelian.
:::

<1>4. Therefore \((C_5\times C_5)\rtimes C_3\), with the above action, is a nonabelian group of order \(75\).
::: {.proof}
This follows from <1>2 and <1>3.
:::
:::
