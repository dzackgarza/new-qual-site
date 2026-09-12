---
schema: qual/card@1
id: P-RASP07F
kind: problem
title: "Distributions annihilated by x and x^2"
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
  note: Checked against Problem 6 of the official UCSD Spring 2007 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
In the following, give complete justification for your answers.

(a) Find all distributions $T \in \mathcal{D}'(\mathbb{R})$ such that $xT = 0$.

(b) Find all distributions $T \in \mathcal{D}'(\mathbb{R})$ such that $x^2 T = 0$.
:::


::: solution
<1>1. Solve $xT=0$.
::: proof
Choose $\chi\in C_c^\infty(\mathbb R)$ with $\chi=1$ on a neighborhood of $0$. For any test function $\varphi\in C_c^\infty(\mathbb R)$, the function
\[
\varphi(x)-\varphi(0)\chi(x)
\]
vanishes at $x=0$. Hence it can be written
\[
\varphi(x)-\varphi(0)\chi(x)=x\psi(x)
\]
for some $\psi\in C_c^\infty(\mathbb R)$.

If $xT=0$, then
\[
T(\varphi)
=\varphi(0)T(\chi)+T(x\psi)
=\varphi(0)T(\chi).
\]
Thus, with $c:=T(\chi)$,
\[
T(\varphi)=c\varphi(0)=c\,\delta_0(\varphi).
\]
Conversely,
\[
(x\delta_0)(\varphi)=\delta_0(x\varphi)=0.
\]
Therefore
\[
\boxed{xT=0\iff T=c\delta_0\text{ for some }c\in\mathbb C.}
\]
:::

<1>2. Solve $x^2T=0$.
::: proof
Using the same cutoff $\chi$, every test function has a second-order decomposition
\[
\varphi(x)
=\varphi(0)\chi(x)+\varphi'(0)x\chi(x)+x^2\psi(x)
\]
for some $\psi\in C_c^\infty(\mathbb R)$.
Indeed, after subtracting the first two terms, the remainder and its first derivative vanish at $0$, so it is divisible by $x^2$ in $C_c^\infty$.

If $x^2T=0$, then
\[
T(\varphi)
=\varphi(0)T(\chi)+\varphi'(0)T(x\chi).
\]
Set
\[
a:=T(\chi),
\qquad
c:=T(x\chi).
\]
Since
\[
\delta_0(\varphi)=\varphi(0),
\qquad
\delta_0'(\varphi)=-\varphi'(0),
\]
we obtain
\[
T=a\delta_0-c\delta_0'.
\]
Thus every solution lies in $\operatorname{span}\{\delta_0,\delta_0'\}$.

Conversely,
\[
x^2\delta_0=0,
\]
and using
\[
x\delta_0'=-\delta_0,
\]
we get
\[
x^2\delta_0'=x(-\delta_0)=0.
\]
Hence every linear combination of $\delta_0$ and $\delta_0'$ is annihilated by $x^2$. Therefore
\[
\boxed{x^2T=0\iff T=a\delta_0+b\delta_0'\text{ for some }a,b\in\mathbb C.}
\]
:::
:::
