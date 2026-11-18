---
schema: qual/card@1
id: P-CAFA19G
kind: problem
title: "The Perron function on the punctured disk with trivial boundary data is zero"
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure. The card states the Perron class explicitly (which boundary points there are, and the boundary values), proves that the zero function is admissible, checks both boundary values of the harmonic comparison function h_eps on the annulus, and states the maximum principle for subharmonic functions that compares phi with h_eps on the annulus. The limiting passage is made explicit: log|z| < 0 and log eps -> -infinity, so the ratio tends to 0. No retained solution set covers the exercise; the card says the argument is its own. No statement repair.
---

::: {.problem}
Let $G = \DD \setminus \{0\}$ and let $f$ be the function on $\partial G$ such that $f(z) = 0$ for $\abs{z} = 1$ and $f(0) = 1$.
Show that the Perron function $u(z)$ of $f$, $$u(z) = \sup\{\phi(z) : \phi \text{ is subharmonic and } \forall a \in \partial G,\; \limsup_{\zeta \to a} \phi(\zeta) \leq f(a)\}$$ is identically zero.

Hint: Consider the family of functions $u_\epsilon(z) = \frac{\log\abs{z}}{\log\epsilon}$ in the annulus $\epsilon < \abs{z} < 1$ for $\epsilon > 0$.
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own, following the hint.

Let $G=\DD\setminus\{0\}$ and let $\mathcal P$ be the Perron class of $f$: the subharmonic $\phi$ on $G$ with $\limsup_{\zeta\to a}\phi(\zeta)\le f(a)$ for every $a\in\partial G$, where $\partial G=\{\abs\zeta=1\}\cup\{0\}$, $f=0$ on the circle and $f(0)=1$.

::: pf

::: {.pf-step #nonneg}
$u\ge0$ on $G$.

::: pf-proof
The zero function is subharmonic on $G$ and has boundary limsup $0$ at every point of the circle and $0\le1$ at $0$, so $0\in\mathcal P$ and $u=\sup_{\phi\in\mathcal P}\phi\ge0$.
:::

:::

::: {.pf-step #annulus}
Let $\phi\in\mathcal P$, $z\in G$ and $\eta>0$. There is $\varepsilon_0>0$ with $\phi\le1+\eta$ on $\{\zeta:0<\abs\zeta\le\varepsilon_0\}$, and for every $\varepsilon\in(0,\min(\varepsilon_0,\abs z))$ one has $\phi\le h_\varepsilon$ on the annulus $A_\varepsilon=\{\varepsilon<\abs\zeta<1\}$, where $h_\varepsilon(\zeta)=(1+\eta)\frac{\log\abs\zeta}{\log\varepsilon}$.

::: pf-proof
The boundary condition at $0$ says $\limsup_{\zeta\to0}\phi(\zeta)\le1<1+\eta$, so $\phi\le1+\eta$ on a punctured disc as stated. $h_\varepsilon$ is harmonic on $\CC\setminus\{0\}$, equal to $1+\eta$ on $\abs\zeta=\varepsilon$ because $\log\varepsilon/\log\varepsilon=1$, and equal to $0$ on $\abs\zeta=1$ because $\log1=0$. On $\partial A_\varepsilon$: at $\abs\zeta=1$ we have $\limsup\phi\le f=0=h_\varepsilon$; at $\abs\zeta=\varepsilon$ we have $\phi\le1+\eta=h_\varepsilon$. The functions $\phi$ and $h_\varepsilon$ are subharmonic and harmonic on a neighbourhood of $\overline{A_\varepsilon}$, so $\phi-h_\varepsilon$ is subharmonic there and has nonpositive boundary limsup, hence $\phi\le h_\varepsilon$ on $A_\varepsilon$ by the maximum principle for subharmonic functions.
:::

:::

::: {.pf-step #zero}
$\phi(z)\le0$ for every $\phi\in\mathcal P$ and $z\in G$.

::: pf-proof
Take $\varepsilon\in(0,\min(\varepsilon_0,\abs z))$ as in step [](#annulus){.pf-ref}. Since $z\in A_\varepsilon$,
$$
\phi(z)\le h_\varepsilon(z)=(1+\eta)\frac{\log\abs z}{\log\varepsilon}.
$$
Here $\log\abs z<0$ and $\log\varepsilon<0$, so the fraction is positive, and as $\varepsilon\downarrow0$ the denominator tends to $-\infty$ with the numerator fixed, so the right side tends to $0$; $\eta>0$ was arbitrary. Hence $\phi(z)\le0$.
:::

:::

::: {.pf-step}
$u\equiv0$ on $G$.

::: pf-proof
Steps [](#nonneg){.pf-ref} and [](#zero){.pf-ref} give $0\le u(z)\le0$ for every $z\in G$.
:::

:::

:::
:::
