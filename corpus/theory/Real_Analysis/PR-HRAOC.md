---
schema: qual/card@1
id: PR-HRAOC
kind: proposition
title: Existence of nonzero smooth compactly supported functions
classification:
  areas:
  - real-analysis
  topics:
  - Density
  - Differentiation
relations: []
review: draft
---

::: {.proposition}
Let $f\colon\RR\to\RR$ be given by $f(x)\coloneqq e^{-1/x^2}$ for $x>0$ and $f(x)\coloneqq0$ for $x\leq0$.
Then $f\in C^\infty(\RR)$, and $\psi(x)\coloneqq f(x)\,f(1-x)$ is a $C^\infty$ function on $\RR$ with $\psi>0$ on $(0,1)$ and $\psi=0$ outside $(0,1)$.
For $n\geq1$, $\phi(x)\coloneqq f\big(1-\abs{x}^2\big)$ is a $C^\infty$ function on $\RR^n$ with $\supp\phi=\theset{x : \abs{x}\leq1}$ [@Fol13].
:::
