---
schema: qual/card@1
id: P-ZJFFS
kind: problem
title: Quadratic extensions in characteristic 0 are Galois; stacked quadratics need
  not be
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Field Extensions
  - Normal Subgroups
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
Take a quadratic extension of a field of characteristic 0. Is it Galois?
Take a degree 2 extension on top of that.
Does it have to be Galois over the base field?
What statement in group theory can you think of that reflects this?
:::

::: {.solution}

::: pf

::: pf-step

Every quadratic extension $K/F$ with $\operatorname{char}F=0$ is Galois.

::: pf-proof

Write $K=F(\alpha)$ with minimal polynomial $x^2+bx+c$. Its other root is $-b-\alpha\in K$, so $K$ is a splitting field over $F$ and $K/F$ is normal. In characteristic $0$ every irreducible polynomial is separable.

:::

:::

::: {.pf-step #tower}

A quadratic extension of a quadratic extension need not be Galois over the base: $\QQ\subset\QQ(\sqrt2)\subset L\coloneqq\QQ(\alpha)$ with $\alpha=\sqrt{1+\sqrt2}$ is a tower of quadratic extensions, and $L/\QQ$ is not Galois.

::: pf-proof

The norm of $1+\sqrt2$ from $\QQ(\sqrt2)$ to $\QQ$ is $1-2=-1$, which is not a square in $\QQ$, while the norm of a square is a square; so $1+\sqrt2$ is not a square in $\QQ(\sqrt2)$ and $[L:\QQ(\sqrt2)]=2$. The element $\alpha$ is a root of $x^4-2x^2-1$, since $\alpha^4=3+2\sqrt2=2\alpha^2+1$. This polynomial also has the roots $\pm\sqrt{1-\sqrt2}$, which are not real because $1-\sqrt2<0$. Since $L\subset\RR$, these roots are not in $L$, so $L/\QQ$ is not normal.

:::

:::

::: pf-step

The group-theoretic counterpart is that normality is not transitive: $\langle(12)(34)\rangle\normal V_4\normal A_4$, but $\langle(12)(34)\rangle$ is not normal in $A_4$.

::: pf-proof

$V_4$ is abelian, so each of its subgroups is normal in it, and $V_4$ is normal in $A_4$ as a union of conjugacy classes. Conjugating $(12)(34)$ by $(123)$ gives $(23)(14)\notin\langle(12)(34)\rangle$. Under the Galois correspondence for the Galois closure of the tower in step [](#tower){.pf-ref}, normal extensions correspond to normal subgroups, so the failure of transitivity of normality is the same phenomenon.

:::

:::

:::

:::
