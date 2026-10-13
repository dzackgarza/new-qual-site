---
schema: qual/card@1
id: P-MAXAT-1-01
kind: problem
title: Maxim algebraic topology 1.1
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against section 1, problem 1 of the retained Laurentiu Maxim Problems in Algebraic Topology PDF.
---

::: {.problem}
Show that if a connected manifold M is the boundary of a compact manifold, then the Euler characteristic of M is even.
:::

::: {.solution}
Let $W$ be a compact manifold with boundary
\[
\partial W=M.
\]
All homology groups below are taken with coefficients in $\mathbb F_2$, so no orientability assumption is needed.

<1>1. If $\dim W=n$, then Poincaré--Lefschetz duality gives
\[
H_i(W,M;\mathbb F_2)
\cong H^{n-i}(W;\mathbb F_2).
\]

::: {.proof}
Every manifold is orientable over $\mathbb F_2$. Poincaré--Lefschetz duality for the compact $n$-manifold $W$ therefore identifies relative homology of $(W,\partial W)$ with cohomology of $W$ in complementary degree. Since $M=\partial W$, this is the displayed isomorphism.
:::

<1>2. Consequently,
\[
\chi(W,M)=(-1)^n\chi(W).
\]

::: {.proof}
Over the field $\mathbb F_2$, the universal coefficient theorem gives
\[
\dim H^j(W;\mathbb F_2)=\dim H_j(W;\mathbb F_2).
\]
Using step <1>1,
\[
\begin{aligned}
\chi(W,M)
&=\sum_i(-1)^i\dim H_i(W,M;\mathbb F_2)\\
&=\sum_i(-1)^i\dim H^{n-i}(W;\mathbb F_2)\\
&=(-1)^n\chi(W).
\end{aligned}
\]
:::

<1>3. Additivity of Euler characteristic for the pair $(W,M)$ gives
\[
\chi(W)=\chi(M)+\chi(W,M).
\]

::: {.proof}
The long exact homology sequence of the pair $(W,M)$ is finite-dimensional in each degree and vanishes outside finitely many degrees. Taking the alternating sum of dimensions in this exact sequence gives
\[
\chi(W)-\chi(M)-\chi(W,M)=0.
\]
:::

<1>4. Combining steps <1>2--<1>3 yields
\[
\chi(M)=\bigl(1-(-1)^n\bigr)\chi(W).
\]

::: {.proof}
Substitute $\chi(W,M)=(-1)^n\chi(W)$ from step <1>2 into step <1>3 and rearrange.
:::

<1>5. Hence $\chi(M)$ is even.

::: {.proof}
If $n$ is even, step <1>4 gives $\chi(M)=0$. If $n$ is odd, it gives
\[
\chi(M)=2\chi(W).
\]
In either case $\chi(M)\in2\mathbb Z$.
:::

<1>6. Therefore
\[
\boxed{\chi(M)\text{ is even}.}
\]

::: {.proof}
This is exactly step <1>5.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 proves the claim.
:::
:::
