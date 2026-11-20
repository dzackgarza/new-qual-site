---
schema: qual/card@1
id: E-SS1.EX-24
kind: problem
title: "Reversing orientation negates a contour integral"
classification:
  areas:
    - complex-analysis
  topics: [Contour Integration]
relations: []
review: draft
audit:
  - event: solution-written
    by: claude
    date: 2026-11-20
    note: >-
      Converted from prose to numbered steps under #2, four of them, each with its proof: the
      reparametrization of the reverse curve and its derivative, the definition of the contour
      integral along that parametrization, the substitution $u=a+b-t$ with both of its sign changes,
      and the conclusion. No retained solution set covers this collection, so the card says the
      argument is its own. No locator of any kind is written. Not checked: no certificate.
  - event: solution-written
    by: gpt-5.6-sol
    date: 2026-09-10
---

::: {.exercise}
Let $\gamma$ be a smooth curve in $\CC$ parametrized by $z(t) \colon [a, b] \to \CC$. Let $\gamma^-$ denote the curve with the same image as $\gamma$ but with the reverse orientation. Prove that for any continuous function $f$ on $\gamma$
$$
\int_{\gamma} f(z)\, dz = -\int_{\gamma^-} f(z)\, dz.
$$
:::

::: {.solution}
The argument is the card's own and uses only the definition of the contour integral and the chain rule.

::: pf

::: {.pf-step #parametrization}
If $\gamma$ is parametrized by $z\colon[a,b]\to\CC$, then $\gamma^-$ is parametrized by $z^-(t)=z(a+b-t)$ on $[a,b]$, and $(z^-)'(t)=-z'(a+b-t)$.

::: pf-proof
Reversing a curve means traversing the same point set in the opposite direction, which is exactly $t\mapsto a+b-t$ composed with $z$, and this is a continuous bijection of $[a,b]$ with $(a+b-a,a+b-b)=(b,a)$. The derivative is the chain rule applied to $z$ at $a+b-t$ times the derivative $-1$ of $a+b-t$.
:::

:::

::: {.pf-step #substitution}
$\displaystyle\int_{\gamma^-}f\,dz=-\int_a^bf(z(a+b-t))z'(a+b-t)\,dt$.

::: pf-proof
By the definition of the contour integral along a piecewise smooth parametrization, $\int_{\gamma^-}f\,dz=\int_a^bf(z^-(t))(z^-)'(t)\,dt$, and step [](#parametrization){.pf-ref} puts $z(a+b-t)$ for $z^-(t)$ and $-z'(a+b-t)$ for $(z^-)'(t)$; the minus sign is taken outside.
:::

:::

::: {.pf-step #change}
$\displaystyle\int_a^bf(z(a+b-t))z'(a+b-t)\,dt=\int_\gamma f\,dz$.

::: pf-proof
Substitute $u=a+b-t$, so $du=-dt$ and the limits $t=a$, $t=b$ become $u=b$, $u=a$; the two sign changes cancel and the integral becomes $\int_a^bf(z(u))z'(u)\,du$, which is $\int_\gamma f\,dz$ by the definition of the contour integral.
:::

:::

::: {.pf-step}
$\displaystyle\int_\gamma f(z)\,dz=-\int_{\gamma^-}f(z)\,dz$.

::: pf-proof
Steps [](#substitution){.pf-ref} and [](#change){.pf-ref} give $\int_{\gamma^-}f\,dz=-\int_\gamma f\,dz$, and multiplying by $-1$ is the assertion.
:::

:::

:::


:::
