---
schema: qual/card@1
id: P-JHUSP07ANG
kind: problem
title: 'Weakly convergent $L^2$ sequences with unbounded norms'
classification:
  areas:
  - real-analysis
  topics:
  - Weak Convergence
  - Lp Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 7 of the JHU Analysis Qualifying Exam, Spring 2007, in the preserved exam collection.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Suppose $(f_n)$ is a sequence in $L^2(\mathbb R)$ that converges weakly to $f\in L^2(\mathbb R)$. Is it possible that
\[
\|f_n\|_{L^2}\longrightarrow\infty?
\]
:::

::: {.solution}
<1>1. The associated functionals have uniformly bounded operator norms.
::: {.proof}
For each $n$, define the bounded linear functional
$$
T_n(g)=\langle f_n,g\rangle_{L^2},
\qquad g\in L^2(\mathbb R).
$$
Weak convergence means that for every fixed $g\in L^2$,
$$
T_n(g)=\langle f_n,g\rangle\longrightarrow\langle f,g\rangle.
$$
Hence for every $g$ the scalar sequence $(T_n(g))$ is bounded. By the [[T-F2THV|uniform boundedness principle]],
$$
\sup_n\|T_n\|<\infty.
$$
:::

<1>2. The functional norms are the $L^2$ norms of the representing functions.
::: {.proof}
By the [[T-LDCZB|Riesz representation theorem for Hilbert spaces]],
$$
\|T_n\|=\|f_n\|_2.
$$
Therefore
$$
\sup_n\|f_n\|_2<\infty.
$$
:::

<1>3. Q.E.D.
::: {.proof}
By step <1>1, the norms $\|T_n\|$ are uniformly bounded; step <1>2 therefore shows that $\|f_n\|_2$ cannot tend to infinity.
:::
:::
