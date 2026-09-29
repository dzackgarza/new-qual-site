---
schema: qual/card@1
id: E-VPWK4
kind: problem
title: Size of a conjugacy class divides the order of the group
classification:
  areas:
  - algebra
  topics:
  - Conjugacy
  - Cosets and Lagrange
  - Centralizers and Normalizers
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.exercise}
Let $G$ be a finite group. Show that the size of every conjugacy class in $G$ divides $|G|$.
:::


::: {.solution}
Let $x\in G$.

::: pf

::: {.pf-step #orbit-stabilizer-conjugation}
Under the conjugation action of $G$ on itself, the orbit of $x$ is its conjugacy class and its stabilizer is the centralizer $C_G(x)$.

::: pf-proof
The conjugation orbit is
\[
G\cdot x=\{gxg^{-1}:g\in G\}=\operatorname{Cl}_G(x).
\]
Moreover,
\[
g\cdot x=x
\quad\Longleftrightarrow\quad
gxg^{-1}=x
\quad\Longleftrightarrow\quad
gx=xg,
\]
so
\[
\operatorname{Stab}_G(x)=C_G(x).
\]
:::

:::

::: {.pf-step #class-size-index}
Hence
\[
|\operatorname{Cl}_G(x)|=[G:C_G(x)].
\]

::: pf-proof
This is the orbit-stabilizer theorem applied to the conjugation action, using step [](#orbit-stabilizer-conjugation){.pf-ref}.
:::

:::

::: pf-step
Therefore the size of the conjugacy class divides $|G|$.

::: pf-proof
Since $C_G(x)\le G$ and $G$ is finite, Lagrange's theorem gives
\[
|G|=|C_G(x)|[G:C_G(x)].
\]
By step [](#class-size-index){.pf-ref}, the second factor is $|\operatorname{Cl}_G(x)|$, so
\[
|\operatorname{Cl}_G(x)|\mid |G|.
\]
:::

:::

:::

:::
