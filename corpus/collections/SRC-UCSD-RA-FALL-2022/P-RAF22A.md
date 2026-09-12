---
schema: qual/card@1
id: P-RAF22A
kind: problem
title: "True or false: sigma-finite mutual absolute continuity, local L^2, Fourier transform of translates"
classification:
  areas:
  - real-analysis
  topics:
  - Sigma-Finite Measures
  - Absolute Continuity
  - L2 Spaces
  - Tempered Distributions
  - Fourier Transform
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 1 of the official UCSD Fall 2022 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Determine if each of the following statements is true or false.
If true, give a brief proof.
If false, give a counterexample or prove your assertion.

1. If $(X, \mathcal{M}, \mu)$ is a $\sigma$-finite measure space, then there exists a finite measure $\nu$ on $\mathcal{M}$ such that $\nu \ll \mu$ and $\mu \ll \nu$.

2. Let $m$ denote Lebesgue measure on $\mathbb{R}$.
   If $f \in L^1(\mathbb{R}, m)$ and $\int_a^{a+1} |f(x)|^2 \, dx < \infty$ for every $a \in \mathbb{R}$, then $f \in L^2(\mathbb{R}, m)$.

3. Let $f$ be a tempered distribution on $\mathbb{R}^n$, with Fourier transform defined by $\langle \hat{f}, \varphi \rangle = \langle f, \hat{\varphi} \rangle$ for $\varphi \in \mathcal{S}$.
   Recall that for a distribution, $\langle \tau_y^\vee f, \varphi \rangle = \langle f, \tau_{-y} \varphi \rangle$.
   Then it must hold
$$
\widehat{(\tau_y f)}(\xi) = e^{-2\pi i \langle \xi, y \rangle} \hat{f}(\xi), \quad \forall y \in \mathbb{R}^n.
$$
:::

::: solution
<1>1. Statement (1) is true.
::: proof
Because $\mu$ is $\sigma$-finite, choose measurable sets $X_n$ such that
\[
X=\bigcup_{n=1}^\infty X_n,
\qquad
\mu(X_n)<\infty.
\]
Define
\[
\nu(E):=\sum_{n=1}^\infty
2^{-n}\frac{\mu(E\cap X_n)}{1+\mu(X_n)}.
\]
Each summand is a finite measure, so $\nu$ is a measure, and
\[
\nu(X)\le\sum_{n=1}^\infty2^{-n}<\infty.
\]

If $\mu(E)=0$, then every summand is zero, so $\nu(E)=0$; hence $\nu\ll\mu$. Conversely, if $\nu(E)=0$, all nonnegative summands vanish, so
\[
\mu(E\cap X_n)=0
\]
for every $n$. Since the $X_n$ cover $X$,
\[
\mu(E)=0.
\]
Thus $\mu\ll\nu$ as well.
:::

<1>2. Statement (2) is false.
::: proof
For $n\ge1$, let
\[
I_n=[n,n+n^{-3}]
\]
and define
\[
f(x):=\sum_{n=1}^\infty n\,\mathbf1_{I_n}(x).
\]
Then
\[
\|f\|_1
=\sum_{n=1}^\infty n\,m(I_n)
=\sum_{n=1}^\infty\frac1{n^2}<\infty.
\]
Every bounded interval meets only finitely many of the supports $I_n$, so in particular
\[
\int_a^{a+1}|f(x)|^2\,dx<\infty
\]
for every $a\in\mathbb R$.

However,
\[
\|f\|_2^2
=\sum_{n=1}^\infty n^2m(I_n)
=\sum_{n=1}^\infty\frac1n
=\infty.
\]
Hence $f\notin L^2(\mathbb R)$.
:::

<1>3. Statement (3) is true.
::: proof
The usual Fourier translation identity holds first for Schwartz functions:
\[
\widehat{\tau_y\psi}(\xi)
=e^{-2\pi i\langle\xi,y\rangle}\widehat\psi(\xi).
\]
The same identity extends to tempered distributions by duality. Indeed, for every $\varphi\in\mathcal S$,
\[
\begin{aligned}
\langle\widehat{\tau_y f},\varphi\rangle
&=\langle\tau_y f,\widehat\varphi\rangle\\
&=\langle f,\tau_{-y}\widehat\varphi\rangle.
\end{aligned}
\]
Using the Schwartz-function modulation/translation identity on the test function converts the last expression into
\[
\left\langle
e^{-2\pi i\langle\cdot,y\rangle}\widehat f,
\varphi
\right\rangle.
\]
Therefore, in $\mathcal S'$,
\[
\boxed{
\widehat{\tau_y f}
=e^{-2\pi i\langle\cdot,y\rangle}\widehat f.}
\]
:::
:::
