---
schema: qual/card@1
id: P-GW3Y7
kind: problem
title: One solution of $-2e^z=z+3$ in the closed left half-plane by Rouché's theorem
classification:
  areas:
  - complex-analysis
  topics:
  - Rouché
  - Zeros
relations: []
review: draft
---

::: {.exercise}
Find the number of solutions in $\theset{\Re(z) \leq 0}$ of
$$
-2e^z = z+3
.$$
:::

::: {.hint}
Show $h(z) = z + 3 + 2e^z$ has one root in $\theset{ \Re(z) \leq 0}$.
:::

::: {.solution}
Write $p(z) \coloneqq z+3+2e^z$ and $F(z)\coloneqq z+3$; the solutions are the zeros of $p$. Let $D$ be the open disk $\abs{z+3}<2$.

::: pf

::: {.pf-step #confine}
Every zero of $p$ with $\Re z\le 0$ lies in $D$.

::: pf-proof
If $p(z)=0$ and $\Re z\le 0$, then $\abs{z+3}=\abs{2e^z}=2e^{\Re z}\le 2$. Equality would force $\Re z=0$, but every point with $\abs{z+3}\le 2$ has $\Re z\le -1$. So $\abs{z+3}<2$.
:::

:::

::: {.pf-step #rouche}
$p$ has exactly one zero in $D$, and $D\subseteq\theset{\Re z\le 0}$.

::: pf-proof
On $\abs{z+3}=2$ we have $\Re z\le -1$, so $\abs{p(z)-F(z)}=2e^{\Re z}\le 2e^{-1}<2=\abs{F(z)}$. By Rouché's theorem $p$ and $F$ have the same number of zeros in $D$, namely one. Every point of $D$ has $\Re z<-1$.
:::

:::

::: pf-step
The equation has $\boxed{1}$ solution in $\theset{\Re z\le 0}$.

::: pf-proof
Steps [](#confine){.pf-ref} and [](#rouche){.pf-ref}.
:::

:::

:::

:::

::: {.solution title="Alternative"}
Apply Rouché's theorem on the half-disk bounded by the segment $C_1=\theset{it \suchthat t\in[-R,R]}$ and the left semicircle $\abs z=R$, $\Re z\le 0$:

![figures/2021-07-29_20-39-31.png](../../assets/figures/2021-07-29_20-39-31.png)

With $p$ and $F$ as above, write $h(z)\coloneqq 2e^z = p(z)-F(z)$.

::: pf

::: pf-step
For $R>5$, $\abs{h}<\abs{F}$ on the boundary of the half-disk.

::: pf-proof
On $C_1$, $\abs{F(it)}=\abs{3+it}\ge 3>2=\abs{h(it)}$. On the semicircle, $\abs{h(z)}=2e^{\Re z}\le 2$ and $\abs{F(z)}\ge R-3>2$.
:::

:::

::: pf-step
$p$ has exactly $\boxed{1}$ zero with $\Re z\le 0$.

::: pf-proof
By Rouché's theorem $p$ has as many zeros in each half-disk as $F$, which has the single zero $-3$. No zero of $p$ lies on $C_1$, by the previous step, and every zero with $\Re z\le 0$ lies in the half-disk for $R$ large; letting $R\to\infty$ gives the count.
:::

:::

:::

:::
