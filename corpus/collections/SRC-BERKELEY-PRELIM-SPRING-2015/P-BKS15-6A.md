---
schema: qual/card@1
id: P-BKS15-6A
kind: problem
title: Lagrange interpolation in Cauchy-matrix form
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UC Berkeley Spring 2015 Graduate Preliminary Examination.
---

::: {.problem}
Fix $N\ge1$.
Let $\mathbf s=(s_1,\ldots,s_N)$ and $\mathbf t=(t_1,\ldots,t_N)$ be $2N$ distinct complex numbers.
Define the $N\times N$ matrices $C(\mathbf t,\mathbf s)$, $P(\mathbf t,\mathbf s)$, and $Q(\mathbf s)$, with $P$ and $Q$ diagonal, by
\[
C(\mathbf t,\mathbf s)_{ij}=\frac1{t_i-s_j},\qquad
P(\mathbf t,\mathbf s)_{ii}=\prod_{k=1}^N(t_i-s_k),\qquad
Q(\mathbf s)_{jj}=\prod_{k\ne j}\frac1{s_j-s_k}.
\]
Show that
\[
p(\mathbf t)=P(\mathbf t,\mathbf s)C(\mathbf t,\mathbf s)Q(\mathbf s)p(\mathbf s),
\]
where $p$ is any polynomial of degree less than $N$ and, for a vector $\mathbf r=(r_1,\ldots,r_N)$, $p(\mathbf r)$ denotes $(p(r_1),\ldots,p(r_N))$.
:::
