---
schema: qual/card@1
id: P-CPB5V
kind: problem
title: Unique halves and centrality in a simple rng without zero-divisors or $2$-torsion
classification:
  areas:
  - algebra
  topics:
  - Rings
  - Ideals
  - Semisimplicity
relations: []
review: draft
---

::: {.problem}
Let $R$ be a simple rng (a nonzero ring which is not assume to have a 1, whose only two-sided ideals are $(0)$ and $R$) satisfying the following two conditions:

i. $R$ has no zero divisors, and
ii. If $x\in R$ with $x\neq 0$ then $2x\neq 0$, where $2x\coloneqq x+x$.

Prove the following:

a.
For each $x\in R$ there is one and only one element $y\in R$ such that $x = 2y$.

b.
Suppose $x,y\in R$ such that $x\neq 0$ and $2(xy) = x$, then $yz = zy$ for all $z\in R$.

> You can get partial credit for (b) by showing it in the case $R$ has a 1.

:::

::: {.warnings}
A general opinion is that this is not a great qual problem! 
Possibly worth skipping.
:::


::: {.concept}
\envlist

- $R$ has no left zero divisors iff $R$ has the left cancellation property: $xa=xb \implies a=b$.
- $R$ has no right zero divisors iff $R$ has the right cancellation property: $ax=bx \implies a=b$.
:::

::: {.solution}

The argument is the card's own, written out; the card is an examination problem and no published solution is retained for it. Call $R$ left cancellative when $xw=0$ with $x\neq0$ forces $w=0$; a ring without zero divisors is left and right cancellative.

::: pf

::: {.pf-step #ideal}
$2R=\theset{2y\st y\in R}$ is a nonzero two-sided ideal of $R$.

::: pf-proof
It is an additive subgroup: $2y-2y'=2(y-y')\in2R$, and $2\cdot0=0\in2R$. It is a right ideal: $(2y)r=2(yr)\in2R$ by distributivity. It is a left ideal: $r(2y)=r(y+y)=ry+ry=2(ry)\in2R$. It is nonzero: $R\neq0$ gives $a\neq0$, and then $2a\neq0$ by hypothesis (ii), so $0\neq2a\in2R$.
:::

:::

::: {.pf-step #existence}
For every $x\in R$ there is $y\in R$ with $x=2y$.

::: pf-proof
By step [](#ideal){.pf-ref} the ideal $2R$ is nonzero, and $R$ is simple, so $2R=R$; hence $x\in2R$.
:::

:::

::: {.pf-step #uniqueness}
Such a $y$ is unique.

::: pf-proof
If $2y_{1}=2y_{2}$ then $0=2y_{1}-2y_{2}=2(y_{1}-y_{2})$, so $y_{1}-y_{2}=0$ by the contrapositive of hypothesis (ii).
:::

:::

::: {.pf-step #a}
For each $x\in R$ there is exactly one $y$ with $x=2y$.

::: pf-proof
Steps [](#existence){.pf-ref} and [](#uniqueness){.pf-ref}.
:::

:::

::: {.pf-step #half}
If $x\neq0$ and $2(xy)=x$, then $2(yz)=z$ for every $z\in R$.

::: pf-proof
$2(xy)=x$ means $xy+xy=x$. Multiplying on the right by $z$ and using distributivity,
$$
0=(xy+xy-x)z=xyz+xyz-xz=x(yz+yz-z).
$$
Since $x\neq0$ and $R$ has no zero divisors, left cancellation gives $yz+yz-z=0$, that is $2(yz)=z$.
:::

:::

::: {.pf-step #half2}
Under the same hypothesis, if $z\neq0$ then $2(zy)=z$.

::: pf-proof
Multiply $yz+yz=z$ on the left by $z$ and use associativity:
$$
zyz+zyz=zz,\qquad\text{that is}\qquad (zy+zy-z)z=0 .
$$
Since $z\neq0$ and $R$ has no zero divisors, right cancellation gives $zy+zy-z=0$, that is $2(zy)=z$.
:::

:::

::: {.pf-step #b}
If $x\neq0$ and $2(xy)=x$, then $yz=zy$ for every $z\in R$.

::: pf-proof
If $z=0$ then $yz=0=zy$. Otherwise step [](#half){.pf-ref} gives $2(yz)=z$ and step [](#half2){.pf-ref} gives $2(zy)=z$, so $2(yz)-2(zy)=0$, that is $2(yz-zy)=0$, and hypothesis (ii) gives $yz-zy=0$.
:::

:::

::: {.pf-step #unital}
If $R$ happens to have an identity, the same conclusion follows directly: $x(2y-1)=0$ with $x\neq0$ gives $2y=1$, and then $2(yz)=z(2y)=z\cdot1=z=1\cdot z=(2y)z=2(zy)$, so $yz=zy$.

::: pf-proof
$2(xy)=x$ reads $x(2y)-x=0$, that is $x(2y-1)=0$, and left cancellation gives $2y-1=0$. Then for any $z$, $2(yz)=(2y)z=1\cdot z=z$ and $2(zy)=z(2y)=z\cdot1=z$, so $2(yz-zy)=0$ and hypothesis (ii) concludes. This is the special case the problem offers for partial credit; the general case is step [](#b){.pf-ref}, which uses cancellation by $z$ instead of an identity.
:::

:::

:::

:::
