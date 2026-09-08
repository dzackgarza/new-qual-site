---
schema: qual/card@1
id: P-RASP13H
kind: problem
title: "Distributional derivative of a monotone function is a Borel measure"
classification:
  areas:
  - real-analysis
  topics:
  - Monotone Functions
  - Distributions
  - Borel Measures
  - Riesz-Markov Theorem
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 8 of the official UCSD Spring 2013 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Let $f$ be a monotonically non-decreasing function on $\mathbb{R}$.
Prove that its distributional derivative is a Borel measure.

(Hint: You may apply the Riesz-Markov representation theorem.
In doing so, you need to state the theorem clearly and verify the assumptions carefully.)
:::

::: solution
<1>1. The distributional derivative of $f$ is positive.
::: proof
A monotone real-valued function is bounded on compact intervals, hence belongs to $L^1_{\mathrm{loc}}(\mathbb R)$ and defines a distribution. Its distributional derivative is
\[
T(\varphi):=-\int_{\mathbb R}f(x)\varphi'(x)\,dx,
\qquad
\varphi\in C_c^\infty(\mathbb R).
\]

Let $\rho\ge0$ be a standard smooth mollifier and put
\[
f_\varepsilon=f*\rho_\varepsilon.
\]
Since $f$ is non-decreasing and $\rho_\varepsilon\ge0$, the smooth function $f_\varepsilon$ is also non-decreasing; hence
\[
f_\varepsilon'(x)\ge0
\]
for every $x$.

Also $f_\varepsilon\to f$ in $L^1_{\mathrm{loc}}$. Therefore, for every nonnegative $\varphi\in C_c^\infty$,
\[
\begin{aligned}
T(\varphi)
&=-\lim_{\varepsilon\downarrow0}
\int f_\varepsilon(x)\varphi'(x)\,dx\\
&=\lim_{\varepsilon\downarrow0}
\int f_\varepsilon'(x)\varphi(x)\,dx
\ge0.
\end{aligned}
\]
Thus $T$ is a positive distribution.
:::

<1>2. Positivity gives the local sup-norm bounds needed for Riesz--Markov.
::: proof
Fix a compact set $K\subset\mathbb R$. Choose
\[
\chi\in C_c^\infty(\mathbb R),
\qquad
\chi\ge0,
\qquad
\chi=1
\]
on a neighborhood of $K$.

If $\varphi\in C_c^\infty$ is supported in $K$, then pointwise
\[
-\|\varphi\|_\infty\chi
\le \varphi
\le \|\varphi\|_\infty\chi.
\]
Since $T$ is positive,
\[
|T(\varphi)|
\le T(\chi)\|\varphi\|_\infty.
\]
Hence $T$ is continuous in the sup norm on test functions supported in each fixed compact set.

Smooth compactly supported functions are uniformly dense in $C_c(\mathbb R)$ after fixing a slightly larger compact support. The preceding estimate therefore extends $T$ uniquely to a positive linear functional
\[
L:C_c(\mathbb R)\to\mathbb R.
\]
:::

<1>3. Apply the Riesz--Markov representation theorem.
::: proof
The Riesz--Markov theorem states that every positive linear functional on $C_c(X)$, for a locally compact Hausdorff space $X$, is integration against a unique positive Radon measure.

Applying it to the positive functional $L$ on $C_c(\mathbb R)$ gives a unique positive Radon measure $\nu$ such that
\[
L(\varphi)=\int_{\mathbb R}\varphi\,d\nu
\qquad
(\varphi\in C_c(\mathbb R)).
\]
In particular, for every test function $\varphi\in C_c^\infty$,
\[
-\int_{\mathbb R}f(x)\varphi'(x)\,dx
=T(\varphi)
=\int_{\mathbb R}\varphi\,d\nu.
\]
Thus the distributional derivative of $f$ is exactly the Borel (indeed Radon) measure $\nu$:
\[
\boxed{Df=\nu.}
\]
:::
:::
