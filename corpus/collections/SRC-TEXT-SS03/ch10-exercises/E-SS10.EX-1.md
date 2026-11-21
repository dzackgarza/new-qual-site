---
schema: qual/card@1
id: E-SS10.EX-1
kind: problem
title: A theta-quotient identity for $\wp_\tau$
classification:
  areas:
  - complex-analysis
  topics:
  - Theta Functions
  - Elliptic Functions
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
  note: 'Repaired the published erratum: "first two derivatives" should read "first three derivatives".'
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Restructured into a structured proof under #2. Re-checked the expansion by multiplying it out: with
    $Theta=aw+\tfrac b2w^2+\tfrac c6w^3+\cdots$, the quotient $Theta'/Theta$ is
    $1/w+b/(2a)+(c/(3a)-b^2/(4a^2))w+\cdots$, and differentiating with a sign change gives
    $H=w^{-2}+(b^2/(4a^2)-c/(3a))+O(w)$, so $c_tau$ is as displayed; $\wp_tau(w)=w^{-2}+O(w^2)$ has no
    constant term, so the constants compare directly. Also checked: $H=-(Theta'/Theta)'$ by the
    quotient rule; the periods of $H$ follow because the multiplier contributes an affine function of
    $z$; the zeros of $Theta$ lie on $1/2+tau/2$ modulo the lattice; and the difference is entire
    elliptic, hence constant by Liouville. Added: the quotient-rule identity, the removal of the
    singularities argument in full, and the sentence explaining why the constant needs the third
    derivative, which is the point of the card's remark. No defect found in the statement beyond the
    recorded discrepancy with the source's 'first two derivatives'.
---

::: {.exercise}
Prove that
$$
\frac{(\Theta'(z \thetaseparator \tau))^2 - \Theta(z \thetaseparator \tau)\, \Theta''(z \thetaseparator \tau)}{\Theta(z \thetaseparator \tau)^2} = \wp_\tau(z - 1/2 - \tau/2) + c_\tau,
$$
where $c_\tau$ can be expressed in terms of the first three derivatives of $\Theta(z \thetaseparator \tau)$, with respect to $z$, at $z = 1/2 + \tau/2$. Compare this formula with the result in Exercise 5 in the previous chapter.
:::

::: {.remark}
The source says "the first two derivatives". The constant term of the Laurent expansion at $z_0 = 1/2 + \tau/2$ involves $\Theta'''(z_0 \thetaseparator \tau)$, which the relation $\Theta(z_0 - w \thetaseparator \tau) = -e^{2\pi i w}\Theta(z_0 + w \thetaseparator \tau)$ does not eliminate; that relation gives only $\Theta''(z_0 \thetaseparator \tau) = -2\pi i\,\Theta'(z_0 \thetaseparator \tau)$.
:::

::: {.solution}
No retained solution set covers this exercise, so the argument is the card's own: identify the left-hand side as $-\bigl(\Theta'/\Theta\bigr)'$, compute its principal part at the zeros of $\Theta$, and compare with $\wp_\tau$. Put $z_0=\tfrac12+\tfrac\tau2$ and
$$
H(z)=\frac{(\Theta'(z\thetaseparator\tau))^2-\Theta(z\thetaseparator\tau)\Theta''(z\thetaseparator\tau)}{\Theta(z\thetaseparator\tau)^2}.
$$

::: pf

::: {.pf-step #elliptic}
$H=-\bigl(\Theta'/\Theta\bigr)'$, and $H$ is elliptic with periods $1$ and $\tau$.

::: pf-proof
$\bigl(\Theta'/\Theta\bigr)'=(\Theta''\Theta-(\Theta')^2)/\Theta^2=-H$ by the quotient rule. The transformation laws $\Theta(z+1)=\Theta(z)$ and $\Theta(z+\tau)=e^{-\pi i\tau-2\pi iz}\Theta(z)$ give $\bigl(\Theta'/\Theta\bigr)(z+1)=\bigl(\Theta'/\Theta\bigr)(z)$ and $\bigl(\Theta'/\Theta\bigr)(z+\tau)=\bigl(\Theta'/\Theta\bigr)(z)-2\pi i$, the multiplier contributing the derivative of $-\pi i\tau-2\pi iz$. Differentiating the second identity and using that the derivative of the constant $-2\pi i$ vanishes gives $H(z+\tau)=H(z)$.
:::

:::

::: {.pf-step #zeros}
$\Theta(\cdot\thetaseparator\tau)$ has simple zeros exactly at $z_0+\Lambda$ with $\Lambda=\ZZ+\ZZ\tau$, so $H$ has a double pole exactly there.

::: pf-proof
The Jacobi product formula exhibits the zero set of $\Theta$ as the coset $z_0+\Lambda$ modulo the lattice, each zero simple because $\Theta$ vanishes to first order there. A simple zero of $\Theta$ gives a simple pole of $\Theta'/\Theta$ with residue $1$, hence a double pole of $H=-(\Theta'/\Theta)'$; elsewhere $\Theta\ne0$ and $H$ is holomorphic.
:::

:::

::: {.pf-step #expansion}
With $w=z-z_0$, $a=\Theta'(z_0\thetaseparator\tau)$, $b=\Theta''(z_0\thetaseparator\tau)$ and $c$ the third derivative of $\Theta$ at $z_0$, one has
$$
H(z)=\frac1{w^2}+\Bigl(\frac{b^2}{4a^2}-\frac c{3a}\Bigr)+O(w).
$$

::: pf-proof
Taylor's formula gives $\Theta=aw+\tfrac b2w^2+\tfrac c6w^3+O(w^4)$ with $a\ne0$, the zero being simple. Dividing the series for $\Theta'$ by that for $\Theta$ and expanding to first order,
$$
\frac{\Theta'}{\Theta}=\frac1w+\frac b{2a}+\Bigl(\frac c{3a}-\frac{b^2}{4a^2}\Bigr)w+O(w^2),
$$
which one checks by multiplying the two expansions out to order $w$; differentiating and changing sign gives the displayed expansion of $H$.
:::

:::

::: {.pf-step #compare}
$H-\wp_\tau(\cdot-z_0)$ is constant, the constant being read off from step [](#expansion){.pf-ref}.

::: pf-proof
$\wp_\tau$ is elliptic with periods $1$ and $\tau$ and has principal part $w^{-2}$ at each lattice point, so $\wp_\tau(z-z_0)$ has the same periods, a shift by $z_0$ permuting the cosets, and the same principal part $w^{-2}$ at each point of $z_0+\Lambda$. By step [](#zeros){.pf-ref} the difference $H-\wp_\tau(\cdot-z_0)$ has only removable singularities and is elliptic, hence extends to an entire elliptic function; it is bounded on a fundamental parallelogram, so on $\CC$, and constant by Liouville's theorem. Since $\wp_\tau(w)=w^{-2}+O(w^2)$ has no constant term, the constant is $\frac{b^2}{4a^2}-\frac c{3a}$.
:::

:::

::: {.pf-step}
$\boxed{H(z)=\wp_\tau(z-\tfrac12-\tfrac\tau2)+c_\tau}$, with $c_\tau$ as displayed below in terms of the derivatives of $\Theta$ at $z_0$.

::: pf-proof
The identity is step [](#compare){.pf-ref}, and substituting $a,b,c$ gives
$$
c_\tau=\frac14\Bigl(\frac{\Theta''(z_0\thetaseparator\tau)}{\Theta'(z_0\thetaseparator\tau)}\Bigr)^2-\frac13\frac{\Theta'''(z_0\thetaseparator\tau)}{\Theta'(z_0\thetaseparator\tau)}.
$$
This is the theta-function analogue of the sigma-function identity of [[E-SS9.EX-5]]. The constant involves the third derivative, as the remark on the card records: the transformation law determines only $\Theta''(z_0)=-2\pi i\Theta'(z_0)$ and does not eliminate $\Theta'''(z_0)$.
:::

:::

:::
:::
