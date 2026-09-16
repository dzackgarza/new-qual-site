---
schema: qual/card@1
id: FF-HK72Z
kind: fact
title: Descartes' rule of signs
prompts:
- State Descartes' rule of signs.
classification:
  areas:
  - algebra
  topics:
  - Polynomials
relations: []
review: draft
---

::: {.fact}
Let $p\in\RR[x]$ be a nonzero polynomial, and let $V(p)$ be the number of sign changes in the sequence of its nonzero coefficients, listed in order of degree.
The number $r^+$ of positive real roots of $p$, counted with multiplicity, satisfies
$$
r^+\le V(p)\qquad\text{and}\qquad V(p)-r^+\in2\ZZ.
$$
The negative real roots of $p$ are the negatives of the positive real roots of $p(-x)$, so their number $r^-$, counted with multiplicity, satisfies $r^-\le V(p(-x))$ and $V(p(-x))-r^-\in2\ZZ$.

Consequently, if $p(0)\ne0$ and $\deg p=d$, then $p$ has at least $d-V(p)-V(p(-x))$ nonreal complex roots, counted with multiplicity.
:::

::: {.example}
Let $f(x)=x^3+x^2-x-1$.
Its coefficient signs are $+,+,-,-$, so $V(f)=1$ and $f$ has exactly one positive root.
The polynomial $f(-x)=-x^3+x^2+x-1$ has signs $-,+,+,-$, so $V(f(-x))=2$ and $f$ has $2$ or $0$ negative roots; in fact $f=(x-1)(x+1)^2$ has the negative root $-1$ with multiplicity $2$.
:::

::: {.example}
Let $g(x)=x^3-1$.
Then $V(g)=1$, so $g$ has exactly one positive root, and $g(-x)=-x^3-1$ has $V(g(-x))=0$, so $g$ has no negative root.
Hence $g$ has at least $3-1-0=2$ nonreal roots, so exactly $2$.
:::
