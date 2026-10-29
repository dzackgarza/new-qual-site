---
schema: qual/card@1
id: P-MAXAT-1-01
kind: problem
title: A connected manifold bounding a compact manifold has even Euler characteristic
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
$$
\partial W=M.
$$
All homology groups below are taken with coefficients in $\FF_2$, so no orientability assumption is needed.

::: pf

::: {.pf-step #s1-1}

If $\dim W=n$, then Poincaré--Lefschetz duality gives
$$
H_i(W,M;\FF_2)
\cong H^{n-i}(W;\FF_2).
$$


::: pf-proof

Every manifold is orientable over $\FF_2$. Poincaré--Lefschetz duality for the compact $n$-manifold $W$ therefore identifies relative homology of $(W,\partial W)$ with cohomology of $W$ in complementary degree. Since $M=\partial W$, this is the displayed isomorphism.

:::

:::

::: {.pf-step #s1-2}

Consequently,
$$
\chi(W,M)=(-1)^n\chi(W).
$$


::: pf-proof

Over the field $\FF_2$, the universal coefficient theorem gives
$$
\dim H^j(W;\FF_2)=\dim H_j(W;\FF_2).
$$
Using step [](#s1-1){.pf-ref},
$$
\begin{aligned}
\chi(W,M)
&=\sum_i(-1)^i\dim H_i(W,M;\FF_2)\\
&=\sum_i(-1)^i\dim H^{n-i}(W;\FF_2)\\
&=(-1)^n\chi(W).
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-3}

Additivity of Euler characteristic for the pair $(W,M)$ gives
$$
\chi(W)=\chi(M)+\chi(W,M).
$$


::: pf-proof

The long exact homology sequence of the pair $(W,M)$ is finite-dimensional in each degree and vanishes outside finitely many degrees. Taking the alternating sum of dimensions in this exact sequence gives
$$
\chi(W)-\chi(M)-\chi(W,M)=0.
$$

:::

:::

::: {.pf-step #s1-4}

Combining steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref} yields
$$
\chi(M)=\bigl(1-(-1)^n\bigr)\chi(W).
$$


::: pf-proof

Substitute $\chi(W,M)=(-1)^n\chi(W)$ from step [](#s1-2){.pf-ref} into step [](#s1-3){.pf-ref} and rearrange.

:::

:::

::: {.pf-step #s1-5}

Hence $\chi(M)$ is even.


::: pf-proof

If $n$ is even, step [](#s1-4){.pf-ref} gives $\chi(M)=0$. If $n$ is odd, it gives
$$
\chi(M)=2\chi(W).
$$
In either case $\chi(M)\in2\ZZ$.

:::

:::

::: {.pf-step #s1-6}

Therefore
$$
\boxed{\chi(M)\text{ is even}.}
$$


::: pf-proof

This is exactly step [](#s1-5){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} proves the claim.

:::

:::

:::
