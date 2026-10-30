---
schema: qual/card@1
id: P-WESCA04-T2
kind: problem
title: "State the Residue Theorem"
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis section 1.1, item 2 (August 2, 2004) in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
---

::: {.problem}
State the Residue Theorem.
:::

::: {.solution}

::: pf

::: pf-step

Let $U\subset\CC$ be open, let
$$
\gamma
$$
be a positively oriented piecewise-$C^1$ simple closed curve such that
$$
\gamma\subset U
$$
and the bounded component
$$
D
$$
of $\CC\setminus\gamma$ has
$$
\overline D\subset U.
$$
Suppose $f$ is holomorphic on $U$ except at finitely many isolated
singularities
$$
a_1,\dots,a_m\in D.
$$
Then
$$
\boxed{
\int_\gamma f(z)\,dz
=
2\pi i
\sum_{j=1}^m
\operatorname{Res}(f,a_j).
}
$$


::: pf-proof

This is the standard contour form of the Residue Theorem. The remaining
steps justify the formula.

:::

:::

::: pf-step

Choose pairwise disjoint closed disks
$$
\overline{B(a_j,r_j)}
\subset D
$$
containing no singularity of $f$ other than $a_j$, and set
$$
\Omega
\coloneqq
D
\setminus
\bigcup_{j=1}^m
\overline{B(a_j,r_j)}.
$$
Then $f$ is holomorphic on a neighborhood of $\overline\Omega$.


::: pf-proof

The singularities are isolated and finite in number. Therefore each
$a_j$ has a sufficiently small disk containing no other singularity, and
the radii may be chosen small enough that these closed disks are pairwise
disjoint and remain inside $D$.

By construction, every singular point has been removed from
$\overline\Omega$, so $f$ is holomorphic on a neighborhood of that compact
set.

:::

:::

::: {.pf-step #s1-3}

Cauchy's theorem on the multiply connected region $\Omega$ gives
$$
\int_\gamma f(z)\,dz
=
\sum_{j=1}^m
\int_{\abs{z-a_j}=r_j}
f(z)\,dz,
$$
where each small circle on the right is positively oriented.


::: pf-proof

The positively oriented boundary of $\Omega$ consists of the outer curve
$\gamma$ together with the small circles oriented clockwise relative to
$\Omega$.

Hence Cauchy's theorem gives
$$
0
=
\int_\gamma f(z)\,dz
-
\sum_{j=1}^m
\int_{\abs{z-a_j}=r_j}^{\mathrm{ccw}}
f(z)\,dz.
$$
Rearranging yields the displayed identity.

:::

:::

::: {.pf-step #s1-4}

For every $j$,
$$
\int_{\abs{z-a_j}=r_j}
f(z)\,dz
=
2\pi i\,
\operatorname{Res}(f,a_j).
$$


::: pf-proof

On the punctured disk around $a_j$, write the Laurent expansion
$$
f(z)
=
\sum_{n=-\infty}^{\infty}
c_n(z-a_j)^n.
$$
By definition,
$$
\operatorname{Res}(f,a_j)=c_{-1}.
$$

Termwise integration around the circle gives
$$
\int_{\abs{z-a_j}=r_j}
(z-a_j)^n\,dz
=
\begin{cases}
2\pi i,&n=-1,\\
0,&n\ne-1.
\end{cases}
$$
Therefore only the coefficient $c_{-1}$ contributes, giving the required
formula.

:::

:::

::: {.pf-step #s1-5}

Combining steps [](#s1-3){.pf-ref} and [](#s1-4){.pf-ref} yields
$$
\int_\gamma f(z)\,dz
=
2\pi i
\sum_{j=1}^m
\operatorname{Res}(f,a_j).
$$


::: pf-proof

Substitute the $m$ identities from step [](#s1-4){.pf-ref} into the sum in step [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-6}

More generally, if $\Gamma$ is a closed piecewise-$C^1$ cycle in
$U$ which is homologous to zero in $U$ and avoids all singularities of
$f$, then
$$
\boxed{
\int_\Gamma f(z)\,dz
=
2\pi i
\sum_a
\operatorname{Ind}(\Gamma,a)
\operatorname{Res}(f,a),
}
$$
where the sum is over the isolated singularities of $f$ and only finitely
many terms are nonzero.


::: pf-proof

The homological version of Cauchy's theorem expresses the cycle $\Gamma$
as the boundary, in homology, of the region obtained after excising small
circles around the singularities. Each small circle occurs with
multiplicity
$$
\operatorname{Ind}(\Gamma,a)
=
\frac1{2\pi i}
\int_\Gamma
\frac{dz}{z-a}.
$$
Applying the local computation from step [](#s1-4){.pf-ref} to each circle gives the
displayed weighted residue sum.

For a positively oriented simple Jordan curve, the index is $1$ at points
inside and $0$ outside, so this reduces to step [](#s1-5){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the usual Residue Theorem, and step [](#s1-6){.pf-ref} records its standard
homological generalization.

:::

:::

:::
