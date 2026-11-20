---
schema: qual/card@1
id: E-P5AAV
kind: problem
title: '$\RR/\ZZ$ as a familiar topological group'
classification:
  areas:
  - topology
  topics:
  - Topological Groups
  - Quotient Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §22 Supplementary Exercise 6, printed p. 146,
    with Corollary 22.3; the stored statement is the printed question.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second Edition
    by James Munkres: Solutions Manual" (30 November 2019), Exercise TG.6, printed p. 270.
    The identification is his: t -> e^{2 pi i t} is a continuous open surjection whose
    fibres are the cosets of Z, so Corollary 22.3 gives a homeomorphism R/Z -> S^1, which is
    a group isomorphism because the map is a homomorphism. (tmp/sources/munkres-solutions-
    whitman.pdf).
---

::: {.exercise}

The integers $\ZZ$ are a normal subgroup of $(\RR, +)$.
The quotient $\RR/\ZZ$ is a familiar topological group; what is it?
:::

::: {.solution}

**Dan Whitman**, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise TG.6, manual p. 270, PDF p. 273 (`tmp/sources/munkres-solutions-whitman.pdf`), states the identification but expressly does not prove it ("We shall not show this rigorously as doing so would be tedious"); the argument below is therefore the card's own, and it replaces the card's earlier attribution of the argument to that set. The statement was checked against Munkres, *Topology* (2000), §22 Supplementary Exercise 6, with the definition of a topological group on printed p. 145, Theorem 22.2 and Corollary 22.3 on printed p. 142, and Theorem 18.4 on printed p. 110.

Throughout, $\ZZ<\RR$ is the subgroup of integers, $\RR/\ZZ$ is the quotient group with the quotient topology, $S^{1}=\theset{z\in\CC\mid\abs{z}=1}$ is the circle group under multiplication, and
$$
q\colon\RR\longrightarrow S^{1},\qquad q(t)\coloneqq e^{2\pi it}.
$$

::: pf

::: {.pf-step #normal}
$\ZZ$ is a normal subgroup of $(\RR,+)$.

::: pf-proof
$\ZZ$ is a subgroup of $(\RR,+)$ under addition, and $(\RR,+)$ is abelian, so $x+h-x=h\in\ZZ$ for every $x\in\RR$ and $h\in\ZZ$; hence $\ZZ$ is normal in the sense of the definition (§22 Supplementary Exercises, printed p. 146) that $x\cdot h\cdot x^{-1}\in\ZZ$.
:::

:::

::: {.pf-step #q-continuous}
$q$ is continuous and surjective.

::: pf-proof
The maps $t\mapsto\cos 2\pi t$ and $t\mapsto\sin 2\pi t$ are continuous real-valued functions of $t$, so $t\mapsto(\cos 2\pi t,\sin 2\pi t)=e^{2\pi it}$ is continuous into $\RR^{2}\cong\CC$ by Theorem 18.4 , and $\cos^{2}2\pi t+\sin^{2}2\pi t=1$ puts its values in $S^{1}$. For surjectivity, every point of $S^{1}$ has polar coordinates $(\cos\theta,\sin\theta)$ for some angle $\theta$ (each unit vector of the plane has a polar angle), and then $q(\theta/2\pi)$ is that point.
:::

:::

::: {.pf-step #fibres}
For $s,t\in\RR$ one has $q(s)=q(t)$ if and only if $s-t\in\ZZ$; hence the fibres of $q$ are exactly the cosets $t+\ZZ$.

::: pf-proof
$q(s)=q(t)$ says that the unit vectors $e^{2\pi is}$ and $e^{2\pi it}$ have the same polar angle modulo $2\pi$, that is $2\pi s-2\pi t\in2\pi\ZZ$, which is $s-t\in\ZZ$. Two points of $\RR$ are in the same fibre exactly when they differ by an element of $\ZZ$, so the fibre through $t$ is the coset $t+\ZZ$.
:::

:::

::: {.pf-step #q-open}
$q$ is an open map.

::: pf-proof
Let $U\subset\RR$ be open and write it as a union of open intervals of length at most $1$. On such an interval $I$ the map $q$ is injective by step [](#fibres){.pf-ref}, since no two points of $I$ differ by a nonzero integer; being a continuous injection of an interval, it carries $I$ onto an open arc of $S^{1}$, and the open arcs form a basis for the topology of $S^{1}$. Hence $q(U)$ is a union of basic open sets, so it is open.
:::

:::

::: {.pf-step #quotient}
$q$ is a quotient map, and it induces a bijection $f\colon\RR/\ZZ\to S^{1}$, $f(t+\ZZ)\coloneqq q(t)$.

::: pf-proof
$q$ is surjective and continuous by step [](#q-continuous){.pf-ref} and open by step [](#q-open){.pf-ref}; a surjective continuous open map is a quotient map (§22). By step [](#fibres){.pf-ref} the map $q$ is constant on each fibre of the quotient map $p\colon\RR\to\RR/\ZZ$ and separates distinct fibres, so it induces a well-defined bijection $f$ with $f\circ p=q$; well-definedness and injectivity are exactly the statement that the fibres of $q$ are the members of $\RR/\ZZ$, and surjectivity is that of $q$.
:::

:::

::: {.pf-step #homeomorphism}
$f$ is a homeomorphism.

::: pf-proof
$f$ is continuous by Theorem 22.2  applied to the quotient map $p$ and the map $q$, which is constant on the fibres of $p$. It is open: if $V\subset\RR/\ZZ$ is open, then $p^{-1}(V)$ is open in $\RR$ because $p$ is a quotient map and hence continuous, and
$$
f(V)=f\big(p(p^{-1}(V))\big)=q\big(p^{-1}(V)\big)
$$
is open by step [](#q-open){.pf-ref}. A continuous open bijection has a continuous inverse, so $f$ is a homeomorphism.
:::

:::

::: {.pf-step #group-map}
$f$ is an isomorphism of groups.

::: pf-proof
For $s,t\in\RR$,
$$
f\big((s+\ZZ)+(t+\ZZ)\big)=f(s+t+\ZZ)=q(s+t)=e^{2\pi i(s+t)}=e^{2\pi is}e^{2\pi it}=q(s)q(t),
$$
using the law of exponents for the exponential; so $f$ carries the group operation of $\RR/\ZZ$ to multiplication in $S^{1}$, and being a bijection it is an isomorphism.
:::

:::

::: pf-step
Therefore the quotient is the circle group:
$$
\boxed{\RR/\ZZ\cong S^{1}}
$$
as topological groups, that is, the reals with addition modulo $1$.

::: pf-proof
Steps [](#homeomorphism){.pf-ref} and [](#group-map){.pf-ref} show that $f$ is at once a homeomorphism and a group isomorphism, which is an isomorphism of topological groups; hence $\RR/\ZZ$ is the circle group, the reals with addition modulo $1$.
:::

:::

:::

:::
