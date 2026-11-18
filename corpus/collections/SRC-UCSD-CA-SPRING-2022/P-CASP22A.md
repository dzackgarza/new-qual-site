---
schema: qual/card@1
id: P-CASP22A
kind: problem
title: "Analytic self-map of a bounded simply connected region fixing a point with derivative 1 is the identity"
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
  - Holomorphic Functions
  - Fixed Points
relations: []
review: draft
---

::: {.problem}
Let $G \subset \CC$ be a bounded, simply connected region and let $a \in G$.
Let $f$ be an analytic self-map of $G$ (i.e., $f(G) \subset G$) such that $f(a) = a$ and $f'(a) = 1$.
Show that $f(z) = z$.
:::

::: {.solution}

No retained solution set covers this exercise: the card's own argument follows, with the conjugation, the chain-rule computation and the equality case as separate steps.

Let $G$ be a bounded simply connected region, $a\in G$, and $f:G\to G$ analytic with $f(a)=a$ and $f'(a)=1$.

::: pf

::: {.pf-step #conjugate}
There is a biholomorphism $\phi:G\to\DD$ with $\phi(a)=0$, and $F=\phi\circ f\circ\phi^{-1}$ is a holomorphic self-map of $\DD$ with $F(0)=0$ and $F'(0)=1$.

::: pf-proof
The Riemann mapping theorem gives a biholomorphism $\psi:G\to\DD$; composing with the disc automorphism $w\mapsto\dfrac{w-\psi(a)}{1-\overline{\psi(a)}w}$ gives a biholomorphism $\phi$ with $\phi(a)=0$. Then $F$ is holomorphic and maps $\DD$ into $\DD$, $F(0)=\phi(f(a))=\phi(a)=0$, and the chain rule gives $F'(0)=\phi'(f(a))f'(a)(\phi^{-1})'(0)=\phi'(a)\cdot1\cdot\dfrac{1}{\phi'(a)}=1$.
:::

:::

::: {.pf-step #schwarz}
$F$ is a rotation $F(z)=e^{i\theta}z$.

::: pf-proof
$F$ is holomorphic on $\DD$, maps $\DD$ into $\DD$ and satisfies $F(0)=0$, so the Schwarz lemma applies and gives $\abs{F(z)}\le\abs{z}$ and $\abs{F'(0)}\le1$. Equality holds in the derivative bound, $F'(0)=1$ by step [](#conjugate){.pf-ref}, and by the Schwarz lemma the equality case of that bound for a self-map fixing $0$ forces $F(z)=e^{i\theta}z$.
:::

:::

::: {.pf-step #rotation}
$e^{i\theta}=1$.

::: pf-proof
$F'(z)=e^{i\theta}$ for a rotation, so $1=F'(0)=e^{i\theta}$.
:::

:::

::: {.pf-qed}
$F=\mathrm{id}$ by steps [](#schwarz){.pf-ref} and [](#rotation){.pf-ref}, hence $f=\phi^{-1}\circ F\circ\phi=\mathrm{id}$ on $G$.
:::

:::

:::
