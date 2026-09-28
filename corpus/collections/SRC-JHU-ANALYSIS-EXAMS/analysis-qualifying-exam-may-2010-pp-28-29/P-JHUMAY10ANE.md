---
schema: qual/card@1
id: P-JHUMAY10ANE
kind: problem
title: 'Uniform $H^\sigma$ bounds pass to an $L^2$ limit'
classification:
  areas:
  - real-analysis
  topics:
  - Fourier Transform
  - Lp Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 5 of the JHU Analysis Qualifying Exam, May 2010, in the preserved exam collection.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Let $f_j\in L^2(\mathbb R^n)$ with $f_j\to f$ in $L^2$. Suppose there exists $M<\infty$ such that
\[
\|f_j\|_{H^\sigma}\le M
\qquad(j\ge1),
\]
where
\[
\|g\|_{H^\sigma}^2=\int_{\mathbb R^n}(1+|\xi|^2)^\sigma|\widehat g(\xi)|^2\,d\xi.
\]
Must $f\in H^\sigma$? Prove your answer.
:::

::: {.solution}
<1>1. After passing to a subsequence, the Fourier transforms converge almost everywhere.
::: {.proof}
By the [[PR-JCZKL|Plancherel theorem]],
$$
\widehat f_j\longrightarrow\widehat f
\qquad\text{in }L^2(\mathbb R^n).
$$
Hence there is a subsequence $(j_k)$ such that
$$
\widehat f_{j_k}(\xi)\longrightarrow\widehat f(\xi)
$$
for almost every $\xi$.
:::

<1>2. The limit belongs to $H^\sigma$ and satisfies $\|f\|_{H^\sigma}\le M$.
::: {.proof}
Set
$$
w(\xi)=(1+|\xi|^2)^\sigma
$$
which is positive and measurable for every real $\sigma$. By step <1>1 and [[FT-P5UNP|Fatou's lemma]],
$$
\begin{aligned}
\|f\|_{H^\sigma}^2
&=\int w(\xi)|\widehat f(\xi)|^2\,d\xi\\
&\le\liminf_{k\to\infty}\int w(\xi)|\widehat f_{j_k}(\xi)|^2\,d\xi\\
&=\liminf_{k\to\infty}\|f_{j_k}\|_{H^\sigma}^2\le M^2.
\end{aligned}
$$
The weighted integral is therefore finite, so
$$
f\in H^\sigma(\mathbb R^n),
\qquad
\|f\|_{H^\sigma}\le M.
$$
:::

<1>3. Q.E.D.
::: {.proof}
Step <1>2 proves that the uniform $H^\sigma$ bound passes to the $L^2$ limit.
:::
:::
