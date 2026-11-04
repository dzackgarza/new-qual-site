---
schema: qual/card@1
id: E-SS9.PR-3
kind: problem
title: Inversion of an elliptic integral by the Weierstrass function
classification:
  areas:
  - complex-analysis
  topics:
  - Elliptic Functions
  - Elliptic Integrals
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-01
  note: >-
    Statement compared with Stein--Shakarchi, *Complex Analysis*, Chapter 9, §4, problem 3, read
    from `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`. The card matches the print; the
    card's remark already records that the identity is local, which the solution confirms. No
    correction is claimed.
- event: solution-written
  by: claude
  date: 2026-11-01
  note: >-
    Proved: with $G(u)^2=4u^3-g_2u-g_3$ and a branch of $\sqrt G$ on the simply connected $\Omega$,
    the derivative of $I(\wp(z+\alpha))$ is $\pm1$ by the differential equation
    $\wp'^2=4\wp^3-g_2\wp-g_3$; the sign is adjusted with the evenness of $\wp$ by using
    $\wp(\alpha-z)$, and $\alpha$ is then chosen so that the value at one point matches, giving
    $I(\wp(z+\alpha))=z$ on a neighbourhood. The two obstructions to a global statement (the branch
    of the square root and the evenness of $\wp$) are stated. Nothing is left in outline.
---

::: {.exercise}
Let $\Omega$ be a simply connected domain excluding the three roots of $4z^3-g_2z-g_3$. Fix $\omega_0\in\Omega$ and define
$$
I(\omega)=\int_{\omega_0}^{\omega}
\frac{dz}{\sqrt{4z^3-g_2z-g_3}},\qquad \omega\in\Omega.
$$
Show that an inverse of $I$ is given by $\wp(z+\alpha)$ for some constant $\alpha$; that is, $I(\wp(z+\alpha))=z$ for an appropriate $\alpha$.
:::

::: {.hint}
Show that $\bigl(I(\wp(z+\alpha))\bigr)'=\pm1$ and use that $\wp$ is even.
:::

::: {.remark}
The inverse identity is local: it holds on a neighborhood where $\wp(z+\alpha)$ takes values in $\Omega$ and the chosen branch of the square root gives the required sign. The statement does not specify a global domain for the inverse.
:::

::: {.solution}

Let $\Omega$ be simply connected and contain none of the three roots of $4z^3-g_2z-g_3$, fix $\omega_0\in\Omega$, and let
$$
I(\omega)=\int_{\omega_0}^{\omega}\frac{dz}{\sqrt{4z^3-g_2z-g_3}}
$$
with a branch of the square root fixed on $\Omega$; the path of integration stays in $\Omega$, so $I$ is holomorphic on $\Omega$ and $I'(\omega)=1/\sqrt{4\omega^3-g_2\omega-g_3}$. Recall $\wp'^2=4\wp^3-g_2\wp-g_3$ and that $\wp$ is even.

::: pf

::: {.pf-step #s1}

Let $\alpha\in\CC$ and let $U$ be a disc on which $z\mapsto\wp(z+\alpha)$ takes values in $\Omega$ and $\wp'$ does not vanish. Then $(I\circ\wp(\cdot+\alpha))'(z)=\pm1$ on $U$, with constant sign.

::: pf-proof

On $U$ the composite $I(\wp(z+\alpha))$ is holomorphic, and by the chain rule
$$
\bigl(I(\wp(z+\alpha))\bigr)'=\frac{\wp'(z+\alpha)}{\sqrt{4\wp(z+\alpha)^3-g_2\wp(z+\alpha)-g_3}} .
$$
By the differential equation $\wp'^2=4\wp^3-g_2\wp-g_3$ the denominator equals $\pm\wp'(z+\alpha)$, and since $\wp'\ne0$ on the connected set $U$ and the branch of the square root is fixed, the sign is constant. Hence the derivative equals $\sigma\in\{\pm1\}$ on $U$.

:::

:::

::: {.pf-step #s2}

The sign can be made $+1$ by using $\wp(\cdot+\alpha)$ or $\wp(\alpha-\cdot)$.

::: pf-proof

Since $\wp$ is even, $\wp(\alpha-z)=\wp(z-\alpha)$. With the constant sign $\sigma$ of step [](#s1){.pf-ref},
$$
\bigl(I(\wp(\alpha-z))\bigr)'=-\frac{\wp'(\alpha-z)}{\sqrt{4\wp(\alpha-z)^3-g_2\wp(\alpha-z)-g_3}}=-\sigma,
$$
the factor $-1$ coming from $\frac{d}{dz}(\alpha-z)=-1$ and the remaining quotient being the same expression as in step [](#s1){.pf-ref}, evaluated at the point $\alpha-z$. So the two maps $z\mapsto\wp(z+\alpha)$ and $z\mapsto\wp(\alpha-z)$ have derivatives $\sigma$ and $-\sigma$, and exactly one of them has derivative $+1$. Replacing $\alpha$ by $-\alpha$ exchanges them, so we may assume $\bigl(I(\wp(z+\alpha))\bigr)'=1$ on $U$.

:::

:::

::: {.pf-step #s3}

Choosing $\alpha$ so that the value matches at one point, $I(\wp(z+\alpha))=z$ on $U$.

::: pf-proof

With the sign $+1$ of step [](#s2){.pf-ref}, $I(\wp(z+\alpha))-z$ is holomorphic on $U$ with derivative $0$, hence constant there; call the constant $\beta$. Then for every $z\in U$
$$
I\bigl(\wp(z+\alpha)\bigr)=z+\beta .
$$
Put $\alpha'=\alpha-\beta$ and $w=z+\beta$. Since $\wp$ is a function of its argument, $\wp(z+\alpha)=\wp(w+\alpha')$, and the displayed identity becomes $I(\wp(w+\alpha'))=w$ for the corresponding $w$. Hence, on that neighbourhood, $I$ and $w\mapsto\wp(w+\alpha')$ are inverse to each other, which is the assertion with $\alpha'$ in place of $\alpha$.

:::

:::

::: {.pf-step #s4}

The identity is local; no global inverse is asserted.

::: pf-proof

Two obstructions prevent a global statement. First, the branch of $\sqrt{4\omega^3-g_2\omega-g_3}$ exists only because $\Omega$ is simply connected and avoids the roots; the inverse image of $\Omega$ under $\wp$ need not be connected. Second, $\wp$ is even and doubly periodic, so it is far from injective on $\CC$: on each of the two sheets $\wp(z+\alpha)$ and $\wp(\alpha-z)$ meet, and any inverse can only be given on a disc where $\wp$ is injective. This is exactly the content of the card's remark, and the argument above proves the local statement and nothing more.

:::

:::

:::

:::
