---
schema: qual/card@1
id: E-HAT-4.2-10
kind: problem
title: "Finiteness of $\\pi_n'$ vs. $\\pi_n$"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.2, Exercise 10; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Let the CW complex $X$ be obtained from $S^1 \vee S^n$, $n \geq 2$, by attaching a cell $e^{n+1}$ by a map representing the polynomial $p(t) \in \mathbb{Z}[t, t^{-1}] \approx \pi_n(S^1 \vee S^n)$, so $\pi_n(X) \approx \mathbb{Z}[t, t^{-1}] / \bigl(p(t)\bigr)$.
Show $\pi_n'(X)$ is cyclic and compute its order in terms of $p(t)$.
Give examples showing that the group $\pi_n(X)$ can be finitely generated or not, independently of whether $\pi_n'(X)$ is finite or infinite.
:::

::: {.solution}
Let
\[
R=\mathbb Z[t,t^{-1}],\qquad M=\pi_n(X)\cong R/(p(t)).
\]
The quotient \(\pi_n'(X)\) is obtained by imposing the relations
\[
t\alpha=\alpha
\]
for all \(\alpha\in M\). Hence
\[
\pi_n'(X)=M/(t-1)M
\cong R/(p(t),t-1).
\]
Evaluation at \(t=1\) gives
\[
R/(t-1)\cong\mathbb Z,
\]
so
\[
\boxed{\pi_n'(X)\cong\mathbb Z/(p(1)).}
\]
Thus it is cyclic of order \(|p(1)|\) when \(p(1)\ne0\), and infinite cyclic when \(p(1)=0\).

The four finiteness possibilities all occur.

- \(p(t)=t+1\): then \(M\cong\mathbb Z\), while \(\pi_n'(X)\cong\mathbb Z/2\).
- \(p(t)=t-1\): then \(M\cong\mathbb Z\), while \(\pi_n'(X)\cong\mathbb Z\).
- \(p(t)=2t-1\): then \(M\cong\mathbb Z[1/2]\), not finitely generated as an abelian group, while \(p(1)=1\) so \(\pi_n'(X)=0\).
- \(p(t)=0\): then \(M=\mathbb Z[t,t^{-1}]\), not finitely generated as an abelian group, while \(\pi_n'(X)\cong\mathbb Z\).

Hence finite generation of \(\pi_n(X)\) and finiteness of \(\pi_n'(X)\) are independent.
:::
