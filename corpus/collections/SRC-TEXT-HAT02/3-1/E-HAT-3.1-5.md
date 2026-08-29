---
schema: qual/card@1
id: E-HAT-3.1-5
kind: exercise
title: Hatcher Section 3.1 Exercise 5
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
# E-HAT-3.1-5

Regarding a cochain $\varphi \in C^1(X; G)$ as a function from paths in $X$ to $G$, show that if $\varphi$ is a cocycle, then

(a) $\varphi(f \cdot g) = \varphi(f) + \varphi(g)$,
(b) $\varphi$ takes the value 0 on constant paths,
(c) $\varphi(f) = \varphi(g)$ if $f \simeq g$,
(d) $\varphi$ is a coboundary iff $\varphi(f)$ depends only on the endpoints of $f$, for all $f$.

[In particular, (a) and (c) give a map $H^1(X; G) \to \operatorname{Hom}(\pi_1(X), G)$, which the universal coefficient theorem says is an isomorphism if $X$ is path-connected.]

::: {.solution}
<1>1. A $1$-cochain $\varphi$ assigns to each path $f$ a value $\varphi(f) \in G$, and $\delta\varphi = 0$ (cocycle condition) means $\varphi(\partial\sigma) = 0$ for every $2$-simplex $\sigma$.
Proof: definition of cocycle.

<1>2. **(a)** For paths $f, g$ with $f(1) = g(0)$, the concatenation $f \cdot g$ bounds a $2$-simplex (the triangle with edges $f$, $g$, and $f \cdot g$), so $\varphi(f \cdot g) - \varphi(f) - \varphi(g) = \varphi(\partial\sigma) = 0$.
Proof: <1>1 (the cocycle vanishes on the boundary of the triangle).

<1>3. Hence $\varphi(f \cdot g) = \varphi(f) + \varphi(g)$.
Proof: <1>2.

<1>4. **(b)** A constant path $c$ satisfies $c \cdot c = c$, so $\varphi(c) = \varphi(c \cdot c) = \varphi(c) + \varphi(c)$, forcing $\varphi(c) = 0$.
Proof: <1>3.

<1>5. **(c)** If $f \simeq g$ (rel endpoints), then $f$ and $g$ differ by the boundary of a $2$-chain (a homotopy gives a $2$-chain whose boundary is $f - g$), so $\varphi(f) - \varphi(g) = \varphi(\partial(\text{homotopy})) = 0$.
Proof: <1>1.

<1>6. Hence $\varphi(f) = \varphi(g)$.
Proof: <1>5.

<1>7. **(d)** ($\Rightarrow$) If $\varphi = \delta\psi$ is a coboundary, then $\varphi(f) = \psi(f(1)) - \psi(f(0))$ depends only on the endpoints.
Proof: definition of coboundary.

<1>8. ($\Leftarrow$) If $\varphi(f)$ depends only on the endpoints, define $\psi(x) = \varphi(f_x)$ for any path $f_x$ from a fixed basepoint to $x$; then $\varphi(f) = \psi(f(1)) - \psi(f(0)) = \delta\psi(f)$, so $\varphi$ is a coboundary.
Proof: <1>7, reversed.

<1>9. Q.E.D.
Proof: <1>3, <1>4, <1>6, <1>7–<1>8.
:::
