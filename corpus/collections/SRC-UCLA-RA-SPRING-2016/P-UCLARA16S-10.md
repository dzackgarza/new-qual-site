---
schema: qual/card@1
id: P-UCLARA16S-10
kind: problem
title: No holomorphic function on the disk tends to infinity at the boundary
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Spring 2016, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Does there exist a function $f(z)$ holomorphic in the disk $\abs{z}<1$ such that
$$
\lim_{\abs{z}\to1}\abs{f(z)}=\infty?
$$
Either find one or prove that none exist.
:::

::: {.solution}

::: pf

::: pf-step

If such a function $f$ existed, all of its zeros would lie in some smaller closed disk
$$
\{\abs{z}\le r\}
\qquad
(r<1),
$$
and there would be only finitely many of them, counted with multiplicity.


::: pf-proof

The boundary-growth hypothesis implies that there is $r<1$ such that
$$
\abs{f(z)}>1
\qquad
(r<\abs{z}<1).
$$
Hence every zero lies in $\abs{z}\le r$. The function is not identically zero because its modulus tends to infinity near the boundary. Zeros of a nonzero holomorphic function are isolated, so a compact subset of the disk contains only finitely many zeros.

:::

:::

::: {.pf-step #s1-2}

Let $a_1,\dots,a_N$ be those zeros, listed with multiplicity, and set
$$
g(z)
\coloneqq
\frac{f(z)}
{\prod_{j=1}^N(z-a_j)}.
$$
Then $g$ is holomorphic and nonvanishing on $\DD$, and
$$
\abs{g(z)}\longrightarrow\infty
\qquad
(\abs{z}\to1).
$$


::: pf-proof

The quotient has removable singularities at the zeros $a_j$, and after removal it is holomorphic with no zeros in $\DD$.

For $\abs{z}<1$,
$$
\abs{
\prod_{j=1}^N(z-a_j)
}
\le
\prod_{j=1}^N(1+\abs{a_j})
\eqqcolon C<\infty.
$$
Therefore
$$
\abs{g(z)}
\ge
\frac{\abs{f(z)}}{C},
$$
and the asserted boundary divergence follows from that of $f$.

:::

:::

::: pf-step

The reciprocal
$$
h\coloneqq\frac1g
$$
extends continuously to $\overline{\DD}$ by setting
$$
h(\zeta)=0
\qquad
(\abs{\zeta}=1).
$$


::: pf-proof

Since $g$ is holomorphic and nonvanishing on $\DD$, the function $h=1/g$ is holomorphic there. Step [](#s1-2){.pf-ref} gives
$$
\abs{h(z)}
=
\frac1{\abs{g(z)}}
\longrightarrow0
\qquad
(\abs{z}\to1).
$$
Thus defining $h=0$ on the unit circle gives a continuous extension to the closed disk.

:::

:::

::: {.pf-step #s1-4}

Such an $h$ cannot exist.


::: pf-proof

The continuous function $\abs{h}$ on the compact disk $\overline{\DD}$ attains its maximum. Since $h$ vanishes on the boundary, if $h$ were not identically zero then its positive maximum would be attained at an interior point. The maximum-modulus principle would then force $h$ to be constant, which is impossible for a nonzero constant with zero boundary values. Hence $h\equiv0$.

But $h=1/g$ on $\DD$, so $h$ cannot vanish anywhere there. This is a contradiction.

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
\boxed{\text{no such holomorphic function }f\text{ exists}.}
$$


::: pf-proof

The assumption of existence leads to the contradiction in step [](#s1-4){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} answers the problem.

:::

:::

:::
