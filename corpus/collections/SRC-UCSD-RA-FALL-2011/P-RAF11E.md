---
schema: qual/card@1
id: P-RAF11E
kind: problem
title: "Uniform convergence of Fourier series for Hölder continuous functions"
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
  note: Checked against Problem 5 of the official UCSD Fall 2011 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Let $f : \mathbb{R} \to \mathbb{R}$ be a $2\pi$-periodic function, i.e. $f(x) = f(x + 2\pi)$, such that there exists $C > 0$ (possibly large) and $\epsilon > 0$ (possibly small) with
$$
|f(x) - f(y)| \leq C|x - y|^{1/2 + \epsilon}.
$$
Show that the Fourier series of $f$ converges uniformly.

Hint: Half credit will be given for the special case $\epsilon = 1/2$, which can be treated more directly.
For the general case try computing $\int_0^{2\pi} |f(x+h) - f(x)|^2\,dx$ two different ways.
:::

::: solution
<1>1. Estimate the $L^2$ norm of a translation difference.
::: proof
Set
\[
\alpha:=\frac12+\varepsilon>\frac12.
\]
By hypothesis,
\[
|f(x+h)-f(x)|\le C|h|^\alpha.
\]
Therefore
\[
\int_0^{2\pi}|f(x+h)-f(x)|^2\,dx
\le 2\pi C^2|h|^{2\alpha}.
\]
:::

<1>2. Express the same quantity using Fourier coefficients.
::: proof
Let
\[
c_n:=\frac1{2\pi}\int_0^{2\pi}f(x)e^{-inx}\,dx.
\]
The Fourier coefficient of
\[
x\longmapsto f(x+h)-f(x)
\]
at frequency $n$ is
\[
(e^{inh}-1)c_n.
\]
By Parseval,
\[
\int_0^{2\pi}|f(x+h)-f(x)|^2\,dx
=2\pi\sum_{n\in\mathbb Z}|c_n|^2|e^{inh}-1|^2.
\]
Combining this with Step 1 gives
\[
\sum_{n\in\mathbb Z}|c_n|^2|e^{inh}-1|^2
\le C^2|h|^{2\alpha}.
\]
:::

<1>3. Obtain a dyadic $\ell^2$ estimate for the coefficients.
::: proof
Fix an integer $N\ge1$ and take
\[
h=\frac1N.
\]
If
\[
N\le |n|\le2N,
\]
then
\[
1\le |nh|\le2.
\]
Hence there is an absolute constant $c_0>0$ such that
\[
|e^{inh}-1|\ge c_0
\]
throughout this range. Therefore Step 2 gives
\[
\sum_{N\le |n|\le2N}|c_n|^2
\le C_1N^{-2\alpha}
\]
for a constant $C_1$ independent of $N$.
:::

<1>4. Upgrade the dyadic estimate to absolute summability.
::: proof
By Cauchy--Schwarz,
\[
\begin{aligned}
\sum_{N\le |n|\le2N}|c_n|
&\le (2N+2)^{1/2}
\left(\sum_{N\le |n|\le2N}|c_n|^2\right)^{1/2}\\
&\le C_2N^{1/2-\alpha}\\
&=C_2N^{-\varepsilon}.
\end{aligned}
\]
Apply this with $N=2^k$. Then
\[
\sum_{2^k\le |n|<2^{k+1}}|c_n|
\le C_2 2^{-k\varepsilon}.
\]
Since
\[
\sum_{k=0}^\infty2^{-k\varepsilon}<\infty,
\]
we obtain
\[
\sum_{n\in\mathbb Z}|c_n|<\infty.
\]
:::

<1>5. Conclude uniform convergence to $f$.
::: proof
Absolute summability implies that
\[
\sum_{n\in\mathbb Z}c_ne^{inx}
\]
converges absolutely and uniformly by the Weierstrass $M$-test, to a continuous $2\pi$-periodic function $S$.

Uniform convergence permits termwise integration, so $S$ has Fourier coefficients $c_n$, the same Fourier coefficients as $f$. Thus the continuous function
\[
h:=f-S
\]
has every Fourier coefficient equal to zero.

By Fejer's theorem, the Cesaro means of the Fourier series of a continuous periodic function converge uniformly to that function. All Cesaro means of $h$ are identically zero, hence
\[
h\equiv0.
\]
Therefore $S=f$, and the Fourier series of $f$ converges uniformly to $f$.
:::
:::
