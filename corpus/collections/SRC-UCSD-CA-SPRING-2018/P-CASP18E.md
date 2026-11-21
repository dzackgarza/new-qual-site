---
schema: qual/card@1
id: P-CASP18E
kind: problem
title: A bounded Blaschke product with zeros $\alpha_n=1-1/n^2$
classification:
  areas:
  - complex-analysis
  topics:
  - Blaschke Products
  - Bounded Holomorphic Functions
  - Zeros
relations: []
review: draft
---

::: {.problem}
Let $\alpha_n := 1 - \frac{1}{n^2}$.
Construct a function $f \in H(\DD)$ whose sequence of zeros (counting multiplicity) is precisely $\{\alpha_n\}$ and for which $\abs{f(z)} \leq 1$ in $\DD$.

Hint: $\varphi_\alpha(z) = \frac{\alpha - z}{1 - \bar\alpha z}$ has a simple zero at $z = \alpha$ and $\abs{\varphi_\alpha(z)} \leq 1$ in $\DD$.
:::

::: {.solution}

The argument is the card's own, with the convergence theorem for Blaschke products; no retained set solves this exercise, and the sets searched are recorded in the audit trail.

Let $\alpha_{n}=1-1/n^{2}$, so that $\alpha_{1}=0$ and $\alpha_{n}\in(0,1)$ for $n\ge2$.

::: pf

::: {.pf-step #blaschke-condition}
$\displaystyle\sum_{n\ge1}\big(1-\abs{\alpha_{n}}\big)=\sum_{n\ge1}\frac{1}{n^{2}}<\infty$.

::: pf-proof
$\abs{\alpha_{n}}=\alpha_{n}\in[0,1)$ for every $n$, so $1-\abs{\alpha_{n}}=1-\alpha_{n}=1/n^{2}$, and $\sum n^{-2}$ converges.
:::

:::

::: {.pf-step #factors}
For $\alpha\in\DD$ the function $\varphi_{\alpha}(z)=\dfrac{\alpha-z}{1-\bar\alpha z}$ is holomorphic on a neighbourhood of $\overline{\DD}$, has $\varphi_{\alpha}(\alpha)=0$ and no other zero in $\DD$, and satisfies $\abs{\varphi_{\alpha}(z)}\le1$ for $z\in\DD$ and $\abs{\varphi_{\alpha}(z)}=1$ for $\abs{z}=1$.

::: pf-proof
The denominator $1-\bar\alpha z$ does not vanish for $\abs{z}\le1$ when $\abs\alpha<1$, so $\varphi_{\alpha}$ is holomorphic there; its numerator vanishes only at $z=\alpha$. For $\abs{z}=1$,
$$
\abs{\varphi_{\alpha}(z)}=\frac{\abs{\alpha-z}}{\abs{1-\bar\alpha z}}=\frac{\abs{\alpha-z}}{\abs{z}\abs{\bar z-\bar\alpha}}=\frac{\abs{\alpha-z}}{\abs{\bar z-\bar\alpha}}=1,
$$
using $\abs{z}=1$ and $\abs{1-\bar\alpha z}=\abs{z}\abs{\bar z-\bar\alpha}$. Since $\varphi_{\alpha}$ has no pole in $\DD$, the maximum modulus principle applied on $\DD$ gives $\abs{\varphi_{\alpha}}\le1$ there.
:::

:::

::: {.pf-step #product}
The product $f(z)=z\displaystyle\prod_{n\ge2}\varphi_{\alpha_{n}}(z)$ converges locally uniformly on $\DD$ to a holomorphic function with $\abs{f}\le1$.

::: pf-proof
By step [](#blaschke-condition){.pf-ref} the zeros satisfy $\sum_{n}(1-\abs{\alpha_{n}})<\infty$, which is the convergence condition for the Blaschke product: the partial products converge uniformly on compact subsets of $\DD$ to a holomorphic function, and no factor vanishes identically. Each factor $\varphi_{\alpha_{n}}$ has modulus at most $1$ in $\DD$ by step [](#factors){.pf-ref}, so every partial product has modulus at most $1$ there, and the limit satisfies $\abs{f}\le1$ by continuity of $\abs{\cdot}$ and local uniform convergence.
:::

:::

::: {.pf-step #zeros}
The zeros of $f$, with multiplicity, are exactly the points $\alpha_{n}$.

::: pf-proof
The factor $z=\varphi_{0}$ vanishes simply at $\alpha_{1}=0$, and each $\varphi_{\alpha_{n}}$ vanishes simply at $\alpha_{n}$ and nowhere else in $\DD$ by step [](#factors){.pf-ref}. A locally uniformly convergent product whose factors are holomorphic and vanish at prescribed points has, on a compact $K\Subset\DD$, only the zeros contributed by the finitely many factors vanishing on $K$ once the tail is chosen with $\abs{\varphi_{\alpha_{n}}-1}<1/2$ on $K$: for such a tail the product is nowhere zero on $K$, since a product of factors each within $1/2$ of $1$ is nonzero. So the zeros of $f$ in $K$ are those of the finitely many retained factors, namely the $\alpha_{n}\in K$, each simple.
:::

:::

:::
:::
