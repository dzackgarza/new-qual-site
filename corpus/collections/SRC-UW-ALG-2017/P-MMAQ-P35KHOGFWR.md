---
schema: qual/card@1
id: P-MMAQ-P35KHOGFWR
kind: problem
title: Kernels of finite free presentations of finitely presented modules are finitely
  generated
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Free Modules
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.problem}
Suppose $A$ is a commutative ring and $M$ is a finitely presented module.
Given any surjection $\phi:A^n\rightarrow M$ from a finite free $A$-module, show that $\ker\phi$ is finitely generated.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Since $M$ is finitely presented, there is an exact sequence $A^m \xrightarrow{\psi} A^r \xrightarrow{\pi} M \to 0$.

::: pf-proof

definition of finitely presented.

:::

:::

::: pf-step

We have a surjection $\phi : A^n \to M$, and we want to show $\ker \phi$ is finitely generated.

::: pf-proof

setup.

:::

:::

::: {.pf-step #s3}

By Schanuel's lemma (applied to the two surjections $\phi : A^n \to M$ and $\pi : A^r \to M$), we get
$$\ker \phi \oplus A^r \cong \ker \pi \oplus A^n.$$

::: pf-proof

Schanuel's lemma.

:::

:::

::: {.pf-step #s4}

$\ker \pi = \operatorname{im} \psi$ is finitely generated (it is the image of the finitely generated module $A^m$).

::: pf-proof

Step [](#s1){.pf-ref}.

:::

:::

::: {.pf-step #s5}

Hence $\ker \phi \oplus A^r \cong \operatorname{im}\psi \oplus A^n$ is finitely generated.

::: pf-proof

Steps [](#s3){.pf-ref} and [](#s4){.pf-ref}.

:::

:::

::: {.pf-step #s6}

A direct summand of a finitely generated module is finitely generated, so $\ker \phi$ is finitely generated.

::: pf-proof

Step [](#s5){.pf-ref} (since $\ker \phi$ is a direct summand of $\ker \phi \oplus A^r$).

:::

:::

::: pf-qed

Step [](#s6){.pf-ref}.

:::

:::

:::
