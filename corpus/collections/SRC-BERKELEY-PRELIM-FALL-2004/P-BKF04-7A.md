---
schema: qual/card@1
id: P-BKF04-7A
kind: problem
title: A disk self-map with $f(-\frac12)=0$ and $f(0)=\frac12$ has $f(\frac12)=\frac45$
classification:
  areas: [prelim]
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
Let $D$ be the open unit disk in $\CC$, and $f\colon D\to D$ a holomorphic function. Suppose that $f(-\frac12)=0$ and $f(0)=\frac12$. Prove that there is only one possible value for $f(\frac12)$, and find it.
:::

::: {.solution}

The argument is the card's own: conjugate $f$ by a disc automorphism to get a self-map of $\DD$ with a fixed point and a fixed origin, where the equality case of Schwarz's lemma applies. The answer $\frac45$ is unchanged; the route below replaces the earlier appeal to Schwarz's lemma at the wrong point.

::: pf

::: {.pf-step #automorphism}

$\phi(z)=\dfrac{z-\frac12}{1-\frac z2}$ is an automorphism of $\DD$ with $\phi\bigl(\tfrac12\bigr)=0$ and $\phi(0)=-\tfrac12$.

::: pf-proof

For $\abs{z}<1$ the denominator $1-z/2$ does not vanish and $\abs{\phi(z)}<1$: indeed $\abs{z-\frac12}^{2}<\abs{1-\frac z2}^{2}$ because the difference is $(1-\frac14)(1-\abs{z}^{2})>0$. The inverse is $\phi^{-1}(w)=\dfrac{w+\frac12}{1+\frac w2}$, of the same shape, so $\phi$ is a biholomorphism of $\DD$ onto itself. Substituting, $\phi(\frac12)=0$ and $\phi(0)=\frac{-1/2}{1}=-\frac12$.

:::

:::

::: {.pf-step #conjugate}

$k=\phi\circ f$ is holomorphic $\DD\to\DD$ with $k(0)=0$ and $k\bigl(-\tfrac12\bigr)=-\tfrac12$.

::: pf-proof

$f$ maps $\DD$ into $\DD$ and $\phi$ maps $\DD$ into $\DD$, so $k$ does too; $k$ is holomorphic as a composite. Then $k(0)=\phi\bigl(f(0)\bigr)=\phi\bigl(\tfrac12\bigr)=0$ using the hypothesis $f(0)=\frac12$, and $k\bigl(-\tfrac12\bigr)=\phi\bigl(f(-\tfrac12)\bigr)=\phi(0)=-\tfrac12$ using $f(-\frac12)=0$.

:::

:::

::: {.pf-step #schwarz}

$k$ is the identity.

::: pf-proof

Schwarz's lemma applies to $k$ because $k(0)=0$ and $k:\DD\to\DD$, giving $\abs{k(z)}\le\abs{z}$ on $\DD$. At $z=-\frac12$ we have $\abs{k(-\frac12)}=\abs{-\frac12}=\abs{-\frac12}$, so equality holds at a nonzero point, and the lemma's equality clause then forces $k(z)=\lambda z$ with $\abs{\lambda}=1$. Evaluating at $z=-\frac12$ gives $-\frac12=\lambda\cdot(-\frac12)$, hence $\lambda=1$ and $k=\mathrm{id}$.

:::

:::

::: {.pf-step #determined}

$f=\phi^{-1}$ is the only possibility, and $f\bigl(\tfrac12\bigr)=\tfrac45$.

::: pf-proof

$k=\phi\circ f=\mathrm{id}$ implies $f=\phi^{-1}$, that is
$$
f(z)=\frac{z+\frac12}{1+\frac z2},
$$
so no other value of $f(\frac12)$ is possible. Substituting $z=\frac12$,
$$
\boxed{f\Bigl(\frac12\Bigr)=\frac{\frac12+\frac12}{1+\frac14}=\frac{1}{5/4}=\frac45.}
$$

:::

:::

:::

:::
