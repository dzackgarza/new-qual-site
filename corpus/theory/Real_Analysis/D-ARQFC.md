---
schema: qual/card@1
id: D-ARQFC
kind: definition
title: Approximations to the identity
classification:
  areas:
  - real-analysis
  topics:
  - Approximations to the Identity
  - Convolution
relations: []
review: draft
---

::: {.definition}
Let $\phi\in L^1(\RR^n)$ with $\int_{\RR^n}\phi = 1$, and for $t>0$ let $\phi_t(x)\coloneqq t^{-n}\phi(t^{-1}x)$ be its [[D-EWXAT|dilations]].
Then $\phi$, or the family $(\phi_t)_{t>0}$, is called an \dfn{approximate identity}.
:::

::: {.proposition}
Let $\phi\in L^1(\RR^n)$ with $\int\phi=1$.
Then:

- $\int \phi_t = \int\phi = 1$ and $\norm{\phi_t}_1 = \norm{\phi}_1$ for every $t>0$; in particular $\norm{\phi_t}_1=1$ when $\phi\geq 0$.

- $\sup_{t>0} \norm{\phi_t}_1 < \infty$.

- For every $h>0$, $\lim_{t\to 0^+} \int_{\abs{x} \geq h} \abs{\phi_t(x)}\dx = 0$.
:::

::: {.proof}
The substitution $x=ty$, $dx=t^n\,dy$, gives $\int\phi_t=\int\phi$ and $\norm{\phi_t}_1=\norm{\phi}_1$, which proves the first two items.
The same substitution gives
$$
\int_{\abs{x}\geq h}\abs{\phi_t(x)}\dx=\int_{\abs{y}\geq h/t}\abs{\phi(y)}\,dy,
$$
and the right side tends to $0$ as $t\to 0^+$ by dominated convergence, with dominating function $\abs{\phi}\in L^1$.
:::
