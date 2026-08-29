---
schema: qual/card@1
id: E-NSN6G
kind: exercise
title: Locally uniform limit theorem for holomorphic functions
classification:
  areas:
  - complex-analysis
  topics:
  - Uniform Convergence
  - Cauchy Estimates
  - Sequences of Functions
  - Holomorphic Functions
relations: []
review: draft
---

:::{.exercise}
Prove that if $f_n\to f$ locally uniformly with $f_n$ holomorphic, then $f_n'\to f'$ locally uniformly and $f'$ is holomorphic.

:::

:::{.solution}
\envlist

- Simplifying step: for some reason, it suffices to assume $f_n\to f$ uniformly on all of $\Omega$?
- Take $\Omega_R$ to be $\Omega$ with a buffer of $R$, so $d(z, \bd \Omega) > R$ for every $z \in \bar{\Omega_R}$.
- It suffices to show the following bound for $F$ any holomorphic function on $\Omega$:
\[
\sup_{z\in \Omega_R} \abs{F'(z)} \leq {1\over R} \sup_{\zeta \in \Omega} \abs{F(\zeta)} && \forall R
,\]
where on the right we take the sup over all $\Omega$.
  - Then take $F \da f_n-f$ and $R\to 0$ to conclude, since the right-hand side is a constant not depending on $\Omega_R$.
- For any $z\in \Omega_R$, we have $\bar{D_R(z)} \subseteq \Omega_R$, so Cauchy's integral formula can be applied:
-
\[
\abs{F'(z)} 
&= \abs{ {1\over 2\pi i} \int_{\bd D_R(z)} {F(\xi) \over (\xi-z)^2 } \dxi  } \\
&\leq {1\over 2\pi} \int_{\bd D_R(z)} { { \abs{F(\xi)} \over \abs{\xi-z}^2 }} \dxi   \\
&\leq {1\over 2\pi} \int_{\bd D_R(z)} { { \sup_{\zeta\in \Omega} \abs{F(\zeta)} \over \abs{\xi-z}^2 }} \dxi   \\
&= {1\over 2\pi} \sup_{\zeta\in \Omega} \abs{F(\zeta)}  \int_{\bd D_R(z)} { { 1 \over R^2 }} \dxi   \\
&= {1\over 2\pi} \sup_{\zeta\in \Omega} \abs{F(\zeta)}  {1\over R^2} \int_{\bd D_R(z)} \dxi   \\
&= {1\over 2\pi} \sup_{\zeta\in \Omega} \abs{F(\zeta)}  {1\over R^2} 2\pi R   \\
&\leq {1\over 2\pi} \sup_{\zeta\in \Omega} \abs{F(\zeta)}  {1\over R^2}\qty{ 2\pi R}   \\
&= {1\over R} \sup_{\zeta \in \Omega}\abs{F(\zeta)}
.\]

- Now
\[
\norm{f_n' - f'}_{\infty, \Omega_R} \leq {1\over R} \norm{f_n - f}_{\infty, \Omega}
,\]
where if $R$ is fixed then by uniform convergence of $f_n\to f$, for $n$ large enough $\norm{f_n - f} < \eps/R$.
:::

