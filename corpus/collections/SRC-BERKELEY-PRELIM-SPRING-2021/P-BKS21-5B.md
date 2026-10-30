---
schema: qual/card@1
id: P-BKS21-5B
kind: problem
title: Disk automorphism carrying one prescribed point to another
classification:
  areas:
  - prelim
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.problem}
If $a,b$ lie in the open unit disk, show that there is a biholomorphic self-map of the disk carrying $a$ to $b$.
:::

::: {.solution}

For $c$ in the open unit disk, define
$$
\phi_c(z)\coloneqq\frac{z-c}{1-\overline c\,z}.
$$

::: pf

::: {.pf-step #s1-1}

For every $c$ in the open unit disk, $\phi_c$ maps the open unit disk into itself.


::: pf-proof

If $\abs{z}<1$ and $\abs{c}<1$, then
$$
\abs{\overline c\,z}<1,
$$
so the denominator does not vanish. Moreover,
$$
\begin{aligned}
\abs{1-\overline c\,z}^2-\abs{z-c}^2
&=
(1-\abs{c}^2)(1-\abs{z}^2)
>0.
\end{aligned}
$$
Therefore
$$
\abs{\phi_c(z)}^2
=
\frac{\abs{z-c}^2}{\abs{1-\overline c\,z}^2}
<1.
$$

:::

:::

::: {.pf-step #s1-2}

The inverse of $\phi_c$ is
$$
\phi_c^{-1}(w)=\frac{w+c}{1+\overline c\,w},
$$
and it also maps the open unit disk into itself.


::: pf-proof

Solving
$$
w=\frac{z-c}{1-\overline c\,z}
$$
for $z$ gives
$$
z=\frac{w+c}{1+\overline c\,w}.
$$
The denominator is nonzero for $\abs{w}<1$ because $\abs{\overline c\,w}<1$. Direct substitution shows that this formula is both a left and right inverse of $\phi_c$. By step [](#s1-1){.pf-ref}, $\phi_c$ maps the disk into itself, and the same calculation from step [](#s1-1){.pf-ref} with $-c$ in place of $c$ shows that the displayed inverse maps the disk into itself as well.

:::

:::

::: {.pf-step #s1-3}

Each $\phi_c$ is a biholomorphic automorphism of the open unit disk, and
$$
\phi_c(c)=0.
$$


::: pf-proof

The formulas in steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref} are holomorphic on the disk because their denominators do not vanish there, and they are inverse to one another. The equality $\phi_c(c)=0$ is immediate from the definition.

:::

:::

::: {.pf-step #s1-4}

The map
$$
\boxed{
F\coloneqq\phi_b^{-1}\circ\phi_a
}
$$
is a biholomorphic self-map of the disk satisfying $F(a)=b$.


::: pf-proof

By step [](#s1-3){.pf-ref}, both $\phi_a$ and $\phi_b^{-1}$ are biholomorphic automorphisms of the disk, so their composition is also one. Furthermore,
$$
F(a)
=
\phi_b^{-1}(\phi_a(a))
=
\phi_b^{-1}(0)
=b.
$$

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} constructs the required map.

:::

:::

:::
