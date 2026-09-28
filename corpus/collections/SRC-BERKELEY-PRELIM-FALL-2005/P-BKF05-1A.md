---
schema: qual/card@1
id: P-BKF05-1A
kind: problem
title: Lebesgue number for an open cover of a compact metric space
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UC Berkeley Fall 2005 preliminary-exam solution packet, which reproduces the problem statement with its solution.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained compactness argument; the explicit
    subsequence indices and triangle inequality show that the paired
    y-subsequence converges to the same cover point.
---

::: {.problem}
Let \(M\) be a compact metric space and let \((U_i)_{i\in I}\) be an open cover of \(M\). Show that there exists \(\varepsilon>0\) such that whenever \(x,y\in M\) satisfy \(d(x,y)<\varepsilon\), there is some \(j\in I\) with \(x,y\in U_j\).
:::

::: {.solution}
<1>1. Suppose, for contradiction, that no such
$\varepsilon>0$ exists. Then for every positive integer $n$ there are
points $x_n,y_n\in M$ such that
$$
d(x_n,y_n)<\frac1n
$$
and no member of the cover contains both $x_n$ and $y_n$.

::: {.proof}
Negating the required statement says that for every
$\varepsilon>0$ there are $x,y\in M$ with
$d(x,y)<\varepsilon$ such that, for every $j\in I$, at least one of
$x,y$ does not belong to $U_j$. Apply this with
$\varepsilon=1/n$.
:::

<1>2. There are indices
$$
n_1<n_2<\cdots
$$
and a point $p\in M$ such that
$$
x_{n_k}\longrightarrow p
\qquad\text{and}\qquad
y_{n_k}\longrightarrow p.
$$

::: {.proof}
Compactness of the metric space $M$ implies sequential compactness, so
the sequence $(x_n)$ has a convergent subsequence
$x_{n_k}\to p$ for some $p\in M$. Since $n_k\to\infty$,
step <1>1 gives
$$
d(x_{n_k},y_{n_k})<\frac1{n_k}\longrightarrow0.
$$
The triangle inequality therefore gives
$$
d(y_{n_k},p)
\le
d(y_{n_k},x_{n_k})+d(x_{n_k},p)
\longrightarrow0.
$$
Hence $y_{n_k}\to p$ as well.
:::

<1>3. The sequences in step <1>2 contradict their defining property
from step <1>1.

::: {.proof}
Because $(U_i)_{i\in I}$ covers $M$, choose $j\in I$ with
$p\in U_j$. Since $U_j$ is open, there is $r>0$ such that
$$
B(p,r)\subseteq U_j.
$$
By step <1>2, for all sufficiently large $k$ both
$x_{n_k}$ and $y_{n_k}$ lie in $B(p,r)$, hence both lie in $U_j$.
This contradicts step <1>1, which says that no cover element contains
both members of any pair $(x_n,y_n)$.
:::

<1>4. There exists $\varepsilon>0$ such that
$$
d(x,y)<\varepsilon
\quad\Longrightarrow\quad
\text{some $U_j$ contains both $x$ and $y$}.
$$

::: {.proof}
Step <1>3 contradicts the negation assumed in step <1>1. Therefore the
required positive $\varepsilon$ exists.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is exactly the required conclusion.
:::
:::
