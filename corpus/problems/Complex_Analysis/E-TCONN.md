---
schema: qual/card@1
id: E-TCONN
kind: problem
title: Iterates of a self-map of the disk converge to an attracting fixed point
classification:
  areas:
  - complex-analysis
  topics:
  - Fixed Points
  - Schwarz Lemma
  - Blaschke Factors
  - Sequences of Functions
relations: []
review: draft
audit:
- event: statement-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: The source does not say that $f$ is holomorphic or that the initial point lies in $\DD$; the statement now says both.
---

::: {.exercise}
Suppose $f:\DD\to \DD$ is holomorphic with $f(a) = a$ a fixed point where $\abs{f'(a)} < 1$.
Show that for any initial point $z_0\in\DD$, the sequence $z_k \coloneqq f(z_{k-1})$ converges to $a$.
:::

::: {.solution}
For $a\in\DD$ let $\psi_a(z) \coloneqq \frac{a-z}{1-\bar az}$, an automorphism of $\DD$ with $\psi_a\circ\psi_a = \mathrm{id}$ and $\psi_a(0)=a$.

::: pf

::: {.pf-step #contraction}
If $a=0$, then for each $r\in(0,1)$ there is $C<1$ with $\abs{f(z)}\leq C\abs{z}$ for $\abs{z}\leq r$.

::: pf-proof
By the Schwarz lemma, $g(z)\coloneqq f(z)/z$, extended by $g(0)=f'(0)$, is holomorphic on $\DD$ with $\abs{g}\leq 1$. Since $\abs{g(0)} = \abs{f'(0)}<1$, $g$ is not a unimodular constant, so by the maximum modulus principle $\abs{g}<1$ on $\DD$. The continuous function $\abs{g}$ attains a maximum $C<1$ on the compact disk $\abs{z}\leq r$.
:::

:::

::: {.pf-step #zero-case}
If $a=0$, then $z_k\to 0$.

::: pf-proof
Choose $r$ with $\abs{z_0}\leq r<1$ and $C$ as in step [](#contraction){.pf-ref}. By induction $\abs{z_k}\leq C^k\abs{z_0}\leq r$ for all $k$, so $z_k\to 0$.
:::

:::

::: {.pf-step #conjugate}
$F \coloneqq \psi_a\circ f\circ\psi_a$ is a holomorphic self-map of $\DD$ with $F(0) = 0$ and $\abs{F'(0)} = \abs{f'(a)}<1$.

::: pf-proof
$F(0) = \psi_a(f(a)) = \psi_a(a) = 0$. By the chain rule,
$$
F'(0) = \psi_a'(f(a))\, f'(a)\,\psi_a'(0) = \psi_a'(\psi_a(0))\,\psi_a'(0)\, f'(a) = (\psi_a\circ\psi_a)'(0)\, f'(a) = f'(a).
$$
:::

:::

::: pf-step
$z_k\to a$.

::: pf-proof
Put $w_k\coloneqq\psi_a(z_k)$. Then $w_k = \psi_a(f(\psi_a(w_{k-1}))) = F(w_{k-1})$, so $w_k\to 0$ by steps [](#conjugate){.pf-ref} and [](#zero-case){.pf-ref} applied to $F$. By continuity, $z_k = \psi_a(w_k)\to\psi_a(0) = a$.
:::

:::

:::

:::
