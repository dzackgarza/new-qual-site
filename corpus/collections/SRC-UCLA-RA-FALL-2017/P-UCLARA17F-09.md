---
schema: qual/card@1
id: P-UCLARA17F-09
kind: problem
title: Holomorphic families of injective maps of $\CC$ are affine
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
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Fall 2017, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Problem 9. Consider a map $F:\CC\times\CC\to\CC$ with the following properties:

1. For each fixed $z\in\CC$, the map $w\mapsto F(z,w)$ is injective.
2. For each fixed $w\in\CC$, the map $z\mapsto F(z,w)$ is holomorphic.
3. $F(0,w)=w$ for $w\in\CC$.

Show that
$$
F(z,w)=a(z)w+b(z)
$$
for $z,w\in\CC$, where $a$ and $b$ are entire functions with $a(0)=1$, $b(0)=0$, and $a(z)\ne0$ for $z\in\CC$.

Hint: Consider
$$
\frac{F(z,w)-F(z,0)}{F(z,1)-F(z,0)}.
$$
:::

::: {.solution}

Define
$$
G(z,w)
\coloneqq
\frac{F(z,w)-F(z,0)}{F(z,1)-F(z,0)}.
$$

::: pf

::: {.pf-step #s1}

The function $G$ is well-defined on $\CC\times\CC$, and for each fixed $w\in\CC$ the map $z\mapsto G(z,w)$ is entire.


::: pf-proof

For each fixed $z$, the map $w\mapsto F(z,w)$ is injective. Since $0\ne1$, this gives
$$
F(z,1)-F(z,0)\ne0
\qquad (z\in\CC).
$$
For fixed $w$, both the numerator and denominator in the definition of $G(z,w)$ are entire functions of $z$, and the denominator has no zeros. Hence $z\mapsto G(z,w)$ is entire.

:::

:::

::: {.pf-step #s2}

For all $z,w\in\CC$,
$$
G(z,w)=w.
$$


::: pf-proof

::: {.pf-step #s2-1}

For all $z\in\CC$,
$$
G(z,0)=0,
\qquad
G(z,1)=1,
$$
and for all $w\in\CC$,
$$
G(0,w)=w.
$$


::: pf-proof

The first two identities follow immediately from the definition of $G$. By the normalization $F(0,w)=w$,
$$
G(0,w)
=
\frac{w-0}{1-0}
=w.
$$

:::

:::

::: {.pf-step #s2-2}

If $w\notin\{0,1\}$, then the entire function $z\mapsto G(z,w)$ omits both $0$ and $1$.


::: pf-proof

Suppose first that $G(z,w)=0$. Then
$$
F(z,w)=F(z,0),
$$
so injectivity of $F(z,\mathord\cdot)$ gives $w=0$, contrary to the hypothesis. Likewise, if $G(z,w)=1$, then
$$
F(z,w)-F(z,0)=F(z,1)-F(z,0),
$$
hence $F(z,w)=F(z,1)$, and injectivity gives $w=1$, again a contradiction.

:::

:::

::: {.pf-step #s2-3}

If $w\notin\{0,1\}$, then $G(z,w)=w$ for every $z\in\CC$.


::: pf-proof

By steps [](#s1){.pf-ref} and [](#s2-2){.pf-ref}, the map $z\mapsto G(z,w)$ is an entire function omitting the two distinct values $0$ and $1$. Little Picard's theorem therefore implies that it is constant. Its value at $z=0$ is $w$ by step [](#s2-1){.pf-ref}, so the constant is $w$.

:::

:::

::: pf-qed

Step [](#s2-1){.pf-ref} proves the claim for $w=0,1$, and step [](#s2-3){.pf-ref} proves it for $w\notin\{0,1\}$.

:::

:::

:::

::: {.pf-step #s3}

Set
$$
a(z)\coloneqq F(z,1)-F(z,0),
\qquad
b(z)\coloneqq F(z,0).
$$
Then $a$ and $b$ are entire,
$$
a(0)=1,
\qquad
b(0)=0,
\qquad
a(z)\ne0\quad(z\in\CC),
$$
and
$$
\boxed{F(z,w)=a(z)w+b(z)}
\qquad (z,w\in\CC).
$$


::: pf-proof

Entirety follows from the hypothesis that $z\mapsto F(z,w)$ is entire for each fixed $w$. The normalization $F(0,w)=w$ gives $a(0)=1$ and $b(0)=0$. Injectivity of $F(z,\mathord\cdot)$ gives $F(z,1)\ne F(z,0)$, hence $a(z)\ne0$. Finally, step [](#s2){.pf-ref} and the definition of $G$ give
$$
F(z,w)-F(z,0)
=
w\bigl(F(z,1)-F(z,0)\bigr),
$$
which is exactly the displayed affine formula.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} gives all asserted properties of $a$, $b$, and $F$.

:::

:::

:::
