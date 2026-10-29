---
schema: qual/card@1
id: P-MAXAT-4-12
kind: problem
title: Cohomology of the free loop spaces of $S^3$, $S^2$ and $\CP^n$
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against section 4, problem 12 of the retained Laurentiu Maxim Problems in Algebraic Topology PDF.
---

::: {.problem}
Calculate the cohomology of the space of maps from $S ^ { 1 } \to S ^ { 3 }$ , and similarly for the space of maps $S ^ { 1 } \to S ^ { 2 }$ and $S ^ { 1 } \to \CP ^ { n }$
:::

::: {.solution}

Write
$$
LX
\coloneqq
\operatorname{Map}(S^1,X)
$$
for the free loop space, with the compact-open topology.
All cohomology groups below have integral coefficients.

::: pf

::: {.pf-step #s1-1}

Since $S^3$ is a topological group, there is a homeomorphism
$$
LS^3
\cong
S^3\times\Omega S^3.
$$


::: pf-proof

Identify $S^3$ with the unit quaternions. For a free loop
$$
\gamma:S^1\to S^3,
$$
define
$$
\Phi(\gamma)
=
\bigl(
\gamma(1),
\gamma(1)^{-1}\gamma(-)
\bigr).
$$
The second coordinate is a based loop at the identity. Conversely, for
$$
(g,\omega)\in S^3\times\Omega S^3,
$$
define
$$
\Psi(g,\omega)(t)=g\omega(t).
$$
These maps are continuous and inverse to one another.

:::

:::

::: {.pf-step #s1-2}

The based loop space has
$$
H_*(\Omega S^3;\ZZ)
\cong
\ZZ[t_2]
$$
as a Pontryagin algebra, and therefore
$$
H^*(\Omega S^3;\ZZ)
\cong
\Gamma_{\ZZ}(u_2),
\qquad
|u_2|=2,
$$
where $\Gamma$ denotes the divided-power algebra.


::: pf-proof

Since
$$
S^3
=
\Sigma S^2,
$$
the James--Bott--Samelson theorem gives
$$
H_*(\Omega S^3;\ZZ)
\cong
T\bigl(\widetilde H_*(S^2;\ZZ)\bigr).
$$
There is one generator $t_2$ in even degree $2$, so the tensor algebra on
that single generator is the polynomial algebra
$$
\ZZ[t_2].
$$

Every homology group is free of rank one in an even degree. The graded dual
Hopf algebra is therefore the divided-power algebra
$$
\Gamma_{\ZZ}(u_2),
$$
with multiplication
$$
\gamma_i(u_2)\gamma_j(u_2)
=
\binom{i+j}{i}\gamma_{i+j}(u_2).
$$

:::

:::

::: {.pf-step #s1-3}

Hence
$$
\boxed{
H^*(LS^3;\ZZ)
\cong
\Lambda_{\ZZ}(z_3)
\otimes
\Gamma_{\ZZ}(u_2).
}
$$
In particular,
$$
H^q(LS^3;\ZZ)
\cong
\begin{cases}
0,&q=1,\\
\ZZ,&q=0\text{ or }q\ge2.
\end{cases}
$$


::: pf-proof

By step [](#s1-1){.pf-ref}, apply the integral Künneth theorem. The cohomology of $S^3$
is
$$
H^*(S^3;\ZZ)
\cong
\Lambda_{\ZZ}(z_3),
$$
and step [](#s1-2){.pf-ref} gives the other factor. Both factors are torsion-free, so no
Tor term occurs.

The divided-power factor has one copy of $\ZZ$ in every nonnegative
even degree. Multiplying by $z_3$ gives one copy in every odd degree at
least $3$, proving the additive statement.

:::

:::

::: {.pf-step #s1-4}

For $n\ge1$, Cohen--Jones--Yan compute the shifted loop homology
algebra
$$
\bH_*(L\CP^n)
\coloneqq
H_{*+2n}(L\CP^n;\ZZ)
$$
as
$$
\boxed{
\bH_*(L\CP^n)
\cong
\frac{
\ZZ[a_{-2},x_{-1},y_{2n}]
}{
(a^{n+1},x^2,a^nx,(n+1)ya^n)
}.
}
$$


::: pf-proof

This is the integral Cohen--Jones--Yan calculation from
R. Cohen, J. Jones, and J. Yan,
*The loop homology algebra of spheres and projective spaces*.
It is obtained from the multiplicative Serre spectral sequence of the
evaluation fibration
$$
\Omega\CP^n
\longrightarrow
L\CP^n
\xrightarrow{\operatorname{ev}}
\CP^n.
$$
The grading displayed here is the string-topology grading shifted downward by
$$
\dim_{\RR}\CP^n=2n.
$$

:::

:::

::: {.pf-step #s1-5}

As an ordinary homology group,
$$
H_q(L\CP^n;\ZZ)
\cong
\begin{cases}
\ZZ,
&q\text{ odd},\\[2mm]
\ZZ,
&q=0,\\[2mm]
\ZZ\oplus\ZZ/(n+1),
&q=2nr\text{ for some }r\ge1,\\[2mm]
\ZZ,
&q>0\text{ even and }2n\nmid q.
\end{cases}
$$


::: pf-proof

Use the monomial basis of the algebra in step [](#s1-4){.pf-ref}.

First consider monomials without $x$:
$$
a^i y^k.
$$
Their shifted degree is
$$
-2i+2nk,
$$
so their ordinary homological degree is
$$
2n-2i+2nk
=
2\bigl(n(k+1)-i\bigr).
$$
For $k=0$ and $0\le i\le n$, these supply one free class in each even
degree
$$
0,2,\dots,2n.
$$
For $k\ge1$ and $0\le i\le n-1$, they supply one free class in each
successive positive even degree. Thus there is exactly one free
$\ZZ$-summand in every nonnegative even degree.

The remaining monomials
$$
a^n y^k,
\qquad
k\ge1,
$$
are killed by $n+1$ because
$$
(n+1)ya^n=0.
$$
They give a cyclic summand
$$
\ZZ/(n+1)
$$
in ordinary degree
$$
2nk.
$$

Finally, the monomials involving $x$ are
$$
x a^i y^k,
\qquad
0\le i\le n-1,
\quad
k\ge0,
$$
because $x^2=a^nx=0$. Their ordinary degrees are
$$
2n-1-2i+2nk.
$$
As $(i,k)$ varies, these run through every positive odd integer exactly
once, and all such monomials are free. This proves the displayed homology
groups.

:::

:::

::: {.pf-step #s1-6}

The integral cohomology groups of the free loop space of
$\CP^n$ are therefore
$$
\boxed{
H^q(L\CP^n;\ZZ)
\cong
\begin{cases}
\ZZ,
&q\text{ even},\\[1mm]
\ZZ,
&q\text{ odd and }q\ne2nr+1\text{ for every }r\ge1,\\[1mm]
\ZZ\oplus\ZZ/(n+1),
&q=2nr+1\text{ for some }r\ge1.
\end{cases}
}
$$
In particular,
$$
H^1(L\CP^n;\ZZ)\cong\ZZ.
$$


::: pf-proof

Apply the universal coefficient theorem:
$$
0
\to
\operatorname{Ext}
\bigl(
H_{q-1}(L\CP^n),\ZZ
\bigr)
\to
H^q(L\CP^n;\ZZ)
\to
\operatorname{Hom}
\bigl(
H_q(L\CP^n),\ZZ
\bigr)
\to0.
$$

By step [](#s1-5){.pf-ref}, every odd homology group is free cyclic, while every even
homology group has one free cyclic summand and, precisely in degrees
$$
2nr,
\qquad r\ge1,
$$
one additional $\ZZ/(n+1)$ summand.

Therefore every even cohomology group is $\ZZ$. Every odd cohomology
group has a free $\ZZ$ from Hom, and it acquires an additional
$$
\operatorname{Ext}(\ZZ/(n+1),\ZZ)
\cong
\ZZ/(n+1)
$$
exactly one degree after those exceptional even homology degrees, namely in
degree
$$
2nr+1.
$$
The resulting short exact sequence splits because its free quotient is
$$
\ZZ,
$$
so the group is the displayed direct sum.

:::

:::

::: {.pf-step #s1-7}

Since
$$
\CP^1\cong S^2,
$$
step [](#s1-6){.pf-ref} with $n=1$ gives
$$
\boxed{
H^q(LS^2;\ZZ)
\cong
\begin{cases}
\ZZ,&q=0,1,\\
\ZZ,&q\ge2\text{ even},\\
\ZZ\oplus\ZZ/2,&q\ge3\text{ odd}.
\end{cases}
}
$$


::: pf-proof

Substitute $n=1$ into step [](#s1-6){.pf-ref}. The exceptional odd degrees are
$$
2r+1,
\qquad
r\ge1,
$$
which are exactly the odd degrees at least $3$.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} computes the cohomology of
$$
\operatorname{Map}(S^1,S^3).
$$
Step [](#s1-7){.pf-ref} computes the cohomology of
$$
\operatorname{Map}(S^1,S^2),
$$
and step [](#s1-6){.pf-ref} computes the cohomology of
$$
\operatorname{Map}(S^1,\CP^n).
$$

:::

:::

:::
