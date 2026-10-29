---
schema: qual/card@1
id: P-MAXAT-3-01
kind: problem
title: Maxim algebraic topology 3.1
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against section 3, problem 1 of the retained Laurentiu Maxim Problems in Algebraic Topology PDF.
---

::: {.problem}
Find the cohomology ring of real/complex projective spaces and of lens spaces.
:::

::: {.solution}

The coefficient ring matters. The standard clean presentations are over $\mathbb F_2$ for real projective space, over $\ZZ$ for complex projective space, and over $\mathbb F_p$ for the standard $(2n-1)$-dimensional lens space with fundamental group $C_p$, where $p$ is an odd prime.

::: pf

::: {.pf-step #s1-1}

For finite real projective space,
\[
\boxed{
H^*(\mathbb{RP}^{m};\mathbb F_2)
\cong\mathbb F_2[x]/(x^{m+1}),
\qquad |x|=1.}
\]


::: pf-proof

Let $\gamma^1$ be the tautological real line bundle and put
\[
x=w_1(\gamma^1)\in H^1(\mathbb{RP}^m;\mathbb F_2).
\]
The standard CW decomposition has one cell in each dimension $0,\ldots,m$, and all mod-$2$ cellular differentials vanish, so every $H^k$ is one-dimensional over $\mathbb F_2$. The restriction from $\mathbb{RP}^{\infty}$ identifies the generator in degree $k$ with $x^k$ for $0\leq k\leq m$, while dimensional reasons give $x^{m+1}=0$. Hence the displayed truncated polynomial ring.

:::

:::

::: {.pf-step #s1-2}

In particular,
\[
H^*(\mathbb{RP}^{\infty};\mathbb F_2)
\cong\mathbb F_2[x],
\qquad |x|=1.
\]


::: pf-proof

Take the direct limit of the presentations in step [](#s1-1){.pf-ref} under the standard inclusions $\mathbb{RP}^m\subset\mathbb{RP}^{m+1}$. No finite power of $x$ vanishes in the limit.

:::

:::

::: {.pf-step #s1-3}

For finite complex projective space,
\[
\boxed{
H^*(\mathbb{CP}^{m};\ZZ)
\cong\ZZ[u]/(u^{m+1}),
\qquad |u|=2.}
\]


::: pf-proof

Let $u=c_1((\gamma^1_{\CC})^*)$ be the positive generator of $H^2$. The standard CW decomposition has one cell in each even dimension $0,2,\ldots,2m$ and none in odd dimensions, so the cellular differentials vanish and $H^{2k}\cong\ZZ$ for $0\leq k\leq m$. The class $u^k$ evaluates nontrivially on the fundamental class of the linear subspace $\mathbb{CP}^k$, hence generates $H^{2k}$. Dimensional reasons give $u^{m+1}=0$.

:::

:::

::: {.pf-step #s1-4}

Thus
\[
H^*(\mathbb{CP}^{\infty};\ZZ)
\cong\ZZ[u],
\qquad |u|=2.
\]


::: pf-proof

As in step [](#s1-2){.pf-ref}, pass to the direct limit under $\mathbb{CP}^m\subset\mathbb{CP}^{m+1}$.

:::

:::

::: {.pf-step #s1-5}

Let
\[
L^{2n-1}(p;q_1,\ldots,q_n)=S^{2n-1}/C_p,
\]
with $p$ an odd prime. Then
\[
\boxed{
H^*(L^{2n-1};\mathbb F_p)
\cong
\Lambda_{\mathbb F_p}(a)\otimes
\mathbb F_p[b]/(b^n),
\qquad |a|=1,\ |b|=2,}
\]
where
\[
b=\beta(a)
\]
is the Bockstein of $a$.


::: pf-proof

The lens space is the $(2n-1)$-skeleton of the infinite lens space
\[
L^{\infty}(p)=S^{\infty}/C_p=BC_p.
\]
For odd $p$, group cohomology gives
\[
H^*(BC_p;\mathbb F_p)
\cong\Lambda(a)\otimes\mathbb F_p[b],
\qquad b=\beta(a),
\]
with $|a|=1$ and $|b|=2$. Restriction to the $(2n-1)$-skeleton preserves all classes through degree $2n-1$, while $b^n$ has degree $2n$ and therefore vanishes. This gives exactly the displayed truncation. In particular $a^2=0$ because $a$ has odd degree and $p$ is odd.

:::

:::

::: {.pf-step #s1-6}

With integral coefficients, the additive cohomology groups of the same lens space are
\[
H^k(L^{2n-1};\ZZ)
\cong
\begin{cases}
\ZZ,&k=0,2n-1,\\
\ZZ/p,&k=2,4,\ldots,2n-2,\\
0,&\text{otherwise}.
\end{cases}
\]


::: pf-proof

From the one-cell-per-dimension cellular structure, the integral cellular boundary maps alternate between $0$ in odd degree and multiplication by $p$ in even degree. The universal coefficient theorem for cohomology then gives the displayed groups.

:::

:::

::: {.pf-step #s1-7}

Therefore the standard ring presentations are
\[
\boxed{H^*(\mathbb{RP}^{m};\mathbb F_2)=\mathbb F_2[x]/(x^{m+1}),}
\]
\[
\boxed{H^*(\mathbb{CP}^{m};\ZZ)=\ZZ[u]/(u^{m+1}),}
\]
and, for odd prime $p$,
\[
\boxed{H^*(L^{2n-1}(p);\mathbb F_p)
=\Lambda(a)\otimes\mathbb F_p[b]/(b^n),\quad b=\beta(a).}
\]


::: pf-proof

These are precisely steps [](#s1-1){.pf-ref} and [](#s1-3){.pf-ref}, and [](#s1-5){.pf-ref}.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-7){.pf-ref} compute the requested cohomology rings with their standard coefficient choices and record the integral additive groups for lens spaces.

:::

:::

:::
