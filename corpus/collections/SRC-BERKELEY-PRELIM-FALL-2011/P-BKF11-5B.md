---
schema: qual/card@1
id: P-BKF11-5B
kind: problem
title: Continuous images of compact metric spaces are closed
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 5B of the retained Berkeley Fall 2011 preliminary-exam solution packet f11solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked compactness of the continuous image and the metric-space argument
    that every compact subset has open complement.
---

::: {.problem}
Prove that a continuous map from a compact metric space to a metric space has closed image.
:::

::: {.solution}
Let $X$ be a compact metric space, let $Y$ be a metric space with
metric $d$, and let $f\colon X\to Y$ be continuous. Put
$$
K\coloneqq f(X).
$$

::: pf

::: {.pf-step #s1}

The subset $K\subseteq Y$ is compact.

::: pf-proof

Let $\{U_\alpha\}_{\alpha\in A}$ be an open cover of $K$. Then
$$
\{f^{-1}(U_\alpha)\}_{\alpha\in A}
$$
is an open cover of $X$ because $f$ is continuous. Compactness of
$X$ gives indices $\alpha_1,\ldots,\alpha_m$ such that
$$
X=\bigcup_{j=1}^m f^{-1}(U_{\alpha_j}).
$$
Applying $f$ shows
$$
K\subseteq\bigcup_{j=1}^m U_{\alpha_j}.
$$
Thus every open cover of $K$ has a finite subcover.

:::

:::

::: {.pf-step #s2}

Every point $y\in Y\setminus K$ has an open neighborhood
disjoint from $K$.

::: pf-proof

Fix $y\notin K$. The function
$$
g\colon K\to\RR,
\qquad
g(z)=d(y,z)
$$
is continuous. By step [](#s1){.pf-ref}, $K$ is compact, so $g$ attains its
minimum at some $z_0\in K$.

Since $y\notin K$, one has $d(y,z)>0$ for every $z\in K$. Hence
$$
\delta\coloneqq d(y,z_0)>0.
$$
If $w\in B(y,\delta/2)$ and $z\in K$, then
$$
d(w,z)
\ge d(y,z)-d(y,w)
\ge\delta-\frac\delta2
>0.
$$
Thus $w\ne z$, so
$$
B(y,\delta/2)\cap K=\varnothing.
$$

:::

:::

::: {.pf-step #s3}

The image $f(X)$ is closed in $Y$.

::: pf-proof

Step [](#s2){.pf-ref} shows that every point of $Y\setminus K$ has an open
neighborhood contained in $Y\setminus K$. Therefore $Y\setminus K$
is open, so
$$
\boxed{f(X)=K\text{ is closed in }Y}.
$$

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} is the required conclusion.

:::

:::

:::
