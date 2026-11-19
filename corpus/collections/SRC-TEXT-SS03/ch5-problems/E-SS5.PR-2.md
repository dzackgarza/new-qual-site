---
schema: qual/card@1
id: E-SS5.PR-2
kind: problem
title: Infinite Blaschke products from sequences satisfying the Blaschke condition
classification:
  areas:
  - complex-analysis
  topics:
  - Blaschke Factors
  - Zeros
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into numbered steps for issue #2: the estimate (a), the identity for $1-b_{\alpha}$, the
    summability on closed discs, the standard product criterion, the zeros, and the bound $\abs{f}\le1$. No
    retained solution set covers this exercise (the collection retains the textbook, not a solutions manual),
    so the argument is the card's own; the identity for $1-b_{\alpha}$ was recomputed for this pass.
---

::: {.exercise}
In this problem, we discuss Blaschke products, which are bounded analogues in the disc of the Weierstrass products for entire functions.

(a) Show that for $0<\abs{\alpha}<1$ and $\abs{z}\leq r<1$, the inequality

$$
\abs{\frac{\alpha+\abs{\alpha}z}{(1-\overline{\alpha}z)\alpha}}
\leq \frac{1+r}{1-r}
$$

holds.

(b) Let $\{\alpha_n\}$ be a sequence in the unit disc such that $\alpha_n\neq 0$ for all $n$ and

$$
\sum_{n=1}^{\infty}(1-\abs{\alpha_n})<\infty.
$$

This condition holds when $\{\alpha_n\}$ are the zeros of a bounded holomorphic function on the unit disc, by Problem 1. Show that the product

$$
f(z)=\prod_{n=1}^{\infty}
\frac{\alpha_n-z}{1-\overline{\alpha_n}z}
\frac{\abs{\alpha_n}}{\alpha_n}
$$

converges uniformly for $\abs{z}\leq r<1$ and defines a holomorphic function on the unit disc with precisely the zeros $\alpha_n$.
Show also that $\abs{f(z)}\leq 1$.
:::

::: {.solution}
No retained solution set covers this exercise; the collection retains the textbook (`assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`) and no solutions manual, so the argument is the card's own. Throughout $0<\abs{\alpha}<1$, $\rho=\abs{\alpha}$, and
$$
b_{\alpha}(z)=\frac{\alpha-z}{1-\overline{\alpha}z}\cdot\frac{\abs{\alpha}}{\alpha},
$$
so that the product in part (b) has $n$-th factor $b_{\alpha_{n}}(z)$.

::: pf

::: {.pf-step #estimate}
(a) For $\abs{z}\le r<1$, $\abs{\dfrac{\alpha+\rho z}{(1-\overline{\alpha}z)\alpha}}\le\dfrac{1+r}{1-r}$.

::: pf-proof
Bound numerator and denominator separately on the circle $\abs{z}\le r$: $\abs{\alpha+\rho z}\le\rho+\rho\abs{z}=\rho(1+\abs{z})$, and $\abs{1-\overline{\alpha}z}\ge1-\abs{\alpha}\abs{z}\ge1-\rho r>0$. Hence
$$
\abs{\frac{\alpha+\rho z}{(1-\overline{\alpha}z)\alpha}}\le\frac{\rho(1+\abs{z})}{\rho(1-\rho\abs{z})}=\frac{1+\abs{z}}{1-\rho\abs{z}}\le\frac{1+r}{1-r},
$$
the last step because $\abs{z}\le r$ makes the function $(1+t)/(1-\rho t)$ increase in $t$ on $[0,r]$.
:::

:::

::: {.pf-step #identity}
$1-b_{\alpha}(z)=\dfrac{(1-\rho)(\alpha+\rho z)}{\alpha(1-\overline{\alpha}z)}$.

::: pf-proof
By definition $b_{\alpha}(z)=\frac{\rho(\alpha-z)}{\alpha(1-\overline{\alpha}z)}$, so
$$
1-b_{\alpha}(z)=\frac{\alpha(1-\overline{\alpha}z)-\rho(\alpha-z)}{\alpha(1-\overline{\alpha}z)}=\frac{\alpha-\alpha\overline{\alpha}z-\rho\alpha+\rho z}{\alpha(1-\overline{\alpha}z)} .
$$
Now $\alpha\overline{\alpha}=\rho^{2}$, so the numerator is $\alpha(1-\rho)-\rho^{2}z+\rho z=(1-\rho)\bigl(\alpha+\rho z\bigr)$, since $\rho^{2}z-\rho z=\rho z(\rho-1)=-(1-\rho)\rho z$. That is the stated identity.
:::

:::

::: {.pf-step #summable}
On $\abs{z}\le r$ one has $\abs{1-b_{\alpha_{n}}(z)}\le\dfrac{1+r}{1-r}\bigl(1-\abs{\alpha_{n}}\bigr)$, and the right-hand side is summable in $n$.

::: pf-proof
Take absolute values in step [](#identity){.pf-ref}: $\abs{1-b_{\alpha_{n}}(z)}=(1-\abs{\alpha_{n}})\abs{\frac{\alpha_{n}+\abs{\alpha_{n}}z}{\alpha_{n}(1-\overline{\alpha_{n}}z)}}$, and the modulus on the right is at most $\frac{1+r}{1-r}$ by step [](#estimate){.pf-ref}. The Blaschke condition $\sum_{n}(1-\abs{\alpha_{n}})<\infty$ then makes the majorant summable, uniformly in $z$ with $\abs{z}\le r$.
:::

:::

::: {.pf-step #factors}
Each $b_{\alpha}$ is holomorphic on $\DD$, vanishes only at $z=\alpha$, and has no pole in $\DD$.

::: pf-proof
The numerator $\alpha-z$ is entire and vanishes exactly at $\alpha$; the numerator $\rho$ is a nonzero constant. The denominator $1-\overline{\alpha}z$ vanishes only at $z=1/\overline{\alpha}$, whose modulus is $1/\rho>1$, so it is nonzero on $\DD$; hence $b_{\alpha}$ is holomorphic on $\DD$ and its only zero there is $\alpha$, of multiplicity one.
:::

:::

::: {.pf-step #convergence}
$\prod_{n}b_{\alpha_{n}}(z)$ converges uniformly on every closed disc $\abs{z}\le r<1$ to a holomorphic $f$ on $\DD$.

::: pf-proof
By steps [](#factors){.pf-ref} and [](#summable){.pf-ref}, each factor is holomorphic on $\DD$ and $\sum_{n}\abs{1-b_{\alpha_{n}}(z)}$ converges uniformly on $\abs{z}\le r$. The standard criterion for infinite products — uniform convergence of $\sum\abs{1-b_{n}}$ on a set makes $\prod b_{n}$ converge uniformly there, and the limit is holomorphic when the factors are and the convergence is uniform on compacta — applies on each closed disc, and $\DD$ is the union of the discs $\abs{z}\le r$ with $r<1$. So $f$ is holomorphic on $\DD$.
:::

:::

::: {.pf-step #zeros}
The zeros of $f$ are precisely the points $\alpha_{n}$, counted with multiplicity, and $\abs{f(z)}\le1$ on $\DD$.

::: pf-proof
At a point $z_{0}$ with $z_{0}\notin\{\alpha_{n}\}$ every factor is nonzero, and a uniformly convergent product of nonzero factors has nonzero value there: the tail is uniformly close to $1$ since $\sum\abs{1-b_{\alpha_{n}}}$ converges uniformly; so $f(z_{0})\ne0$. Conversely at $z_{0}=\alpha_{m}$ the single factor vanishes and all others are nonzero, so $f$ has a zero there of the multiplicity of $\alpha_{m}$ among the $\alpha_{n}$. For the bound, $\abs{1-\overline{\alpha}z}^{2}-\abs{\alpha-z}^{2}=(1-\abs{\alpha}^{2})(1-\abs{z}^{2})>0$ for $\abs{z}<1$, so $\abs{\frac{\alpha-z}{1-\overline{\alpha}z}}<1$ and $\abs{b_{\alpha}(z)}<1$; every partial product therefore has modulus at most $1$, and passing to the locally uniform limit gives $\abs{f(z)}\le1$. That is the product of part (b), holomorphic with exactly the zeros $\alpha_{n}$ and bounded by $1$.
:::

:::

:::
:::
