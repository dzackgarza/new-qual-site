---
schema: qual/card@1
id: D-AUD6K
kind: definition
title: Poles and their order
prompts:
- What does it mean for $f$ to have a pole of order $m$ at $a$?
- What is the order of a pole of $f$ at $a$?
classification:
  areas:
  - complex-analysis
  topics:
  - Poles
  - Laurent Series
  - Singularities
relations: []
review: draft
---

::: {.definition}
Let $z_0\in\CC$, let $r>0$, and let $f$ be [[D-E7A5W|holomorphic]] on the punctured disc $D_r(z_0)\setminus\{z_0\}$.
For an integer $n\ge1$, $f$ has a \dfn{pole of order $n$} at $z_0$ if there exist $0<\rho\le r$ and a holomorphic function $h\colon D_\rho(z_0)\to\CC$ with $h(z_0)\neq0$ such that
$$
f(z)=(z-z_0)^{-n}h(z)\qquad\text{for } 0<\abs{z-z_0}<\rho.
$$
$f$ has a \dfn{pole} at $z_0$ if it has a pole of some order $n\ge1$ there, and a pole of order $1$ is a \dfn{simple pole}.
:::

::: {.proposition}
Let $f$ be holomorphic on $D_r(z_0)\setminus\{z_0\}$ and let $n\ge1$.
The following are equivalent.

(a) $f$ has a pole of order $n$ at $z_0$.

(b) There is $0<\rho\le r$ such that $f$ has no zeros in $D_\rho(z_0)\setminus\{z_0\}$ and $g\coloneqq1/f$, extended by $g(z_0)\coloneqq0$, is holomorphic on $D_\rho(z_0)$ with a [[D-65VIK|zero of order $n$]] at $z_0$.

(c) The Laurent expansion of $f$ on $D_r(z_0)\setminus\{z_0\}$ has the form $f(z)=\sum_{k\ge-n}c_k(z-z_0)^k$ with $c_{-n}\neq0$.

Moreover, $f$ has a pole at $z_0$ if and only if $\abs{f(z)}\to\infty$ as $z\to z_0$.
:::

::: {.proof}
(a)$\Rightarrow$(b).
Since $h(z_0)\neq0$ and $h$ is continuous, shrinking $\rho$ makes $h$ nonvanishing on $D_\rho(z_0)$.
Then $1/f(z)=(z-z_0)^n\cdot(1/h(z))$ for $0<\abs{z-z_0}<\rho$, and the right side is holomorphic on $D_\rho(z_0)$, vanishes at $z_0$, and has $1/h(z_0)\neq0$.

(b)$\Rightarrow$(a).
Write $g(z)=(z-z_0)^n k(z)$ with $k$ holomorphic near $z_0$ and $k(z_0)\neq0$; shrinking $\rho$, $k$ is nonvanishing, and $h\coloneqq1/k$ satisfies $f(z)=(z-z_0)^{-n}h(z)$ with $h(z_0)\neq0$.

(a)$\Rightarrow$(c).
Expand $h(z)=\sum_{j\ge0}b_j(z-z_0)^j$ on $D_\rho(z_0)$ with $b_0=h(z_0)\neq0$.
Then $f(z)=\sum_{k\ge-n}b_{k+n}(z-z_0)^k$ on $D_\rho(z_0)\setminus\{z_0\}$, and by uniqueness of Laurent coefficients this is the Laurent expansion of $f$, with $c_{-n}=b_0\neq0$.

(c)$\Rightarrow$(a).
The power series $h(z)\coloneqq\sum_{k\ge-n}c_k(z-z_0)^{k+n}$ converges for $0<\abs{z-z_0}<r$, hence on $D_r(z_0)$, and defines a holomorphic function there with $h(z_0)=c_{-n}\neq0$ and $f(z)=(z-z_0)^{-n}h(z)$.

Finally, if $f$ has a pole of order $n$, then $\abs{f(z)}=\abs{h(z)}/\abs{z-z_0}^n\to\infty$ because $h(z_0)\neq0$.
Conversely, if $\abs{f(z)}\to\infty$, then $f$ has no zeros on some $D_\rho(z_0)\setminus\{z_0\}$, and $1/f$ is holomorphic and bounded there with $1/f(z)\to0$.
By [[T-ZZJDP|Riemann's removable singularity theorem]], $g\coloneqq1/f$ with $g(z_0)\coloneqq0$ is holomorphic on $D_\rho(z_0)$.
It is not identically zero, so $z_0$ is a zero of $g$ of some order $n\ge1$, and (b) holds.
:::

::: {.remark title="Variations"}
A pole may be defined by condition (b) without naming $n$: $f$ has no zeros near $z_0$ and $1/f$, extended by $0$ at $z_0$, is holomorphic.
The order is then the least integer $n\ge1$ for which $f(z)=(z-z_0)^{-n}h(z)$ near $z_0$ with $h$ holomorphic, without the condition $h(z_0)\neq0$.
This least $n$ is the order in the definition above: if $f=(z-z_0)^{-n}h_0$ with $h_0(z_0)\neq0$ and $f=(z-z_0)^{-m}h$ with $m<n$, then $h=(z-z_0)^{m-n}h_0$ is unbounded near $z_0$, a contradiction.

The order is also read off from limits: $f$ has a pole of order $n$ at $z_0$ if and only if $\lim_{z\to z_0}(z-z_0)^nf(z)$ exists in $\CC\setminus\{0\}$, and then $n$ is the least integer $m\ge0$ with $\lim_{z\to z_0}(z-z_0)^{m+1}f(z)=0$.
Indeed, if $f=(z-z_0)^{-n}h$ with $h(z_0)\neq0$, then $(z-z_0)^kf(z)=(z-z_0)^{k-n}h(z)$ tends to $0$ for $k>n$, to $h(z_0)\neq0$ for $k=n$, and in modulus to $\infty$ for $k<n$.
Conversely, if $(z-z_0)^nf(z)\to c\neq0$, then $(z-z_0)^nf$ is bounded near $z_0$, so by [[T-ZZJDP|Riemann's removable singularity theorem]] it extends to a holomorphic $h$ with $h(z_0)=c$, and $f=(z-z_0)^{-n}h$.
:::
