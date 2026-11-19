---
schema: qual/card@1
id: P-CASP22F
kind: problem
title: 'A bounded harmonic function on $\DD$ with $\limsup\leq 0$ at all but one boundary point'
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
  - Maximum Principle
  - Boundary Values
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewritten as a Lamport structured proof of the argument already on the card, correct as it
    stood. Added: the compactness argument on the complementary arc giving r_0 from the
    limsup hypothesis; the Poisson formula written with the kernel and its unit mass, and the
    splitting of the integral with the two bounds; the quantitative shrinking step, that the
    Poisson mass of a short arc about e^{it} = z/|z| can be made at most eta uniformly in r in
    a compact subinterval of (|z|,1), which is what the prose left as "the second term can be
    made arbitrarily small"; and a clean set of the quantifiers in the conclusion (eta = eps/M
    first, then r_0 depending on the chosen arc, then r). Not claimed: a retained solution set;
    the provenance names the examination paper.
---

::: {.problem}
Let $h$ be a bounded harmonic function on the unit disc $\DD = \{z : \abs{z} < 1\}$.
Assume that
$$
\limsup_{z \to a} h(z) \leq 0
$$
for all $a \in \partial \DD \setminus \{1\}$.
Show that $h \leq 0$ in $\DD$.
:::

::: {.solution}
No retained solution set covers this problem: the collection's `provenance` names the Spring 2022 complex-analysis examination paper, which carries no solutions. The argument below is the card's own and follows the card's previous prose: a Poisson representation on a slightly smaller disk, the exceptional arc around $1$ isolated, and two limits.

Throughout $h$ is harmonic on $\DD$ with $\abs h\le M$, and $\limsup_{z\to a}h(z)\le0$ for every $a\in\partial\DD\setminus\set1$.

::: pf

::: {.pf-step #complement}
For every $z\in\DD$ and $\varepsilon>0$ there is a closed arc $I\subset\partial\DD$ about $1$, with $I$ as short as we please, and $r_0<1$ such that $h(re^{it})\le\varepsilon$ whenever $r_0<r<1$ and $e^{it}\notin I$.

::: pf-proof
The complement of an open arc about $1$ is a compact arc $J$ not containing $1$. For $a\in J$ the limsup hypothesis gives a neighbourhood $U_a$ of $a$ on which $h\le\varepsilon/2$ near the boundary, i.e. $\limsup_{z\to a}h(z)\le0$ and continuity of $h$ on compact pieces of the disk give $r_a<1$ with $h(re^{it})\le\varepsilon$ for $re^{it}$ in $U_a\cap\DD$ and $r>r_a$. Finitely many $U_a$ cover the compact $J$, and the maximum of the corresponding $r_a$ gives $r_0$.

:::

:::

::: {.pf-step #poisson}
For $r$ with $\abs z<r<1$,
$$
h(z)=\frac1{2\pi}\int_{-\pi}^{\pi}P_{\abs z/r}(\arg z-t)\,h(re^{it})\,dt,
$$
and consequently
$$
h(z)\le\varepsilon+M\cdot\frac1{2\pi}\int_{\theset{t:\,e^{it}\in I}}P_{\abs z/r}(\arg z-t)\,dt .
$$

::: pf-proof
The first identity is the Poisson formula for the harmonic function $h$ on the disk of radius $r$, evaluated at the interior point $z$: $P_\rho(\varphi)=\frac{1-\rho^2}{1-2\rho\cos\varphi+\rho^2}$ is the Poisson kernel with $\frac1{2\pi}\int P_\rho=1$ for $\rho<1$. Splitting the integral over the set where $e^{it}\in I$ and its complement, and using $h\le\varepsilon$ on the complement when $r>r_0$ (step [](#complement){.pf-ref}) together with $h\le M$ everywhere and $P_\rho\ge0$, gives the second inequality.

:::

:::

::: {.pf-step #shrink}
The arc $I$ may be chosen, once $z$ and $\eta>0$ are fixed, so that the Poisson mass it carries is at most $\eta$ uniformly for $r$ in a compact subinterval of $(\abs z,1)$.

::: pf-proof
For fixed $z$ and $r\ge\abs z+\delta$ the kernel $t\mapsto P_{\abs z/r}(\arg z-t)$ is continuous in $(r,t)$ and bounded by a constant depending only on $\abs z$ and $\delta$: the denominator is bounded away from $0$ because $\cos(\arg z-t)=1$ forces $e^{it}=z/\abs z$, and near that point the numerator $1-\abs z^2/r^2$ is bounded. Hence the integral over a short arc about that point tends to $0$ as the arc shrinks, uniformly in $r$ in a compact subinterval of $(\abs z,1)$; take the arc short enough that the integral is at most $\eta$.

:::

:::

::: {.pf-step #conclusion}
$h(z)\le0$ for every $z\in\DD$.

::: pf-proof
Fix $z$ and $\varepsilon>0$. Choose the arc $I$ by step [](#shrink){.pf-ref} with $\eta=\varepsilon/M$ (and $\eta=\varepsilon$ if $M=0$), then $r_0$ by step [](#complement){.pf-ref} for that $I$, and take $r$ with $\max(r_0,\abs z)<r<1$. Step [](#poisson){.pf-ref} then gives $h(z)\le\varepsilon+M\eta=2\varepsilon$. Since $\varepsilon>0$ was arbitrary, $h(z)\le0$; and $z$ was arbitrary.

:::

:::

:::
:::
