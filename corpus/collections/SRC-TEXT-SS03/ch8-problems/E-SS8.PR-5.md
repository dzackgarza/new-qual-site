---
schema: qual/card@1
id: E-SS8.PR-5
kind: problem
title: Zeros of bounded holomorphic functions on the upper half-plane
classification:
  areas:
  - complex-analysis
  topics:
  - Blaschke Products
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-01
  note: >-
    Statement compared with Stein--Shakarchi, *Complex Analysis*, Chapter 8, §3, problem 5, read
    from `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`. The card matches the printed
    exercise, parts (a) and (b); nothing was changed.
- event: solution-written
  by: claude
  date: 2026-11-01
  note: >-
    Both parts, by transport to the disc with $\varphi(z)=(z-i)/(z+i)$: the zero $ir$ goes to
    $(r-1)/(r+1)$ with $1-\abs{\varphi(ir)}=2\min(r,1)/(1+r)$, comparable to $\min(r,1)$ because
    $\{r_n\}$ is bounded. (a) is the Blaschke necessity $\sum(1-\abs{z_n})<\infty$ obtained from
    Jensen's formula, so divergence of the sum forces $F\equiv0$; (b) is the Blaschke product of the
    image sequence, which converges exactly under $\sum r_n<\infty$. Nothing is left in outline.
---

::: {.exercise}
Let $\{r_n\}_{n=1}^{\infty}$ be a bounded sequence of positive numbers and let $\halfplane$ be the upper half-plane.

(a) Suppose $F:\halfplane\to\CC$ is bounded and holomorphic and vanishes at $ir_n$ for every $n$. Prove that $\sum_{n=1}^{\infty}r_n=\infty$ implies $F=0$.

(b) If $\sum_{n=1}^{\infty}r_n<\infty$, construct a bounded holomorphic function on $\halfplane$ whose zeros are exactly the points $ir_n$.

For related results in the unit disc, see Problems 1 and 2 in Chapter 5.
:::

::: {.solution}

Let $\HH$ be the upper half-plane and $\varphi(z)=\dfrac{z-i}{z+i}$, a biholomorphism of $\HH$ onto the unit disc $\DD$ with inverse $\varphi^{-1}(w)=i\dfrac{1+w}{1-w}$. For $r>0$,
$$
\varphi(ir)=\frac{r-1}{r+1}=:z_r,\qquad 1-\abs{z_r}=\frac{2\min(r,1)}{1+r}.
$$

::: pf

::: {.pf-step #s1}

Since $\{r_n\}$ is bounded, say $r_n\le M$ with $M\ge1$, one has
$$
\frac{2}{1+M}\min(r_n,1)\le1-\abs{z_{r_n}}\le\min(r_n,1),
$$
so $\sum_n r_n$ and $\sum_n\bigl(1-\abs{z_{r_n}}\bigr)$ diverge or converge together.

::: pf-proof

For $0<r\le1$: $1-\abs{z_r}=1-\frac{1-r}{1+r}=\frac{2r}{1+r}$ and $\min(r,1)=r$, so the ratio is $\frac{2}{1+r}\in\bigl[\frac{2}{1+M},2\bigr]$ because $r\le M$.

For $r\ge1$: $1-\abs{z_r}=1-\frac{r-1}{r+1}=\frac{2}{1+r}$ and $\min(r,1)=1$, so $1-\abs{z_r}=\frac{2}{1+r}\ge\frac{2}{1+M}$ and $\frac{2}{1+r}\le1$.

Also $\sum_n r_n$ diverges if and only if $\sum_n\min(r_n,1)$ diverges, since $\min(r_n,1)\ge r_n/M$.

:::

:::

::: {.pf-step #s2}

A non-zero bounded holomorphic function on $\DD$ with zeros $z_n$ (counted without multiplicity) satisfies $\sum_n\bigl(1-\abs{z_n}\bigr)<\infty$.

::: pf-proof

This is the Blaschke necessary condition. Let $G$ be holomorphic on $\DD$ with $\abs{G}\le A$ and $G\not\equiv0$, and let $z_1,z_2,\dots$ be its zeros other than $0$; write $G(w)=w^kH(w)$ with $H$ holomorphic and $H(0)\ne0$.

For $0<\varrho<1$ Jensen's formula on the disc $\abs{w}<\varrho$ gives
$$
\log\abs{H(0)}+\sum_{\abs{z_n}<\varrho}\log\frac{\varrho}{\abs{z_n}}=\frac{1}{2\pi}\int_0^{2\pi}\log\abs{H(\varrho e^{i\theta})}\,d\theta\le\log M_\varrho,
\qquad M_\varrho=\max_{\abs{w}=\varrho}\abs{H(w)} .
$$
For $\varrho\ge\frac12$ one has $M_\varrho\le2^kA$, because $\abs{H(w)}=\abs{G(w)}\abs{w}^{-k}\le A\varrho^{-k}\le2^kA$ on $\abs{w}=\varrho$. Hence
$$
\sum_{\abs{z_n}<\varrho}\log\frac{\varrho}{\abs{z_n}}\le\log(2^kA)-\log\abs{H(0)}<\infty
$$
with a bound independent of $\varrho\ge\frac12$. As $\varrho$ increases to $1$ both the set of terms and each term $\log(\varrho/\abs{z_n})$ increase, so the limit is $\sum_n\log\frac{1}{\abs{z_n}}$, which is therefore finite. Since $\log(1/t)\ge1-t$ for $0<t\le1$,
$$
\sum_n\bigl(1-\abs{z_n}\bigr)\le\sum_n\log\frac{1}{\abs{z_n}}<\infty .
$$

:::

:::

::: {.pf-step #s3}

Part (a): if $F$ is bounded and holomorphic on $\HH$ and $F(ir_n)=0$ for all $n$, and $\sum r_n=\infty$, then $F\equiv0$.

::: pf-proof

Suppose $F\not\equiv0$. Then $G=F\circ\varphi^{-1}$ is holomorphic and bounded on $\DD$, not identically zero, and $G(z_{r_n})=F(ir_n)=0$ for every $n$. By step [](#s2){.pf-ref}, $\sum_n(1-\abs{z_{r_n}})<\infty$, and by step [](#s1){.pf-ref} this forces $\sum_n r_n<\infty$, contradicting the hypothesis. Hence $F\equiv0$.

:::

:::

::: {.pf-step #s4}

Part (b): if $\sum_n r_n<\infty$, there is a bounded holomorphic $F$ on $\HH$ whose zeros are exactly the points $ir_n$.

::: pf-proof

By step [](#s1){.pf-ref}, $\sum_n(1-\abs{z_{r_n}})<\infty$. Let $k$ be the number of $n$ with $z_{r_n}=0$ (that is, $r_n=1$), which is finite because $\sum r_n<\infty$. For every $n$ with $z_{r_n}\ne0$ put
$$
b_n(w)=\frac{\abs{z_{r_n}}}{z_{r_n}}\cdot\frac{z_{r_n}-w}{1-\overline{z_{r_n}}\,w},
$$
a disc automorphism exchanging $0$ and $z_{r_n}$ and with $\abs{b_n(w)}=1$ on $\abs{w}=1$. The Blaschke product
$$
B(w)=w^k\prod_{n\,:\,z_{r_n}\ne0}b_n(w)
$$
converges uniformly on compact subsets of $\DD$ because $\sum_n(1-\abs{z_{r_n}})<\infty$, and $\abs{B(w)}\le1$ there; its zeros are exactly the points $z_{r_n}$, with the point $0$ accounted for by $w^k$.

Set $F(z)=B(\varphi(z))$. Then $F$ is holomorphic on $\HH$, bounded by $1$, and $F(z)=0$ exactly when $\varphi(z)=z_{r_n}$ for some $n$, that is exactly when $z=ir_n$, since $z_r$ determines $r>0$ and $\varphi$ is injective.

:::

:::

:::

:::
