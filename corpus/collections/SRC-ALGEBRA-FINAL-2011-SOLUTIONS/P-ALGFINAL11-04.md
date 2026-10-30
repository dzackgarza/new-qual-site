---
schema: qual/card@1
id: P-ALGFINAL11-04
kind: problem
title: Primitive roots of unity over finite fields
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $K$ be a finite field of cardinality $q$, let $n > 0$ be an integer relatively prime to $q$, and let $\zeta$ be a primitive $n$-th root of unity lying in some field $L \supset K$ with $[L : K] = m$.

(a) Show that $n$ divides $q^{m} - 1$.

(b) Show that $[K(\zeta) : K]$ is the order of $q$ in the group $(\ZZ/n\ZZ)^{*}$ (units in $\ZZ/n\ZZ$).
:::

::: {.solution}

::: pf

::: {.pf-step #s1}
(a) $n\mid q^m-1$.

::: pf-proof
As $\zeta$ is a primitive $n$-th root of unity, its order in $L^*$ is $n$. As $\cardinality{L}=q^m$, Lagrange's theorem gives $n\mid\cardinality{L^*}=q^m-1$.
:::

:::

::: {.pf-step #s2}
(b) Let $\mu$ be the order of $q$ in $(\ZZ/n\ZZ)^*$ and $d=[K(\zeta):K]$. Then $\mu\mid d$.

::: pf-proof
Step [](#s1){.pf-ref} applied to $L=K(\zeta)$ gives $n\mid q^d-1$, that is, $q^d\equiv1\pmod n$. Hence $\mu\mid d$.
:::

:::

::: {.pf-step #s3}
(b) $d=\mu$.

::: pf-proof
By step [](#s2){.pf-ref}, the finite field $K(\zeta)$ has a subfield $L'\supseteq K$ with $[L':K]=\mu$. The group $L'^*$ is cyclic of order $q^\mu-1$, which $n$ divides, so $L'^*$ contains $n$ distinct roots of $X^n-1$. These are all the roots of $X^n-1$ in $K(\zeta)$, so $\zeta\in L'$. Hence $L'=K(\zeta)$ and $d=\mu$.
:::

:::

::: pf-qed
Step [](#s1){.pf-ref} proves (a), and step [](#s3){.pf-ref} proves (b).
:::

:::

:::
