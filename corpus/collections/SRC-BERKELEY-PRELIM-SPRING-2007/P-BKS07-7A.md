---
schema: qual/card@1
id: P-BKS07-7A
kind: problem
title: A nonconstant entire function with $f(az+b)=f(z)$ forces $a$ to be a root of unity
classification:
  areas: [prelim]
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
Let $a$ and $b$ be complex numbers, and let $f \colon \CC \to \CC$ be a non-constant entire function such that $f(az + b) = f(z)$ for all $z \in \CC$. Prove that there is a positive integer $n$ such that $a^{n} = 1$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

If $a\ne1$, let $c=b/(1-a)$, the fixed point of $z\mapsto az+b$, and let $g(z)=f(z+c)$. Then $g(az)=g(z)$ for all $z$.

::: pf-proof

$g(az)=f(az+c)=f(az+ac+b)=f(a(z+c)+b)=f(z+c)=g(z)$, using $c=ac+b$.

:::

:::

::: {.pf-step #s2}

If $a\ne1$, then $a^n=1$ for some $n\ge1$.

::: pf-proof

Write $g(z)=\sum_{n\ge0}g_nz^n$. Comparing coefficients in $g(az)=g(z)$ gives $a^ng_n=g_n$ for every $n$. Since $f$ is not constant, $g$ is not constant, so $g_n\ne0$ for some $n\ge1$, and then $a^n=1$.

:::

:::

::: pf-qed

If $a=1$, take $n=1$. Otherwise, use step [](#s2){.pf-ref}.

:::

:::

:::
