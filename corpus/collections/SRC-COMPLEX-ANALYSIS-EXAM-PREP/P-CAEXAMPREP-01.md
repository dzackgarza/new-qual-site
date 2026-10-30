---
schema: qual/card@1
id: P-CAEXAMPREP-01
kind: problem
title: Sum of the residues of the reciprocal of a polynomial
classification: {areas: [complex-analysis], topics: [Residue Theorem, Residue at Infinity]}
relations: []
review: draft
audit:
  - event: source-checked
    by: gpt-5.6-sol
    date: 2026-09-14
    note: Checked against the deterministic MinerU Flash extraction assets/attachments/Complex_Analysis_Exam_Prep_Solutions_extracted.md.
---

::: {.problem}
If $p(z)$ is a polynomial of degree at least $2$, show that the sum of the residues of $1/p(z)$ at all zeros of $p$ is $0$.
:::

::: {.solution}

Write
$$
p(z)=a_mz^m+a_{m-1}z^{m-1}+\cdots+a_0,
\qquad
m\ge2,
\qquad
a_m\ne0,
$$
and let
$$
S=\sum_{p(b)=0}\operatorname{Res}_{z=b}\frac1{p(z)},
$$
where the sum is over the distinct zeros of $p$.

::: pf

::: {.pf-step #s1-1}

There exist constants $R_0>0$ and $c>0$ such that
$$
\abs{p(z)}\ge c\abs{z}^m
$$
whenever $\abs{z}\ge R_0$.


::: pf-proof

For $z\ne0$,
$$
\frac{p(z)}{z^m}
=a_m+\frac{a_{m-1}}z+\cdots+\frac{a_0}{z^m}
\longrightarrow a_m
$$
as $\abs{z}\to\infty$. Hence there is $R_0>0$ such that
$$
\abs{\frac{p(z)}{z^m}-a_m}\le\frac{\abs{a_m}}{2}
$$
for $\abs{z}\ge R_0$. The reverse triangle inequality then gives
$$
\frac{\abs{p(z)}}{\abs{z}^m}\ge\frac{\abs{a_m}}{2}.
$$
Thus one may take $c=\abs{a_m}/2$.

:::

:::

::: {.pf-step #s1-2}

If $R\ge R_0$ is larger than the modulus of every zero of $p$, then
$$
\int_{\abs{z}=R}\frac{dz}{p(z)}=2\pi i\,S.
$$


::: pf-proof

All poles of $1/p$ are precisely the zeros of $p$, and by the choice of $R$ every such pole lies strictly inside the positively oriented circle $\abs{z}=R$. The residue theorem therefore gives the displayed identity, with the residues summed once over the distinct poles.

:::

:::

::: {.pf-step #s1-3}

One has
$$
\int_{\abs{z}=R}\frac{dz}{p(z)}\longrightarrow0
\qquad\text{as }R\to\infty.
$$


::: pf-proof

By step [](#s1-1){.pf-ref}, for every sufficiently large $R$,
$$
\abs{\int_{\abs{z}=R}\frac{dz}{p(z)}}
\le
2\pi R\sup_{\abs{z}=R}\frac1{\abs{p(z)}}
\le
\frac{2\pi}{c}R^{1-m}.
$$
Since $m\ge2$, the exponent $1-m\le-1$, so the right-hand side tends to $0$.

:::

:::

::: {.pf-step #s1-4}

The sum of the residues is
$$
\boxed{S=0}.
$$


::: pf-proof

For every sufficiently large $R$, step [](#s1-2){.pf-ref} gives
$$
2\pi i\,S=\int_{\abs{z}=R}\frac{dz}{p(z)}.
$$
Letting $R\to\infty$ and applying step [](#s1-3){.pf-ref} yields $2\pi iS=0$, hence $S=0$.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} is the required residue sum.

:::

:::

:::
