---
schema: qual/card@1
id: P-BKS04-2B
kind: problem
title: Maximum of $\abs{f'(1)}$ for $f$ holomorphic with $\abs{f}\le1$ on $\abs{z}=2$
classification:
  areas: [prelim]
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the retained UC Berkeley Spring 2004 preliminary exam and its companion solution packet.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Compared the authored solution with the retained `s04solution.pdf` solution packet.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Structured the argument into numbered steps and supplied what it asserted in passing: that the
    boundary map z |-> 2(z-1)/(4-z) has modulus 1 on |z| = 2 (checked by computing both moduli
    squared in terms of Re z) and hence maps the disc onto the unit disc biholomorphically because
    it is Mobius and sends 1 to 0; the computation |g'(1)| = 2/3 from the quotient rule; the use of
    the maximum modulus principle to get |h| <= 1 on the whole unit disc from its boundary; and the
    Cauchy estimate |h'(0)| <= 1 together with the chain rule h'(0) = f'(1)/g'(1). Also recorded
    that the bound is attained by f = g, which is what makes 2/3 the maximum rather than only an
    upper bound. Every macro used is one the preamble defines. Not checked this session: the
    retained solution packet's page.

---

::: {.problem}
Find the maximum possible value of $\abs{f'(1)}$ given that $f$ is holomorphic on an open neighborhood of $\{z\in\CC:\abs{z}\leq2\}$ and satisfies $\abs{f(z)}\leq1$ when $\abs{z}=2$.
:::

::: {.solution}

The argument is the card's own; the statement was checked against the retained UC Berkeley Spring 2004 preliminary examination, and the companion solution packet is not transcribed here.

Write $D_{2}=\{z:\abs{z}<2\}$ and $D=D_{1}$, and suppose $f$ is holomorphic on a neighbourhood of the closed disc $\overline{D_{2}}$ with $\abs{f(z)}\leq1$ for $\abs{z}=2$.

::: pf

::: {.pf-step #mobius}
$g(z)=\dfrac{2(z-1)}{4-z}$ maps $\overline{D_{2}}$ biholomorphically onto $\overline{D}$, with $g(1)=0$.

::: pf-proof
$g$ is a Möbius transformation (the denominator vanishes only at $z=4\notin\overline{D_{2}}$), hence holomorphic and injective there. On $\abs{z}=2$, with $r=\operatorname{Re}z$,
$$
\abs{z-1}^{2}=\abs{z}^{2}-2r+1=5-2r,\qquad \abs{4-z}^{2}=16-8r+\abs{z}^{2}=20-8r=4(5-2r),
$$
so $\abs{g(z)}^{2}=4(5-2r)/\bigl(4(5-2r)\bigr)=1$: the circle maps into the unit circle. A nonconstant holomorphic map carries the interior of a Jordan domain onto one of the two components of the complement of the image curve, and $g(1)=0$ lies in $D$, so $g(D_{2})=D$ and $g$ is a bijection $\overline{D_{2}}\to\overline{D}$.
:::

:::

::: {.pf-step #derivative}
$g'(1)=\dfrac23$.

::: pf-proof
The quotient rule gives $g'(z)=2\dfrac{(4-z)+(z-1)}{(4-z)^{2}}=\dfrac{6}{(4-z)^{2}}$, and at $z=1$ this is $6/9=2/3$.
:::

:::

::: {.pf-step #composition}
$h=f\circ g^{-1}$ is holomorphic on a neighbourhood of $\overline{D}$, satisfies $\abs{h}\leq1$ on $\abs{w}=1$, and $h'(0)=f'(1)/g'(1)$.

::: pf-proof
$g^{-1}$ is holomorphic on $D$ and extends past $\overline{D}$ because $g$ is Möbius and maps a neighbourhood of $\overline{D_{2}}$ bijectively onto a neighbourhood of $\overline{D}$; so $h$ is holomorphic on a neighbourhood of $\overline{D}$. For $\abs{w}=1$ we have $g^{-1}(w)\in\partial D_{2}$ by step [](#mobius){.pf-ref}, hence $\abs{h(w)}=\abs{f(g^{-1}(w))}\leq1$. Differentiating $h\circ g=f$ at $z=1$, where $g(1)=0$, gives $h'(0)g'(1)=f'(1)$.
:::

:::

::: {.pf-step #cauchy}
$\abs{h'(0)}\leq1$.

::: pf-proof
By the maximum modulus principle applied to $h$ on $D$, $\abs{h}\leq1$ on all of $D$. Cauchy's integral formula for the derivative,
$$
h'(0)=\frac{1}{2\pi i}\int_{\abs{w}=1}\frac{h(w)}{w^{2}}\,dw,
$$
then gives $\abs{h'(0)}\leq\frac{1}{2\pi}\cdot1\cdot2\pi=1$, since $\abs{h(w)}\leq1$ and $\abs{w}=1$ on the circle.
:::

:::

::: {.pf-step #bound}
$\abs{f'(1)}\leq\dfrac23$.

::: pf-proof
$\abs{f'(1)}=\abs{h'(0)}\abs{g'(1)}\leq\abs{g'(1)}=2/3$ by steps [](#composition){.pf-ref}, [](#cauchy){.pf-ref} and [](#derivative){.pf-ref}.
:::

:::

::: {.pf-step #sharp}
The bound is attained, by $f=g$.

::: pf-proof
$g$ is holomorphic on a neighbourhood of $\overline{D_{2}}$ and $\abs{g}=1$ on $\abs{z}=2$ by step [](#mobius){.pf-ref}, so it satisfies the hypotheses, and $\abs{g'(1)}=2/3$ by step [](#derivative){.pf-ref}. Hence the maximum of $\abs{f'(1)}$ over the admissible functions is exactly $2/3$.
:::

:::

:::

:::
