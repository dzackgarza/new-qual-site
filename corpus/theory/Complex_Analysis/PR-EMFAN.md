---
schema: qual/card@1
id: PR-EMFAN
kind: proposition
title: Holomorphic functions are continuous
classification:
  areas:
  - complex-analysis
  topics:
  - Holomorphic Functions
  - Continuity
relations: []
review: draft
---

::: {.proposition}
Let $U\subseteq\CC$ be open, let $z_0\in U$, and let $f\colon U\to\CC$.

(a) $f$ is [[D-E7A5W|holomorphic]] at $z_0$ if and only if there exist $a\in \CC$ and a function $\psi$, defined for small $h\neq0$, such that
$$
f(z_0 + h) - f(z_0) - ah = h\, \psi(h) \quad\text{and}\quad \lim_{h\to0}\psi(h)=0.
$$
In this case, $a = f'(z_0)$.

(b) If $f$ is holomorphic at $z_0$, then $f$ is continuous at $z_0$.
:::

::: {.proof}
For (a), if $f'(z_0)$ exists, put $a\coloneqq f'(z_0)$ and $\psi(h)\coloneqq\frac{f(z_0+h)-f(z_0)}{h}-a$, which tends to $0$.
Conversely, given $a$ and $\psi$, $\frac{f(z_0+h)-f(z_0)}{h}=a+\psi(h)\to a$, so $f'(z_0)$ exists and equals $a$.
For (b), $f(z_0+h)-f(z_0)=h\qty{a+\psi(h)}\to0$ as $h\to0$.
:::
