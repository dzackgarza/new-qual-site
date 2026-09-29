---
schema: qual/card@1
id: P-AGHOLDIFFDIM
kind: problem
title: Holomorphic differentials on a Riemann surface of genus $g$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Differentials
  - Riemann Surfaces
  - Genus
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the Harvard sample qualifying-exam algebraic-geometry PDF; this is Wodzicki's question following the request to state Riemann--Roch.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
Compute the dimension of the space of holomorphic differentials on a Riemann surface of genus $g$.
:::

::: {.solution}
Let $X$ be a compact Riemann surface of genus $g$, and let $K$ denote a canonical divisor.  The holomorphic differentials are the global sections
\[
H^0(X,\Omega_X^1)=H^0(X,\mathcal O_X(K)).
\]

::: pf

::: {.pf-step #riemann-roch-zero-divisor}
Riemann--Roch for the zero divisor says
\[
\ell(0)-\ell(K)=1-g.
\]

::: pf-proof
Riemann--Roch states that for every divisor $D$,
\[
\ell(D)-\ell(K-D)=\deg D+1-g.
\]
Taking $D=0$ gives
\[
\ell(0)-\ell(K)=1-g.
\]
:::

:::

::: {.pf-step #l0-equals-one}
One has
\[
\ell(0)=1.
\]

::: pf-proof
A section of $\mathcal O_X$ is a holomorphic function on the compact connected Riemann surface $X$.  By the maximum principle every such function is constant.  Hence
\[
H^0(X,\mathcal O_X)=\mathbb C
\]
and $\ell(0)=1$.
:::

:::

::: {.pf-step #lk-equals-g}
Therefore
\[
\ell(K)=g.
\]

::: pf-proof
Substitute step [](#l0-equals-one){.pf-ref} into step [](#riemann-roch-zero-divisor){.pf-ref}:
\[
1-\ell(K)=1-g,
\]
so
\[
\ell(K)=g.
\]
:::

:::

::: {.pf-step #holomorphic-diff-dimension}
Thus
\[
\boxed{
\dim_{\mathbb C}H^0(X,\Omega_X^1)=g.
}
\]

::: pf-proof
The line bundle $\mathcal O_X(K)$ is the holomorphic cotangent bundle $\Omega_X^1$, so its global sections are precisely the holomorphic differentials.  Apply step [](#lk-equals-g){.pf-ref}.
:::

:::

::: pf-qed
Step [](#holomorphic-diff-dimension){.pf-ref} is the required dimension.
:::

:::
:::
