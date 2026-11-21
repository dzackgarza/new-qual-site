---
schema: qual/card@1
id: P-CAF07A
kind: problem
title: "True or False: subsequential convergence, contour integrals, entire functions omitting a disk, biholomorphisms, and harmonicity"
classification:
  areas:
  - complex-analysis
  topics:
  - Point-Set Topology
  - Contour Integration
  - Entire Functions
  - Conformal Maps
  - Harmonic Functions
relations: []
review: draft
---

::: {.problem}
Determine if the statements below are True or False.
If True, give a brief proof.
If False, give a counterexample.

(a) Let $(X, d)$ be a metric space.
Let $\{x_n\}_{n=1}^{\infty}$ be a sequence and assume that every subsequence has a convergent subsequence.
Then $\{x_n\}_{n=1}^{\infty}$ is convergent.

(b) Let $\gamma_+(t) = e^{it}$, $t \in [0, \pi]$, and $\gamma_-(t) = e^{-it}$, $t \in [0, \pi]$.
Then $\int_{\gamma_+} e^{1/z^2}\,dz = \int_{\gamma_-} e^{1/z^2}\,dz$.

(c) If $f(z)$ is an entire function and there are $\alpha \in \CC$, $r > 0$, such that $f(\CC) \subset \CC \setminus \overline{B(\alpha, r)}$, then $f(z)$ is constant.

(d) There is an analytic bijection (biholomorphism) from $\DD \setminus \{0\}$ onto $\CC \setminus \{0\}$.

(e) The function $u(z) := \ln\abs{z^2 + 1}$ is harmonic in $\CC \setminus \{-i, i\}$.
:::

::: {.solution}

The five verdicts and their witnesses are the card's own; no retained set solves this exercise, and the sets searched are recorded in the audit trail.

::: pf

::: {.pf-step #a}
(a) False: in $\RR$ the sequence $x_{n}=0$ for $n$ even and $x_{n}=1$ for $n$ odd has the property that every subsequence has a convergent subsequence, and does not converge.

::: pf-proof
Let $(x_{n_{k}})$ be a subsequence. Its index set is infinite, so it contains either infinitely many even indices or infinitely many odd indices; in the first case the further subsequence of the even ones is constantly $0$, in the second the further subsequence of the odd ones is constantly $1$, and a constant sequence converges. So every subsequence has a convergent subsequence. But the full sequence alternates between $0$ and $1$, so its even terms converge to $0$ and its odd terms to $1$; a convergent sequence has all its subsequences converging to the same limit, so $(x_{n})$ does not converge.
:::

:::

::: {.pf-step #b}
(b) True: $\displaystyle\int_{\gamma_{+}}e^{1/z^{2}}dz=\int_{\gamma_{-}}e^{1/z^{2}}dz$.

::: pf-proof
Both paths run from $\gamma(0)=1$ to $\gamma(\pi)=-1$; $\gamma_{+}$ is the upper unit semicircle and $\gamma_{-}$ the lower one. The closed curve $\gamma_{+}-\gamma_{-}$ is (up to parametrisation) the positively oriented unit circle, so
$$
\int_{\gamma_{+}}e^{1/z^{2}}dz-\int_{\gamma_{-}}e^{1/z^{2}}dz=\int_{\abs{z}=1}e^{1/z^{2}}dz .
$$
On $\abs{z}=1$ the function has the Laurent expansion $e^{1/z^{2}}=\sum_{n\ge0}z^{-2n}/n!$, which contains no $z^{-1}$ term, so its residue at $0$ is $0$ and the circle integral equals $2\pi i\cdot0=0$.
:::

:::

::: {.pf-step #c}
(c) True: if $f$ is entire and $f(\CC)\subset\CC\setminus\overline{B(\alpha,r)}$ with $r>0$, then $f$ is constant.

::: pf-proof
The hypothesis says $\abs{f(z)-\alpha}>r$ — or $\ge r$ if the open ball is meant, either way $\abs{f(z)-\alpha}\ge r>0$ — for every $z$. So $f-\alpha$ never vanishes, $g=1/(f-\alpha)$ is entire, and $\abs{g}\le1/r$ everywhere. A bounded entire function is constant (Liouville's theorem), so $g\equiv c\ne0$ and $f=\alpha+1/c$ is constant.
:::

:::

::: {.pf-step #d}
(d) False: there is no biholomorphism $\DD\setminus\{0\}\to\CC\setminus\{0\}$.

::: pf-proof
Suppose $F:\DD\setminus\{0\}\to\CC\setminus\{0\}$ were biholomorphic, with holomorphic inverse $G:\CC\setminus\{0\}\to\DD\setminus\{0\}$. Then $G$ is bounded, since its values lie in $\DD$, so its isolated singularity at $0$ is removable (Riemann's removable singularity theorem) and $G$ extends to an entire function $\widetilde G$ with $\abs{\widetilde G}\le1$. By Liouville's theorem $\widetilde G$ is constant, hence $G$ is constant, contradicting the injectivity of $F$; so no such $F$ exists.
:::

:::

::: {.pf-step #e}
(e) True: $u(z)=\ln\abs{z^{2}+1}$ is harmonic on $\CC\setminus\{-i,i\}$.

::: pf-proof
On that set $z^{2}+1$ never vanishes. Each point has a simply connected neighbourhood $U$ on which $z^{2}+1$ has a holomorphic logarithm $L$, that is $e^{L(z)}=z^{2}+1$ there; then $\operatorname{Re}L(z)=\ln\abs{z^{2}+1}=u(z)$ on $U$. A holomorphic function is harmonic and the real part of a holomorphic function is harmonic, being the sum of the real and imaginary parts of a holomorphic function in the Cauchy--Riemann sense — concretely, if $L=U+iV$ then $\Delta U=0$ because $U_{xx}+U_{yy}=V_{xy}-V_{yx}=0$. So $u$ is harmonic on a neighbourhood of each point of the domain, hence on the domain.
:::

:::

:::
:::
