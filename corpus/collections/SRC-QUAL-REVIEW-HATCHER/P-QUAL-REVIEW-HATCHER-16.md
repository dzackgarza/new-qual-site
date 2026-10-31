---
schema: qual/card@1
id: P-QUAL-REVIEW-HATCHER-16
kind: problem
title: Degree of a normalized polynomial counts roots in the unit disk
classification:
  areas: [topology]
  topics:
  - Degree of a Map
  - Winding Number
  - Argument Principle
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against practice problem 16 in assets/attachments/Qual_Review_Selection_of_Hatcher_Problems_-_Unknown_extracted.md.
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: The deterministic extraction writes the initial inclusion as “S^1 ∈ C”; it is normalized here to the evident inclusion arrow.
---

::: {.problem}
Let $f\in\CC[z]$ and assume that $f$ has no roots on the unit circle.
Consider
$$
S^1\hookrightarrow\CC\xrightarrow{f}\CC\setminus\{0\}\xrightarrow{\pi}S^1,
$$
where $\pi$ is the norm map.
Prove that the degree of this composition equals the number of roots of $f$ inside the unit circle.
:::

::: {.solution}

Write the polynomial as
$$
\boxed{
f(z)=c\prod_{j=1}^{d}(z-a_j)},
$$
where the roots $a_j$ are listed with multiplicity and
$$
c\in\CC^\times.
$$

Because $f$ has no roots on $S^1$,
$$
\abs{a_j}\ne1
$$
for every $j$.

Let
$$
F:S^1\to S^1
$$
be the normalized map
$$
F(z)=\frac{f(z)}{\abs{f(z)}}.
$$

::: pf

::: {.pf-step #s1-1}

For $z\in S^1$,
$$
\boxed{
F(z)
=
\frac{c}{\abs{c}}
\prod_{j=1}^{d}
\frac{z-a_j}{\abs{z-a_j}}}.
$$


::: pf-proof

Using multiplicativity of the complex modulus,
$$
\abs{f(z)}
=
\abs{c}\prod_{j=1}^{d}\abs{z-a_j}.
$$
Divide the factorization of $f$ by this expression.

:::

:::

::: {.pf-step #s1-2}

The homotopy
$$
H:S^1\times[0,1]\to\CC^\times,
\qquad
H(z,t)=z-ta
$$
never takes the value $0$.


::: pf-proof

If
$$
z-ta=0,
$$
then
$$
\abs{z}=t\abs{a}\le\abs{a}<1,
$$
contradicting
$$
\abs{z}=1.
$$

:::

:::

::: pf-step

After normalization,
$$
\widetilde H(z,t)
=
\frac{z-ta}{\abs{z-ta}}
$$
is a homotopy in $S^1$ from $g_a$ to the identity map $z\mapsto z$.


::: pf-proof

At $t=1$,
$$
\widetilde H(z,1)=g_a(z).
$$
At $t=0$,
$$
\widetilde H(z,0)=\frac z{\abs{z}}=z
$$
because $z\in S^1$. Step [](#s1-2){.pf-ref} guarantees the normalization is defined throughout.

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\boxed{\deg g_a=1}
$$
when
$$
\abs{a}<1.
$$


::: pf-proof

Degree is invariant under homotopy, and the identity map of $S^1$ has degree $1$.

:::

:::

::: {.pf-step #s1-5}

The homotopy
$$
K:S^1\times[0,1]\to\CC^\times,
\qquad
K(z,t)=tz-a
$$
never takes the value $0$.


::: pf-proof

If
$$
tz-a=0,
$$
then
$$
\abs{a}=t\abs{z}\le1,
$$
contradicting
$$
\abs{a}>1.
$$

:::

:::

::: pf-step

After normalization,
$$
\widetilde K(z,t)
=
\frac{tz-a}{\abs{tz-a}}
$$
is a homotopy from $g_a$ to the constant map
$$
z\longmapsto -\frac a{\abs{a}}.
$$


::: pf-proof

At $t=1$,
$$
\widetilde K(z,1)=g_a(z).
$$
At $t=0$,
$$
\widetilde K(z,0)
=
\frac{-a}{\abs{a}},
$$
independent of $z$. Step [](#s1-5){.pf-ref} guarantees the denominator is never zero.

:::

:::

::: {.pf-step #s1-7}

Therefore
$$
\boxed{\deg g_a=0}
$$
when
$$
\abs{a}>1.
$$


::: pf-proof

A constant map $S^1\to S^1$ has degree $0$, and degree is homotopy invariant.

:::

:::

::: {.pf-step #s1-8}

If
$$
u,v:S^1\to S^1,
$$
then for the pointwise product
$$
(uv)(z)=u(z)v(z),
$$
one has
$$
\boxed{
\deg(uv)=\deg u+\deg v}.
$$


::: pf-proof

On
$$
H_1(S^1;\ZZ)\cong\ZZ,
$$
the multiplication map
$$
m:S^1\times S^1\to S^1,
\qquad
m(\zeta,\eta)=\zeta\eta,
$$
induces
$$
m_*(r,s)=r+s.
$$
The pointwise product is
$$
uv=m\circ(u,v),
$$
so its induced map on $H_1$ multiplies by
$$
\deg u+\deg v.
$$

:::

:::

::: {.pf-step #s1-9}

The constant factor
$$
z\longmapsto\frac c{\abs{c}}
$$
has degree $0$.


::: pf-proof

Every constant map has degree $0$.

:::

:::

::: {.pf-step #s1-10}

Hence
$$
\deg F
=
\sum_{j=1}^{d}\deg g_{a_j}.
$$


::: pf-proof

Apply step [](#s1-8){.pf-ref} repeatedly to the product decomposition in step [](#s1-1){.pf-ref}, and use step [](#s1-9){.pf-ref} for the leading constant.

:::

:::

::: {.pf-step #s1-11}

Each root with
$$
\abs{a_j}<1
$$
contributes $1$, and each root with
$$
\abs{a_j}>1
$$
contributes $0$.


::: pf-proof

Use steps [](#s1-4){.pf-ref} and [](#s1-7){.pf-ref}.

:::

:::

::: {.pf-step #s1-12}

Therefore
$$
\boxed{
\deg F
=
\#\{j:\abs{a_j}<1\}},
$$
where roots are counted with multiplicity.


::: pf-proof

The roots $a_j$ were listed with multiplicity in the factorization of $f$, and step [](#s1-10){.pf-ref} sums exactly the contributions from step [](#s1-11){.pf-ref}.

:::

:::

::: {.pf-step #s1-13}

Thus the degree of
$$
S^1\hookrightarrow\CC
\xrightarrow{f}
\CC\setminus\{0\}
\xrightarrow{\pi}
S^1
$$
equals the number of roots of $f$ inside the unit circle, counted with multiplicity.


::: pf-proof

The displayed composite is exactly
$$
z\longmapsto\frac{f(z)}{\abs{f(z)}}=F(z),
$$
whose degree was computed in step [](#s1-12){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-13){.pf-ref} is the required conclusion.

:::

:::

:::
