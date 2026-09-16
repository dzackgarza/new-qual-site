---
schema: qual/card@1
id: P-SP3LC
kind: problem
title: Every linear map $\mathbb{R}^2\to\mathbb{R}^2$ is continuous
classification:
  areas:
  - prelim
  topics:
  - Linear Maps
  - Continuity
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
Prove that any linear function $L: \mathbb{R}^2 \to \mathbb{R}^2$ is continuous.
:::

::: {.solution}
<1>1. Let
\[
L(x,y)=(ax+by,cx+dy)
\]
for some $a,b,c,d\in\mathbb R$.
::: {.proof}
A linear map $\mathbb R^2\to\mathbb R^2$ is represented in the standard bases by a $2\times2$ real matrix.
:::

<1>2. There is a constant $C\ge0$ such that
\[
\|L(v)\|\le C\|v\|
\qquad(v\in\mathbb R^2).
\]
::: {.proof}
For $v=(x,y)$, Cauchy--Schwarz gives
\[
|ax+by|^2\le(a^2+b^2)(x^2+y^2),
\]
and
\[
|cx+dy|^2\le(c^2+d^2)(x^2+y^2).
\]
Hence
\[
\|L(v)\|^2
\le(a^2+b^2+c^2+d^2)\|v\|^2.
\]
Thus the claim holds with
\[
C=\sqrt{a^2+b^2+c^2+d^2}.
\]
:::

<1>3. The map $L$ is continuous at every $v_0\in\mathbb R^2$.
::: {.proof}
If $C=0$, then $L=0$ and continuity is immediate. Suppose $C>0$. Given $\varepsilon>0$, choose $\delta=\varepsilon/C$. If $\|v-v_0\|<\delta$, then by linearity and <1>2,
\[
\|L(v)-L(v_0)\|=\|L(v-v_0)\|\le C\|v-v_0\|<\varepsilon.
\]
:::

<1>4. Therefore every linear map $\mathbb R^2\to\mathbb R^2$ is continuous.
:::
