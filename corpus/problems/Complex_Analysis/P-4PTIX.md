---
schema: qual/card@1
id: P-4PTIX
kind: problem
title: Fixed points of holomorphic self-maps of the disk
classification:
  areas:
  - complex-analysis
  topics:
  - Fixed Points
  - Schwarz Lemma
  - Blaschke Factors
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.problem}
Let $g$ be analytic for $\abs{z}\leq 1$ and $\abs{g(z)} < 1$ for $\abs{z} = 1$.

(a) Show that $g$ has a unique fixed point in $\abs{z} < 1$.

(b) What happens if we replace $\abs{g(z)} < 1$ with $\abs{g(z)}\leq 1$ for $\abs{z}=1$?
Give an example if (a) is not true or give a proof if (a) is still true.

(c) What happens if we simply assume that $f$ is analytic for $\abs{z} < 1$ and $\abs{f(z)} < 1$ for $\abs{z} < 1$?
Suppose that $f(z)     \not\equiv  z$.
Can $f$ have more than one fixed point in $\abs{z} < 1$?
:::

::: {.hint}
The map
$\displaystyle{\psi_{\alpha}(z)=\frac{\alpha-z}{1-\bar{\alpha}z}}$
may be useful.
:::

::: {.solution}

For $\alpha\in\DD$, $\psi_\alpha$ is an automorphism of $\DD$ with $\psi_\alpha(0)=\alpha$, $\psi_\alpha(\alpha)=0$ and $\psi_\alpha\circ\psi_\alpha=\id_\DD$ ([[E-ZSOC4]]).

::: pf

::: pf-step
(a) $g$ has exactly one fixed point in $\abs{z}<1$.

::: pf-proof
On $\abs{z}=1$, $\abs{g(z)}<1=\abs{z}$.
By Rouché's theorem, $g(z)-z$ and $-z$ have the same number of zeros in $\abs{z}<1$, counted with multiplicity, namely one.
:::

:::

::: pf-step
(b) The conclusion of (a) can fail: $g(z)=\frac{z+1}{2}$ satisfies $\abs{g(z)}\leq1$ on $\abs{z}=1$ but has no fixed point in $\abs{z}<1$.

::: pf-proof
$\abs{g(z)}\leq\frac{\abs{z}+1}{2}=1$ on $\abs{z}=1$, and $g(z)=z$ only for $z=1$.
:::

:::

::: {.pf-step #at-most-one}
(c) No: if $f\not\equiv z$, then $f$ has at most one fixed point in $\abs{z}<1$.

::: pf-proof
Suppose $f(a)=a$ and $f(b)=b$ with $a\neq b$ in $\DD$.
Let $h\coloneqq\psi_a\circ f\circ\psi_a\colon\DD\to\DD$.
Then $h(0)=\psi_a(f(a))=0$, and $c\coloneqq\psi_a(b)\neq0$ satisfies $h(c)=\psi_a(f(b))=c$.
The equality case of the Schwarz lemma gives $h(z)=\lambda z$ with $\abs{\lambda}=1$, and $h(c)=c$ forces $\lambda=1$.
Hence $f=\psi_a\circ h\circ\psi_a=\id_\DD$, a contradiction.
:::

:::

::: pf-step
In (c), $f$ may also have no fixed point in $\abs{z}<1$.

::: pf-proof
Let $C(w)\coloneqq\frac{w-i}{w+i}$, which maps the upper half-plane $\HH$ biholomorphically onto $\DD$, and let $f\coloneqq C\circ\tau\circ C^{-1}$ with $\tau(w)=w+1$.
Then $f$ is analytic with $\abs{f}<1$ on $\DD$, and $f(z)=z$ would give $\tau(C^{-1}(z))=C^{-1}(z)$, which has no solution.
:::

:::

:::

:::
