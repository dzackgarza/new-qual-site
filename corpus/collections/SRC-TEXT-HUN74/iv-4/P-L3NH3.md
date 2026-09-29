---
schema: qual/card@1
id: P-L3NH3
kind: problem
title: $\operatorname{Hom}_R(R,R)\cong R^{\mathrm{op}}$
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Rings
  - Homomorphisms
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Let $R$ be a unital ring, show that there is a ring homomorphism $\mathrm{Hom}_R(R, R) \to R^{op}$ where $\mathrm{Hom}_R$ denotes left $R-$module homomorphisms.
Conclude that if $R$ is commutative, then there is a ring isomorphism $\mathrm{Hom}_R(R, R) \cong R$.
:::

::: {.solution}
Let $\Phi\colon \operatorname{Hom}_R(R,R) \to R^{\mathrm{op}}$ be evaluation at $1$, $\Phi(f) = f(1)$. For $a\in R$ let $f_a\colon R\to R$ be $f_a(r)=ra$.

::: pf

::: {.pf-step #s1}

$\Phi$ is a bijection with inverse $a \mapsto f_a$.

::: pf-proof

Each $f_a$ is a left $R$-module homomorphism: $f_a(r_1 + r_2) = r_1 a + r_2 a$ and $f_a(sr) = (sr)a = s f_a(r)$. Also $\Phi(f_a)=a$. Conversely, for $f\in\operatorname{Hom}_R(R,R)$, $R$-linearity gives $f(r) = f(r \cdot 1) = r f(1)$, so $f=f_{\Phi(f)}$.

:::

:::

::: {.pf-step #s2}

$\Phi$ is a ring homomorphism $\operatorname{Hom}_R(R,R)\to R^{\mathrm{op}}$.

::: pf-proof

We have $\Phi(f+g)=f(1)+g(1)$ and $\Phi(\operatorname{id}_R)=1$. For composition, $R$-linearity of $f$ gives
$$\Phi(f \circ g) = f(g(1)) = f(g(1)\cdot 1) = g(1) f(1) = f(1)\cdot_{\mathrm{op}} g(1) = \Phi(f)\cdot_{\mathrm{op}}\Phi(g),$$
where $x\cdot_{\mathrm{op}}y=yx$ is the multiplication of $R^{\mathrm{op}}$.

:::

:::

::: pf-qed

By steps [](#s1){.pf-ref} and [](#s2){.pf-ref}, $\Phi$ is a ring isomorphism $\operatorname{Hom}_R(R,R)\cong R^{\mathrm{op}}$. If $R$ is commutative, then $x\cdot_{\mathrm{op}}y=yx=xy$, so $R^{\mathrm{op}}=R$ as rings and $\operatorname{Hom}_R(R,R) \cong R$.

:::

:::

:::
