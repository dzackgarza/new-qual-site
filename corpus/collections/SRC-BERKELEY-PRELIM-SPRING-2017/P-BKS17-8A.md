---
schema: qual/card@1
id: P-BKS17-8A
kind: problem
title: Power sums $\sum_{k=0}^n k^p$ are polynomials of degree $p+1$ in $n$
classification:
  areas:
  - prelim
  topics:
  - Abstract Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored spaces around inline math and normalized LaTeX against Sp17_Exam_0.pdf page 9 problem 8A.
- event: source-checked
  by: chatgpt
  date: 2026-10-02
  note: Independently reviewed the supplied Berkeley Spring 2017 finite-difference solution. Its displayed definition of $\Delta S_p(n)$ uses $S_{p-1}(n)$ where a backward difference would require $S_p(n-1)$, and the following equality instead computes the difference of $n^p$. The solution below uses a separate telescoping induction.
- event: solution-written
  by: chatgpt
  date: 2026-10-02
- event: solution-reviewed
  by: chatgpt
  date: 2026-10-02
  note: Verified the base case, the telescoping binomial identity, and the leading coefficient in the inductive step.
---

::: {.problem}
Show that for each integer $p \geq 0$ the sum

$$
S_p(n) = \sum_{k=0}^{n} k^p
$$

is a polynomial of degree $p + 1$ in the variable $n$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For $p=0$, one has $S_0(n)=n+1$, a polynomial of degree $1$ with leading coefficient $1$.


::: pf-proof

With the usual zeroth-power convention in the statement, every summand $k^0$ equals $1$. Hence
$$
S_0(n)=\sum_{k=0}^n 1=n+1.
$$

:::

:::

::: {.pf-step #s1-2}

Let $p\geq1$, and suppose that for every integer $j$ with $0\leq j<p$, the function $S_j(n)$ is a polynomial of degree $j+1$ with leading coefficient $1/(j+1)$. Then
$$
(p+1)S_p(n)
=
(n+1)^{p+1}
-
\sum_{j=0}^{p-1}\binom{p+1}{j}S_j(n).
$$


::: pf-proof

For every integer $k\geq0$, the binomial theorem gives
$$
\begin{aligned}
(k+1)^{p+1}-k^{p+1}
&=\sum_{j=0}^{p}\binom{p+1}{j}k^j.
\end{aligned}
$$
Summing this identity from $k=0$ to $k=n$ telescopes on the left and yields
$$
(n+1)^{p+1}
=
\sum_{j=0}^{p}\binom{p+1}{j}S_j(n).
$$
Since $\binom{p+1}{p}=p+1$, isolating the term with $j=p$ gives the claimed identity.

:::

:::

::: {.pf-step #s1-3}

Under the induction hypothesis in step [](#s1-2){.pf-ref}, $S_p(n)$ is a polynomial of degree $p+1$ with leading coefficient $1/(p+1)$.


::: pf-proof

By step [](#s1-2){.pf-ref}, $(p+1)S_p(n)$ is a polynomial in $n$. For every $j<p$, the induction hypothesis gives
$$
\deg S_j=j+1\leq p.
$$
Therefore every term in
$$
\sum_{j=0}^{p-1}\binom{p+1}{j}S_j(n)
$$
has degree at most $p$. The remaining term $(n+1)^{p+1}$ has degree $p+1$ and leading coefficient $1$, so no term in the sum can cancel its leading term. Thus $(p+1)S_p(n)$ has degree $p+1$ and leading coefficient $1$, and division by $p+1$ gives the assertion.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} is the base case, and steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref} establish the induction step. Hence the assertion holds for every integer $p\geq0$.

:::

:::

:::
