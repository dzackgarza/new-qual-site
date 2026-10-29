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

::: {.solution}

These denote the total characteristic classes of the tangent bundles. Let
\[
a\in H^1(\mathbb{RP}^n;\mathbb F_2),
\qquad
x\in H^2(\mathbb{CP}^n;\ZZ)
\]
be the standard generators, with $x=c_1(\gamma^*)$ for the dual tautological complex line bundle.

::: pf

::: {.pf-step #s1-1}

For real projective space there is a stable bundle isomorphism
\[
T\mathbb{RP}^n\oplus\varepsilon^1
\cong(n+1)\gamma^1,
\]
where $\gamma^1$ is the tautological real line bundle.


::: pf-proof

At a line $\ell\subset\RR^{n+1}$,
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

::: {.pf-step #s1-2}

Since
\[
w(\gamma^1)=1+a,
\]
the Whitney product formula gives
\[
\boxed{w(T\mathbb{RP}^n)=(1+a)^{n+1}.}
\]


::: pf-proof

Apply total Stiefel--Whitney classes to step [](#s1-1){.pf-ref}. The trivial line has total class $1$, and Whitney multiplicativity gives
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

::: {.pf-step #s1-3}

For complex projective space the Euler sequence gives a stable complex bundle isomorphism
\[
T\mathbb{CP}^n\oplus\varepsilon^1_{\CC}
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

::: {.pf-step #s1-4}

Therefore
\[
\boxed{c(T\mathbb{CP}^n)=(1+x)^{n+1}.}
\]


::: pf-proof

The total Chern class of $\gamma^*$ is $1+x$. Apply Whitney multiplicativity to step [](#s1-3){.pf-ref} and use $c(\varepsilon^1_{\CC})=1$. The formula is interpreted in
\[
H^*(\mathbb{CP}^n;\ZZ)
=\ZZ[x]/(x^{n+1}).
\]
Thus explicitly
\[
c_i(T\mathbb{CP}^n)=\binom{n+1}{i}x^i.
\]

:::

:::

::: {.pf-step #s1-5}

For a complex vector bundle $E$, the Pontryagin class of its underlying real bundle satisfies
\[
p(E_{\RR})=c(E)c(\overline E)
\]
after retaining the even-degree signs, equivalently under the splitting principle
\[
p(E_{\RR})=\prod_j(1+y_j^2)
\]
for Chern roots $y_j$.


::: pf-proof

By definition,
\[
p_i(E_{\RR})=(-1)^ic_{2i}(E_{\RR}\otimes\CC).
\]
There is a natural complex-bundle isomorphism
\[
E_{\RR}\otimes\CC\cong E\oplus\overline E.
\]
If the Chern roots of $E$ are $y_j$, those of $\overline E$ are $-y_j$, and the definition yields the product $\prod_j(1+y_j^2)$.

:::

:::

::: {.pf-step #s1-6}

Applying step [](#s1-5){.pf-ref} to the stable splitting in step [](#s1-3){.pf-ref} gives
\[
\boxed{p(T\mathbb{CP}^n)=(1+x^2)^{n+1}.}
\]


::: pf-proof

Pontryagin classes are stable, so the trivial complex line in step [](#s1-3){.pf-ref} contributes $1$. The underlying real bundle of each copy of $\gamma^*$ has total Pontryagin class
\[
1+c_1(\gamma^*)^2=1+x^2.
\]
Whitney multiplicativity over the $(n+1)$ copies gives the displayed formula. Explicitly,
\[
p_i(T\mathbb{CP}^n)=\binom{n+1}{i}x^{2i}.
\]

:::

:::

::: {.pf-step #s1-7}

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

These are steps [](#s1-2){.pf-ref} and [](#s1-4){.pf-ref}, and [](#s1-6){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} gives all three requested total characteristic classes.

:::

:::

:::
