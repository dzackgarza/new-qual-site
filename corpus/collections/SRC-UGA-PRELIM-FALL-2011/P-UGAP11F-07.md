---
schema: qual/card@1
id: P-UGAP11F-07
kind: problem
title: Characterize when $f(f^{-1}(S))=S$
classification:
  areas: [prelim]
  topics:
  - Functions and Relations
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Let $f:X\to Y$ be a map of sets and let $S\subseteq Y$. Give, with proof, necessary and sufficient conditions for
$$
f\bigl(f^{-1}(S)\bigr)=S.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For every map $f:X\to Y$ and every subset $S\subseteq Y$,
$$
\boxed{
f\bigl(f^{-1}(S)\bigr)
=
S\cap f(X)}.
$$


::: pf-proof

First suppose
$$
y\in f(f^{-1}(S)).
$$
Then
$$
y=f(x)
$$
for some
$$
x\in f^{-1}(S).
$$
The latter condition means
$$
f(x)\in S.
$$
Thus
$$
y\in S
$$
and also
$$
y\in f(X),
$$
so
$$
y\in S\cap f(X).
$$

Conversely, suppose
$$
y\in S\cap f(X).
$$
Since
$$
y\in f(X),
$$
there is some $x\in X$ with
$$
f(x)=y.
$$
Because $y\in S$, this $x$ belongs to
$$
f^{-1}(S).
$$
Therefore
$$
y=f(x)\in f(f^{-1}(S)).
$$
This proves the equality.

:::

:::

::: {.pf-step #s1-2}

One has
$$
f(f^{-1}(S))=S
$$
if and only if
$$
\boxed{S\subseteq f(X)}.
$$


::: pf-proof

By step [](#s1-1){.pf-ref},
$$
f(f^{-1}(S))
=
S\cap f(X).
$$
Thus
$$
f(f^{-1}(S))=S
$$
if and only if
$$
S\cap f(X)=S.
$$
The latter equality holds exactly when every element of $S$ lies in $f(X)$, i.e.
$$
S\subseteq f(X).
$$

:::

:::

::: {.pf-step #s1-3}

Equivalently, the necessary and sufficient condition is that every point of $S$ have at least one preimage under $f$.


::: pf-proof

The condition
$$
S\subseteq f(X)
$$
means precisely that for every $y\in S$ there exists some $x\in X$ such that
$$
f(x)=y.
$$

:::

:::

::: pf-qed

Steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref} give the requested necessary and sufficient condition.

:::

:::

:::
