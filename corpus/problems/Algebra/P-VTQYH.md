---
schema: qual/card@1
id: P-VTQYH
kind: problem
title: An irreducible in $\FF_p[x]$ divides $x^{p^n}-x$ iff its degree divides $n$
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
  - Irreducibility Criteria
  - Polynomials
relations: []
review: draft
---

::: {.problem}
Let $\pi(x)\in\FF_p[x]$ be irreducible of degree $d$. Prove
$$
\pi(x)\mid x^{p^n}-x
\iff
d\mid n.
$$
:::

::: {.solution}
Let $\alpha$ be a root of $\pi$ in an algebraic closure $\overline{\FF}_p$, and let $\FF_{p^m}$ denote the unique subfield of $\overline{\FF}_p$ of order $p^m$. Since $\pi$ is irreducible of degree $d$, $\FF_p(\alpha)=\FF_{p^d}$.

::: pf

::: {.pf-step #root}

$\pi(x)\mid x^{p^n}-x$ if and only if $\alpha^{p^n}=\alpha$.

::: pf-proof

$\pi$ is, up to a unit, the minimal polynomial of $\alpha$ over $\FF_p$, so it divides a polynomial over $\FF_p$ exactly when $\alpha$ is a root of that polynomial.

:::

:::

::: {.pf-step #subfield}

$\alpha^{p^n}=\alpha$ if and only if $\FF_{p^d}\subseteq\FF_{p^n}$.

::: pf-proof

The roots of $x^{p^n}-x$ in $\overline{\FF}_p$ are exactly the elements of $\FF_{p^n}$, and $\alpha\in\FF_{p^n}$ exactly when $\FF_p(\alpha)=\FF_{p^d}\subseteq\FF_{p^n}$.

:::

:::

::: pf-qed

Subfields of finite fields satisfy $\FF_{p^d}\subseteq\FF_{p^n}\iff d\mid n$. Combine with steps [](#root){.pf-ref} and [](#subfield){.pf-ref}.

:::

:::

:::
