---
schema: qual/card@1
id: P-TOPF20A
kind: problem
title: "No symmetric map from T^2 to S^1 fixing the diagonal"
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Degree
relations: []
review: draft
---

::: {.problem}
Show that there does not exist a continuous map $f : S^1 \times S^1 \to S^1$ that satisfies both of the following conditions:

- $f(x, x) = x$ for any $x \in S^1$;

- $f(x, y) = f(y, x)$ for any $x, y \in S^1$.
:::

::: {.solution}
<1>1. Let $a,b$ be the standard generators of $\pi_1(T^2)\cong\mathbb Z^2$, and let $f_*(a)=m$, $f_*(b)=n$ in $\pi_1(S^1)\cong\mathbb Z$.
::: {.proof}
Every homomorphism $\mathbb Z^2\to\mathbb Z$ is determined by these two integers.
:::

<1>2. Symmetry forces $m=n$.
::: {.proof}
Let $\tau(x,y)=(y,x)$. The condition $f\circ\tau=f$ gives $f_*\tau_*=f_*$. Since $\tau_*$ interchanges $a$ and $b$, their images agree.
:::

<1>3. On the diagonal $\Delta:S^1\to T^2$, $\Delta_*(1)=a+b$, hence
$$(f\circ\Delta)_*(1)=m+n=2m.$$
::: {.proof}
The diagonal winds once around each circle factor.
:::

<1>4. But $f(x,x)=x$ says $f\circ\Delta=\operatorname{id}_{S^1}$, whose induced map is multiplication by $1$.
::: {.proof}
This is exactly the first condition.
:::

<1>5. Thus $2m=1$, impossible in $\mathbb Z$. Hence no such map exists.
::: {.proof}
Combine <1>2--<1>4.
:::
:::
