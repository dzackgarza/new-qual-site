---
schema: qual/card@1
id: P-L7G3D
kind: problem
title: If $\mu(X\setminus E_n)\to 0$ then almost every point lies in infinitely many
  $E_n$
classification:
  areas:
  - real-analysis
  topics:
  - Borel-Cantelli
  - Measure Theory
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 4 of the official UGA August 2016 real-analysis qualifying exam; repaired the legacy proof, whose final summability step was invalid.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

Let $(X, \mathcal M, \mu)$ be a measure space and suppose $\theset{E_n} \subset \mathcal M$ satisfies
\[
\lim _{n \rightarrow \infty} \mu\left(X \backslash E_{n}\right)=0.
\]

Define
\[
G \definedas \theset{x\in X \suchthat x\in E_n \text{ for only finitely many  } n}.
\]

Show that $G \in \mathcal M$ and $\mu(G) = 0$.

::: solution

Set
\[
F_N:=\bigcap_{n=N}^\infty E_n^c.
\]
A point belongs to only finitely many $E_n$ exactly when it belongs to $E_n^c$ for all sufficiently large $n$, so
\[
G=\bigcup_{N=1}^\infty F_N.
\]
Thus $G\in\mathcal M$.

Fix $N$. For every $m\ge N$,
\[
F_N\subseteq E_m^c,
\]
and hence
\[
0\le \mu(F_N)\le \mu(E_m^c)=\mu(X\setminus E_m).
\]
Letting $m\to\infty$ gives $\mu(F_N)=0$. Therefore
\[
\mu(G)\le \sum_{N=1}^\infty\mu(F_N)=0.
\]
Hence
\[
\boxed{G\in\mathcal M\quad\text{and}\quad \mu(G)=0.}
\]
No summability hypothesis on the numbers $\mu(X\setminus E_n)$ is needed.
:::
