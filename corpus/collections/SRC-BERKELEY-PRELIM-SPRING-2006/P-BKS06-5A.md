---
schema: qual/card@1
id: P-BKS06-5A
kind: problem
title: Nonzero prime ideals that are not maximal in $\ZZ$, $\ZZ[x]$, $\RR[x]$, $\RR[x,y]$
classification:
  areas: [prelim]
  topics:
  - Abstract Algebra
relations: []
review: draft
---

::: {.problem}
Consider the following four commutative rings:

$$
\ZZ , \ZZ [ x ] , \RR [ x ] , \RR [ x , y ] .
$$

Which of these rings contains a nonzero prime ideal that is not a maximal ideal?
:::

::: {.solution}

The answer is $\ZZ[x]$ and $\RR[x,y]$.

::: pf

::: {.pf-step #s1}

In a principal ideal domain, every nonzero prime ideal is maximal. Hence $\ZZ$ and $\RR[x]$ have no nonzero prime ideal that is not maximal.

::: pf-proof

Let $(p)\ne0$ be prime and let $(p)\subseteq(q)$. Then $p=qr$ for some $r$, so $p\mid q$ or $p\mid r$. If $p\mid q$, then $(q)=(p)$. If $p\mid r$, write $r=ps$; then $p=qps$, so $qs=1$ and $(q)$ is the whole ring. Both $\ZZ$ and $\RR[x]$ are principal ideal domains, because each has a division algorithm.

:::

:::

::: {.pf-step #s2}

The ideal $(x)$ of $\ZZ[x]$ is a nonzero prime ideal that is not maximal.

::: pf-proof

Evaluation at $0$ gives $\ZZ[x]/(x)\cong\ZZ$. This is an integral domain that is not a field, so $(x)$ is prime and not maximal.

:::

:::

::: {.pf-step #s3}

The ideal $(x)$ of $\RR[x,y]$ is a nonzero prime ideal that is not maximal.

::: pf-proof

Setting $x=0$ gives $\RR[x,y]/(x)\cong\RR[y]$. This is an integral domain that is not a field, because $y$ has no inverse.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} to [](#s3){.pf-ref} give the answer.

:::

:::

:::
