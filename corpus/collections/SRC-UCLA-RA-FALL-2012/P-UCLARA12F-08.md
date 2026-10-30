---
schema: qual/card@1
id: P-UCLARA12F-08
kind: problem
title: Entire square root from even zero multiplicities
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Zeros
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the Fall 2012 section of the vendored UCLA Analysis Qualifying Exam Solutions compilation.
---

::: {.problem}
Let $f:\CC\to\CC$ be a nonconstant holomorphic function such that every zero of $f$ has even multiplicity.
Show that $f$ has a holomorphic square root: there exists an entire function $g$ such that
$$
f(z)=g(z)^2
$$
for every $z\in\CC$.
:::

::: {.solution}

Let
$$
Z\coloneqq\{z\in\CC:f(z)=0\},
\qquad
\Omega\coloneqq\CC\setminus Z.
$$
Choose $z_0\in\Omega$ and choose $c\in\CC$ with
$$
c^2=f(z_0).
$$

::: pf

::: {.pf-step #s1-1}

For every closed piecewise smooth curve $\gamma$ in $\Omega$,
$$
\frac12\int_\gamma\frac{f'(z)}{f(z)}\,dz
\in2\pi i\ZZ.
$$


::: pf-proof

By the argument principle,
$$
\frac1{2\pi i}
\int_\gamma\frac{f'}f\,dz
=\sum_{a\in Z}
m(a)\operatorname{Ind}(\gamma,a),
$$
where $m(a)$ is the multiplicity of the zero $a$. Only finitely many terms are nonzero for a fixed compact curve. By hypothesis every $m(a)$ is even, so the integer on the right is even. Therefore half of the integral is an integral multiple of $2\pi i$.

:::

:::

::: pf-step

For $z\in\Omega$, define
$$
g(z)
\coloneqq
c\exp\!\left(
\frac12\int_{z_0}^z\frac{f'(\zeta)}{f(\zeta)}\,d\zeta
\right),
$$
where the integral is taken along any path in $\Omega$ from $z_0$ to $z$. Then $g$ is well-defined and holomorphic on $\Omega$.


::: pf-proof

If two paths from $z_0$ to $z$ are chosen, their difference is a closed curve in $\Omega$. By step [](#s1-1){.pf-ref}, the difference between the corresponding half-integrals is in $2\pi i\ZZ$, so their exponentials agree. Thus $g$ is well-defined.

Locally, on a simply connected disk contained in $\Omega$, the integral has a holomorphic primitive. Hence the displayed formula is locally the exponential of a holomorphic function and is therefore holomorphic.

:::

:::

::: {.pf-step #s1-3}

On $\Omega$,
$$
g(z)^2=f(z).
$$


::: pf-proof

By construction,
$$
\frac{g'(z)}{g(z)}
=\frac12\frac{f'(z)}{f(z)}.
$$
Therefore
$$
\frac{d}{dz}\left(\frac{g(z)^2}{f(z)}\right)=0
$$
on the connected set $\Omega$. At $z=z_0$,
$$
\frac{g(z_0)^2}{f(z_0)}
=\frac{c^2}{f(z_0)}=1.
$$
Hence $g^2/f\equiv1$ on $\Omega$.

:::

:::

::: {.pf-step #s1-4}

The function $g$ extends holomorphically across every point of $Z$.


::: pf-proof

Let $a\in Z$ have multiplicity $2m$. On a sufficiently small disk about $a$,
$$
f(z)=(z-a)^{2m}h(z),
$$
where $h$ is holomorphic and nonvanishing. By step [](#s1-3){.pf-ref}, on the punctured disk,
$$
\abs{g(z)}^2
=\abs{f(z)}
=\abs{z-a}^{2m}\abs{h(z)}.
$$
Since $h$ is bounded near $a$, the function $g$ is bounded near $a$ and in fact tends to $0$ there. By Riemann's removable singularity theorem, $g$ extends holomorphically across $a$. This applies to every zero.

:::

:::

::: {.pf-step #s1-5}

The extended function, still denoted $g$, is entire and satisfies
$$
\boxed{f(z)=g(z)^2\qquad(z\in\CC)}.
$$


::: pf-proof

Step [](#s1-4){.pf-ref} extends $g$ holomorphically over all zeros, so $g$ is entire. The identity $g^2=f$ holds on the dense open set $\Omega$ by step [](#s1-3){.pf-ref} and therefore, by continuity, also at every zero of $f$.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the required entire square root.

:::

:::

:::
