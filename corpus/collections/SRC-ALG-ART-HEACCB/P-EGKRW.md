---
schema: qual/card@1
id: P-EGKRW
kind: problem
title: The ideal $(2,x)$ in $\ZZ[x]$ is not a direct sum of nontrivial cyclic modules
classification:
  areas:
  - algebra
  topics:
  - Free Modules
  - Ideals
  - Principal Ideal Domains
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-09
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---
::: {.problem}
Let $I = (2, x)$ be an ideal in $R = \ZZ[x]$, and show that $I$ is not a direct sum of nontrivial cyclic $R\dash$modules.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The ideal $I$ is torsionfree and has rank $1$ as an $R$-module.

::: pf-proof

The ring $R=\ZZ[x]$ is an integral domain and $I\subseteq R$, so $I$ is torsionfree. Let $K=\operatorname{Frac}(R)$. Since $I$ contains the nonzero element $2$, one has
$$
K\otimes_R I\cong K,
$$
so
$$
\operatorname{rank}_R I=\dim_K(K\otimes_RI)=1.
$$

:::

:::

::: {.pf-step #s2}

Every nonzero cyclic submodule of a torsionfree $R$-module is isomorphic to $R$.

::: pf-proof

If $C=Rv$ is nonzero and torsionfree, the map
$$
R\to C,\qquad r\mapsto rv
$$
is surjective. Its kernel is $\operatorname{Ann}(v)$. Torsionfreeness and $v\ne0$ imply $\operatorname{Ann}(v)=0$, so $C\cong R$.

:::

:::

::: {.pf-step #s3}

If $I$ were a direct sum of nontrivial cyclic modules, then in fact $I$ would be cyclic.

::: pf-proof

Suppose
$$
I\cong C_1\oplus\cdots\oplus C_t
$$
with each $C_i$ nonzero and cyclic. Each direct summand is torsionfree because $I$ is torsionfree, hence $C_i\cong R$ by step [](#s2){.pf-ref}. Therefore
$$
\operatorname{rank}_R I=t.
$$
By step [](#s1){.pf-ref} this rank is $1$, so $t=1$ and $I$ is cyclic.

:::

:::

::: {.pf-step #s4}

The ideal $I=(2,x)$ is not principal.

::: pf-proof

If $I=(f)$, then $f$ divides both $2$ and $x$ in the UFD $\ZZ[x]$. Any common divisor of $2$ and $x$ is a unit, so $(f)=R$. But $I$ is proper because
$$
R/I\cong\FF_2\ne0.
$$
This is a contradiction.

:::

:::

::: {.pf-step #s5}

Hence
$$
\boxed{I\text{ is not a direct sum of nontrivial cyclic }R\text{-modules}}.
$$

::: pf-proof

By step [](#s3){.pf-ref} such a decomposition would make $I$ cyclic, contradicting step [](#s4){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} is the required conclusion.

:::

:::

:::
