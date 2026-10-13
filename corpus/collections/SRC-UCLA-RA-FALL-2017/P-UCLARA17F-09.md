---
schema: qual/card@1
id: P-UCLARA17F-09
kind: problem
title: Holomorphic families of injective maps of $\mathbb C$ are affine
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
Problem 9. Consider a map $F:\mathbb C\times\mathbb C\to\mathbb C$ with the following properties:

1. For each fixed $z\in\mathbb C$, the map $w\mapsto F(z,w)$ is injective.
2. For each fixed $w\in\mathbb C$, the map $z\mapsto F(z,w)$ is holomorphic.
3. $F(0,w)=w$ for $w\in\mathbb C$.

Show that
\[
F(z,w)=a(z)w+b(z)
\]
for $z,w\in\mathbb C$, where $a$ and $b$ are entire functions with $a(0)=1$, $b(0)=0$, and $a(z)\ne0$ for $z\in\mathbb C$.

Hint: Consider
\[
\frac{F(z,w)-F(z,0)}{F(z,1)-F(z,0)}.
\]
:::

::: {.solution}
Define
\[
G(z,w)
\coloneqq
\frac{F(z,w)-F(z,0)}{F(z,1)-F(z,0)}.
\]

<1>1. The function $G$ is well-defined on $\mathbb C\times\mathbb C$, and for each fixed $w\in\mathbb C$ the map $z\mapsto G(z,w)$ is entire.

::: {.proof}
For each fixed $z$, the map $w\mapsto F(z,w)$ is injective. Since $0\ne1$, this gives
\[
F(z,1)-F(z,0)\ne0
\qquad (z\in\mathbb C).
\]
For fixed $w$, both the numerator and denominator in the definition of $G(z,w)$ are entire functions of $z$, and the denominator has no zeros. Hence $z\mapsto G(z,w)$ is entire.
:::

<1>2. For all $z,w\in\mathbb C$,
\[
G(z,w)=w.
\]

<2>1. For all $z\in\mathbb C$,
\[
G(z,0)=0,
\qquad
G(z,1)=1,
\]
and for all $w\in\mathbb C$,
\[
G(0,w)=w.
\]

::: {.proof}
The first two identities follow immediately from the definition of $G$. By the normalization $F(0,w)=w$,
\[
G(0,w)
=
\frac{w-0}{1-0}
=w.
\]
:::

<2>2. If $w\notin\{0,1\}$, then the entire function $z\mapsto G(z,w)$ omits both $0$ and $1$.

::: {.proof}
Suppose first that $G(z,w)=0$. Then
\[
F(z,w)=F(z,0),
\]
so injectivity of $F(z,\mathord\cdot)$ gives $w=0$, contrary to the hypothesis. Likewise, if $G(z,w)=1$, then
\[
F(z,w)-F(z,0)=F(z,1)-F(z,0),
\]
hence $F(z,w)=F(z,1)$, and injectivity gives $w=1$, again a contradiction.
:::

<2>3. If $w\notin\{0,1\}$, then $G(z,w)=w$ for every $z\in\mathbb C$.

::: {.proof}
By steps <1>1 and <2>2, the map $z\mapsto G(z,w)$ is an entire function omitting the two distinct values $0$ and $1$. Little Picard's theorem therefore implies that it is constant. Its value at $z=0$ is $w$ by step <2>1, so the constant is $w$.
:::

<2>4. Q.E.D.

::: {.proof}
Step <2>1 proves the claim for $w=0,1$, and step <2>3 proves it for $w\notin\{0,1\}$.
:::

<1>3. Set
\[
a(z)\coloneqq F(z,1)-F(z,0),
\qquad
b(z)\coloneqq F(z,0).
\]
Then $a$ and $b$ are entire,
\[
a(0)=1,
\qquad
b(0)=0,
\qquad
a(z)\ne0\quad(z\in\mathbb C),
\]
and
\[
\boxed{F(z,w)=a(z)w+b(z)}
\qquad (z,w\in\mathbb C).
\]

::: {.proof}
Entirety follows from the hypothesis that $z\mapsto F(z,w)$ is entire for each fixed $w$. The normalization $F(0,w)=w$ gives $a(0)=1$ and $b(0)=0$. Injectivity of $F(z,\mathord\cdot)$ gives $F(z,1)\ne F(z,0)$, hence $a(z)\ne0$. Finally, step <1>2 and the definition of $G$ give
\[
F(z,w)-F(z,0)
=
w\bigl(F(z,1)-F(z,0)\bigr),
\]
which is exactly the displayed affine formula.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 gives all asserted properties of $a$, $b$, and $F$.
:::
:::
