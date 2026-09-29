---
schema: qual/card@1
id: P-BKF91-4
kind: problem
title: Decomposition of a real matrix into antisymmetric, traceless symmetric, and scalar parts
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: >-
    Split M into skew and symmetric parts, removed the scalar trace component,
    and used trace orthogonality of skew-symmetric and symmetric matrices to
    eliminate the cross terms in tr(M^2).
---

::: {.problem}
Let $M$ be a real $n\times n$ matrix.

1. Prove that
\[
M=A+S+cI,
\]
where $A$ is antisymmetric, $S$ is symmetric with $\operatorname{tr}S=0$, and $c$ is a scalar.

2. Prove that, with this notation,
\[
\operatorname{tr}(M^2)
=\operatorname{tr}(A^2)+\operatorname{tr}(S^2)
+\frac1n(\operatorname{tr}M)^2.
\]
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Define
$$
A\coloneqq\frac{M-M^T}{2},
\qquad
T\coloneqq\frac{M+M^T}{2}.
$$
Then $A$ is antisymmetric, $T$ is symmetric, and
$$
M=A+T.
$$

::: pf-proof

One has
$$
A^T=-A,
\qquad
T^T=T,
$$
by direct transposition, and adding the two definitions gives $A+T=M$.

:::

:::

::: {.pf-step #s2}

Set
$$
c\coloneqq\frac{\operatorname{tr}M}{n},
\qquad
S\coloneqq T-cI.
$$
Then $S$ is symmetric, $\operatorname{tr}S=0$, and
$$
M=A+S+cI.
$$

::: pf-proof

Since $T$ and $I$ are symmetric, so is $S$. Also
$$
\operatorname{tr}T
=
\frac12\left(\operatorname{tr}M+\operatorname{tr}M^T\right)
=
\operatorname{tr}M.
$$
Therefore
$$
\operatorname{tr}S
=
\operatorname{tr}M-cn
=0.
$$
Finally, $T=S+cI$, so step [](#s1){.pf-ref} gives the claimed decomposition.

:::

:::

::: {.pf-step #s3}

One has
$$
\operatorname{tr}(AS)=0.
$$

::: pf-proof

Using invariance of trace under transpose and cyclicity of trace,
$$
\operatorname{tr}(AS)
=
\operatorname{tr}((AS)^T)
=
\operatorname{tr}(S^TA^T)
=
-\operatorname{tr}(SA)
=
-\operatorname{tr}(AS).
$$
Hence $2\operatorname{tr}(AS)=0$.

:::

:::

::: {.pf-step #s4}

One also has
$$
\operatorname{tr}A=0,
\qquad
\operatorname{tr}S=0.
$$

::: pf-proof

The second equality is step [](#s2){.pf-ref}. For the first,
$$
\operatorname{tr}A
=
\operatorname{tr}A^T
=
-\operatorname{tr}A,
$$
so $\operatorname{tr}A=0$.

:::

:::

::: {.pf-step #s5}

One has
$$
\operatorname{tr}(M^2)
=
\operatorname{tr}(A^2)+\operatorname{tr}(S^2)+nc^2.
$$

::: pf-proof

From step [](#s2){.pf-ref},
$$
M=A+S+cI.
$$
Expanding $M^2$ and taking traces gives
$$
\begin{aligned}
\operatorname{tr}(M^2)
&=\operatorname{tr}(A^2)+\operatorname{tr}(S^2)+nc^2\\
&\quad+\operatorname{tr}(AS+SA)
+2c\operatorname{tr}A
+2c\operatorname{tr}S.
\end{aligned}
$$
By step [](#s3){.pf-ref},
$$
\operatorname{tr}(AS+SA)=2\operatorname{tr}(AS)=0,
$$
and step [](#s4){.pf-ref} kills the remaining cross terms.

:::

:::

::: {.pf-step #s6}

Therefore
$$
\boxed{
\operatorname{tr}(M^2)
=
\operatorname{tr}(A^2)+\operatorname{tr}(S^2)
+\frac1n(\operatorname{tr}M)^2}.
$$

::: pf-proof

By step [](#s2){.pf-ref},
$$
c=\frac{\operatorname{tr}M}{n},
$$
so
$$
nc^2=\frac1n(\operatorname{tr}M)^2.
$$
Substitute this into step [](#s5){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s2){.pf-ref} proves part 1, and step [](#s6){.pf-ref} proves part 2.

:::

:::

:::
