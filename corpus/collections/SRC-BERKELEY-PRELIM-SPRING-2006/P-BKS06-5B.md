---
schema: qual/card@1
id: P-BKS06-5B
kind: problem
title: No continuous bijection from $(0,1)$ onto $[0,1]$
classification:
  areas: [prelim]
  topics:
  - Real Analysis
relations: []
review: draft
---

::: {.problem}
Prove that there exists no continuous bijection from $(0,1)$ to $[0,1]$. (Recall that a bijection is a map that is both one-to-one and onto.)
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Suppose $f\colon(0,1)\to[0,1]$ is a continuous bijection, and let $x\in(0,1)$ be the point with $f(x)=0$. Then $f((0,x))$ and $f((x,1))$ are disjoint.

::: pf-proof

The sets $(0,x)$ and $(x,1)$ are disjoint and $f$ is injective.

:::

:::

::: {.pf-step #s2}

There is $a>0$ with $(0,a)\subseteq f((0,x))$, and there is $b>0$ with $(0,b)\subseteq f((x,1))$.

::: pf-proof

The set $(0,x]$ is connected and has more than one point, so $f((0,x])$ is a connected subset of $[0,1]$ that contains $0$ and, by injectivity, a point $c>0$. So it contains $[0,c]$. Since $f$ is injective, $f((0,x))=f((0,x])-\{0\}\supseteq(0,c]$. The argument for $[x,1)$ is the same.

:::

:::

::: pf-qed

By step [](#s2){.pf-ref}, $f((0,x))$ and $f((x,1))$ both contain $(0,\min(a,b))$, which contradicts step [](#s1){.pf-ref}. So no such $f$ exists.

:::

:::

:::
