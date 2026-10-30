---
schema: qual/card@1
id: P-VUVYD
kind: problem
title: An entire function with polynomial real part is a polynomial
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
  - Cauchy-Riemann
  - Entire Functions
  - Polynomials
relations: []
review: draft
---

::: {.problem}
Let $f = u + iv$ be an entire function such that $\Re(f(x+iy))$ is polynomial in $x$ and $y$.
Show that $f(z)$ is polynomial in $z$.
:::

::: {.solution}
Write $f=u+iv$ with $u$ a polynomial in $x,y$ of total degree at most $d$.

::: pf

::: {.pf-step #deriv}
$f'(z)=u_x(x,y)-iu_y(x,y)$ for $z=x+iy$.

::: pf-proof
$f'=u_x+iv_x$, and the Cauchy–Riemann equation $v_x=-u_y$ gives the formula.
:::

:::

::: {.pf-step #vanish}
$f^{(d+1)}\equiv0$.

::: pf-proof
Apply step [](#deriv){.pf-ref} to the entire function $f'$, whose real part $u_x$ is again a polynomial, and repeat. By induction $f^{(k)}$ is a linear combination with constant coefficients of the partial derivatives of $u$ of order $k$. Every partial derivative of order $d+1$ of a polynomial of degree at most $d$ is zero.
:::

:::

::: {.pf-step #poly}
$f$ is a polynomial in $z$ of degree at most $d$.

::: pf-proof
$f$ is entire, so $f(z)=\sum_{k\ge0}\frac{f^{(k)}(0)}{k!}z^k$ on $\CC$. By step [](#vanish){.pf-ref}, $f^{(k)}(0)=0$ for every $k\ge d+1$.
:::

:::

::: pf-qed
Step [](#poly){.pf-ref} is the claim.
:::

:::

:::
