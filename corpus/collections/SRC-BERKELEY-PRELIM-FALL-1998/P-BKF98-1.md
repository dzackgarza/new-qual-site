---
schema: qual/card@1
id: P-BKF98-1
kind: problem
title: Ambient Lebesgue number for an open cover of a compact subset
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-25
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-25
  note: >-
    Chose doubled local balls inside cover members, covered the compact set
    by the corresponding half-radius balls, and took the minimum of finitely
    many radii to control an entire ambient ball around every point of C.
---

::: {.problem}
Let $(M,d)$ be a metric space, let $C\subseteq M$ be compact, and let $(U_\alpha)_{\alpha\in I}$ be an open cover of $C$. Show that there exists $\varepsilon>0$ such that for every $p\in C$, the open ball
\[
B(p,\varepsilon)
\]
is contained in at least one $U_\alpha$.
:::

::: {.solution}
<1>1. For every $p\in C$, there are an index $\alpha(p)\in I$ and a number
$r_p>0$ such that
$$
B(p,2r_p)\subseteq U_{\alpha(p)}.
$$

::: {.proof}
Since the family $(U_\alpha)$ covers $C$, choose $\alpha(p)$ with
$$
p\in U_{\alpha(p)}.
$$
The set $U_{\alpha(p)}$ is open in the ambient metric space $M$, so there
is $\rho_p>0$ such that
$$
B(p,\rho_p)\subseteq U_{\alpha(p)}.
$$
Take
$$
r_p=\frac{\rho_p}{2}.
$$
:::

<1>2. There are points
$$
p_1,\ldots,p_m\in C
$$
such that
$$
C
\subseteq
\bigcup_{j=1}^m B(p_j,r_{p_j}).
$$

::: {.proof}
The balls
$$
B(p,r_p),
\qquad
p\in C,
$$
form an open cover of the compact set $C$. Compactness gives a finite
subcover.
:::

<1>3. Define
$$
\varepsilon
\coloneqq
\min_{1\leq j\leq m}r_{p_j}.
$$
Then
$$
\varepsilon>0.
$$

::: {.proof}
Every $r_{p_j}$ is positive, and the minimum is taken over finitely many
numbers.
:::

<1>4. For every $p\in C$, there is some $j$ such that
$$
B(p,\varepsilon)
\subseteq
B(p_j,2r_{p_j}).
$$

::: {.proof}
Fix $p\in C$. By step <1>2, choose $j$ such that
$$
d(p,p_j)<r_{p_j}.
$$
If
$$
q\in B(p,\varepsilon),
$$
then step <1>3 gives
$$
d(q,p)<\varepsilon\leq r_{p_j}.
$$
The triangle inequality therefore gives
$$
d(q,p_j)
\leq
d(q,p)+d(p,p_j)
<
r_{p_j}+r_{p_j}
=
2r_{p_j}.
$$
Thus $q\in B(p_j,2r_{p_j})$.
:::

<1>5. For every $p\in C$, the ambient ball
$$
B(p,\varepsilon)
$$
is contained in one member of the original cover.

::: {.proof}
Choose $j$ as in step <1>4. By step <1>1,
$$
B(p_j,2r_{p_j})
\subseteq
U_{\alpha(p_j)}.
$$
Hence
$$
B(p,\varepsilon)
\subseteq
U_{\alpha(p_j)}.
$$
:::

<1>6. Q.E.D.

::: {.proof}
The positive number $\varepsilon$ from step <1>3 has the required property
by step <1>5.
:::
:::
