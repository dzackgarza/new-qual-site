---
schema: qual/card@1
id: E-SS8.EX-17
kind: problem
title: The area integrals of $\abs{\psi_\alpha'}^2$ and $\abs{\psi_\alpha'}$ over the disc
classification:
  areas:
  - complex-analysis
  topics:
  - Blaschke Factors
  - Integrals
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
    Restructured as a Lamport proof of the two computations already on the card, both of which
    are correct: the first by the area formula for a disc automorphism, the second by the
    Poisson kernel and one elementary integral. Added: the explicit differentiation giving
    psi_alpha' = -(1-|alpha|^2)/(1-bar alpha z)^2, the rotation reduction to alpha = r >= 0, the
    evaluation of int_0^1 rho/(1-r^2 rho^2) d rho, and the expansion showing the limit at alpha
    = 0 is 1, which is the convention the statement refers to. The card's 'Poisson-kernel
    identity' is now derived from the real part of (1+tw)/(1-tw) rather than quoted. Not
    claimed: a retained solution set; the collection's provenance is the Stein--Shakarchi
    textbook.
---

::: {.exercise}
If $\psi_\alpha(z) = (\alpha - z)/(1 - \overline{\alpha} z)$ for $\abs{\alpha} < 1$, prove that
$$
\frac{1}{\pi} \iint_{\DD} \abs{\psi_\alpha'}^2\, dx\, dy = 1 \quad \text{and} \quad \frac{1}{\pi} \iint_{\DD} \abs{\psi_\alpha'}\, dx\, dy = \frac{1 - \abs{\alpha}^2}{\abs{\alpha}^2} \log\frac{1}{1 - \abs{\alpha}^2},
$$
where in the case $\alpha = 0$ the expression on the right is understood as the limit as $\abs{\alpha} \to 0$.

[Hint: The first integral can be evaluated without a calculation. For the second, use polar coordinates, and for each fixed $r$ use contour integration to evaluate the integral in $\theta$.]
:::

::: {.solution}
Throughout $\alpha \in \DD$, $r \coloneqq \abs{\alpha}$, $\psi_{\alpha}(z) = \frac{\alpha - z}{1 - \bar\alpha z}$ and $dx\,dy$ is area measure, so that $\int\int_{\DD}dx\,dy = \pi$. The exercise is Exercise 17 of Stein--Shakarchi, *Complex Analysis*, Chapter 8.

::: pf

::: {.pf-step #derivative}
$\psi_{\alpha}'(z) = -\frac{1 - \abs{\alpha}^{2}}{(1 - \bar\alpha z)^{2}}$, and $\psi_{\alpha}$ is an automorphism of $\DD$.

::: pf-proof
The quotient rule gives $\psi_{\alpha}'(z) = \frac{-(1 - \bar\alpha z) + (\alpha - z)\bar\alpha}{(1-\bar\alpha z)^{2}} = \frac{-1 + \abs{\alpha}^{2}}{(1-\bar\alpha z)^{2}}$, the $\bar\alpha z$ terms cancelling. That $\psi_{\alpha}$ maps $\DD$ biholomorphically to itself with inverse $\psi_{-\alpha}$ is the standard fact about disc automorphisms, checked directly by $\psi_{-\alpha}(\psi_{\alpha}(z)) = z$.

:::

:::

::: {.pf-step #area}
$\frac{1}{\pi}\iint_{\DD}\abs{\psi_{\alpha}'}^{2}dx\,dy = 1$.

::: pf-proof
The change of variables $w = \psi_{\alpha}(z)$ for the biholomorphism $\psi_{\alpha}$ has Jacobian $\abs{\psi_{\alpha}'}^{2}$ in the area element, so $\iint_{\DD}\abs{\psi_{\alpha}'}^{2}dx\\,dy = \iint_{\psi_{\alpha}(\DD)}du\\,dv = \operatorname{Area}(\DD) = \pi$; dividing by $\pi$ gives the assertion. This is the computation the hint refers to as needing no calculation.

:::

:::

::: {.pf-step #rotate}
For the second integral one may assume $\alpha = r \ge 0$, and then $\frac{1}{\pi}\iint_{\DD}\abs{\psi_{\alpha}'}dx\,dy = \frac{1-r^{2}}{\pi}\int_{0}^{1}\rho\\,d\rho\int_{0}^{2\pi}\frac{d\theta}{\abs{1 - r\rho e^{i\theta}}^{2}}$.

::: pf-proof
Composing with the rotation $z \mapsto e^{i\theta_{0}}z$, where $\alpha = re^{i\theta_{0}}$, carries $\psi_{\alpha}$ to $\psi_{r}$ and preserves both the disc and the area element, so the integral depends only on $r$. In polar coordinates $z = \rho e^{i\theta}$ one has $dx\\,dy = \rho\\,d\rho\\,d\theta$ and $\abs{1 - \bar\alpha z} = \abs{1 - r\rho e^{i\theta}}$ for $\alpha = r$, and $\abs{\psi_{\alpha}'} = \frac{1-r^{2}}{\abs{1-r\rho e^{i\theta}}^{2}}$ by step [](#derivative){.pf-ref}.

:::

:::

::: {.pf-step #poisson}
$\int_{0}^{2\pi}\frac{d\theta}{1 - 2t\cos\theta + t^{2}} = \frac{2\pi}{1-t^{2}}$ for $0 \le t < 1$.

::: pf-proof
With $t = r\rho \in [0,1)$ the denominator is $\abs{1 - te^{i\theta}}^{2} = (1-te^{i\theta})(1-te^{-i\theta})$, and $\frac{1-t^{2}}{1-2t\cos\theta+t^{2}} = \operatorname{Re}\frac{1+te^{i\theta}}{1-te^{i\theta}}$: indeed $\frac{1+tw}{1-tw} = 1 + \frac{2tw}{1-tw}$ for $w = e^{i\theta}$, and $\operatorname{Re}\frac{2te^{i\theta}}{1-te^{i\theta}} = \frac{2t\cos\theta - 2t^{2}}{1-2t\cos\theta+t^{2}}$, so adding $1$ and putting over the common denominator gives $\frac{1-t^{2}}{1-2t\cos\theta+t^{2}}$. Now $w \mapsto \frac{1+tw}{1-tw}$ is holomorphic on a neighbourhood of the closed unit disc, since $\abs{t} < 1$, so by the mean-value property its average over $\abs{w} = 1$ equals its value at $w = 0$, namely $1$; taking real parts, $\frac{1}{2\pi}\int_{0}^{2\pi}\frac{1-t^{2}}{1-2t\cos\theta+t^{2}}d\theta = 1$, which is the displayed identity after multiplying by $1-t^{2}$.

:::

:::

::: {.pf-step #evaluate}
$\frac{1}{\pi}\iint_{\DD}\abs{\psi_{\alpha}'}dx\,dy = \frac{1-r^{2}}{r^{2}}\log\frac{1}{1-r^{2}}$ for $r > 0$.

::: pf-proof
Substituting the identity of step [](#poisson){.pf-ref} with $t = r\rho$ into step [](#rotate){.pf-ref} gives $\frac{1-r^{2}}{\pi}\int_{0}^{1}\rho\cdot\frac{2\pi}{1-r^{2}\rho^{2}}d\rho = 2(1-r^{2})\int_{0}^{1}\frac{\rho\\,d\rho}{1-r^{2}\rho^{2}}$. With $u = r^{2}\rho^{2}$, $du = 2r^{2}\rho\\,d\rho$, the remaining integral is $\frac{1}{2r^{2}}\int_{0}^{r^{2}}\frac{du}{1-u} = -\frac{\log(1-r^{2})}{2r^{2}}$, so the whole expression is $2(1-r^{2})\bigl(-\frac{\log(1-r^{2})}{2r^{2}}\bigr) = \frac{1-r^{2}}{r^{2}}\log\frac{1}{1-r^{2}}$.

:::

:::

::: pf-step
The two identities hold: $\frac{1}{\pi}\iint_{\DD}\abs{\psi_{\alpha}'}^{2} = 1$, and $\frac{1}{\pi}\iint_{\DD}\abs{\psi_{\alpha}'} = \frac{1-\abs{\alpha}^{2}}{\abs{\alpha}^{2}}\log\frac{1}{1-\abs{\alpha}^{2}}$ for $\alpha \ne 0$, with limit $1$ as $\abs{\alpha} \to 0$.

::: pf-proof
The first is step [](#area){.pf-ref}, the second step [](#evaluate){.pf-ref} with $r = \abs{\alpha}$. For the excluded case $\alpha = 0$ one has $\psi_{0}(z) = -z$ and $\abs{\psi_{0}'} = 1$, so $\frac{1}{\pi}\iint_{\DD}\abs{\psi_{0}'} = 1$; and $\frac{1-r^{2}}{r^{2}}\log\frac{1}{1-r^{2}} = (1-r^{2})\bigl(1 + \frac{r^{2}}{2} + O(r^{4})\bigr) \to 1$ as $r \to 0$, by the expansion $-\log(1-r^{2}) = r^{2} + \frac{r^{4}}{2} + \cdots$, so the right-hand side has the limit the statement prescribes.

:::

:::

:::
:::
