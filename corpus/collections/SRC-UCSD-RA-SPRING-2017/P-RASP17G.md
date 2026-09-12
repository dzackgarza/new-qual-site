---
schema: qual/card@1
id: P-RASP17G
kind: problem
title: "Vanishing moments against powers of a strictly increasing function"
classification:
  areas:
  - real-analysis
  topics:
  - Moment Problems
  - Monotone Functions
  - Density
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 7 of the official UCSD Spring 2017 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Let $g$ be a real valued function in $L^1([0, 1], m)$ and $h : [0, 1] \to \mathbb{R}$ be a strictly increasing function such that
$$
\int_0^1 g(x) [h(x)]^n \, dm(x) = 0 \quad \text{for } n \in \mathbb{N}.
$$

1. Under the further assumption that $h$ is continuous and $h(0) > 0$, show $g(x) = 0$ $m$-a.e.

2. Is it still true that $g(x) = 0$ $m$-a.e. when $h$ is continuous with $h(1/2) = 0$?
   Justify your answer.
:::


::: solution
<1>1. Prove the conclusion when \(h(0)>0\).
::: proof
Because \(h\) is continuous and strictly increasing on \([0,1]\), it is a homeomorphism onto the compact interval
\[
K=[h(0),h(1)].
\]
Under the hypothesis \(h(0)>0\), we have \(0\notin K\).

Let \(F\in C(K)\). Since \(1/t\) is continuous on \(K\), the Weierstrass theorem gives polynomials \(q_m\) such that
\[
tq_m(t)\longrightarrow F(t)
\]
uniformly on \(K\): simply approximate \(F(t)/t\) uniformly by \(q_m(t)\). Thus polynomials with zero constant term are uniformly dense in \(C(K)\).

Every \(\phi\in C([0,1])\) has the form
\[
\phi(x)=F(h(x))
\]
for some \(F\in C(K)\). By the moment hypothesis,
\[
\int_0^1 g(x)P(h(x))\,dx=0
\]
for every polynomial \(P\) with zero constant term. Passing to the uniform limit gives
\[
\int_0^1 g(x)\phi(x)\,dx=0
\]
for every \(\phi\in C([0,1])\). Since continuous functions separate \(L^1\) functions, this implies
\[
\boxed{g=0\text{ a.e.}}
\]
:::

<1>2. The conclusion remains true when \(h(1/2)=0\).
::: proof
Again let \(K=h([0,1])\). Now \(0\in K\). Define a finite signed Borel measure \(\nu\) on \(K\) by pushforward:
\[
\nu(E):=\int_{h^{-1}(E)} g(x)\,dx.
\]
Then the moment hypothesis says
\[
\int_K t^n\,d\nu(t)=0
\qquad(n\ge1).
\]
Polynomials with zero constant term are uniformly dense in
\[
\{F\in C(K):F(0)=0\}.
\]
Indeed, if \(F(0)=0\), then \(F(t)\) can be uniformly approximated by ordinary polynomials \(P_m\), and replacing \(P_m\) by \(P_m-P_m(0)\) gives zero-constant polynomials converging uniformly to \(F\).

Hence
\[
\int_K F\,d\nu=0
\]
for every continuous \(F\) vanishing at \(0\). Therefore \(\nu\) is supported on \(\{0\}\).

But strict monotonicity and \(h(1/2)=0\) give
\[
h^{-1}(\{0\})=\{1/2\}.
\]
Thus
\[
\nu(\{0\})
=\int_{\{1/2\}}g(x)\,dx=0.
\]
A finite signed measure supported at \(\{0\}\) with zero mass there is the zero measure. Hence \(\nu=0\). In particular,
\[
\int_0^1 g(x)\phi(x)\,dx=0
\]
for every \(\phi\in C([0,1])\), and therefore
\[
\boxed{g=0\text{ a.e.}}
\]
So the answer to part (2) is yes.
:::
:::
