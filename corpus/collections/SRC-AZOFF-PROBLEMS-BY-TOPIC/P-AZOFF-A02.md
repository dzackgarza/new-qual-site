---
schema: qual/card@1
id: P-AZOFF-A02
kind: problem
title: Continuous functions vanishing at $\pm\infty$ are uniformly continuous
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Compactness, connectedness, and functions of one real variable, Problem 2, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Proved uniform continuity by combining the two tail limits with
    Heine-Cantor on a compact interval enlarged by one unit. Choosing the final
    delta at most 1 makes every close pair either lie in that compact interval
    or have both points in the small-value tails. The source compilation
    contains no worked solution for this problem.
---

::: {.problem}
Suppose $f:\mathbb R\to\mathbb R$ is continuous and
\[
\lim_{x\to\pm\infty}f(x)=0.
\]
Prove that $f$ is uniformly continuous.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

For every $\varepsilon>0$ there is $R>0$ such that
$$
\abs{f(x)}<\frac{\varepsilon}{2}
$$
whenever
$$
\abs{x}>R.
$$

::: pf-proof

The hypotheses
$$
\lim_{x\to+\infty}f(x)=0
\qquad\text{and}\qquad
\lim_{x\to-\infty}f(x)=0
$$
give numbers $R_+,R_->0$ such that the displayed bound holds for
$x>R_+$ and for $x<-R_-$, respectively. Taking
$$
R=\max\{R_+,R_-\}
$$
gives the claim.

:::

:::

::: {.pf-step #s2}

For the $R$ from step [](#s1){.pf-ref}, there is $\delta_0>0$ such that
$$
\abs{x-y}<\delta_0,
\qquad
x,y\in[-R-1,R+1]
$$
implies
$$
\abs{f(x)-f(y)}<\varepsilon.
$$

::: pf-proof

The interval
$$
[-R-1,R+1]
$$
is compact, and $f$ is continuous on it. By the Heine--Cantor theorem, the
restriction of $f$ to this interval is uniformly continuous. Applying that
uniform continuity with the given $\varepsilon$ gives $\delta_0$.

:::

:::

::: {.pf-step #s3}

With
$$
\delta=\min\{1,\delta_0\},
$$
every $x,y\in\RR$ satisfying $\abs{x-y}<\delta$ also satisfy
$$
\abs{f(x)-f(y)}<\varepsilon.
$$

::: pf-proof

Suppose first that
$$
\abs{x}\leq R
\qquad\text{or}\qquad
\abs{y}\leq R.
$$
Since $\abs{x-y}<1$, both points then belong to
$$
[-R-1,R+1].
$$
The desired estimate follows from step [](#s2){.pf-ref} because
$$
\abs{x-y}<\delta\leq\delta_0.
$$

Otherwise
$$
\abs{x}>R
\qquad\text{and}\qquad
\abs{y}>R.
$$
By step [](#s1){.pf-ref},
$$
\abs{f(x)}<\frac{\varepsilon}{2},
\qquad
\abs{f(y)}<\frac{\varepsilon}{2}.
$$
Hence
$$
\abs{f(x)-f(y)}
\leq
\abs{f(x)}+\abs{f(y)}
<
\varepsilon.
$$
Thus the same $\delta$ works in every case.

:::

:::

::: {.pf-step #s4}

The function $f$ is uniformly continuous on $\RR$.

::: pf-proof

Step [](#s3){.pf-ref} shows that for every $\varepsilon>0$ there is a single
$\delta>0$, independent of $x$ and $y$, such that
$$
\abs{x-y}<\delta
\quad\Longrightarrow\quad
\abs{f(x)-f(y)}<\varepsilon.
$$
This is the definition of uniform continuity.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} is the required conclusion.

:::

:::

:::
