---
schema: qual/card@1
id: P-UCI18H5-3
kind: problem
title: Iterates of a disk self-map fixing the origin converge locally uniformly to zero unless it is a rotation
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
  - Iteration
relations:
- kind: related-to
  target: E-HM213A17-53
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-10-31
---

::: {.problem}
Suppose $f:\DD\to\DD$ is holomorphic and $f(0)=0$.
Prove that either $f$ is a rotation of the unit disc, or the sequence of iterates $\{f^n\}$ converges to zero uniformly on compact subsets of $\DD$.
:::

::: {.solution}
For $0<r<1$ write $M(r)=\max_{\abs z\le r}\abs{f(z)}$, which is attained because the closed disc is compact.

::: pf

::: {.pf-step #schwarz}
$M(r)\le r$, and $M(r)<r$ unless $f$ is a rotation.

::: pf-proof
The Schwarz lemma gives $\abs{f(z)}\le\abs z$ on $\DD$ because $f(0)=0$, so $M(r)\le r$.
If $M(r)=r$, pick $z_0$ with $\abs{z_0}\le r$ and $\abs{f(z_0)}=r$. If $\abs{z_0}<r$ then $\abs{f(z_0)}\le\abs{z_0}<r$, so $\abs{z_0}=r$ and equality holds in the Schwarz lemma at a point of the open disc; the equality case of the Schwarz lemma then makes $f$ a rotation.
Hence for a non-rotation $M(r)<r$ for every $r\in(0,1)$.
:::

:::

::: {.pf-step #iterates-shrink}
If $f$ is not a rotation, then $M(r_n)\to0$ for every decreasing sequence $r_{n+1}=M(r_n)$ with $0<r_0<1$.

::: pf-proof
The sequence $(r_n)$ is decreasing because $M(r)\le r$, and bounded below by $0$, so it converges to some $L\ge0$.
If $L>0$ then $L=\lim r_{n+1}=\lim M(r_n)=M(L)$ by continuity of $M$, contradicting step [](#schwarz){.pf-ref} which gives $M(L)<L$ for a non-rotation.
Hence $L=0$.
:::

:::

::: {.pf-step #uniform-convergence}
Either $f$ is a rotation of the unit disc, or $f^n\to0$ uniformly on compact subsets of $\DD$.

::: pf-proof
Let $K\subseteq\DD$ be compact and choose $0<r_0<1$ with $K\subseteq\overline{D_{r_0}}$, and define $r_{n+1}=M(r_n)$.
Since $f$ maps $\overline{D_{r_n}}$ into $\overline{D_{r_{n+1}}}$, induction gives $f^n(K)\subseteq\overline{D_{r_n}}$.
By step [](#iterates-shrink){.pf-ref} the numbers $r_n$ tend to $0$, so $\sup_{z\in K}\abs{f^n(z)}\le r_n\to0$, which is uniform convergence to $0$ on $K$.
Since $K$ was arbitrary, this gives the second alternative whenever $f$ is not a rotation, and a rotation satisfies the first alternative.
:::

:::

:::
:::
