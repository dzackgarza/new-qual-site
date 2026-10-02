---
schema: qual/card@1
id: P-WESRA11-4
kind: problem
title: 'Only countably many centered spheres can have positive mass'
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 4 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md.
---

::: {.problem}
Let $\mu$ be a finite Borel measure on $\mathbb R^d$.
For $t>0$ set
\[
S_t=\{x\in\mathbb R^d:|x|=t\}.
\]
Prove that
\[
\{t>0:\mu(S_t)>0\}
\]
is at most countable.
:::

::: {.solution}
Let
\[
A=\{t>0:\mu(S_t)>0\},
\qquad
A_n=\left\{t>0:\mu(S_t)\ge\frac1n\right\}
\quad(n\ge1).
\]

<1>1. For distinct \(s,t>0\), the spheres \(S_s\) and \(S_t\) are disjoint.

::: {.proof}
If \(x\in S_s\cap S_t\), then \(|x|=s\) and \(|x|=t\), hence \(s=t\). Thus distinct radii give disjoint spheres.
:::

<1>2. Every set \(A_n\) is finite.

::: {.proof}
Suppose \(A_n\) were infinite. For any integer \(N\ge1\), choose distinct \(t_1,\dots,t_N\in A_n\). By step <1>1 the Borel sets \(S_{t_1},\dots,S_{t_N}\) are pairwise disjoint, so finite additivity gives
\[
\mu(\mathbb R^d)
\ge
\mu\!\left(\bigcup_{j=1}^N S_{t_j}\right)
=\sum_{j=1}^N\mu(S_{t_j})
\ge\frac{N}{n}.
\]
Since \(\mu(\mathbb R^d)<\infty\), this is impossible for arbitrarily large \(N\). Hence \(A_n\) is finite.
:::

<1>3. One has
\[
A=\bigcup_{n=1}^\infty A_n.
\]

::: {.proof}
Every \(A_n\) is contained in \(A\). Conversely, if \(t\in A\), then \(\mu(S_t)>0\), so there exists \(n\) with \(1/n\le\mu(S_t)\). Thus \(t\in A_n\).
:::

<1>4. Therefore \(\boxed{A\text{ is at most countable}}\).

::: {.proof}
By step <1>2 each \(A_n\) is finite, and by step <1>3 the set \(A\) is a countable union of these finite sets.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required conclusion.
:::
:::
