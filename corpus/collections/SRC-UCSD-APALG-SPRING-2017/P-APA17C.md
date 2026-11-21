---
schema: qual/card@1
id: P-APA17C
kind: problem
title: Pointwise larger Euclidean action implies strictly larger singular values
classification:
  areas:
  - applied-algebra
  topics:
  - Linear Algebra
  - Singular Values
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Provenance recorded: Problem 3 of the Qualifying Exam in Applied Algebra of May 30, 2017, printed p.
    3 of the nine-page paper retained at assets/attachments/APPLIED-ALGEBRA-EXAM.pdf, is the statement
    the card answers, and the paragraph at the head of the solution records that the paper prints no
    solutions, so the argument is the card's own. Checked: the statement against the paper's text layer
    at the page named; the Courant-Fischer min-max argument and the compactness step on the unit sphere
    of the maximising subspace; `qualc.authoring check` on the card, and `tmp/lam.sh` for the numbering
    and the QED. Not checked: no retained solution set exists for this paper to compare the argument
    with, and no other card of the collection in this pass.
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Let $A, B \in \RR^{n \times n}$ be two real matrices.
Denote by $\sigma_i(A)$ (resp., $\sigma_i(B)$) the $i$-th largest singular value of $A$ (resp., $B$). If $\norm{Ax}_2 > \norm{Bx}_2$ for all $x \neq 0$, show that $\sigma_i(A) > \sigma_i(B)$ for all $i = 1, \dots, n$.
:::

::: {.solution}

The problem is Problem 3 of the Qualifying Exam in Applied Algebra of May 30, 2017, retained at `assets/attachments/APPLIED-ALGEBRA-EXAM.pdf`. The paper prints no solutions, so nothing below is transcribed: the argument is the card's own, and what it supplies is the min-max argument: a subspace attaining the maximum for $B$ gives $\sigma_i(A)>\sigma_i(B)$ through the strict inequality on its compact unit sphere and the Courant--Fischer characterisation for $A$


::: pf

::: {.pf-step #s1}

By the Courant–Fischer (min-max) characterization, the $i$-th singular value of an $n \times n$ matrix $M$ is given by:
$$
\sigma_i(M) = \max_{\substack{V \subseteq \RR^n \\ \dim V = n - i + 1}} \min_{\substack{x \in V \\ \norm{x}_2 = 1}} \norm{Mx}_2.
$$

::: pf-proof

min-max theorem for singular values (eigenvalues of $M^T M$).

:::

:::

::: {.pf-step #s2}

Choose a subspace $V_i \subseteq \RR^n$ of dimension $n - i + 1$ that achieves the maximum for $B$:
$$
\sigma_i(B) = \min_{\substack{x \in V_i \\ \norm{x}_2 = 1}} \norm{Bx}_2.
$$

::: pf-proof

the set of $(n-i+1)$-dimensional subspaces is a Grassmannian, and the maximum is attained (for instance, by the span of the right singular vectors $v_i, v_{i+1}, \dots, v_n$ of $B$).

:::

:::

::: pf-step

The unit sphere $S(V_i) = \{x \in V_i : \norm{x}_2 = 1\}$ is compact.

::: pf-proof

the unit sphere in a finite-dimensional Euclidean subspace is closed and bounded.

:::

:::

::: pf-step

For all $x \in S(V_i)$, $\norm{Ax}_2 > \norm{Bx}_2$.

::: pf-proof

hypothesis applied to nonzero vectors $x \in S(V_i)$.

:::

:::

::: {.pf-step #s5}

The function $f(x) = \norm{Ax}_2 - \norm{Bx}_2$ is continuous and strictly positive on the compact set $S(V_i)$, so it attains a strictly positive minimum:
$$
\min_{x \in S(V_i)} \bigl(\norm{Ax}_2 - \norm{Bx}_2\bigr) = \varepsilon > 0.
$$

::: pf-proof

Extreme Value Theorem for continuous functions on compact sets.

:::

:::

::: {.pf-step #s6}

Therefore, for every $x \in S(V_i)$, $\norm{Ax}_2 \ge \norm{Bx}_2 + \varepsilon$.

::: pf-proof

Step [](#s5){.pf-ref}.

:::

:::

::: {.pf-step #s7}

Taking the minimum over $x \in S(V_i)$ gives:
$$
\min_{x \in S(V_i)} \norm{Ax}_2 \ge \min_{x \in S(V_i)} \norm{Bx}_2 + \varepsilon = \sigma_i(B) + \varepsilon > \sigma_i(B).
$$

::: pf-proof

Steps [](#s2){.pf-ref} and [](#s6){.pf-ref}.

:::

:::

::: {.pf-step #s8}

By the min-max characterization step [](#s1){.pf-ref} for $A$, since $\dim V_i = n - i + 1$:
$$
\sigma_i(A) \ge \min_{x \in S(V_i)} \norm{Ax}_2 > \sigma_i(B).
$$

::: pf-proof

Steps [](#s1){.pf-ref} and [](#s7){.pf-ref}.

:::

:::

::: {.pf-step #s9}

Thus $\sigma_i(A) > \sigma_i(B)$ for all $i = 1, \dots, n$.

::: pf-proof

Step [](#s8){.pf-ref} holds for each index $i \in \{1, \dots, n\}$.

:::

:::

::: pf-qed

Step [](#s9){.pf-ref}.

:::

:::

:::
