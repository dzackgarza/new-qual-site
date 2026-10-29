---
schema: qual/card@1
id: P-AA27R
kind: problem
title: Irreducibility of $(x^p-1)/(x-1)$ over $\QQ$
classification:
  areas:
  - algebra
  topics:
  - Irreducibility Criteria
  - Roots of Unity
  - Polynomials
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
Why is $\Phi_p(x) = \frac{x^p - 1}{x - 1} = x^{p-1} + x^{p-2} + \cdots + x + 1$ irreducible over $\QQ$ for $p$ prime?
:::

::: {.solution}
Set
$$
g(y)\coloneqq\Phi_p(y+1)=\frac{(y+1)^p-1}{y}
=\sum_{m=1}^p\binom pm y^{m-1}.
$$

::: pf

::: {.pf-step #eisenstein}

$g(y)$ is irreducible over $\QQ$.

::: pf-proof

Its leading coefficient is $\binom pp=1$. For $1\le m\le p-1$, the prime $p$ divides $\binom pm$, and the constant term is $\binom p1=p$, which is not divisible by $p^2$. Thus $g$ is Eisenstein at $p$.

:::

:::

::: pf-step

$\Phi_p(x)$ is irreducible over $\QQ$.

::: pf-proof

The substitution $x\mapsto y+1$ induces a ring automorphism of $\QQ[x]$ that preserves degree, so a factorization $\Phi_p=fh$ into nonconstant factors would give the factorization $g(y)=f(y+1)h(y+1)$ into nonconstant factors, contradicting step [](#eisenstein){.pf-ref}.

:::

:::

:::

:::
