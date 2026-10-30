---
schema: qual/card@1
id: P-CHAVAN-CA-9-4
kind: problem
title: Zeros of a multivariable complex polynomial are not isolated
classification: {areas: [complex-analysis], topics: [Several Complex Variables]}
relations: []
review: draft
audit:
  - event: source-checked
    by: gpt-5.6-sol
    date: 2026-09-14
    note: A stray dot on the final p in the machine extraction is omitted; the public text rendering of the same source confirms p.
---

::: {.problem}
Let $p$ be a nonconstant complex polynomial in more than one variable.
Show that every open neighborhood of a zero of $p$ contains infinitely many zeros of $p$.
:::

::: {.solution}

Let $p\in\CC[z_1,\ldots,z_n]$ with $n\geq2$, and let $a\in\CC^n$ satisfy
$p(a)=0$.

::: pf

::: {.pf-step #s1-1}

After translating $a$ to the origin and making an invertible complex
linear change of coordinates, it is enough to consider the case
$$
p(0)=0
\qquad\text{and}\qquad
q(\zeta)\coloneqq p(0,\ldots,0,\zeta)
$$
is a nonzero one-variable polynomial.


::: pf-proof

Translation preserves the local zero-set question, so first replace $p(z)$ by
$p(a+z)$. The resulting polynomial is nonzero and vanishes at the origin.
Write it as a sum of homogeneous parts
$$
p=p_1+p_2+\cdots+p_d,
$$
where some $p_j$ is nonzero. Choose $v\in\CC^n$ with $p_j(v)\neq0$. Then
$t\mapsto p(tv)$ is not the zero polynomial. Extend $v$ to a basis of
$\CC^n$ and use that basis as new coordinates, with $v$ as the last basis
vector. In those coordinates, the restriction of $p$ to the last coordinate
axis is the required nonzero polynomial $q$. Invertible affine changes of
coordinates are homeomorphisms, so they preserve the assertion about every
open neighborhood.

:::

:::

::: {.pf-step #s1-2}

Let $U$ be any open neighborhood of $0$ in $\CC^n$. There exist
$\rho>0$ and an open neighborhood $V$ of $0$ in $\CC^{n-1}$ such that
$$
V\times\{\zeta\in\CC:\abs{\zeta}<\rho\}\subseteq U
$$
and $q$ has no zero on the circle $\abs{\zeta}=\rho$.


::: pf-proof

Because $q$ is a nonzero one-variable polynomial with $q(0)=0$, its zeros are
isolated. Hence arbitrarily small positive radii avoid all nonzero zeros of
$q$. Choose such a radius $\rho$ small enough that a product neighborhood of
the displayed form is contained in $U$.

:::

:::

::: {.pf-step #s1-3}

After shrinking $V$ if necessary, for every $z'\in V$ and every
$\abs{\zeta}=\rho$ one has
$$
\abs{p(z',\zeta)-q(\zeta)}<\abs{q(\zeta)}.
$$


::: pf-proof

By step [](#s1-2){.pf-ref},
$$
m\coloneqq\min_{\abs{\zeta}=\rho}\abs{q(\zeta)}>0.
$$
The polynomial $p(z',\zeta)$ converges uniformly to
$p(0,\zeta)=q(\zeta)$ on the compact circle $\abs{\zeta}=\rho$ as
$z'\to0$. Thus $V$ may be shrunk so that
$$
\abs{p(z',\zeta)-q(\zeta)}<m
$$
throughout $V\times\{\abs{\zeta}=\rho\}$.

:::

:::

::: {.pf-step #s1-4}

For every $z'\in V$, the one-variable polynomial
$\zeta\mapsto p(z',\zeta)$ has at least one zero with $\abs{\zeta}<\rho$.


::: pf-proof

By step [](#s1-3){.pf-ref} and Rouché's theorem, $p(z',\cdot)$ and $q$ have the same number
of zeros in the disc $\abs{\zeta}<\rho$, counted with multiplicity. Since
$q(0)=0$, that number is at least one.

:::

:::

::: {.pf-step #s1-5}

The neighborhood $U$ contains infinitely many distinct zeros of $p$.


::: pf-proof

Because $n-1\geq1$, the open set $V\subseteq\CC^{n-1}$ contains infinitely
many distinct points $z'_1,z'_2,\ldots$. By step [](#s1-4){.pf-ref}, choose
$\zeta_k$ with $\abs{\zeta_k}<\rho$ and
$$
p(z'_k,\zeta_k)=0.
$$
Step [](#s1-2){.pf-ref} places every $(z'_k,\zeta_k)$ in $U$, and the points are distinct
because their first $n-1$ coordinates are distinct.

:::

:::

::: {.pf-step #s1-6}

Every open neighborhood of every zero of the original polynomial contains
infinitely many zeros.


::: pf-proof

Step [](#s1-5){.pf-ref} proves the statement in the normalized coordinates, and step [](#s1-1){.pf-ref}
transports it back through the invertible affine change of coordinates.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the required conclusion.

:::

:::

:::
