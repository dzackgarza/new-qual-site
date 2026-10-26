---
schema: qual/card@1
id: P-MAXAT-6-01
kind: problem
title: Maxim algebraic topology 6.1
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against section 6, problem 1 of the retained Laurentiu Maxim Problems in Algebraic Topology PDF.
---

::: {.problem}
Calculate $w ( \mathbb { R P } ^ { n } ) , c ( \mathbb { C P } ^ { n } ) , p ( \mathbb { C P } ^ { n } )$
:::

These denote the total characteristic classes of the tangent bundles. Let
\[
a\in H^1(\mathbb{RP}^n;\mathbb F_2),
\qquad
x\in H^2(\mathbb{CP}^n;\mathbb Z)
\]
be the standard generators, with $x=c_1(\gamma^*)$ for the dual tautological complex line bundle.

::: pf

::: pf-step

For real projective space there is a stable bundle isomorphism
\[
T\mathbb{RP}^n\oplus\varepsilon^1
\cong(n+1)\gamma^1,
\]
where $\gamma^1$ is the tautological real line bundle.


::: pf-proof

At a line $\ell\subset\mathbb R^{n+1}$,
\[
T_{\ell}\mathbb{RP}^n\cong\operatorname{Hom}(\ell,\ell^\perp).
\]
Since $\gamma^1$ is a real line bundle, tensoring the decomposition
\[
\gamma^1\oplus(\gamma^1)^\perp\cong\varepsilon^{n+1}
\]
by $\gamma^1$ gives
\[
\varepsilon^1\oplus T\mathbb{RP}^n
\cong(n+1)\gamma^1,
\]
because $\gamma^1\otimes\gamma^1\cong\varepsilon^1$.

:::

:::

::: pf-step

Since
\[
w(\gamma^1)=1+a,
\]
the Whitney product formula gives
\[
\boxed{w(T\mathbb{RP}^n)=(1+a)^{n+1}.}
\]


::: pf-proof

Apply total Stiefel--Whitney classes to step <1>1. The trivial line has total class $1$, and Whitney multiplicativity gives
\[
w(T\mathbb{RP}^n)=(1+a)^{n+1}
\]
in
\[
H^*(\mathbb{RP}^n;\mathbb F_2)
=\mathbb F_2[a]/(a^{n+1}).
\]

:::

:::

::: pf-step

For complex projective space the Euler sequence gives a stable complex bundle isomorphism
\[
T\mathbb{CP}^n\oplus\varepsilon^1_{\mathbb C}
\cong(n+1)\gamma^*.
\]


::: pf-proof

The holomorphic Euler sequence is
\[
0\to\mathcal O
\to\mathcal O(1)^{\oplus(n+1)}
\to T\mathbb{CP}^n\to0.
\]
As complex topological bundles, $\mathcal O(1)=\gamma^*$, and a short exact sequence splits after choosing a Hermitian metric, yielding the stable isomorphism.

:::

:::

::: pf-step

Therefore
\[
\boxed{c(T\mathbb{CP}^n)=(1+x)^{n+1}.}
\]


::: pf-proof

The total Chern class of $\gamma^*$ is $1+x$. Apply Whitney multiplicativity to step <1>3 and use $c(\varepsilon^1_{\mathbb C})=1$. The formula is interpreted in
\[
H^*(\mathbb{CP}^n;\mathbb Z)
=\mathbb Z[x]/(x^{n+1}).
\]
Thus explicitly
\[
c_i(T\mathbb{CP}^n)=\binom{n+1}{i}x^i.
\]

:::

:::

::: pf-step

For a complex vector bundle $E$, the Pontryagin class of its underlying real bundle satisfies
\[
p(E_{\mathbb R})=c(E)c(\overline E)
\]
after retaining the even-degree signs, equivalently under the splitting principle
\[
p(E_{\mathbb R})=\prod_j(1+y_j^2)
\]
for Chern roots $y_j$.


::: pf-proof

By definition,
\[
p_i(E_{\mathbb R})=(-1)^ic_{2i}(E_{\mathbb R}\otimes\mathbb C).
\]
There is a natural complex-bundle isomorphism
\[
E_{\mathbb R}\otimes\mathbb C\cong E\oplus\overline E.
\]
If the Chern roots of $E$ are $y_j$, those of $\overline E$ are $-y_j$, and the definition yields the product $\prod_j(1+y_j^2)$.

:::

:::

::: pf-step

Applying step <1>5 to the stable splitting in step <1>3 gives
\[
\boxed{p(T\mathbb{CP}^n)=(1+x^2)^{n+1}.}
\]


::: pf-proof

Pontryagin classes are stable, so the trivial complex line in step <1>3 contributes $1$. The underlying real bundle of each copy of $\gamma^*$ has total Pontryagin class
\[
1+c_1(\gamma^*)^2=1+x^2.
\]
Whitney multiplicativity over the $(n+1)$ copies gives the displayed formula. Explicitly,
\[
p_i(T\mathbb{CP}^n)=\binom{n+1}{i}x^{2i}.
\]

:::

:::

::: pf-step

Hence
\[
\boxed{w(\mathbb{RP}^n)=(1+a)^{n+1},}
\]
\[
\boxed{c(\mathbb{CP}^n)=(1+x)^{n+1},}
\]
and
\[
\boxed{p(\mathbb{CP}^n)=(1+x^2)^{n+1}.}
\]


::: pf-proof

These are steps <1>2, <1>4, and <1>6.

:::

:::

::: pf-qed

Step <1>7 gives all three requested total characteristic classes.

:::

:::
