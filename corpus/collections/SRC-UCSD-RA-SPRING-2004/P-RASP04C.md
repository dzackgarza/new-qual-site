---
schema: qual/card@1
id: P-RASP04C
kind: problem
title: "Orthonormal set is a basis if Parseval holds on a dense set"
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
  date: 2026-09-08
  note: Checked against Problem 3 of the official UCSD Spring 2004 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Suppose that $\{u_n\}_{n=1}^{\infty}$ is an orthonormal subset of a Hilbert space $H$, and $S$ is a dense subset of $H$.
Show $\{u_n\}_{n=1}^{\infty}$ is an orthonormal basis for $H$ if
$$
\|f\|_H^2 = \sum_{n=1}^{\infty} |\langle f | u_n \rangle|^2 \quad \text{for all } f \in S.
$$
:::

::: solution
<1>1. Let $M$ be the closed span of the orthonormal system.
::: proof
Set
\[
M:=\overline{\operatorname{span}}\{u_n:n\ge1\}.
\]
For each $f\in H$, the orthogonal projection $P_Mf$ has Fourier expansion
\[
P_Mf=\sum_{n=1}^\infty \langle f,u_n\rangle u_n
\]
with convergence in $H$. Hence Parseval's identity inside the Hilbert space $M$ gives
\[
\|P_Mf\|_H^2
=\sum_{n=1}^\infty |\langle f,u_n\rangle|^2.
\]
:::

<1>2. Use the assumed identity on the dense set.
::: proof
For every $f\in S$, the hypothesis and Step 1 give
\[
\|f\|_H^2=\|P_Mf\|_H^2.
\]
Since
\[
f=P_Mf+(f-P_Mf)
\]
is an orthogonal decomposition,
\[
\|f\|_H^2=\|P_Mf\|_H^2+\|f-P_Mf\|_H^2.
\]
Therefore $f=P_Mf$, so every $f\in S$ belongs to $M$.

The set $S$ is dense in $H$ and $M$ is closed. Hence
\[
H=\overline S\subseteq M\subseteq H,
\]
so $M=H$. Thus the closed linear span of $(u_n)$ is all of $H$, i.e.
\[
\boxed{\{u_n\}_{n=1}^\infty\text{ is an orthonormal basis of }H.}
\]
:::
:::
