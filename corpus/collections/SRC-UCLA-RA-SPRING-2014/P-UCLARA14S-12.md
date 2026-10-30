---
schema: qual/card@1
id: P-UCLARA14S-12
kind: problem
title: 'Zeros of $z^6+iz^4+1$ in the upper half-plane'
classification:
  areas:
  - complex-analysis
  topics:
  - Argument Principle
  - Zeros
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Transcribed from the UCLA Analysis Qualifying Exam Solutions compendium, Spring 2014 section.
---

::: {.problem}
Compute the number of zeros, counted with multiplicity, of
$$
f(z)=z^6+i z^4+1
$$
in the open upper half-plane.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The polynomial $f$ has no real zeros.


::: pf-proof

Let $x\in\RR$. Then
$$
f(x)=x^6+1+i x^4.
$$
If $x\ne0$, its imaginary part is
$$
x^4>0,
$$
so $f(x)\ne0$. At $x=0$,
$$
f(0)=1.
$$
Thus $f$ has no zeros on the real axis.

:::

:::

::: {.pf-step #s1-2}

If $z_0$ is a zero of $f$ of multiplicity $m$, then $-z_0$ is also a zero of multiplicity $m$.


::: pf-proof

The polynomial is even:
$$
f(-z)
=
(-z)^6+i(-z)^4+1
=
z^6+i z^4+1
=
f(z).
$$
Thus zeros occur in pairs $z_0,-z_0$. Replacing $z$ by $-z$ preserves the order of vanishing, so the multiplicities agree.

:::

:::

::: {.pf-step #s1-3}

The map
$$
z\longmapsto -z
$$
gives a multiplicity-preserving bijection between the zeros of $f$ in the open upper half-plane and those in the open lower half-plane.


::: pf-proof

If $\operatorname{Im}z>0$, then
$$
\operatorname{Im}(-z)<0,
$$
and conversely. Step [](#s1-2){.pf-ref} shows that this involution preserves zeros and their multiplicities.

:::

:::

::: pf-step

The polynomial $f$ has exactly
$$
\boxed{3}
$$
zeros in the open upper half-plane, counted with multiplicity.


::: pf-proof

Since $f$ has degree $6$, the fundamental theorem of algebra gives exactly six zeros in $\CC$, counted with multiplicity. By step [](#s1-1){.pf-ref}, none lies on the real axis. By step [](#s1-3){.pf-ref}, the numbers of zeros in the upper and lower half-planes are equal, counted with multiplicity. Therefore each half-plane contains
$$
\frac62=3
$$
zeros.

:::

:::

:::

:::
