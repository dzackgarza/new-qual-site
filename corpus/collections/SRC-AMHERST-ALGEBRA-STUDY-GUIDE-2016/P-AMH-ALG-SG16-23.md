---
schema: qual/card@1
id: P-AMH-ALG-SG16-23
kind: problem
title: The kernel of a ring homomorphism restricted to an ideal is an ideal
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored Amherst College Study Guide for Algebra (September 2016).
---

::: {.problem}
(February 2008) Let $\varphi:R\to S$ be a ring homomorphism.
Let $I\subseteq R$ be an ideal of $R$, and set
$$
J=\{x\in I\mid \varphi(x)=0_S\},
$$
where $0_S$ denotes the zero element of $S$.
Prove that $J$ is an ideal of $R$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}
The set $J$ is nonempty.

::: pf-proof
Because $I$ is an ideal, $0_R\in I$.  Every ring homomorphism preserves zero,
so
$$
\varphi(0_R)=0_S.
$$
Hence $0_R\in J$.
:::

:::

::: {.pf-step #s1-2}
The set $J$ is closed under subtraction.

::: pf-proof
Let $x,y\in J$.  Then $x,y\in I$, so
$$
x-y\in I
$$
because $I$ is an ideal.  Also,
$$
\varphi(x-y)
=\varphi(x)-\varphi(y)
=0_S-0_S
=0_S.
$$
Therefore $x-y\in J$.
:::

:::

::: {.pf-step #s1-3}
The set $J$ is closed under left multiplication by arbitrary elements
of $R$.

::: pf-proof
Let $r\in R$ and $x\in J$.  Since $x\in I$ and $I$ is an ideal,
$rx\in I$.  Moreover,
$$
\varphi(rx)
=\varphi(r)\varphi(x)
=\varphi(r)0_S
=0_S.
$$
Thus $rx\in J$.
:::

:::

::: {.pf-step #s1-4}
The set $J$ is closed under right multiplication by arbitrary elements
of $R$.

::: pf-proof
Let $r\in R$ and $x\in J$.  Since $x\in I$,
$xr\in I$.  Furthermore,
$$
\varphi(xr)
=\varphi(x)\varphi(r)
=0_S\varphi(r)
=0_S.
$$
Hence $xr\in J$.
:::

:::

::: pf-step
Therefore $J$ is a two-sided ideal of $R$.

::: pf-proof
Steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref} show that $J$ is an additive subgroup of $R$ by the
subtraction criterion.  Steps [](#s1-3){.pf-ref} and [](#s1-4){.pf-ref} give absorption under
multiplication by arbitrary ring elements on both sides.  These are exactly
the two-sided ideal axioms.
:::

:::

:::

:::
