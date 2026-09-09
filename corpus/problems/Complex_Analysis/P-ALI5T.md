---
schema: qual/card@1
id: P-ALI5T
kind: problem
title: A holomorphic function real-valued on a closed curve is constant
classification:
  areas:
  - complex-analysis
  topics:
  - Open Mapping Theorem
  - Maximum Modulus Principle
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: problem
Assume $f(z)$ is analytic in a region $D$ and $\Gamma$ is a simple closed rectifiable curve in $D$ whose interior $\Omega$ is contained in $D$.
Prove that if $f(z)$ is real-valued for all $z \in \Gamma$, then $f(z)$ is constant on $D$.
:::

::: solution
Write
\[
f=u+iv.
\]
Since $f$ is holomorphic, $v$ is harmonic on $D$. By hypothesis,
\[
v=0\quad\text{on }\Gamma=\partial\Omega.
\]
Because $\Gamma$ is a simple closed curve and $\Omega$ is its bounded interior, $\overline\Omega=\Omega\cup\Gamma\subset D$.

<1>1. The harmonic maximum principle applied to $v$ on $\Omega$ gives
\[
v\le0
\]
throughout $\Omega$, because the boundary values are zero. Applying it to $-v$ gives
\[
-v\le0.
\]
Hence
\[
v\equiv0\quad\text{on }\Omega.
\]

<1>2. Thus $f(\Omega)\subset\mathbb R$. If $f$ were nonconstant on the connected open set $\Omega$, the open mapping theorem would imply that $f(\Omega)$ is open in $\mathbb C$, impossible for a subset of $\mathbb R$. Therefore $f$ is constant on $\Omega$.

<1>3. Since $D$ is connected and $f-c$ vanishes on the nonempty open subset $\Omega$, the identity theorem gives
\[
f\equiv c\quad\text{on }D.
\]
:::
