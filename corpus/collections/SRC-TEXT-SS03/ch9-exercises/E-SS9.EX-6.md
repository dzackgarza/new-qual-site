---
schema: qual/card@1
id: E-SS9.EX-6
kind: problem
title: The differential equation of $\wp$
classification:
  areas:
  - complex-analysis
  topics:
  - Elliptic Functions
  - Weierstrass P
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.exercise}
Prove that $\wp''$ is a quadratic polynomial in $\wp$.
:::

::: {.solution}

The argument is the card's own: the Laurent expansion of $\wp$ shows $\wp''-6\wp^{2}$ has only removable singularities, and an entire elliptic function is constant by Liouville's theorem.

::: pf

::: {.pf-step #laurent}

$\wp(z)=\dfrac{1}{z^{2}}+c_{2}z^{2}+O(z^{4})$ near $0$, for a constant $c_{2}$.

::: pf-proof

The defining series of the Weierstrass function about the origin is $\wp(z)=\frac{1}{z^{2}}+\sum_{k\ge1}(2k+1)G_{2k+2}z^{2k}$ with $G_{2k}=\sum_{\omega\ne0}\omega^{-2k}$ the Eisenstein sums; this is the standard expansion, obtained by expanding $(z-\omega)^{-2}$ about $z=0$ and summing over the lattice. In particular the coefficient of $z^{2}$ is $c_{2}=3G_{4}$, and there are no odd powers because $\wp$ is even.

:::

:::

::: {.pf-step #expansion}

$\wp''(z)=\dfrac{6}{z^{4}}+2c_{2}+O(z^{2})$ and $6\wp(z)^{2}=\dfrac{6}{z^{4}}+12c_{2}+O(z^{2})$.

::: pf-proof

Differentiating the expansion of step [](#laurent){.pf-ref} twice term by term, legitimate inside the punctured disc where the Laurent series converges,
$$
\wp''(z)=6z^{-4}+2c_{2}+O(z^{2}).
$$
Squaring, $\wp(z)^{2}=z^{-4}+2c_{2}+O(z^{2})$ because the cross terms of $\frac{1}{z^{2}}$ with the $z^{2}$ term give the constant $2c_{2}$ and all other products are $O(z^{2})$; multiplying by $6$ gives the second display.

:::

:::

::: {.pf-step #removable}

$H=\wp''-6\wp^{2}$ extends holomorphically across every lattice point, hence is entire.

::: pf-proof

By step [](#expansion){.pf-ref}, $H(z)=-10c_{2}+O(z^{2})$ near $0$: the polar terms $\frac{6}{z^{4}}$ cancel. So $H$ is bounded near $0$ and has a removable singularity there. Both $\wp$ and $\wp''$ are meromorphic with poles only at lattice points, so $H$ is holomorphic off the lattice; translating, the same argument at any lattice point $\omega$ (using the periodicity $\wp(z+\omega)=\wp(z)$) shows the singularity there is removable too. Hence $H$ extends to an entire function.

:::

:::

::: {.pf-step #constant}

$H$ is constant.

::: pf-proof

$\wp$ is elliptic with a lattice $\Lambda$ of periods, and both $\wp$ and its derivative are invariant under $\Lambda$, so $H$ is elliptic: $H(z+\omega)=H(z)$ for $\omega\in\Lambda$. A fundamental parallelogram is compact and $H$ is continuous on it, so $H$ is bounded there, and periodicity makes $H$ bounded on all of $\CC$. An entire bounded function is constant by Liouville's theorem.

:::

:::

::: {.pf-step #conclusion}

$\wp''$ is a quadratic polynomial in $\wp$, namely $\wp''=6\wp^{2}-\frac{g_{2}}{2}$.

::: pf-proof

By steps [](#removable){.pf-ref} and [](#constant){.pf-ref} there is $C$ with $\wp''-6\wp^{2}=C$, so $\wp''=6\wp^{2}+C$ is a polynomial of degree $2$ in $\wp$. For the value of $C$: $g_{2}=60\sum_{\omega\ne0}\omega^{-4}=60G_{4}$, so $c_{2}=3G_{4}=\frac{g_{2}}{20}$, and step [](#expansion){.pf-ref} gives $C=-10c_{2}=-\frac{g_{2}}{2}$. Hence
$$
\boxed{\wp''(z)=6\wp(z)^{2}-\frac{g_{2}}{2}.}
$$

:::

:::

:::

:::
