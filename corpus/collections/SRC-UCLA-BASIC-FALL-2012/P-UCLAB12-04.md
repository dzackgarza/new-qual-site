---
schema: qual/card@1
id: P-UCLAB12-04
kind: problem
title: Baire category theorem
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-28
  note: Corrected the source misprint d(y, x) to d(y, x_1) in the hint's definition of B(x_1, delta_1).
---

::: {.problem}
A subset $K$ of a metric space $(X, d)$ is called nowhere dense if $K$ has empty interior (i.e., if $U \subseteq K$, $U$ open in $X$ imply $U = \emptyset$). Prove the Baire theorem that if $(X, d)$ is a complete metric space, then $X$ is not a countable union of closed nowhere dense sets.
Hint: Assume $X = \bigcup_n K_n$ where each $K_n$ is closed and nowhere dense.
Show there is $x_1 \in X$ and $0 < \delta_1 < 1/2$ such that $B_1 = B(x_1, \delta_1) = \{y \in X : d(y, x_1) < \delta_1\}$ satisfies $B_1 \cap K_1 = \emptyset$, and there is $x_2 \in X$ and $0 < \delta_2 < \frac{\delta_1}{2}$ such that $B_2 = B(x_2, \delta_2)$ satisfies $B_2 \subset B_1$ and $B_2 \cap K_2 = \emptyset$. Then continue by induction to find a sequence $\{x_n\}$ in $X$ that converges to $x \in X \setminus \bigcup_{n=1}^\infty K_n$.
:::


::: {.solution}

Assume $X\ne\varnothing$, as is standard in the Baire category theorem.
Suppose for contradiction that
$$
X=\bigcup_{n=1}^{\infty}K_n,
$$
where every $K_n$ is closed and nowhere dense.

::: pf

::: {.pf-step #s1-1}

If $U\subseteq X$ is nonempty and open, and $K\subseteq X$ is closed and nowhere dense, then there is a closed ball
$$
\overline B(x,r)
$$
with $r>0$ such that
$$
\overline B(x,r)\subseteq U\setminus K.
$$


::: pf-proof

Because $K$ is nowhere dense, it has empty interior. Thus the nonempty open set $U$ cannot be contained in $K$, so choose
$$
x\in U\setminus K.
$$
The set
$$
U\setminus K
$$
is open because $K$ is closed. Hence there exists $\rho>0$ such that
$$
B(x,\rho)\subseteq U\setminus K.
$$
Choose
$$
0<r<\rho.
$$
Then
$$
\overline B(x,r)\subseteq B(x,\rho)\subseteq U\setminus K.
$$

:::

:::

::: {.pf-step #s1-2}

There are points $x_n\in X$ and radii $\delta_n>0$ such that for every $n\ge1$,
$$
\delta_n<2^{-n},
$$
$$
\overline B(x_{n+1},\delta_{n+1})
\subseteq
B(x_n,\delta_n),
$$
and
$$
\overline B(x_n,\delta_n)\cap K_n=\varnothing.
$$


::: pf-proof

Apply step [](#s1-1){.pf-ref} to
$$
U=X
$$
and $K_1$, choosing additionally
$$
\delta_1<\frac12.
$$
This gives the first ball.

Suppose $\overline B(x_n,\delta_n)$ has been chosen.
The open ball
$$
B(x_n,\delta_n)
$$
is nonempty. Apply step [](#s1-1){.pf-ref} to this open set and $K_{n+1}$.
Choose the resulting radius also small enough that
$$
\delta_{n+1}<\min\left\{2^{-(n+1)},\frac{\delta_n}{2}\right\}.
$$
Then
$$
\overline B(x_{n+1},\delta_{n+1})
\subseteq
B(x_n,\delta_n)\setminus K_{n+1}.
$$
This completes the induction.

:::

:::

::: {.pf-step #s1-3}

The sequence $(x_n)$ is Cauchy.


::: pf-proof

If $m>n$, repeated nesting from step [](#s1-2){.pf-ref} gives
$$
x_m\in B(x_n,\delta_n).
$$
Hence
$$
d(x_m,x_n)<\delta_n<2^{-n}.
$$
Given $\varepsilon>0$, choose $N$ such that
$$
2^{-N}<\varepsilon.
$$
Then for $m>n\ge N$,
$$
d(x_m,x_n)<2^{-n}\le2^{-N}<\varepsilon.
$$
Thus $(x_n)$ is Cauchy.

:::

:::

::: {.pf-step #s1-4}

There exists $x\in X$ such that
$$
x_n\to x.
$$


::: pf-proof

The space $X$ is complete and $(x_n)$ is Cauchy by step [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

For every $n$,
$$
x\in\overline B(x_n,\delta_n).
$$


::: pf-proof

Fix $n$. For every $m>n$,
$$
x_m\in B(x_n,\delta_n)
\subseteq
\overline B(x_n,\delta_n)
$$
by the nesting in step [](#s1-2){.pf-ref}.
The closed ball
$$
\overline B(x_n,\delta_n)
$$
is closed, and the tail $(x_m)_{m>n}$ converges to $x$. Therefore
$$
x\in\overline B(x_n,\delta_n).
$$

:::

:::

::: {.pf-step #s1-6}

For every $n$,
$$
x\notin K_n.
$$


::: pf-proof

By step [](#s1-5){.pf-ref},
$$
x\in\overline B(x_n,\delta_n),
$$
while step [](#s1-2){.pf-ref} gives
$$
\overline B(x_n,\delta_n)\cap K_n=\varnothing.
$$
Hence $x\notin K_n$.

:::

:::

::: {.pf-step #s1-7}

The assumed covering
$$
X=\bigcup_{n=1}^{\infty}K_n
$$
is impossible.


::: pf-proof

Step [](#s1-4){.pf-ref} gives $x\in X$, while step [](#s1-6){.pf-ref} gives
$$
x\notin\bigcup_{n=1}^{\infty}K_n.
$$
This contradicts the assumed equality.

:::

:::

::: {.pf-step #s1-8}

Therefore a nonempty complete metric space cannot be a countable union of closed nowhere dense sets.


::: pf-proof

This is exactly the contradiction established in step [](#s1-7){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-8){.pf-ref} is the Baire category theorem in the form requested.

:::

:::

:::
