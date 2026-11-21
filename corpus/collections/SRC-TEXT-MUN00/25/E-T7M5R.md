---
schema: qual/card@1
id: E-T7M5R
kind: problem
title: The identity component of a topological group is normal
classification:
  areas:
  - topology
  topics:
  - Connectedness
  - Topological Groups
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §25 Exercise 9, printed p. 162, with
    Supplementary Exercise TG.4 and the hint; the stored statement is the printed one.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 25.9, PDF p. 10. Translations are homeomorphisms,
    so xC and Cx are both the component of x and hence equal, which is normality.
    (tmp/sources/munkres-solutions-positron-ch3.pdf).
---

::: {.exercise}

Let $G$ be a topological group; let $C$ be the component of $G$ containing the identity element $e$.
Show that $C$ is a normal subgroup of $G$.
[Hint: If $x \in G$, then $xC$ is the component of $G$ containing $x$.]
:::

::: {.solution}

The strategy and the use of left and right translations are due to **"positron0802"**, *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 25.9, PDF p. 10 (`tmp/sources/munkres-solutions-positron-ch3.pdf`); the verification that $C$ is a subgroup is written out here. The statement was checked against Munkres, *Topology* (2000), §25 Exercise 9, printed p. 163, with §22 Supplementary Exercises 3 and 4 on printed p. 146, Theorem 23.3 on printed p. 150 and Theorem 23.6 on printed p. 151.

Throughout, $G$ is a topological group with identity $e$, $C$ is the component of $G$ containing $e$, and for $x\in G$ the maps $\ell_{x}(y)\coloneqq xy$ and $r_{x}(y)\coloneqq yx$ are the left and right translations by $x$.

::: pf

::: {.pf-step #translations}
For every $x\in G$ the maps $\ell_{x}$ and $r_{x}$ are homeomorphisms of $G$.

::: pf-proof
This is §22 Supplementary Exercise 4 (printed p. 146): for each $a\in G$ the maps $f_{a}(x)=a\cdot x$ and $g_{a}(x)=x\cdot a$ are homeomorphisms.
:::

:::

::: {.pf-step #coset-component}
For every $x\in G$ the set $xC$ is the component of $G$ containing $x$.

:::: pf-proof

::: {.pf-step #coset-connected}
$xC$ is connected and contains $x$.

::: pf-proof
$xC=\ell_{x}(C)$ is the image of the connected set $C$ under the homeomorphism $\ell_{x}$, hence connected, and $x=xe\in xC$ because $e\in C$.
:::

:::

::: {.pf-step #coset-largest}
Every connected subspace of $G$ that contains $x$ is contained in $xC$.

::: pf-proof
Let $D$ be connected with $x\in D$. Then $x^{-1}D=\ell_{x^{-1}}(D)$ is connected by step [](#translations){.pf-ref}, and it contains $x^{-1}x=e$; since $C$ is the component, that is the largest connected subspace, containing $e$, one has $x^{-1}D\subset C$, hence $D\subset xC$.
:::

:::

::::

:::

::: {.pf-step #right-coset-component}
For every $x\in G$ the set $Cx$ is the component of $G$ containing $x$.

::: pf-proof
Repeat the argument of step [](#coset-component){.pf-ref} with $\ell_{x}$ replaced by $r_{x}$: $Cx=r_{x}(C)$ is connected and contains $x$, and if $D$ is connected with $x\in D$ then $Dx^{-1}\subset C$, so $D\subset Cx$.
:::

:::

::: {.pf-step #subgroup}
$C$ is a subgroup of $G$.

:::: pf-proof

::: {.pf-step #closed-under-product}
$C\cdot C\subset C$.

::: pf-proof
The product $C\times C$ is connected by Theorem 23.6 (printed p. 151), and multiplication $G\times G\to G$ is continuous, so its image $C\cdot C$ is connected (Theorem 23.5, printed p. 150). It contains $e=e\cdot e$, so by step [](#coset-component){.pf-ref} applied with $x=e$ it lies in the component $C$ of $e$.
:::

:::

::: {.pf-step #closed-under-inverse}
$C^{-1}\subset C$.

::: pf-proof
Inversion is a homeomorphism of $G$, so $C^{-1}$ is connected and contains $e^{-1}=e$; it therefore lies in the component $C$ of $e$.
:::

:::

::: {.pf-step}
$e\in C$ and $C$ is closed under products and inverses, hence a subgroup.

::: pf-proof
$C$ contains $e$ by definition, and steps [](#closed-under-product){.pf-ref} and [](#closed-under-inverse){.pf-ref} give the two closure properties; a nonempty subset of a group with those two properties is a subgroup.
:::

:::

::::

:::

::: pf-step
Therefore $C$ is a normal subgroup of $G$.

::: pf-proof
By steps [](#coset-component){.pf-ref} and [](#right-coset-component){.pf-ref} the two sets $xC$ and $Cx$ are both the component of $G$ containing $x$, hence $xC=Cx$ for every $x\in G$. For $c\in C$ and $x\in G$ this gives $xc\in Cx$, so $xc=c'x$ for some $c'\in C$ and $xcx^{-1}=c'\in C$; that is the defining property of normality, and $C$ is a subgroup by step [](#subgroup){.pf-ref}.
:::

:::

:::

:::
