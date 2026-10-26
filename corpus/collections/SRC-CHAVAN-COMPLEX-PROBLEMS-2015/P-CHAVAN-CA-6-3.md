---
schema: qual/card@1
id: P-CHAVAN-CA-6-3
kind: problem
title: The automorphism group of the unit disk acts transitively
classification: {areas: [complex-analysis], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
---

::: {.problem}
Let $\mathbb D$ be the open unit disk.
Show that $\operatorname{Aut}(\mathbb D)$ acts transitively on $\mathbb D$: for every $a,b\in\mathbb D$, there exists a biholomorphism
\[
f:\mathbb D\to\mathbb D
\]
such that $f(a)=b$.
:::

For $c\in\DD$, define
$$
\psi_c(z)=\frac{c-z}{1-\overline c z}.
$$

::: pf

::: pf-step

For every $c\in\DD$, the map $\psi_c$ is holomorphic on $\DD$.


::: pf-proof

If $z\in\DD$, then
$$
\abs{\overline c z}=\abs{c}\,\abs{z}<1,
$$
so $1-\overline c z\neq0$. Hence the displayed rational function is holomorphic
throughout $\DD$.

:::

:::

::: pf-step

For every $c,z\in\DD$, one has $\psi_c(z)\in\DD$.


::: pf-proof

A direct calculation gives
$$
1-\abs{\psi_c(z)}^2
=
\frac{\abs{1-\overline c z}^2-\abs{c-z}^2}
     {\abs{1-\overline c z}^2}
=
\frac{(1-\abs{c}^2)(1-\abs{z}^2)}
     {\abs{1-\overline c z}^2}.
$$
Since $c,z\in\DD$, the right-hand side is positive. Thus
$\abs{\psi_c(z)}<1$.

:::

:::

::: pf-step

Each $\psi_c$ is an involution of $\DD$, hence a biholomorphism
$\DD\to\DD$.


::: pf-proof

Put $w=\psi_c(z)$. Then
$$
c-w
=
\frac{z(1-\abs{c}^2)}{1-\overline c z},
\qquad
1-\overline c w
=
\frac{1-\abs{c}^2}{1-\overline c z}.
$$
Therefore
$$
\psi_c(\psi_c(z))=\frac{c-w}{1-\overline c w}=z.
$$
By steps <1>1 and <1>2, $\psi_c$ is a holomorphic self-map of $\DD$, and the
identity above shows that its inverse is the same holomorphic map.

:::

:::

::: pf-step

For every $a,b\in\DD$, the biholomorphism
$$
f=\psi_b\circ\psi_a
$$
satisfies $f(a)=b$.


::: pf-proof

Step <1>3 shows that both factors are automorphisms of $\DD$, so their
composition is an automorphism. Moreover,
$$
\psi_a(a)=0,
\qquad
\psi_b(0)=b,
$$
and hence $f(a)=b$.

:::

:::

::: pf-qed

Step <1>4 gives an automorphism carrying an arbitrary $a\in\DD$ to an arbitrary
$b\in\DD$, which is exactly transitivity.

:::

:::
