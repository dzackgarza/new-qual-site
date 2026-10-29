---
schema: qual/card@1
id: P-UCLARA16F-10
kind: problem
title: Filled Julia set of $z^2-1$
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Fall 2016, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Consider the quadratic polynomial $f(z)=z^2-1$ on $\CC$.
We are interested in the iterates $f^n$ of $f$, defined by $f^0=\operatorname{id}_{\CC}$ and
\[
f^n=\underbrace{f\circ\cdots\circ f}_{n\text{ factors}}
\]
for $n\in\NN$.

(a) Find an explicit constant $M>0$ such that for each $z\in\CC$ either (i) $|f^n(z)|\to\infty$ as $n\to\infty$, or (ii) $|f^n(z)|\le M$ for all $n\in\NN_0$.

(b) Let $U$ be the set of all $z\in\CC$ for which (i) holds and $K$ the set of all $z\in\CC$ for which (ii) holds.
Show that $U$ is open and $K$ is compact without “holes”, i.e. $\CC\setminus K$ has no bounded connected components.
:::

::: {.solution}

Let
\[
f(z)=z^2-1.
\]

## Part (a)

We claim that
\[
\boxed{M=2}
\]
works.

::: pf

::: {.pf-step #s1-1}

If
\[
|w|>2,
\]
then
\[
\boxed{
|f(w)|
\ge
|w|^2-1}.
\]


::: pf-proof

By the reverse triangle inequality,
\[
|w^2-1|
\ge
\bigl||w|^2-1\bigr|
=
|w|^2-1,
\]
since \(|w|>1\).

:::

:::

::: {.pf-step #s1-2}

If
\[
|w|>2,
\]
then
\[
\boxed{
|w|^2-1>\frac32|w|}.
\]


::: pf-proof

For \(r=|w|>2\),
\[
r^2-1-\frac32r
=
\left(r-2\right)\left(r+\frac12\right)
>0.
\]

:::

:::

::: {.pf-step #s1-3}

Hence if
\[
|w|>2,
\]
then
\[
\boxed{
|f(w)|>\frac32|w|>2}.
\]


::: pf-proof

Combine steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

For every \(m\ge0\),
\[
\boxed{
|f^{N+m}(z)|
>
\left(\frac32\right)^m
|f^N(z)|}.
\]


::: pf-proof

Use induction. The case \(m=0\) is equality. If the bound holds at \(m\), then in particular
\[
|f^{N+m}(z)|>2,
\]
so step [](#s1-3){.pf-ref} gives
\[
|f^{N+m+1}(z)|
>
\frac32|f^{N+m}(z)|
>
\left(\frac32\right)^{m+1}|f^N(z)|.
\]

:::

:::

::: {.pf-step #s1-5}

Therefore
\[
\boxed{
|f^n(z)|\to\infty}.
\]


::: pf-proof

The lower bound in step [](#s1-4){.pf-ref} grows geometrically to \(+\infty\).

:::

:::

::: {.pf-step #s1-6}

Consequently, if the orbit does not tend to infinity, then
\[
\boxed{
|f^n(z)|\le2}
\]
for every \(n\ge0\).


::: pf-proof

If some iterate had modulus \(>2\), step [](#s1-5){.pf-ref} would force escape.

:::

:::

::: {.pf-step #s1-7}

Thus for every \(z\in\CC\), exactly one of the following holds:
- \(|f^n(z)|\to\infty\);
- \(|f^n(z)|\le2\) for all \(n\ge0\).


::: pf-proof

Step [](#s1-5){.pf-ref} handles any orbit that ever leaves the closed disk of radius \(2\), while step [](#s1-6){.pf-ref} handles every remaining orbit.

:::

:::

::: {.pf-step #s1-8}

Hence
\[
\boxed{M=2}
\]
is an admissible constant.


::: pf-proof

This is exactly the dichotomy in step [](#s1-7){.pf-ref}.

:::

:::

::: {.pf-step #s1-9}

One has
\[
\boxed{
U
=
\bigcup_{N=0}^{\infty}
\{z:|f^N(z)|>2\}}.
\]


::: pf-proof

If \(z\in U\), then eventually \(|f^N(z)|>2\). Conversely, if some iterate has modulus \(>2\), step [](#s1-5){.pf-ref} gives escape.

:::

:::

::: {.pf-step #s1-10}

For each \(N\),
\[
\{z:|f^N(z)|>2\}
\]
is open.


::: pf-proof

The iterate \(f^N\) is a polynomial, hence continuous, and
\[
\{w:|w|>2\}
\]
is open.

:::

:::

::: {.pf-step #s1-11}

Therefore
\[
\boxed{U\text{ is open}.}
\]


::: pf-proof

Use steps [](#s1-9){.pf-ref} through [](#s1-10){.pf-ref} and closure of open sets under arbitrary unions.

:::

:::

::: pf-step

One has
\[
\boxed{
K=\CC\setminus U}.
\]


::: pf-proof

Part (a), step [](#s1-7){.pf-ref}, gives the exact dichotomy between escape and boundedness by \(2\).

:::

:::

::: {.pf-step #s1-13}

Hence
\[
\boxed{K\text{ is closed}.}
\]


::: pf-proof

It is the complement of the open set \(U\).

:::

:::

::: {.pf-step #s1-14}

Also,
\[
\boxed{
K\subseteq\{z:|z|\le2\}}.
\]


::: pf-proof

The defining condition for \(K\) includes the case \(n=0\):
\[
|f^0(z)|=|z|\le2.
\]

:::

:::

::: {.pf-step #s1-15}

Therefore
\[
\boxed{K\text{ is compact}.}
\]


::: pf-proof

The set \(K\) is closed by step [](#s1-13){.pf-ref} and bounded by step [](#s1-14){.pf-ref}. Apply Heine--Borel in \(\CC\cong\RR^2\).

:::

:::

::: {.pf-step #s1-16}

The boundary of \(V\) satisfies
\[
\boxed{
\partial V\subseteq K}.
\]


::: pf-proof

Since \(V\) is a connected component of the open set \(U\), no boundary point of \(V\) can lie in \(U\). Indeed, if \(z_0\in\partial V\cap U\), then because \(U\) is open there is a connected disk
\[
D(z_0,\rho)\subseteq U.
\]
Because \(z_0\in\partial V\), this disk meets \(V\). Thus the disk and \(V\) lie in the same connected component of \(U\), forcing \(z_0\in V\), contradiction. Hence
\[
\partial V\subseteq\CC\setminus U=K.
\]

:::

:::

::: {.pf-step #s1-17}

For every \(n\ge0\) and every \(z\in\partial V\),
\[
\boxed{
|f^n(z)|\le2}.
\]


::: pf-proof

By step [](#s1-16){.pf-ref},
\[
z\in K,
\]
and this is the defining property of \(K\).

:::

:::

::: {.pf-step #s1-18}

For each fixed \(n\), the maximum modulus principle gives
\[
\boxed{
|f^n(z)|\le2}
\]
for every \(z\in V\).


::: pf-proof

The domain \(V\) is bounded, and the polynomial \(f^n\) is holomorphic on a neighborhood of \(\overline V\) and continuous there. By step [](#s1-17){.pf-ref}, its modulus is at most \(2\) on \(\partial V\). The maximum modulus principle therefore gives the same bound throughout \(V\).

:::

:::

::: {.pf-step #s1-19}

Hence every \(z\in V\) satisfies
\[
|f^n(z)|\le2
\]
for all \(n\ge0\).


::: pf-proof

Step [](#s1-18){.pf-ref} holds for each \(n\).

:::

:::

::: pf-step

Therefore
\[
V\subseteq K.
\]


::: pf-proof

Step [](#s1-19){.pf-ref} is exactly the defining condition for membership in \(K\).

:::

:::

::: {.pf-step #s1-21}

This contradicts
\[
V\subseteq U=\CC\setminus K.
\]


::: pf-proof

A set cannot be contained simultaneously in \(K\) and its complement.

:::

:::

::: pf-step

Therefore \(U\) has no bounded connected components.


::: pf-proof

The assumption of a bounded connected component led to the contradiction in step [](#s1-21){.pf-ref}.

:::

:::

::: {.pf-step #s1-23}

Equivalently,
\[
\boxed{
K\text{ has no holes}.}
\]


::: pf-proof

By definition in the problem, “no holes” means that \(\CC\setminus K\) has no bounded connected components.

:::

:::

::: pf-qed

Step [](#s1-8){.pf-ref} proves part (a); steps [](#s1-11){.pf-ref} and [](#s1-15){.pf-ref} prove openness of \(U\) and compactness of \(K\); step [](#s1-23){.pf-ref} proves that \(K\) has no holes.

:::

:::

:::
