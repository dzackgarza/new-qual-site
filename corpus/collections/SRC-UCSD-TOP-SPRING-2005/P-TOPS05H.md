---
schema: qual/card@1
id: P-TOPS05H
kind: problem
title: 'No map $\quatprojective^n\to\CP^{2n}$ sending the generator to a nonzero multiple'
classification:
  areas:
  - topology
  topics:
  - Cohomology
  - Projective Spaces
  - Degree
relations: []
review: draft
---

::: {.problem}
Show there is no map $f : \quatprojective^n \to \CP^{2n}$ such that the induced map $H_{4n}(f) : H_{4n}(\quatprojective^n; \ZZ) \to H_{4n}(\CP^{2n}; \ZZ)$ maps the generator $\zeta_{\quatprojective^n}$ to $k\zeta_{\CP^{2n}}$ for $k \neq 0$.
:::

::: {.solution}

::: pf

::: pf-step

Write
$$
H^*(\CP^{2n};\ZZ)=\ZZ[x]/(x^{2n+1}),\quad \gradeddegree{x}=2,
$$
and
$$
H^*(\quatprojective^{n};\ZZ)=\ZZ[u]/(u^{n+1}),\quad \gradeddegree{u}=4.
$$

::: pf-proof

These are the standard integral cohomology rings of complex and quaternionic projective spaces.

:::

:::

::: pf-step

Since $H^2(\quatprojective^n;\ZZ)=0$, every map $f:\quatprojective^n\to\CP^{2n}$ satisfies
$$
f^*x=0.
$$

::: pf-proof

The target of $f^*:H^2(\CP^{2n})\to H^2(\quatprojective^n)$ is zero.

:::

:::

::: {.pf-step #s3}

Hence
$$
f^*(x^{2n})=(f^*x)^{2n}=0.
$$

::: pf-proof

Pullback is a ring homomorphism.

:::

:::

::: {.pf-step #s4}

If $f_*$ sent the top homology generator to $k$ times the top generator with $k\ne0$, then $f^*$ on top cohomology would also be multiplication by $k$, hence nonzero.

::: pf-proof

For top cohomology generators $\eta_{\CP}$ and $\eta_{\quatprojective}$ dual to the fundamental classes,
$$
\langle f^*\eta_{\CP},[\quatprojective^n]\rangle
=\langle \eta_{\CP},f_*[\quatprojective^n]\rangle=k.
$$

:::

:::

::: {.pf-step #s5}

But $x^{2n}$ is a generator of top cohomology and step [](#s3){.pf-ref} says its pullback is zero. Contradiction.

::: pf-proof

The top degree of $\CP^{2n}$ is $4n$, and $x^{2n}$ generates that group.

:::

:::

::: pf-step

Therefore no such map exists for $k\ne0$.

::: pf-proof

The assumed nonzero top degree contradicts steps [](#s3){.pf-ref}, [](#s4){.pf-ref} and [](#s5){.pf-ref}.

:::

:::

:::

:::
