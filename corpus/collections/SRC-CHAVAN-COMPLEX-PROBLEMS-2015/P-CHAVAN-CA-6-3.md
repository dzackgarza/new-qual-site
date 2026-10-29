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
Let $\DD$ be the open unit disk.
Show that $\operatorname{Aut}(\DD)$ acts transitively on $\DD$: for every $a,b\in\DD$, there exists a biholomorphism
$$
f:\DD\to\DD
$$
such that $f(a)=b$.
:::

::: {.solution}

For $c\in\DD$, define
$$
\psi_c(z)=\frac{c-z}{1-\overline c z}.
$$

::: pf

::: {.pf-step #s1-1}

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

::: {.pf-step #s1-2}

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

::: {.pf-step #s1-3}

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
By steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref}, $\psi_c$ is a holomorphic self-map of $\DD$, and the
identity above shows that its inverse is the same holomorphic map.

:::

:::

::: {.pf-step #s1-4}

For every $a,b\in\DD$, the biholomorphism
$$
f=\psi_b\circ\psi_a
$$
satisfies $f(a)=b$.


::: pf-proof

Step [](#s1-3){.pf-ref} shows that both factors are automorphisms of $\DD$, so their
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

Step [](#s1-4){.pf-ref} gives an automorphism carrying an arbitrary $a\in\DD$ to an arbitrary
$b\in\DD$, which is exactly transitivity.

:::

:::

:::
