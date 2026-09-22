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

<1>1. The map
$$
g=\phi_a\circ f\circ\phi_a^{-1}:D\longrightarrow D
$$
is analytic and fixes both $0$ and the nonzero point $c=\phi_a(b)$.

::: {.proof}
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

<1>2. There exists $\eta\in\CC$ with $\abs{\eta}=1$ such that
$$
g(z)=\eta z
$$
for every $z\in D$.

::: {.proof}
Since $g:D\to D$ is analytic and $g(0)=0$, Schwarz's lemma gives
$$
\abs{g(z)}\leq\abs{z}
$$
for every $z\in D$. By step <1>1, $g(c)=c$ for some $c\neq0$, so equality
holds at the nonzero point $c$:
$$
\abs{g(c)}=\abs{c}.
$$
The equality case of Schwarz's lemma therefore implies that
$g(z)=\eta z$ for some $\eta$ with $\abs{\eta}=1$.
:::

<1>3. The map $g$ is the identity on $D$.

::: {.proof}
By steps <1>1 and <1>2,
$$
c=g(c)=\eta c.
$$
Since $c\neq0$, this gives $\eta=1$. Hence $g(z)=z$ for every $z\in D$.
:::

<1>4. For every $z\in D$,
$$
\boxed{f(z)=z}.
$$

::: {.proof}
The definition of $g$ gives
$$
f=\phi_a^{-1}\circ g\circ\phi_a.
$$
By step <1>3, $g$ is the identity, so
$$
f=\phi_a^{-1}\circ\phi_a=\operatorname{id}_D.
$$
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required conclusion.
:::
:::
