---
schema: qual/card@1
id: P-RASP17D
kind: problem
title: "True or false: uniform boundedness variants and an L^2 membership criterion"
classification:
  areas:
  - real-analysis
  topics:
  - Uniform Boundedness Principle
  - Banach-Steinhaus Theorem
  - L2 Spaces
  - Baire Category
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 4 of the official UCSD Spring 2017 real-analysis qualifying exam. Part (3) is corrected to place an absolute value around the complex scalar integral; otherwise the displayed supremum is undefined.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Answer true or false.
For true statements give a brief justification; for false statements give a counterexample.

1. If $X$ is a Banach space and $\{\varphi_n\}_{n=1}^\infty \subset X^*$ satisfies $\sup_n |\varphi_n(x)| < \infty$ for all $x \in X$, then $\sup_n \sup_{\|x\|=1} |\varphi_n(x)| < \infty$.

2. If $X$ is a Banach space, $D$ is a dense subspace of $X$, and $\{\varphi_n\}_{n=1}^\infty \subset X^*$ satisfies $\sup_n |\varphi_n(x)| < \infty$ for all $x \in D$, then $\sup_n \sup_{\|x\|=1} |\varphi_n(x)| < \infty$.

3. Suppose $(\Omega, \mathcal{B}, \mu)$ is a measure space, $\Omega_n \in \mathcal{B}$ with $\Omega_n \uparrow \Omega$ and $\mu(\Omega_n) < \infty$ for all $n$.
   If $f : \Omega \to \mathbb{C}$ is measurable such that $\sup_{n \in \mathbb{N}} \left|\int_{\Omega_n} f \mathbf{1}_{|f| \leq n} g \, d\mu\right| < \infty$ for all $g \in L^2(\mu)$, then $f \in L^2(\mu)$.
:::


::: solution
<1>1. Statement (1) is true.
::: proof
For every fixed \(x\in X\), the hypothesis says
\[
\sup_n|\varphi_n(x)|<\infty.
\]
Since \(X\) is Banach, the Uniform Boundedness Principle yields
\[
\sup_n\|\varphi_n\|<\infty.
\]
But
\[
\|\varphi_n\|=\sup_{\|x\|=1}|\varphi_n(x)|,
\]
so
\[
\boxed{
\sup_n\sup_{\|x\|=1}|\varphi_n(x)|<\infty.}
\]
:::

<1>2. Statement (2) is false.
::: proof
Take
\[
X=\ell^1,
\qquad
D=c_{00},
\]
where \(c_{00}\) is the dense subspace of finitely supported sequences. Define
\[
\varphi_n(x)=n x_n.
\]
Then \(\varphi_n\in(\ell^1)^*=\ell^\infty\) and
\[
\|\varphi_n\|=n.
\]
Hence the operator norms are unbounded.

However, for every \(x\in c_{00}\), only finitely many coordinates of \(x\) are nonzero, so
\[
\sup_n|\varphi_n(x)|<\infty.
\]
Thus pointwise boundedness merely on a dense subspace does not imply uniform boundedness.
:::

<1>3. Statement (3), with the corrected absolute-value hypothesis, is true.
::: proof
Set
\[
f_n:=\mathbf1_{\Omega_n}f\,\mathbf1_{\{|f|\le n\}}.
\]
Since \(|f_n|\le n\) and \(\mu(\Omega_n)<\infty\), we have \(f_n\in L^2(\mu)\). Define
\[
T_n:L^2(\mu)\to\mathbb C,
\qquad
T_n(g)=\int_\Omega f_n g\,d\mu.
\]
By the \(L^2\) Riesz representation theorem,
\[
\|T_n\|=\|f_n\|_2.
\]
The corrected hypothesis is exactly
\[
\sup_n|T_n(g)|<\infty
\qquad\text{for every }g\in L^2(\mu).
\]
Therefore the Uniform Boundedness Principle gives a constant \(C\) such that
\[
\|f_n\|_2\le C
\qquad\text{for every }n.
\]

Because \(\Omega_n\uparrow\Omega\) and \(\mathbf1_{\{|f|\le n\}}\uparrow1\),
\[
|f_n|^2|f_n|^2\uparrow |f|^2
\]
pointwise. By the Monotone Convergence Theorem,
\[
\int_\Omega|f|^2\,d\mu
=\lim_{n\to\infty}\int_\Omega|f_n|^2\,d\mu
\le C^2.
\]
Hence
\[
\boxed{f\in L^2(\mu).}
\]
:::
:::
