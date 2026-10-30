---
schema: qual/card@1
id: P-BTUCW
kind: problem
title: Open mapping theorem for holomorphic functions
classification:
  areas:
  - complex-analysis
  topics:
  - Open Mapping Theorem
  - Argument Principle
  - Zeros
relations: []
review: draft
---

::: {.problem}
Prove the open mapping theorem for holomorphic functions: If $f$ is a non-constant holomorphic function on an open set $U$ in $\CC$, then $f(U)$ is also an open set.
:::

::: {.solution}
Nonconstant means nonconstant on each connected component of $U$; a function constant on a component maps it to a point, and then $f(U)$ need not be open. Fix $z_0\in U$ and put $w_0=f(z_0)$.

::: pf

::: {.pf-step #iso}
There is $r>0$ such that $\overline{D(z_0,r)}\subseteq U$ and $f(z)\neq w_0$ for $0<\abs{z-z_0}\le r$.

::: pf-proof
$f-w_0$ is holomorphic and not identically zero on the component of $U$ containing $z_0$, so its zeros are isolated.
:::

:::

::: {.pf-step #disk}
Let $\delta=\min_{\abs{z-z_0}=r}\abs{f(z)-w_0}$. Then $\delta>0$, and every $w$ with $\abs{w-w_0}<\delta$ is a value of $f$ on $D(z_0,r)$.

::: pf-proof
$\delta>0$ because the circle is compact and $f-w_0$ has no zero on it by step [](#iso){.pf-ref}. On the circle, $\abs{(f(z)-w)-(f(z)-w_0)}=\abs{w-w_0}<\delta\le\abs{f(z)-w_0}$. By Rouché's theorem, $f-w$ and $f-w_0$ have the same number of zeros in $D(z_0,r)$, and $f-w_0$ has at least one, at $z_0$.
:::

:::

::: pf-qed
By step [](#disk){.pf-ref}, $D(w_0,\delta)\subseteq f(U)$. Since $w_0\in f(U)$ was arbitrary, $f(U)$ is open.
:::

:::

:::
