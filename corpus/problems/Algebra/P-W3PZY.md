---
schema: qual/card@1
id: P-W3PZY
kind: problem
title: In characteristic $p$, an irreducible polynomial is $g(x^{p^e})$ with $g$ separable,
  and every root has multiplicity $p^e$
classification:
  areas:
  - algebra
  topics:
  - Separability
  - Characteristic
  - Irreducibility Criteria
relations: []
review: draft
---

::: {.problem}
Let $F$ be a field of characteristic $p>0$ and let $f\in F[x]$ be irreducible. Show that there are a unique integer $e\ge0$ and an irreducible separable polynomial $g\in F[x]$ such that
$$
f(x)=g(x^{p^e}),
$$
and that every root of $f$ in an algebraic closure has multiplicity $p^e$.
:::

::: {.solution}
Since $f$ is nonconstant, some positive exponent occurs in $f$. Choose $e\ge0$ maximal such that every exponent occurring in $f$ is divisible by $p^e$, and let $g\in F[x]$ be the polynomial with $f(x)=g(x^{p^e})$.

::: pf

::: pf-step

$g$ is irreducible.

::: pf-proof

If $g=uv$ with nonconstant $u,v\in F[x]$, then $f(x)=u(x^{p^e})v(x^{p^e})$ would be a factorization of $f$ into nonconstant factors.

:::

:::

::: {.pf-step #sep}

$g$ is separable.

::: pf-proof

By maximality of $e$, some exponent occurring in $g$ is not divisible by $p$, so $g'\ne0$. Since $g$ is irreducible and $\deg g'<\deg g$, $\gcd(g,g')=1$.

:::

:::

::: {.pf-step #mult}

If $f(x)=h(x^{p^c})$ for some $c\ge0$ and some separable $h\in F[x]$, then every root of $f$ in $\overline F$ has multiplicity exactly $p^c$.

::: pf-proof

Write $h(y)=a\prod_{i=1}^r(y-\beta_i)$ with distinct $\beta_i\in\overline F$, and choose $\alpha_i\in\overline F$ with $\alpha_i^{p^c}=\beta_i$. In characteristic $p$, $x^{p^c}-\beta_i=(x-\alpha_i)^{p^c}$, so
$$
f(x)=a\prod_{i=1}^r(x-\alpha_i)^{p^c},
$$
and the $\alpha_i$ are distinct because the $\beta_i$ are.

:::

:::

::: pf-qed

By steps [](#sep){.pf-ref} and [](#mult){.pf-ref}, every root of $f$ has multiplicity $p^e$. If also $f(x)=h(x^{p^c})$ with $h$ separable, step [](#mult){.pf-ref} gives $p^c=p^e$, so $c=e$; and then $h=g$, since $g(x^{p^e})$ determines the coefficients of $g$.

:::

:::

:::
