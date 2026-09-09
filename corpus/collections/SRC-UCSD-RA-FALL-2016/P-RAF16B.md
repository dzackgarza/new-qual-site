---
schema: qual/card@1
id: P-RAF16B
kind: problem
title: "Limits involving sin^k x, convergence in measure, and distributional derivatives"
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
  note: Checked against Problem 2 of the official UCSD Fall 2016 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
(1) Let $f \in C(\mathbb{R})$ with $f(0) = 1$.
Calculate with justification the limit $\lim_{k \to \infty} \int_0^\pi f(\sin^k x)\,dx$.

(2) Let $(X, \mathcal{M}, \mu)$ be a measure space with $\mu(X) < \infty$.
Assume that $f$ and $f_k$ ($k = 1, 2, \ldots$) are all real-valued, $\mu$-measurable functions on $X$, and $f_k \to f$ in measure.
Let $F \in C(\mathbb{R})$ be uniformly continuous.
Prove that $F(f_k) \to F(f)$ in measure.

(3) Let $m$ denote the Lebesgue measure on $\mathbb{R}^n$.
Assume $g_k \to g$ weakly in $L^1(m)$.
Prove that $\partial^\alpha g_k \to \partial^\alpha g$ in $\mathcal{D}'(\mathbb{R}^n)$ for any multi-index $\alpha$.
:::

::: solution
<1>1. Evaluate the limit in part (1).
::: proof
For every $x\in[0,\pi]$ except $x=\pi/2$,
\[
0\le \sin x<1,
\]
so
\[
\sin^k x\longrightarrow0.
\]
Hence
\[
f(\sin^k x)\longrightarrow f(0)=1
\]
for almost every $x\in[0,\pi]$.

Since $0\le\sin^k x\le1$ and $f$ is continuous, $f$ is bounded on $[0,1]$. Thus there is $M<\infty$ such that
\[
|f(\sin^k x)|\le M
\]
for every $k$ and every $x\in[0,\pi]$. By dominated convergence,
\[
\lim_{k\to\infty}\int_0^\pi f(\sin^k x)\,dx
=\int_0^\pi1\,dx
=\boxed{\pi}.
\]
:::

<1>2. Prove preservation of convergence in measure under $F$.
::: proof
Fix $\varepsilon>0$. Since $F$ is uniformly continuous, there exists $\delta>0$ such that
\[
|u-v|<\delta
\quad\Longrightarrow\quad
|F(u)-F(v)|<\varepsilon.
\]
Therefore
\[
\{|F(f_k)-F(f)|\ge\varepsilon\}
\subseteq
\{|f_k-f|\ge\delta\}.
\]
Taking measures and using $f_k\to f$ in measure gives
\[
\mu\bigl(|F(f_k)-F(f)|\ge\varepsilon\bigr)
\le
\mu\bigl(|f_k-f|\ge\delta\bigr)
\longrightarrow0.
\]
Thus
\[
\boxed{F(f_k)\to F(f)\text{ in measure}.}
\]
:::

<1>3. Pass weak $L^1$ convergence to distributional derivatives.
::: proof
Let $\varphi\in C_c^\infty(\mathbb R^n)$. By definition of distributional derivatives,
\[
\langle \partial^\alpha g_k,\varphi\rangle
=(-1)^{|\alpha|}\int_{\mathbb R^n}g_k(x)\,\partial^\alpha\varphi(x)\,dx.
\]
The test function $\partial^\alpha\varphi$ is bounded, hence belongs to $L^\infty(\mathbb R^n)$. Since $g_k\rightharpoonup g$ weakly in $L^1$,
\[
\int g_k\,\partial^\alpha\varphi
\longrightarrow
\int g\,\partial^\alpha\varphi.
\]
Therefore
\[
\langle \partial^\alpha g_k,\varphi\rangle
\longrightarrow
\langle \partial^\alpha g,\varphi\rangle.
\]
Since this holds for every $\varphi\in C_c^\infty(\mathbb R^n)$,
\[
\boxed{\partial^\alpha g_k\to\partial^\alpha g\text{ in }\mathcal D'(\mathbb R^n).}
\]
:::
:::
