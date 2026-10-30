---
schema: qual/card@1
id: P-TOP-WORKSHOP-QPH-04
kind: problem
title: A homeomorphism of the closed disk preserves its boundary
classification:
  areas: [topology]
  topics: [Homeomorphisms, Manifolds]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 4, labeled Arizona Fall 2005, in assets/attachments/Legacy_packet_-_Homotopy_and_Retractions_extracted.md.
---

::: {.problem}
Let $f:D^2\to D^2$ be a homeomorphism, where $D^2$ is the closed unit disk in $\RR^2$.
Show that every boundary point $x\in\partial D^2$ satisfies
$$
f(x)\in\partial D^2.
$$
:::

::: {.solution}

Write
$$
\mathring D^2
\coloneqq
D^2\setminus\partial D^2
$$
for the open unit disk.

::: pf

::: {.pf-step #s1-1}

One has
$$
f(\mathring D^2)
\subseteq
\mathring D^2.
$$


::: pf-proof

Fix
$$
x\in\mathring D^2.
$$
Choose an open Euclidean disk
$$
U\subset\RR^2
$$
with
$$
x\in U\subset\mathring D^2.
$$
The restriction
$$
f\restrict_U:
U\longrightarrow\RR^2
$$
is continuous and injective. By invariance of domain,
$$
f(U)
$$
is open in $\RR^2$.

Suppose
$$
f(x)\in\partial D^2.
$$
Since $f(x)\in f(U)$ and $f(U)$ is Euclidean-open, some Euclidean ball about $f(x)$ is contained in $f(U)$. But
$$
f(U)\subset f(D^2)=D^2,
$$
whereas no Euclidean neighborhood of a boundary point of $D^2$ is contained in $D^2$. This is a contradiction.

Thus
$$
f(x)\in\mathring D^2.
$$

:::

:::

::: {.pf-step #s1-2}

One has
$$
f^{-1}(\mathring D^2)
\subseteq
\mathring D^2.
$$


::: pf-proof

The inverse
$$
f^{-1}:D^2\to D^2
$$
is also a homeomorphism. Apply step [](#s1-1){.pf-ref} to $f^{-1}$.

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
f(\mathring D^2)
=
\mathring D^2.
$$


::: pf-proof

Step [](#s1-1){.pf-ref} gives one inclusion. For the reverse inclusion, let
$$
y\in\mathring D^2.
$$
By step [](#s1-2){.pf-ref},
$$
f^{-1}(y)\in\mathring D^2.
$$
Hence
$$
y
=
f(f^{-1}(y))
\in
f(\mathring D^2).
$$

:::

:::

::: {.pf-step #s1-4}

One has
$$
f(\partial D^2)
=
\partial D^2.
$$


::: pf-proof

Since $f$ is a bijection,
$$
f(D^2\setminus\mathring D^2)
=
f(D^2)\setminus f(\mathring D^2).
$$
Using
$$
f(D^2)=D^2
$$
and step [](#s1-3){.pf-ref},
$$
f(\partial D^2)
=
D^2\setminus\mathring D^2
=
\partial D^2.
$$

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} implies in particular that every
$$
x\in\partial D^2
$$
satisfies
$$
f(x)\in\partial D^2.
$$

:::

:::

:::
