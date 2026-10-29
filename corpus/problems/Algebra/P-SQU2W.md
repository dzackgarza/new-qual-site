---
schema: qual/card@1
id: P-SQU2W
kind: problem
title: Perfect fields
classification:
  areas:
  - algebra
  topics:
  - Separability
  - Fields
  - Counterexamples
relations: []
review: draft
---

::: {.problem}
What is a perfect field, why is perfection important, and what is an example of a nonperfect field?
:::

::: {.solution}

A field $F$ is perfect if every algebraic extension of $F$ is separable; equivalently, every irreducible polynomial in $F[x]$ is separable. An irreducible $f\in F[x]$ is inseparable exactly when $\gcd(f,f')\neq1$, that is, exactly when $f'=0$.

::: pf

::: pf-step

Every field of characteristic $0$ is perfect.

::: pf-proof

In characteristic $0$ a nonconstant $f$ has $f'\neq0$.

:::

:::

::: pf-step

If $\operatorname{char}F=p>0$, then $F$ is perfect if and only if the Frobenius map $x\mapsto x^p$ is surjective, that is, $F^p=F$.

::: pf-proof

An irreducible $f$ with $f'=0$ has the form $f(x)=\sum a_ix^{pi}$. If $F^p=F$, write $a_i=b_i^p$; then $f=\bigl(\sum b_ix^i\bigr)^p$ is not irreducible, so every irreducible polynomial is separable. If $a\in F\setminus F^p$, then $x^p-a=(x-\alpha)^p$ over a splitting field, where $\alpha^p=a$; any monic factor in $F[x]$ is $(x-\alpha)^k$ with $1\le k\le p$, and its coefficient $-k\alpha$ lies in $F$, so $k<p$ would give $\alpha\in F$. Hence $x^p-a$ is irreducible with derivative $0$, and $F$ is not perfect.

:::

:::

::: pf-step

$F=\FF_p(t)$ is not perfect.

::: pf-proof

The element $t$ is not a $p$th power: if $t=(g/h)^p$ with $g,h\in\FF_p[t]$, then $th^p=g^p$, and the degrees $1+p\deg h$ and $p\deg g$ differ modulo $p$. So $x^p-t\in F[x]$ is irreducible and inseparable.

:::

:::

::: pf-qed

Perfection matters because over a perfect field every finite extension is separable, so every finite normal extension is Galois and the fundamental theorem of Galois theory applies without separability hypotheses; every finite field and every algebraically closed field is perfect.

:::

:::

:::
