---
schema: qual/card@1
id: P-RASP07D
kind: problem
title: "Weak convergence in l^p implies boundedness and pointwise convergence"
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
  note: Checked against Problem 4 of the official UCSD Spring 2007 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Prove that if $1 < p < \infty$ and $f_n$ converges to $f$ weakly in $\ell^p(\mathbb{N})$, then $\sup_n \|f_n\|_p < \infty$ and $f_n \to f$ pointwise.

(The converse is also true, but you are not asked to prove it here.)
:::


::: solution
<1>1. Weak convergence implies uniform boundedness of the norms.
::: proof
Let $q=p/(p-1)$, so $(\ell^p)^*=\ell^q$. For each $n$, define
\[
T_n:\ell^q\to\mathbb C,
\qquad
T_n(g)=\sum_{k=1}^\infty f_n(k)g(k).
\]
Then $T_n$ is bounded and
\[
\|T_n\|=(\|f_n\|_p).
\]
For every fixed $g\in\ell^q$, weak convergence gives
\[
T_n(g)\longrightarrow \sum_{k=1}^\infty f(k)g(k),
\]
so the scalar sequence $(T_n(g))_n$ is bounded. Since $\ell^q$ is Banach, the Uniform Boundedness Principle yields
\[
\sup_n\|T_n\|<\infty.
\]
Hence
\[
\boxed{\sup_n\|f_n\|_p<\infty.}
\]
:::

<1>2. Weak convergence implies coordinatewise convergence.
::: proof
Fix $k\in\mathbb N$. Let $e_k\in\ell^q$ be the sequence with $1$ in the $k$th coordinate and $0$ elsewhere. The corresponding continuous linear functional on $\ell^p$ is
\[
x\longmapsto \langle x,e_k\rangle=x(k).
\]
By weak convergence,
\[
f_n(k)=\langle f_n,e_k\rangle
\longrightarrow
\langle f,e_k\rangle=f(k).
\]
Since $k$ was arbitrary,
\[
\boxed{f_n\to f\text{ pointwise on }\mathbb N.}
\]
:::
:::
