---
schema: qual/card@1
id: P-RASP21A
kind: problem
title: "Sumset of measurable set with null set"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 1 of the official UCSD Spring 2021 real-analysis qualifying exam. The card had transposed the hypothesis and conclusion; the official statement assumes A+B is contained in the irrationals and asks to prove that one set is null.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Let $A, B \subseteq \mathbb{R}$ be Lebesgue measurable and suppose
$$
\{a+b:a\in A,\ b\in B\}\subseteq\mathbb R\setminus\mathbb Q.
$$
Prove that either $m(A)=0$ or $m(B)=0$.
:::


::: solution
Suppose, toward a contradiction, that
\[
m(A)>0
\qquad\text{and}\qquad
m(B)>0.
\]
Because Lebesgue measure on $\mathbb R$ is $\sigma$-finite, there exist bounded measurable subsets
\[
A_0\subseteq A,\qquad B_0\subseteq B
\]
with
\[
0<m(A_0)<\infty,\qquad 0<m(B_0)<\infty.
\]

For $t\in\mathbb R$, set
\[
h(t):=m\bigl(A_0\cap(t-B_0)\bigr).
\]
Equivalently,
\[
h=\mathbf1_{A_0}*\mathbf1_{B_0}
\]
up to the harmless reflection convention for convolution. Since $\mathbf1_{A_0},\mathbf1_{B_0}\in L^1(\mathbb R)$, the function $h$ is continuous. Moreover, by Tonelli,
\[
\int_{\mathbb R}h(t)\,dt=m(A_0)m(B_0)>0.
\]
Hence $h(t_0)>0$ for some $t_0$. By continuity, $h>0$ on a nonempty open interval $I$ containing $t_0$.

If $h(t)>0$, then $A_0\cap(t-B_0)\neq\varnothing$, so there are $a\in A_0$ and $b\in B_0$ with $t=a+b$. Thus
\[
I\subseteq A_0+B_0\subseteq A+B.
\]
Every nonempty open interval contains a rational number, contradicting
\[
A+B\subseteq\mathbb R\setminus\mathbb Q.
\]
Therefore at least one of $A$ or $B$ must have measure zero.
:::
