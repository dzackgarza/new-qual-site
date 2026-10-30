---
schema: qual/card@1
id: P-WESCA08-II1
kind: problem
title: 'Laurent series of $1/(z^2+1)^2$ about $i$'
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problems, problem 1 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md.
---

::: {.problem}
Find the Laurent series centered at $i$ for
$$
f(z)=\frac1{(z^2+1)^2},
$$
and determine where the series converges.
:::

::: {.solution}

Set
$$
w=z-i.
$$
Then
$$
z+i=w+2i
$$
and
$$
\boxed{
f(z)
=
\frac1{w^2(w+2i)^2}}.
$$

## The annulus $0<\abs{w}<2$

::: pf

::: pf-step

Rewrite
$$
\frac1{(w+2i)^2}
=
\frac1{(2i)^2}
\frac1{\left(1+\frac{w}{2i}\right)^2}.
$$


::: pf-proof

Factor $2i$ out of $w+2i$.

:::

:::

::: {.pf-step #s1-2}

For $\abs{u}<1$,
$$
\boxed{
\frac1{(1+u)^2}
=
\sum_{n=0}^{\infty}
(-1)^n(n+1)u^n}.
$$


::: pf-proof

Differentiate the geometric series
$$
\frac1{1+u}
=
\sum_{n=0}^{\infty}(-1)^n u^n
$$
term by term:
$$
-\frac1{(1+u)^2}
=
\sum_{n=1}^{\infty}
(-1)^n n u^{n-1}.
$$
Reindex.

:::

:::

::: pf-step

Therefore, when
$$
\abs{\frac{w}{2i}}<1,
$$
one has
$$
\frac1{(w+2i)^2}
=
-\frac14
\sum_{n=0}^{\infty}
(-1)^n(n+1)
\left(\frac{w}{2i}\right)^n.
$$


::: pf-proof

Substitute
$$
u=\frac{w}{2i}
$$
into step [](#s1-2){.pf-ref} and use
$$
(2i)^2=-4.
$$

:::

:::

::: {.pf-step #s1-4}

Multiplying by $w^{-2}$,
$$
\boxed{
f(z)
=
-\frac1{4w^2}
\sum_{n=0}^{\infty}
(-1)^n(n+1)
\left(\frac{w}{2i}\right)^n}.
$$


::: pf-proof

Use the factorization
$$
f(z)=w^{-2}(w+2i)^{-2}.
$$

:::

:::

::: {.pf-step #s1-5}

Equivalently,
$$
\boxed{
f(z)
=
-\frac1{4(z-i)^2}
-\frac{i}{4(z-i)}
+\frac3{16}
+\frac{i}{8}(z-i)
-\frac5{64}(z-i)^2
+\cdots }.
$$


::: pf-proof

Expand the first few terms of the series in step [](#s1-4){.pf-ref}.

:::

:::

::: {.pf-step #s1-6}

This Laurent series converges exactly on
$$
\boxed{
0<\abs{z-i}<2}.
$$


::: pf-proof

The geometric-series condition is
$$
\abs{\frac{w}{2i}}<1,
$$
equivalently
$$
\abs{w}<2.
$$
The center $w=0$ is a pole, so it is excluded. The boundary circle
$$
\abs{w}=2
$$
contains the other pole $w=-2i$, corresponding to $z=-i$, so the
maximal annulus cannot extend across it.

:::

:::

::: pf-step

Rewrite
$$
\frac1{(w+2i)^2}
=
\frac1{w^2}
\frac1{\left(1+\frac{2i}{w}\right)^2}.
$$


::: pf-proof

Factor $w$ out of $w+2i$.

:::

:::

::: {.pf-step #s1-8}

If
$$
\abs{\frac{2i}{w}}<1,
$$
then
$$
\frac1{(w+2i)^2}
=
\frac1{w^2}
\sum_{n=0}^{\infty}
(-1)^n(n+1)
\left(\frac{2i}{w}\right)^n.
$$


::: pf-proof

Apply step [](#s1-2){.pf-ref} with
$$
u=\frac{2i}{w}.
$$

:::

:::

::: {.pf-step #s1-9}

Hence
$$
\boxed{
f(z)
=
\sum_{n=0}^{\infty}
(-1)^n(n+1)(2i)^n
\,w^{-n-4}}.
$$


::: pf-proof

Multiply step [](#s1-8){.pf-ref} by the additional factor $w^{-2}$ from
$$
f(z)=w^{-2}(w+2i)^{-2}.
$$

:::

:::

::: {.pf-step #s1-10}

The first terms are
$$
\boxed{
f(z)
=
\frac1{(z-i)^4}
-\frac{4i}{(z-i)^5}
-\frac{12}{(z-i)^6}
+\frac{32i}{(z-i)^7}
+\cdots }.
$$


::: pf-proof

Use
$$
n=0,1,2,3
$$
in step [](#s1-9){.pf-ref}.

:::

:::

::: {.pf-step #s1-11}

The exterior Laurent series converges exactly on
$$
\boxed{\abs{z-i}>2}.
$$


::: pf-proof

The condition
$$
\abs{\frac{2i}{w}}<1
$$
is equivalent to
$$
\abs{w}>2.
$$
Again the circle $\abs{w}=2$ contains the singularity $w=-2i$, so this is
the maximal exterior annulus.

:::

:::

::: pf-step

Thus the complete Laurent expansions centered at $i$ are the series
in steps [](#s1-4){.pf-ref} and [](#s1-9){.pf-ref} on the two maximal annuli separated by
$$
\abs{z-i}=2.
$$


::: pf-proof

The only finite singularities are
$$
z=i
\qquad\text{and}\qquad
z=-i.
$$
Their distances from the center $i$ are $0$ and $2$, so these are
exactly the maximal Laurent annuli.

:::

:::

::: pf-qed

Steps [](#s1-4){.pf-ref} through [](#s1-6){.pf-ref} give the local Laurent expansion and its region, while
steps [](#s1-9){.pf-ref} through [](#s1-11){.pf-ref} give the exterior expansion and its region.

:::

:::

:::
