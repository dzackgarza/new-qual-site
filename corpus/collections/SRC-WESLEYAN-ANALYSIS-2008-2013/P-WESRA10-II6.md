---
schema: qual/card@1
id: P-WESRA10-II6
kind: problem
title: 'Closed support subspaces and an orthogonal projection in $L^2$'
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Part II, problem 6 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md.
---

::: {.problem}
Let $\mathcal H=L^2([0,1],m)$ and let $E\subset[0,1]$ be Lebesgue measurable.
Define
$$
H_E=\{f\in\mathcal H:f=f\chi_E\}.
$$

(a) Prove $H_E$ is a closed subspace of $\mathcal H$.

(b) Identify $H_E^\perp$.

(c) Let $P(f)=f\chi_E$.
Calculate $\norm{P}$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The set $H_E$ is a linear subspace of $\mathcal H$.


::: pf-proof

If $f,g\in H_E$ and $a,b$ are scalars, then
$$
(af+bg)\chi_E
=a(f\chi_E)+b(g\chi_E)
=af+bg.
$$
Hence $af+bg\in H_E$.

:::

:::

::: {.pf-step #s1-2}

The subspace $H_E$ is closed in $L^2([0,1])$.


::: pf-proof

Let $f_n\in H_E$ and suppose
$$
f_n\to f
$$
in $L^2$. Since
$$
f_n\chi_{E^c}=0,
$$
one has
$$
\norm{f\chi_{E^c}}_2
=\norm{(f-f_n)\chi_{E^c}}_2
\le
\norm{f-f_n}_2
\longrightarrow0.
$$
Thus
$$
f\chi_{E^c}=0
$$
in $L^2$, so
$$
f=f\chi_E.
$$
Hence $f\in H_E$.

:::

:::

::: {.pf-step #s1-3}

One has
$$
\boxed{H_E^\perp=H_{E^c}}.
$$


::: pf-proof

If $g\in H_{E^c}$ and $f\in H_E$, then
$$
f\overline g=0
$$
almost everywhere, because $f$ vanishes off $E$ and $g$ vanishes on $E$.
Therefore
$$
\langle f,g\rangle=0,
$$
so
$$
H_{E^c}\subseteq H_E^\perp.
$$

Conversely, suppose $g\in H_E^\perp$. The function
$$
h=g\chi_E
$$
belongs to $H_E$. Hence
$$
0
=\langle g,h\rangle
=\int_0^1 g\,\overline{g\chi_E}\,dm
=\int_E \abs{g}^2\,dm.
$$
Thus $g=0$ almost everywhere on $E$, which means
$$
g=g\chi_{E^c}.
$$
Therefore $g\in H_{E^c}$.

:::

:::

::: {.pf-step #s1-4}

The operator
$$
P(f)=f\chi_E
$$
satisfies
$$
\norm{P}\le1.
$$


::: pf-proof

For every $f\in L^2([0,1])$,
$$
\norm{Pf}_2^2
=\int_E \abs{f}^2\,dm
\le
\int_{[0,1]}\abs{f}^2\,dm
=\norm{f}_2^2.
$$
Hence $\norm{Pf}_2\le\norm{f}_2$, so $\norm{P}\le1$.

:::

:::

::: pf-step

If $m(E)>0$, then
$$
\boxed{\norm{P}=1}.
$$


::: pf-proof

Since $m(E)>0$ and $E\subset[0,1]$ has finite measure,
$$
\chi_E\in L^2([0,1])
$$
and $\chi_E\ne0$ in $L^2$. Moreover,
$$
P\chi_E=\chi_E.
$$
Therefore
$$
\norm{P}
\ge
\frac{\norm{P\chi_E}_2}{\norm{\chi_E}_2}
=1.
$$
Together with step [](#s1-4){.pf-ref}, this gives $\norm{P}=1$.

:::

:::

::: {.pf-step #s1-6}

If $m(E)=0$, then
$$
\boxed{\norm{P}=0}.
$$


::: pf-proof

If $m(E)=0$, then
$$
f\chi_E=0
$$
in $L^2$ for every $f$. Hence $P$ is the zero operator, whose norm is $0$.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref} prove part (a), step [](#s1-3){.pf-ref} proves part (b), and steps
[](#s1-4){.pf-ref} through [](#s1-6){.pf-ref} compute the norm in all cases for part (c).

:::

:::

:::
