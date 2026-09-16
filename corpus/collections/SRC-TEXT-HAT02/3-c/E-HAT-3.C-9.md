---
schema: qual/card@1
id: E-HAT-3.C-9
kind: problem
title: "Euler characteristic of finite H-spaces"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.C, Exercise 9; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Apply the theorems of Hopf and Borel to show that for an H-space $X$ that is a connected finite CW complex with $\tilde{H}_*(X; \mathbb{Z}) \neq 0$, the Euler characteristic $\chi(X)$ is $0$.
:::

::: {.solution}
Let
\[
P_F(t)=\sum_i \dim_F H^i(X;F)t^i.
\]
Since $X$ is a finite CW complex, $P_F$ is a polynomial and
\[
\chi(X)=P_F(-1)
\]
for every field $F$.

First take $F=\mathbb Q$. Hopf's theorem says that the connected graded Hopf algebra $H^*(X;\mathbb Q)$ is, as an algebra, a tensor product of an exterior algebra on odd-dimensional generators and a polynomial algebra on even-dimensional generators. Because $X$ is finite, $H^*(X;\mathbb Q)$ is finite-dimensional, so no polynomial generator can occur. Hence
\[
H^*(X;\mathbb Q)\cong\Lambda_{\mathbb Q}(x_1,\dots,x_r)
\]
with all $|x_i|$ odd. If $r>0$, then
\[
P_{\mathbb Q}(-1)=\prod_{i=1}^r(1+(-1)^{|x_i|})=0,
\]
so $\chi(X)=0$.

It remains to rule out $r=0$ under the hypothesis $\widetilde H_*(X;\mathbb Z)\ne0$. If $r=0$, then $H^*(X;\mathbb Q)=\mathbb Q$, so $\chi(X)=1$ and all positive-dimensional integral homology is torsion. Choose a prime $p$ for which $\widetilde H^*(X;\mathbb F_p)\ne0$; such a prime exists by the universal coefficient theorem.

Borel's theorem expresses the finite-dimensional Hopf algebra $H^*(X;\mathbb F_p)$ as a tensor product of single-generator factors, each either an exterior algebra on an odd-dimensional generator or a truncated polynomial algebra
\[
\mathbb F_p[y]/(y^{p^k})
\]
with $|y|$ even when $p$ is odd. If an exterior factor occurs, its Poincare polynomial vanishes at $-1$, giving $\chi(X)=0$, contradicting $\chi(X)=1$. If there are no exterior factors, every nontrivial truncated factor contributes
\[
1+1+\cdots+1=p^k
\]
to $P_{\mathbb F_p}(-1)$, so $\chi(X)$ is divisible by $p$, again contradicting $\chi(X)=1$. Therefore $r=0$ is impossible.

Hence necessarily
\[
\boxed{\chi(X)=0.}
\]
:::
