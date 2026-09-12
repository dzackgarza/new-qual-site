---
schema: qual/card@1
id: E-HAT-2.1-16
kind: problem
title: When relative homology $H_0(X,A)$ and $H_1(X,A)$ vanish
classification:
  areas:
  - topology
  topics:
  - Homology
  - Relative Homology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.1, Exercise 16; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Read H_0 maps componentwise in the long exact sequence of the pair and applied the exact-sequence criterion from the preceding exercise.
---

(a) Show that $H_0(X, A) = 0$ iff $A$ meets each path-component of $X$.

(b) Show that $H_1(X, A) = 0$ iff $H_1(A) \to H_1(X)$ is surjective and each path-component of $X$ contains at most one path-component of $A$.

::: {.solution}
Use the long exact sequence of the pair $(X,A)$.

<1>1. One has
\[
\boxed{H_0(X,A)=0
\iff A\text{ meets every path-component of }X.}
\]
::: {.proof}
The tail of the long exact sequence is
\[
H_0(A)\xrightarrow{i_*}H_0(X)\to H_0(X,A)\to0.
\]
Thus $H_0(X,A)=0$ iff
\[
i_*:H_0(A)\to H_0(X)
\]
is surjective.

The group $H_0(X)$ is free on the path-components of $X$, and a component of $A$ maps to the generator of the component of $X$ containing it. Hence $i_*$ is surjective exactly when every component of $X$ contains a point, equivalently a component, of $A$.
:::

<1>2. One has
\[
H_1(X,A)=0
\]
if and only if
\[
H_1(A)\to H_1(X)
\]
is surjective and
\[
H_0(A)\to H_0(X)
\]
is injective.
::: {.proof}
Use the exact segment
\[
H_1(A)\to H_1(X)\to H_1(X,A)
\to H_0(A)\to H_0(X)
\]
and apply the five-term criterion proved in Exercise 15.
:::

<1>3. The map
\[
H_0(A)\to H_0(X)
\]
is injective if and only if each path-component of $X$ contains at most one path-component of $A$.
::: {.proof}
Again use the component bases. Two distinct component generators of $H_0(A)$ have the same image exactly when their components lie in the same component of $X$. Thus injectivity is equivalent to the stated condition.
:::

<1>4. Hence
\[
\boxed{H_1(X,A)=0}
\]
if and only if $H_1(A)\to H_1(X)$ is surjective and every path-component of $X$ contains at most one path-component of $A$.
::: {.proof}
Combine <1>2 and <1>3.
:::
:::
