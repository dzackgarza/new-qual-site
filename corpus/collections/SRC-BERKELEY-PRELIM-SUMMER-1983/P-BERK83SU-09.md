---
schema: qual/card@1
id: P-BERK83SU-09
kind: problem
title: Argument principle and a boundary integral locating a simple zero
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Factoring f=g product_j(z-z_j)^{n_j} with g holomorphic and nonvanishing
    near the closure gives f'/f=g'/g+sum_j n_j/(z-z_j). Cauchy's formula
    yields the zero count; multiplying by z before integrating yields
    sum_j n_j z_j and hence the unique simple zero.
---

::: {.problem}
Let $\Omega\subset\mathbb C$ be a bounded domain whose boundary is a smooth Jordan curve $\gamma$. Let $f$ be holomorphic on a neighborhood of $\overline\Omega$, assume $f\ne0$ on $\gamma$, and let $z_1,\ldots,z_k$ be the zeros of $f$ in $\Omega$ with multiplicities $n_1,\ldots,n_k$.

1. Using Cauchy's integral formula, prove
\[
\frac1{2\pi i}\int_\gamma\frac{f'(z)}{f(z)}\,dz
=\sum_{j=1}^k n_j.
\]
2. If $f$ has exactly one zero $z_1$ in $\Omega$, and it is simple, find a boundary integral involving $f$ whose value is $z_1$.
:::

::: {.solution}
Orient $\gamma$ positively. Define
$$
P(z)=\prod_{j=1}^k(z-z_j)^{n_j}.
$$

::: pf

::: {.pf-step #s1}

There is a holomorphic function $g$, nonvanishing on a
neighborhood of $\overline\Omega$, such that
$$
f(z)=g(z)P(z)
$$
there.

::: pf-proof

The quotient $f/P$ is holomorphic away from the points $z_j$. Since
$n_j$ is exactly the order of the zero of $f$ at $z_j$, each apparent
singularity is removable and the quotient extends holomorphically
across $z_j$. Call the extension $g$.

The zeros $z_1,\ldots,z_k$ are all the zeros of $f$ in $\Omega$,
and $f$ is nonzero on $\gamma$, so $g$ has no zeros on
$\overline\Omega$. By compactness, after shrinking the ambient
neighborhood if necessary, $g$ is nonvanishing on a neighborhood of
$\overline\Omega$.

:::

:::

::: {.pf-step #s2}

Part 1 gives
$$
\boxed{
\frac1{2\pi i}
\int_\gamma\frac{f'(z)}{f(z)}\,dz
=
\sum_{j=1}^k n_j
}.
$$

::: pf-proof

By step [](#s1){.pf-ref}, away from the zeros of $f$,
$$
\frac{f'(z)}{f(z)}
=
\frac{g'(z)}{g(z)}
+
\sum_{j=1}^k\frac{n_j}{z-z_j}.
$$
Since $g$ is nonvanishing near $\overline\Omega$, the function
$g'/g$ is holomorphic there, so Cauchy's theorem gives
$$
\int_\gamma\frac{g'(z)}{g(z)}\,dz=0.
$$
For each $j$, Cauchy's integral formula applied to the constant
function $1$ gives
$$
\frac1{2\pi i}
\int_\gamma\frac{1}{z-z_j}\,dz
=
1.
$$
Integrating the logarithmic-derivative identity therefore yields the
displayed formula.

:::

:::

::: {.pf-step #s3}

More generally,
$$
\frac1{2\pi i}
\int_\gamma
z\frac{f'(z)}{f(z)}\,dz
=
\sum_{j=1}^k n_jz_j.
$$

::: pf-proof

Differentiating the factorization from step [](#s1){.pf-ref} and multiplying the
resulting logarithmic-derivative identity by $z$ gives
$$
z\frac{f'(z)}{f(z)}
=
z\frac{g'(z)}{g(z)}
+
\sum_{j=1}^k n_j\frac{z}{z-z_j}.
$$
The first term is holomorphic near $\overline\Omega$, so its
boundary integral is zero. Cauchy's integral formula applied to the
holomorphic function $h(z)=z$ gives
$$
\frac1{2\pi i}
\int_\gamma\frac{z}{z-z_j}\,dz
=
z_j.
$$
Summing over $j$ proves the formula.

:::

:::

::: {.pf-step #s4}

Under the hypothesis of part 2,
$$
\boxed{
z_1
=
\frac1{2\pi i}
\int_\gamma
z\frac{f'(z)}{f(z)}\,dz
}.
$$

::: pf-proof

If $z_1$ is the only zero and it is simple, then $k=1$ and $n_1=1$.
Step [](#s3){.pf-ref} reduces exactly to the displayed boundary integral.

:::

:::

::: pf-qed

Step [](#s2){.pf-ref} proves part 1, and step [](#s4){.pf-ref} gives the boundary integral
requested in part 2.

:::

:::

:::
