---
schema: qual/card@1
id: E-HAT-3.1-5
kind: problem
title: 1-cocycles as functions on paths and $H^1(X;G)\to\operatorname{Hom}(\pi_1(X),G)$
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.problem}
Regarding a cochain $\varphi \in C^1(X; G)$ as a function from paths in $X$ to $G$, show that if $\varphi$ is a cocycle, then

(a) $\varphi(f \cdot g) = \varphi(f) + \varphi(g)$,
(b) $\varphi$ takes the value 0 on constant paths,
(c) $\varphi(f) = \varphi(g)$ if $f \simeq g$,
(d) $\varphi$ is a coboundary iff $\varphi(f)$ depends only on the endpoints of $f$, for all $f$.

[In particular, (a) and (c) give a map $H^1(X; G) \to \operatorname{Hom}(\pi_1(X), G)$, which the universal coefficient theorem says is an isomorphism if $X$ is path-connected.]
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

A $1$-cochain $\varphi$ assigns to each path $f$ a value $\varphi(f) \in G$, and $\delta\varphi = 0$ (cocycle condition) means $\varphi(\partial\sigma) = 0$ for every $2$-simplex $\sigma$.

::: pf-proof

definition of cocycle.

:::

:::

::: {.pf-step #s2}

**(a)** For paths $f, g$ with $f(1) = g(0)$, the concatenation $f \cdot g$ bounds a $2$-simplex (the triangle with edges $f$, $g$, and $f \cdot g$), so $\varphi(f \cdot g) - \varphi(f) - \varphi(g) = \varphi(\partial\sigma) = 0$.

::: pf-proof

Step [](#s1){.pf-ref} (the cocycle vanishes on the boundary of the triangle).

:::

:::

::: {.pf-step #s3}

Hence $\varphi(f \cdot g) = \varphi(f) + \varphi(g)$.

::: pf-proof

Step [](#s2){.pf-ref}.

:::

:::

::: {.pf-step #s4}

**(b)** A constant path $c$ satisfies $c \cdot c = c$, so $\varphi(c) = \varphi(c \cdot c) = \varphi(c) + \varphi(c)$, forcing $\varphi(c) = 0$.

::: pf-proof

Step [](#s3){.pf-ref}.

:::

:::

::: {.pf-step #s5}

**(c)** If $f \simeq g$ (rel endpoints), then $f$ and $g$ differ by the boundary of a $2$-chain (a homotopy gives a $2$-chain whose boundary is $f - g$), so $\varphi(f) - \varphi(g) = \varphi(\partial(\text{homotopy})) = 0$.

::: pf-proof

Step [](#s1){.pf-ref}.

:::

:::

::: {.pf-step #s6}

Hence $\varphi(f) = \varphi(g)$.

::: pf-proof

Step [](#s5){.pf-ref}.

:::

:::

::: {.pf-step #s7}

**(d)** ($\Rightarrow$) If $\varphi = \delta\psi$ is a coboundary, then $\varphi(f) = \psi(f(1)) - \psi(f(0))$ depends only on the endpoints.

::: pf-proof

definition of coboundary.

:::

:::

::: {.pf-step #s8}

($\Leftarrow$) If $\varphi(f)$ depends only on the endpoints, define $\psi(x) = \varphi(f_x)$ for any path $f_x$ from a fixed basepoint to $x$; then $\varphi(f) = \psi(f(1)) - \psi(f(0)) = \delta\psi(f)$, so $\varphi$ is a coboundary.

::: pf-proof

Step [](#s7){.pf-ref}, reversed.

:::

:::

::: pf-qed

Steps [](#s3){.pf-ref}, [](#s4){.pf-ref}, [](#s6){.pf-ref}, [](#s7){.pf-ref} and [](#s8){.pf-ref}.

:::

:::

:::
