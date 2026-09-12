---
schema: qual/card@1
id: P-RASP17B
kind: problem
title: "Closures in L^1 of continuous compactly supported function classes"
classification:
  areas:
  - real-analysis
  topics:
  - L1 Spaces
  - Density
  - Closures
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 2 of the official UCSD Spring 2017 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
What is the closure of each of $\Gamma \subset L^1(\mathbb{R}, m)$ in the Banach space norm, $\|f\|_1 := \int_\mathbb{R} |f| \, dm$, in each of the three cases listed below? Briefly justify your answer.

1) $\Gamma = C_c(\mathbb{R}, \mathbb{R})$

2) $\Gamma = \{f \in C_c(\mathbb{R}, \mathbb{R}) : f(0) = 0\}$

3) $\Gamma = \left\{f \in C_c(\mathbb{R}, \mathbb{R}) : \int_{[-1,1]} f \, dm = 0\right\}$
:::

::: solution
<1>1. For \(\Gamma=C_c(\mathbb R)\), the closure is all of \(L^1(\mathbb R)\).
::: proof
The standard density theorem for Lebesgue spaces states that
\[
C_c(\mathbb R)\text{ is dense in }L^1(\mathbb R).
\]
Hence
\[
\boxed{\overline\Gamma^{\,L^1}=L^1(\mathbb R).}
\]
:::

<1>2. Imposing the point condition \(f(0)=0\) does not change the closure.
::: proof
Let \(u\in C_c(\mathbb R)\). Choose continuous cutoffs \(\chi_n:\mathbb R\to[0,1]\) such that
\[
\chi_n(0)=0,
\qquad
\chi_n(x)=1\quad\text{for }|x|\ge1/n.
\]
Then
\[
u_n:=\chi_nu\in C_c(\mathbb R),
\qquad
u_n(0)=0.
\]
Moreover,
\[
|u_n-u|\le |u|\mathbf1_{[-1/n,1/n]},
\]
so by absolute continuity of the Lebesgue integral,
\[
\|u_n-u\|_1\to0.
\]
Thus every compactly supported continuous function lies in the \(L^1\)-closure of the subclass vanishing at \(0\). By Step 1,
\[
\boxed{
\overline{\{u\in C_c:u(0)=0\}}^{\,L^1}=L^1(\mathbb R).}
\]
:::

<1>3. Identify the closure of the zero-integral class.
::: proof
Define
\[
L:L^1(\mathbb R)\to\mathbb R,
\qquad
L(f)=\int_{[-1,1]}f\,dm.
\]
Then
\[
|L(f)|\le\|f\|_1,
\]
so \(L\) is continuous. Therefore
\[
\ker L
=\left\{f\in L^1:\int_{[-1,1]}f=0\right\}
\]
is closed, and the third class is contained in \(\ker L\). Hence its closure is contained in \(\ker L\).

Conversely, take \(f\in\ker L\). Choose \(u_n\in C_c(\mathbb R)\) with \(u_n\to f\) in \(L^1\). Then
\[
L(u_n)\to L(f)=0.
\]
Fix \(\psi\in C_c(\mathbb R)\) with support in \((-1,1)\) and
\[
\int_{[-1,1]}\psi\,dm=1.
\]
Set
\[
v_n:=u_n-L(u_n)\psi.
\]
Then \(v_n\in C_c(\mathbb R)\) and
\[
\int_{[-1,1]}v_n\,dm=0.
\]
Also
\[
\|v_n-f\|_1
\le \|u_n-f\|_1+|L(u_n)|\,\|\psi\|_1
\to0.
\]
Thus
\[
\boxed{
\overline\Gamma^{\,L^1}
=\left\{f\in L^1(\mathbb R):\int_{[-1,1]}f\,dm=0\right\}.}
\]
:::
:::
