---
schema: qual/card@1
id: P-CAF11D
kind: problem
title: "Analytic functions on a strip that do not extend beyond any boundary point"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured the prose solution into a Lamport proof and checked it: the strip is
    mapped conformally onto the disc, the weighted series of Cayley factors converges
    locally uniformly with positive real part, F = exp(-H) is zero-free, the radial limit
    at each dense boundary point is 0, and a continuation across an interior boundary
    point would vanish at boundary points accumulating inside its disc, forcing F = 0.
    The transfer of the non-extendability from the disc back to the strip is now a step:
    phi is conformal on a neighbourhood of each boundary point of the strip, since
    psi(z_0) is real and non-zero and so avoids the pole -i. The collection's provenance
    is the examination paper only, so no retained solution set covers the exercise and
    the argument is the card's own.
---

::: {.problem}
Let $G$ be the open strip $\{z \in \CC : 1 < \operatorname{Im} z < 2\}$.

(a) Prove that there exists a function $f \in H(G)$ with the following property: For any $z \in \partial G$ and any $\epsilon > 0$ there is no function $g \in H(B(z; \epsilon))$ such that $g(z) = f(z)$ for all $z \in G \cap B(z; \epsilon)$.
(This means that $f$ does not extend analytically beyond any boundary point of $G$.)

(b) Prove or disprove: There is a function $f \in H(G)$ satisfying the conditions of (a) and such that $f$ has no zeroes in $G$.
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own.
A single construction answers both parts: the function produced in the last two steps has no analytic continuation across any boundary point and has no zeros.

::: pf

::: {.pf-step #strip}
$\psi(z)\coloneqq e^{\pi(z-i)}$ maps $G$ conformally onto the upper half-plane $\HH$.

::: pf-proof
For $z=x+iy\in G$ one has $\pi(z-i)=\pi x+i\pi(y-1)$ with $0<\pi(y-1)<\pi$, so $\psi(z)=e^{\pi x}e^{i\pi(y-1)}$ has positive modulus and argument in $(0,\pi)$; thus $\psi(G)\subset\HH$. Conversely, given $w\in\HH$ write $w=\abs{w}e^{i\theta}$ with $0<\theta<\pi$, and then $z\coloneqq\frac{\log\abs{w}}{\pi}+i\left(1+\frac{\theta}{\pi}\right)$ satisfies $1<\operatorname{Im}z<2$ and $\psi(z)=w$. The exponential is conformal and $\psi'\ne0$ everywhere.
:::

:::

::: {.pf-step #cayley}
$\phi\coloneqq\frac{\psi-i}{\psi+i}$ maps $G$ conformally onto the unit disc $\DD$.

::: pf-proof
The Cayley transform $w\mapsto\frac{w-i}{w+i}$ maps $\HH$ conformally onto $\DD$: for $w=u+iv$ with $v>0$, $\abs{w-i}^2<\abs{w+i}^2$, and the map is a Möbius transformation with nonzero derivative. Composing with the conformal $\psi$ of step [](#strip){.pf-ref} gives the claim.
:::

:::

::: {.pf-step #dense}
$\{\zeta_n\}_{n\ge1}\coloneqq\{e^{2\pi iq}:q\in\QQ\cap[0,1)\}$ is a sequence of distinct points of the unit circle that is dense in it.

::: pf-proof
$q\mapsto e^{2\pi iq}$ is a continuous map of $\QQ\cap[0,1)$, which is countable and dense in $[0,1)$, onto the circle; a continuous surjection takes dense sets to dense sets, and the points are distinct for distinct $q$ in that half-open interval.
:::

:::

::: {.pf-step #H}
The series
$$
H(w)\coloneqq\sum_{n=1}^{\infty}2^{-n}\frac{\zeta_n+w}{\zeta_n-w}
$$
converges locally uniformly on $\DD$ to a holomorphic function with $\operatorname{Re}H(w)>0$ there.

::: pf-proof
For $\abs{w}\le r<1$, the $n$-th summand is bounded by $2^{-n}\frac{1+r}{1-r}$, since $\abs{\zeta_n+w}\le1+r$ and $\abs{\zeta_n-w}\ge1-r$; Weierstrass' theorem on locally uniform convergence of holomorphic functions then makes $H$ holomorphic. Moreover
$$
\operatorname{Re}\frac{\zeta+w}{\zeta-w}=\frac{1-\abs{w}^2}{\abs{\zeta-w}^2}>0\qquad(\abs{\zeta}=1,\ \abs{w}<1),
$$
as one checks by multiplying by $\overline{\zeta}-\overline{w}$; each summand of $\operatorname{Re}H$ is therefore positive, and the sum of the series is positive as a sum of positive terms.
:::

:::

::: {.pf-step #F}
$F\coloneqq e^{-H}$ is holomorphic in $\DD$, never vanishes, and satisfies $\abs{F(w)}=e^{-\operatorname{Re}H(w)}<1$ there.

::: pf-proof
$H$ is holomorphic by step [](#H){.pf-ref}, and the exponential of a holomorphic function is holomorphic and has no zeros. Finally $\abs{e^{-H(w)}}=e^{-\operatorname{Re}H(w)}<1$ because $\operatorname{Re}H>0$.
:::

:::

::: {.pf-step #radial}
For every $n$, $F(r\zeta_n)\to0$ as $r\uparrow1$.

::: pf-proof
At $w=r\zeta_n$ the $n$-th summand of $\operatorname{Re}H$ equals $\operatorname{Re}\frac{1+r}{1-r}=\frac{1+r}{1-r}$, which tends to $+\infty$, and every other summand is positive by step [](#H){.pf-ref}. Hence $\operatorname{Re}H(r\zeta_n)\to+\infty$ and so $\abs{F(r\zeta_n)}=e^{-\operatorname{Re}H(r\zeta_n)}\to0$.
:::

:::

::: {.pf-step #no-extension}
There are no $\eta\in\partial\DD$, $\varepsilon>0$ and $g\in H(B(\eta;\varepsilon))$ with $g=F$ on $B(\eta;\varepsilon)\cap\DD$.

::: pf-proof

::: {.pf-step #vanishing-points}
If such $g$ exist, then $g$ vanishes at points of $\partial\DD$ lying in $B(\eta;\varepsilon)$ and accumulating at $\eta$.

::: pf-proof
By step [](#dense){.pf-ref} the points $\zeta_n$ are dense in $\partial\DD$, so there are distinct indices $n_k$ with $\zeta_{n_k}\in B(\eta;\varepsilon/2)$ and $\zeta_{n_k}\to\eta$; a subsequence converges to a point of the circle at distance at most $\varepsilon/2$ from $\eta$, and dropping to that subsequence gives $\zeta_{n_k}\in B(\eta;\varepsilon)$ for all $k$, with $\zeta_{n_k}\to\eta$. For each $k$, continuity of $g$ at $\zeta_{n_k}$ and step [](#radial){.pf-ref} give
$$
g(\zeta_{n_k})=\lim_{r\uparrow1}F(r\zeta_{n_k})=0.
$$
:::

:::

::: {.pf-step}
Such a $g$ would force $F\equiv0$, which contradicts step [](#F){.pf-ref}.

::: pf-proof
The points of step [](#vanishing-points){.pf-ref} are distinct and tend to $\eta$, which is an interior point of the disc $B(\eta;\varepsilon)$, so the zero set of $g$ accumulates at a point of that disc. As $B(\eta;\varepsilon)$ is connected, the identity theorem gives $g\equiv0$ there. Then $F=0$ on the nonempty open set $B(\eta;\varepsilon)\cap\DD$, and the identity theorem on the connected $\DD$ gives $F\equiv0$, contradicting step [](#F){.pf-ref}, which says that $F$ never vanishes.
:::

:::


:::

:::

::: {.pf-step #conformal-at-boundary}
For every $z_0\in\partial G$ the map $\phi$ is conformal on some open neighbourhood of $z_0$.

::: pf-proof
Let $z_0\in\partial G$. If $\operatorname{Im}z_0=1$ then $\psi(z_0)=e^{\pi x_0}>0$ is a positive real number; if $\operatorname{Im}z_0=2$ then $\psi(z_0)=-e^{\pi x_0}<0$. In either case $\psi(z_0)\ne-i$, and $\phi$ is the composition of the entire function $\psi$ with the Möbius map $w\mapsto\frac{w-i}{w+i}$, which is conformal on $\CC\setminus\{-i\}$; since $\psi$ is continuous and nonconstant, a neighbourhood of $z_0$ is mapped into $\CC\setminus\{-i\}$, and $\phi'=\frac{2i\psi'}{(\psi+i)^2}\ne0$ there.
:::

:::

::: {.pf-step}
(a) $f\coloneqq F\circ\phi$ lies in $H(G)$ and has no analytic continuation across any boundary point of $G$.

::: pf-proof
$f$ is holomorphic as a composition of holomorphic maps. Suppose $g\in H(B(z_0;\varepsilon))$ satisfied $g=f$ on $G\cap B(z_0;\varepsilon)$ for some $z_0\in\partial G$ and some $\varepsilon>0$. By step [](#conformal-at-boundary){.pf-ref} there is an open neighbourhood $V$ of $z_0$, contained in $B(z_0;\varepsilon)$ after shrinking, on which $\phi$ is conformal; then $\phi(V)$ is open and contains $\eta\coloneqq\phi(z_0)\in\partial\DD$, and $g\circ(\phi^{-1})$ is holomorphic on $\phi(V)$ and equals $F$ on $\phi(V)\cap\DD$, since $\phi$ carries $G\cap V$ onto $\DD\cap\phi(V)$. Choosing a disc $B(\eta;\varepsilon')\subset\phi(V)$ gives exactly the forbidden continuation of step [](#no-extension){.pf-ref}.
:::

:::

::: {.pf-step}
(b) The function $f=F\circ\phi$ can be chosen with no zeros in $G$.

::: pf-proof
$F$ never vanishes by step [](#F){.pf-ref} and $\phi$ maps into $\DD$, so the composition has no zeros; with step [](#strip){.pf-ref} and step [](#cayley){.pf-ref} the same $f$ has no analytic continuation across any boundary point of $G$. So the answer to (b) is affirmative: such a zero-free $f$ exists.
:::

:::

:::

:::
