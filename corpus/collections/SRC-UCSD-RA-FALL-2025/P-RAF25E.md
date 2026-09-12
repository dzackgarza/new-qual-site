---
schema: qual/card@1
id: P-RAF25E
kind: problem
title: "Translations of an L^2 function with nonvanishing Fourier transform span a dense subspace"
classification:
  areas:
  - real-analysis
  topics:
  - Fourier Transform
  - L2 Spaces
  - Density
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 5 of the official UCSD Fall 2025 real-analysis qualifying exam; corrected the ambient-space typo for f_a from L^2(R) to L^2(R^n).
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Let $f \in L^2(\mathbb{R}^n)$ such that $\hat{f}(\xi) \neq 0$ for a.e. $\xi \in \mathbb{R}^n$.
For $a \in \mathbb{R}^n$, let $f_a \in L^2(\mathbb{R}^n)$ be given by $f_a(x) = f(x - a)$.

(1) Prove that if $a \in \mathbb{R}^n$, then $\hat{f_a}(\xi) = e^{-2\pi i \xi \cdot a} \hat{f}(\xi)$ for a.e. $\xi \in \mathbb{R}^n$.
(You can use without proof the fact that this identity holds if $f \in L^1(\mathbb{R})$.)

(2) Prove that the linear span of $\{f_a : a \in \mathbb{R}^n\}$ is dense in $L^2(\mathbb{R}^n)$.
:::

::: solution
<1>1. Extend the translation identity from $L^1\cap L^2$ to all of $L^2$.
::: proof
Fix $a\in\mathbb R^n$. Choose $f_j\in L^1(\mathbb R^n)\cap L^2(\mathbb R^n)$ such that
\[
f_j\to f
\qquad\text{in }L^2.
\]
Translations are isometries of $L^2$, so
\[
(f_j)_a\to f_a
\qquad\text{in }L^2.
\]
By Plancherel,
\[
\widehat{(f_j)_a}\to\widehat{f_a}
\qquad\text{in }L^2.
\]

For $f_j\in L^1\cap L^2$, the usual translation formula gives
\[
\widehat{(f_j)_a}(\xi)
=e^{-2\pi i\xi\cdot a}\widehat{f_j}(\xi).
\]
Again by Plancherel,
\[
\widehat{f_j}\to\widehat f
\qquad\text{in }L^2,
\]
and multiplication by the unimodular factor $e^{-2\pi i\xi\cdot a}$ is an $L^2$ isometry. Passing to the $L^2$ limit yields
\[
\boxed{
\widehat{f_a}(\xi)
=e^{-2\pi i\xi\cdot a}\widehat f(\xi)
\quad\text{a.e.}}
\]
:::

<1>2. Compute the orthogonal complement of the translation span.
::: proof
Let
\[
V:=\overline{\operatorname{span}}\{f_a:a\in\mathbb R^n\}
\]
and suppose $g\in V^\perp$. Then for every $a\in\mathbb R^n$,
\[
0=\langle g,f_a\rangle.
\]
By Plancherel and Step 1,
\[
\begin{aligned}
0
&=\int_{\mathbb R^n}\widehat g(\xi)
\overline{\widehat{f_a}(\xi)}\,d\xi\\
&=\int_{\mathbb R^n}
\widehat g(\xi)\overline{\widehat f(\xi)}
e^{2\pi i\xi\cdot a}\,d\xi.
\end{aligned}
\]

Set
\[
h(\xi):=\widehat g(\xi)\overline{\widehat f(\xi)}.
\]
By Cauchy--Schwarz,
\[
h\in L^1(\mathbb R^n).
\]
The preceding identity says that the inverse Fourier transform of $h$ vanishes at every $a\in\mathbb R^n$. By uniqueness of the Fourier transform on $L^1$,
\[
h=0
\qquad\text{a.e.}
\]
Since $\widehat f(\xi)\ne0$ almost everywhere, it follows that
\[
\widehat g=0
\qquad\text{a.e.}
\]
and therefore $g=0$ by Plancherel.
:::

<1>3. Conclude density.
::: proof
Step 2 shows
\[
V^\perp=\{0\}.
\]
Since $V$ is a closed subspace of the Hilbert space $L^2(\mathbb R^n)$,
\[
V=(V^\perp)^\perp=L^2(\mathbb R^n).
\]
Hence
\[
\boxed{
\operatorname{span}\{f_a:a\in\mathbb R^n\}
\text{ is dense in }L^2(\mathbb R^n).}
\]
:::
:::
