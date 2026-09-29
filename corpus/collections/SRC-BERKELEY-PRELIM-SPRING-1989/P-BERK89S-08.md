---
schema: qual/card@1
id: P-BERK89S-08
kind: problem
title: A holomorphic disk self-map with two interior fixed points is the identity
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-22
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: >-
    Conjugated one fixed point to the origin and applied the equality case of
    Schwarz's lemma at the second, nonzero fixed point.
---

::: {.problem}
Let $f$ be analytic from the open unit disk $D$ to itself. Suppose there are distinct $a,b\in D$ such that
\[
f(a)=a,
\qquad
f(b)=b.
\]
Prove that
\[
f(z)=z
\]
for all $z\in D$.
:::

::: {.solution}
Set
$$
\phi_a(z)=\frac{z-a}{1-\overline a z},
$$
the standard automorphism of $D$ carrying $a$ to $0$.

::: pf

::: {.pf-step #g-defined-fixes-two}
The map
$$
g=\phi_a\circ f\circ\phi_a^{-1}:D\longrightarrow D
$$
is analytic and fixes both $0$ and the nonzero point $c=\phi_a(b)$.

::: pf-proof
Because $\phi_a$ is a biholomorphic automorphism of $D$, the map $g$ is an
analytic self-map of $D$. Since $f(a)=a$ and $\phi_a(a)=0$,
$$
g(0)=\phi_a(f(a))=0.
$$
Also, with $c=\phi_a(b)$,
$$
g(c)=\phi_a(f(b))=\phi_a(b)=c.
$$
The points $a$ and $b$ are distinct and $\phi_a$ is injective, so
$c\neq0$.
:::

:::

::: {.pf-step #schwarz-rotation}
There exists $\eta\in\CC$ with $\abs{\eta}=1$ such that
$$
g(z)=\eta z
$$
for every $z\in D$.

::: pf-proof
Since $g:D\to D$ is analytic and $g(0)=0$, Schwarz's lemma gives
$$
\abs{g(z)}\leq\abs{z}
$$
for every $z\in D$. By step [](#g-defined-fixes-two){.pf-ref}, $g(c)=c$ for some $c\neq0$, so equality
holds at the nonzero point $c$:
$$
\abs{g(c)}=\abs{c}.
$$
The equality case of Schwarz's lemma therefore implies that
$g(z)=\eta z$ for some $\eta$ with $\abs{\eta}=1$.
:::

:::

::: {.pf-step #g-is-identity}
The map $g$ is the identity on $D$.

::: pf-proof
By steps [](#g-defined-fixes-two){.pf-ref} and [](#schwarz-rotation){.pf-ref},
$$
c=g(c)=\eta c.
$$
Since $c\neq0$, this gives $\eta=1$. Hence $g(z)=z$ for every $z\in D$.
:::

:::

::: {.pf-step #f-is-identity-boxed}
For every $z\in D$,
$$
\boxed{f(z)=z}.
$$

::: pf-proof
The definition of $g$ gives
$$
f=\phi_a^{-1}\circ g\circ\phi_a.
$$
By step [](#g-is-identity){.pf-ref}, $g$ is the identity, so
$$
f=\phi_a^{-1}\circ\phi_a=\operatorname{id}_D.
$$
:::

:::

::: pf-qed
Step [](#f-is-identity-boxed){.pf-ref} is the required conclusion.
:::

:::
:::
