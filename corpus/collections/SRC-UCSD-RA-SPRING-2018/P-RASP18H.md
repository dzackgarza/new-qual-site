---
schema: qual/card@1
id: P-RASP18H
kind: problem
title: "Banach limit extension and non-representability by l^1"
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
  note: Checked against Problem 8 of the official UCSD Spring 2018 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Let $\ell^\infty(\mathbb{N})$ be the Banach space of bounded complex sequences $x = (x_1, x_2, x_3, \ldots)$ such that $\|x\|_\infty = \sup_n |x_n| < \infty$ and let $V$ be the subspace defined as:
$$
V = \left\{x \in \ell^\infty(\mathbb{N}) : \lim_{n \to \infty} \frac{1}{n}(x_1 + x_2 + \cdots + x_n) \text{ exists in } \mathbb{C}\right\}.
$$

1. Prove that there exists $\varphi \in \ell^\infty(\mathbb{N})^*$ such that $\varphi(x) = \lim_{n \to \infty} \frac{1}{n}(x_1 + x_2 + \cdots + x_n)$ for every $x \in V$.

Let $\psi \in \ell^\infty(\mathbb{N})^*$ be any continuous linear functional such that $\psi(x) = \lim_{n \to \infty} \frac{1}{n}(x_1 + x_2 + \cdots + x_n)$ when $x \in V$.

2. Show $\psi(\tilde{x}) = \psi(x)$ for every $x = (x_1, x_2, x_3, x_4, \ldots) \in \ell^\infty(\mathbb{N})$ where $\tilde{x} := (x_2, x_3, x_4, \ldots)$.

3. Show there is no $y \in \ell^1(\mathbb{N})$ such that $\psi(x) = \sum_{n=1}^{\infty} x_n y_n$ for all $x \in \ell^\infty(\mathbb{N})$.
:::


::: solution
<1>1. Extend the Cesaro-limit functional by Hahn--Banach.
::: proof
Define
\[
L:V\to\mathbb C,
\qquad
L(x)=\lim_{n\to\infty}\frac1n\sum_{j=1}^n x_j.
\]
This is linear. Moreover,
\[
|L(x)|
\le \limsup_{n\to\infty}\frac1n\sum_{j=1}^n|x_j|
\le \|x\|_\infty.
\]
Thus \(L\) is bounded and \(\|L\|\le1\). Since the constant sequence \(\mathbf1=(1,1,\ldots)\) lies in \(V\) and \(L(\mathbf1)=1=\|\mathbf1\|_\infty\), in fact \(\|L\|=1\).

By the Hahn--Banach theorem, \(L\) extends to a bounded linear functional
\[
\varphi\in(\ell^\infty)^*
\]
with the same norm. Hence
\[
\boxed{
\varphi(x)=\lim_{n\to\infty}\frac1n\sum_{j=1}^n x_j
\quad\text{for every }x\in V.}
\]
:::

<1>2. Prove shift invariance of every such extension.
::: proof
Let
\[
x=(x_1,x_2,\ldots),
\qquad
\widetilde x=(x_2,x_3,\ldots).
\]
Set \(z=\widetilde x-x\). Then
\[
\frac1n\sum_{j=1}^n z_j
=\frac1n\sum_{j=1}^n(x_{j+1}-x_j)
=\frac{x_{n+1}-x_1}{n}.
\]
Because \(x\in\ell^\infty\), the last quantity tends to \(0\). Hence \(z\in V\) and every extension \(\psi\) agreeing with \(L\) on \(V\) satisfies
\[
\psi(z)=0.
\]
Therefore
\[
\boxed{\psi(\widetilde x)=\psi(x)}
\]
for every \(x\in\ell^\infty\).
:::

<1>3. Rule out representation by an \(\ell^1\) sequence.
::: proof
Suppose there were \(y=(y_n)\in\ell^1\) such that
\[
\psi(x)=\sum_{n=1}^\infty x_ny_n
\]
for every \(x\in\ell^\infty\). Shift invariance gives
\[
\sum_{n=1}^\infty x_{n+1}y_n
=\sum_{n=1}^\infty x_ny_n
\]
for every bounded sequence \(x\).

Taking \(x=e_1=(1,0,0,\ldots)\) gives
\[
y_1=0.
\]
Taking \(x=e_m\) for \(m\ge2\) gives
\[
y_{m-1}=y_m.
\]
Thus inductively
\[
y_n=0
\qquad\text{for every }n.
\]
Hence the alleged representation would make \(\psi=0\). But the constant sequence \(\mathbf1\) belongs to \(V\), so
\[
\psi(\mathbf1)=1.
\]
This contradiction proves that no such \(y\in\ell^1\) exists.
:::
:::
