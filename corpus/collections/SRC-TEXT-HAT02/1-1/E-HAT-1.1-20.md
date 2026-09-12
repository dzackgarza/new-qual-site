---
schema: qual/card@1
id: E-HAT-1.1-20
kind: problem
title: Loops extending to loop of maps $X \to X$ lie in the center of $\pi_1(X)$
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Center of Groups
  - Homotopy
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 1.1, Exercise 20; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Applied Lemma 1.19 with both endpoint maps equal to the identity, forcing conjugation by the basepoint track to be the identity automorphism.
---

Suppose $f_t: X \to X$ is a homotopy such that $f_0$ and $f_1$ are each the identity map.
Use Lemma 1.19 to show that for any $x_0 \in X$, the loop $f_t(x_0)$ represents an element of the center of $\pi_1(X, x_0)$.
[One can interpret the result as saying that a loop represents an element of the center of $\pi_1(X)$ if it extends to a loop of maps $X \to X$.]

::: {.solution}
Fix $x_0\in X$ and define
\[
h(t)=f_t(x_0).
\]

<1>1. The path $h$ is a loop based at $x_0$.
::: {.proof}
Since
\[
f_0=f_1=\operatorname{id}_X,
\]
one has
\[
h(0)=f_0(x_0)=x_0=f_1(x_0)=h(1).
\]
:::

<1>2. Lemma 1.19 gives
\[
(f_0)_*=\beta_h\,(f_1)_*.
\]
::: {.proof}
Lemma 1.19 states that for a homotopy $f_t:X\to X$ and the basepoint track $h(t)=f_t(x_0)$, the induced maps satisfy exactly this relation after the appropriate change of basepoint by $h$.
Here both endpoint maps take $x_0$ to $x_0$, so all three maps act on
\[
\pi_1(X,x_0).
\]
:::

<1>3. Therefore
\[
\beta_h=\operatorname{id}_{\pi_1(X,x_0)}.
\]
::: {.proof}
Both $f_0$ and $f_1$ are the identity map, so
\[
(f_0)_*=(f_1)_*=\operatorname{id}_{\pi_1(X,x_0)}.
\]
Substituting into <1>2 gives
\[
\operatorname{id}=\beta_h\operatorname{id}=\beta_h.
\]
:::

<1>4. For every $[\gamma]\in\pi_1(X,x_0)$,
\[
[h][\gamma][h]^{-1}=[\gamma].
\]
::: {.proof}
By the definition of the change-of-basepoint automorphism associated to the loop $h$,
\[
\beta_h([\gamma])=[h\cdot\gamma\cdot\bar h]
=[h][\gamma][h]^{-1}.
\]
Now use <1>3.
:::

<1>5. Hence $[h]$ lies in the center of $\pi_1(X,x_0)$.
::: {.proof}
Multiplying the equality in <1>4 on the right by $[h]$ gives
\[
[h][\gamma]=[\gamma][h]
\]
for every $[\gamma]\in\pi_1(X,x_0)$.
This is precisely the condition that $[h]$ be central.
:::
:::
