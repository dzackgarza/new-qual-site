---
schema: qual/card@1
id: P-CASP04E
kind: problem
title: "Points connected to infinity outside a compact set are not in its polynomial hull"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
Let $K$ be a compact subset of $\CC$ and $\hat{K}$ its polynomial hull, i.e. $$\hat{K} := \{z \in \CC : \abs{p(z)} \leq \sup_{w \in K} \abs{p(w)}, \text{ for every polynomial } p\}.$$ Show that if $z \in \CC \setminus K$ and there is a curve $\gamma \subset \CC_\infty \setminus K$ connecting $z$ to $\infty$, then $z \notin \hat{K}$.
:::

::: {.solution}

The argument is the card's own, by Runge's theorem in its pole-moving form; no retained set solves this exercise, and the sets searched are recorded in the audit trail.

Let $K\subset\CC$ be compact with polynomial hull $\widehat K$, let $z\in\CC\setminus K$, and suppose a curve $\gamma\subset\CC_{\infty}\setminus K$ joins $z$ to $\infty$; write $\Omega_{\infty}$ for the component of $\CC_{\infty}\setminus K$ containing $\infty$.

::: pf

::: {.pf-step #component}
$z\in\Omega_{\infty}$.

::: pf-proof
$\gamma$ is a connected subset of $\CC_{\infty}\setminus K$ containing both $z$ and $\infty$, so $z$ lies in the same component of $\CC_{\infty}\setminus K$ as $\infty$, namely $\Omega_{\infty}$.
:::

:::

::: {.pf-step #runge}
For every $\varepsilon>0$ there is a polynomial $q$ with $\sup_{w\in K}\abs{q(w)-1/(w-z)}<\varepsilon$.

::: pf-proof
$h(w)=1/(w-z)$ is holomorphic on $\CC\setminus\{z\}$, which is a neighbourhood of $K$ since $z\notin K$. Its only pole is $z$, which lies in $\Omega_{\infty}$ by step [](#component){.pf-ref}, the unbounded component of $\CC_{\infty}\setminus K$. Runge's theorem in the pole-moving form then says that a rational function whose poles all lie in the component of $\CC_{\infty}\setminus K$ containing $\infty$ can be approximated uniformly on $K$ by polynomials; hence such a $q$ exists.
:::

:::

::: {.pf-step #polynomial}
There is a polynomial $p$ with $p(z)=1$ and $\sup_{w\in K}\abs{p(w)}<1$.

::: pf-proof
Let $M=\max_{w\in K}\abs{w-z}$, which is finite and positive because $K$ is compact and $z\notin K$. Apply step [](#runge){.pf-ref} with $\varepsilon<1/M$ and put
$$
p(w)=1-(w-z)q(w),
$$
a polynomial. Then $p(z)=1$, and for $w\in K$
$$
\abs{p(w)}=\abs{w-z}\cdot\abs{\frac{1}{w-z}-q(w)}\le M\varepsilon<1 .
$$
So $\sup_{K}\abs{p}\le M\varepsilon<1=\abs{p(z)}$.
:::

:::

::: {.pf-step #not-in-hull}
$z\notin\widehat K$.

::: pf-proof
By step [](#polynomial){.pf-ref} there is a polynomial $p$ with $\abs{p(z)}=1>\sup_{w\in K}\abs{p(w)}$; the defining condition of the polynomial hull requires $\abs{p(z)}\le\sup_{K}\abs{p}$ for every polynomial $p$, and this $p$ violates it. Hence $z$ is not in $\widehat K$.
:::

:::

:::
:::
