---
schema: qual/card@1
id: P-RASP21G
kind: problem
title: "Absolutely continuous measure via continuous density"
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
  note: Checked against Problem 7 of the official UCSD Spring 2021 real-analysis qualifying exam. The card omitted the source hypothesis that phi is positive; that hypothesis is restored.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Let $\mu$ be a $\sigma$-finite Radon measure on an LCH space $X$, and $\varphi$ a positive continuous function on $X$.
Show that $\nu(E) := \int_E \varphi\,d\mu$ defines a Radon measure $\nu$ on $X$.

Hint: First consider the positive linear functional $I(f) := \int f\varphi\,d\mu$ on $C_c(X)$ and show that $\nu$ coincides with the Radon measure associated with this functional on open sets.
:::


::: solution
Define
\[
I:C_c(X)\to\mathbb R,
\qquad
I(f):=\int_X f\varphi\,d\mu.
\]
Because $\varphi\ge0$, the functional $I$ is positive. It is also well defined: if $f\in C_c(X)$ and $K=\operatorname{supp}f$, then $\varphi$ is bounded on $K$ and $\mu(K)<\infty$, so
\[
\int_X|f|\varphi\,d\mu
\le \|f\|_\infty\sup_K\varphi\,\mu(K)<\infty.
\]

By the Riesz--Markov representation theorem, there is a unique Radon measure $\lambda$ on $X$ such that
\[
I(f)=\int_X f\,d\lambda
\qquad(f\in C_c(X)).
\]
We show that $\lambda$ is precisely
\[
\nu(E):=\int_E\varphi\,d\mu.
\]

Let $U\subseteq X$ be open. For a Radon measure,
\[
\lambda(U)
=\sup\left\{\int f\,d\lambda:
 f\in C_c(X),\ 0\le f\le1,\operatorname{supp}f\subseteq U\right\}.
\]
Using the representation of $I$,
\[
\lambda(U)
=\sup_f\int f\varphi\,d\mu
\le \int_U\varphi\,d\mu
=\nu(U).
\]

For the reverse inequality, fix a compact set $K\subseteq U$. By the standard cutoff lemma for LCH spaces, there exists $f\in C_c(X)$ with
\[
0\le f\le1,
\qquad
f=1\text{ on }K,
\qquad
\operatorname{supp}f\subseteq U.
\]
Hence
\[
\lambda(U)
\ge \int f\varphi\,d\mu
\ge \int_K\varphi\,d\mu.
\]
Since $\mu$ is Radon and $\varphi$ is positive continuous, the weighted integral is inner regular on open sets:
\[
\int_U\varphi\,d\mu
=\sup_{K\subseteq U\text{ compact}}\int_K\varphi\,d\mu.
\]
Therefore
\[
\lambda(U)\ge\nu(U).
\]
Thus $\lambda(U)=\nu(U)$ for every open $U$.

Both $\lambda$ and $\nu$ are Borel measures, and equality on open sets determines a Radon measure. Hence
\[
\lambda=\nu.
\]
Since $\lambda$ is Radon, so is $\nu$. Therefore
\[
\boxed{\nu(E)=\int_E\varphi\,d\mu\text{ defines a Radon measure on }X.}
\]
:::
