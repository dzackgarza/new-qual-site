---
schema: qual/card@1
id: E-UVNVV
kind: exercise
title: Injectivity relates to derivatives
classification:
  areas:
  - complex-analysis
  topics:
  - Zeros
  - Open Mapping Theorem
  - Argument Principle
relations: []
review: draft
---

::: {.exercise}
Show that if $z_0$ is a zero of $f'$ of order $n$, then $f$ is $(n+1)$-to-one in a neighborhood of $z_0$.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** Show that if $z_0$ is a zero of $f'$ of order $n$, then $f$ is $(n+1)$-to-one in a neighborhood of $z_0$ (for $z$ near $z_0$, the equation $f(z) = w$ has exactly $n+1$ solutions in a punctured neighborhood of $z_0$, for $w$ near $f(z_0)$, $w \neq f(z_0)$).

<1>1. Setup: expand $f$ about $z_0$.
Proof: Since $z_0$ is a zero of $f'$ of order $n$, we have $f'(z) = (z - z_0)^n h(z)$ with $h$ analytic near $z_0$, $h(z_0) \neq 0$.
Integrating, $f(z) - f(z_0) = (z - z_0)^{n+1} \phi(z)$ where $\phi$ is analytic near $z_0$ and $\phi(z_0) = h(z_0)/(n+1) \neq 0$.

<1>2. $\phi$ is nonzero on a neighborhood of $z_0$, so $\phi$ has an $(n+1)$-st root $\psi$ with $\psi^{n+1} = \phi$, $\psi$ analytic, $\psi(z_0) \neq 0$.
Proof: $\phi(z_0) \neq 0$ by <1>1; by continuity $\phi \neq 0$ in a disk around $z_0$, where a holomorphic branch of the $(n+1)$-st root exists (the disk is simply connected and $\phi$ avoids $0$).

<1>3. Define $\zeta(z) = (z - z_0)\psi(z)$; then $\zeta$ is a biholomorphism from a neighborhood of $z_0$ onto a neighborhood of $0$, with $\zeta(z_0) = 0$ and $\zeta'(z_0) = \psi(z_0) \neq 0$.
Proof: $\zeta'(z_0) = \psi(z_0) \neq 0$, so the inverse function theorem gives the local biholomorphism.

<1>4. In the $\zeta$ coordinate, $f(z) = f(z_0) + \zeta(z)^{n+1}$.
Proof: <1>1 and <1>2: $f(z) - f(z_0) = (z - z_0)^{n+1}\phi(z) = ((z - z_0)\psi(z))^{n+1} = \zeta(z)^{n+1}$.

<1>5. The map $w \mapsto f(z_0) + w^{n+1}$ is $(n+1)$-to-one on a punctured neighborhood of $0$.
Proof: For $w' \neq 0$ near $0$, the equation $w^{n+1} = w'$ has exactly $n+1$ distinct solutions (the $n+1$ roots of $w'$), all lying in a small disk around $0$.

<1>6. Q.E.D. Proof: <1>3 shows the change of variables $z \leftrightarrow \zeta$ is one-to-one, and <1>5 shows $f$ in these coordinates is $(n+1)$-to-one; composing, $f$ is $(n+1)$-to-one near $z_0$.
:::
