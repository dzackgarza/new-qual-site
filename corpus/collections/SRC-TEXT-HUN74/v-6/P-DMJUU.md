---
schema: qual/card@1
id: P-DMJUU
kind: problem
title: An irreducible polynomial whose degree is prime to the characteristic is separable
classification:
  areas:
  - algebra
  topics:
  - Separability
  - Irreducibility Criteria
  - Characteristic
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
If $f \in K[x]$ is irreducible of degree $m > 0$ and $\mathrm{char}(K)$ does not divide $m$, then $f$ is separable.
:::

::: {.solution}
Write $f(x) = \sum_{k=0}^m a_k x^k$ with $a_m \neq 0$, and let $\overline K$ be an algebraic closure of $K$.

::: pf

::: {.pf-step #s1}

$\deg f' = m-1$; in particular $f'\ne0$.

::: pf-proof

The formal derivative is
$$f'(x) = \sum_{k=1}^m k a_k x^{k-1},$$
with coefficient $(m \cdot 1_K) a_m$ of $x^{m-1}$. Since $\operatorname{char}(K) \nmid m$, $m \cdot 1_K \neq 0$, and since $K$ is a field and $a_m\ne0$, this coefficient is nonzero.

:::

:::

::: {.pf-step #s2}

$\gcd(f, f') = 1$ in $K[x]$.

::: pf-proof

The monic gcd $d$ divides $f$. Because $f$ is irreducible, $d$ is $1$ or $a_m^{-1} f$. The second case would give $f\mid f'$, which is impossible because $f'\ne0$ and $\deg f' = m - 1 < m$ by step [](#s1){.pf-ref}.

:::

:::

::: pf-qed

A root $\alpha\in\overline K$ of $f$ is a multiple root if and only if $f'(\alpha)=0$. By step [](#s2){.pf-ref} there are $u,v\in K[x]$ with $uf+vf'=1$; evaluating at a common root $\alpha$ of $f$ and $f'$ would give $0=1$. Hence $f$ has no multiple root in $\overline K$, so $f$ is separable.

:::

:::

:::
