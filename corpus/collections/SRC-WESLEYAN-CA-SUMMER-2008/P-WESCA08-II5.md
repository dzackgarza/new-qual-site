---
schema: qual/card@1
id: P-WESCA08-II5
kind: problem
title: 'Residues of sums and products'
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problems, problem 5 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md.
---

::: {.problem}
Let $U\subset\CC$ be open and let $f,g:U\to\CC$ be analytic except for isolated singularities.
Let $z_0\in U$.

1. Is the residue of $f+g$ at $z_0$ equal to the sum of the residues of $f$ and $g$ at $z_0$?

2. Is the residue of $fg$ at $z_0$ equal to the product of the residues of $f$ and $g$ at $z_0$?
:::

::: {.solution}

Fix a punctured neighborhood of $z_0$ on which both functions are
holomorphic, and write their Laurent expansions
$$
f(z)=\sum_{n=-\infty}^{\infty}a_n(z-z_0)^n,
$$
$$
g(z)=\sum_{n=-\infty}^{\infty}b_n(z-z_0)^n.
$$

::: pf

::: {.pf-step #s1-1}

The residues are
$$
\boxed{
\operatorname{Res}(f,z_0)=a_{-1}}
$$
and
$$
\boxed{
\operatorname{Res}(g,z_0)=b_{-1}}.
$$


::: pf-proof

By definition, the residue at an isolated singularity is the coefficient of
$$
(z-z_0)^{-1}
$$
in the Laurent expansion.

:::

:::

::: {.pf-step #s1-2}

The Laurent expansion of $f+g$ is
$$
\boxed{
(f+g)(z)
=
\sum_{n=-\infty}^{\infty}
(a_n+b_n)(z-z_0)^n}.
$$


::: pf-proof

Laurent series may be added term by term on a common annulus of convergence.

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
\boxed{
\operatorname{Res}(f+g,z_0)
=
\operatorname{Res}(f,z_0)
+
\operatorname{Res}(g,z_0)}.
$$


::: pf-proof

By step [](#s1-2){.pf-ref}, the coefficient of $(z-z_0)^{-1}$ in $f+g$ is
$$
a_{-1}+b_{-1}.
$$
Apply step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

Hence the answer to part $1$ is
$$
\boxed{\text{yes}}.
$$


::: pf-proof

This is exactly step [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

For products, the coefficient of $(z-z_0)^{-1}$ is generally
$$
\boxed{
\sum_{k\in\ZZ}
a_kb_{-1-k}},
$$
not merely
$$
a_{-1}b_{-1}.
$$


::: pf-proof

The Laurent series product is the Cauchy product
$$
f(z)g(z)
=
\sum_{n}
\left(
\sum_k a_kb_{n-k}
\right)
(z-z_0)^n.
$$
Set $n=-1$.

:::

:::

::: pf-step

In particular, multiplication of residues cannot hold in general.


::: pf-proof

Step [](#s1-5){.pf-ref} shows that the residue of a product receives contributions from all
pairs of Laurent coefficients whose exponents sum to $-1$, whereas the
product of the residues only uses the pair $(-1,-1)$, whose exponents sum
to $-2$.

:::

:::

::: pf-step

An explicit counterexample is obtained at
$$
z_0=0
$$
by taking
$$
\boxed{
f(z)=\frac1z,
\qquad
g(z)=1}.
$$


::: pf-proof

Both functions are analytic on a punctured neighborhood of $0$, and $g$
is actually entire.

:::

:::

::: {.pf-step #s1-8}

Their residues satisfy
$$
\boxed{
\operatorname{Res}(f,0)=1}
$$
and
$$
\boxed{
\operatorname{Res}(g,0)=0}.
$$


::: pf-proof

The Laurent expansions are
$$
f(z)=z^{-1}
$$
and
$$
g(z)=1.
$$
Read off the $z^{-1}$-coefficients.

:::

:::

::: {.pf-step #s1-9}

But
$$
fg(z)=\frac1z,
$$
so
$$
\boxed{
\operatorname{Res}(fg,0)=1}.
$$


::: pf-proof

The product is again $z^{-1}$, whose residue is $1$.

:::

:::

::: {.pf-step #s1-10}

Thus
$$
\operatorname{Res}(fg,0)
=
1
\ne
0
=
\operatorname{Res}(f,0)
\operatorname{Res}(g,0).
$$


::: pf-proof

Use steps [](#s1-8){.pf-ref} through [](#s1-9){.pf-ref}.

:::

:::

::: {.pf-step #s1-11}

Hence the answer to part $2$ is
$$
\boxed{\text{no}}.
$$


::: pf-proof

Step [](#s1-10){.pf-ref} provides a counterexample.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} answers part $1$, and step [](#s1-11){.pf-ref} answers part $2$.

:::

:::

:::
