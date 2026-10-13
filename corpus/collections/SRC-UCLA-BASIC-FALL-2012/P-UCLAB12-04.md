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
---

::: {.problem}
A subset K of a metric space $( X , d )$ is called nowhere dense if K has empty interior, (i. e., if $U \subseteq K$ , U open in X imply $U = \emptyset .$ Prove the Baire theorem that if $( X , d )$ is a complete metric space, then X is not a countable union of closed nowhere dense sets.
Hint: Assume $X = \textstyle \bigcup _ { n } K _ { n }$ where each $K _ { n }$ is closed and nowhere dense.
Show there is $x _ { 1 } \in X$ and $0 < \delta _ { 1 } < 1 / 2$ such that $B _ { 1 } = B ( x _ { 1 } , \delta _ { 1 } ) = \{ y \in X : d ( y , x ) < \delta _ { 1 } \}$ satisfies $B _ { 1 } \cap K _ { 1 } = \emptyset$ and there is $x _ { 2 } \in X$ and $\begin{array} { r } { 0 < \delta _ { 2 } < \frac { \delta _ { 1 } } { 2 } } \end{array}$ such that $B _ { 2 } = B ( x _ { 2 } , \delta _ { 2 } )$ satisfies $B _ { 2 } \subset B _ { 1 }$ and $B _ { 2 } \cap K _ { 2 } = \emptyset$ . Then continue by induction to find a sequence $\{ x _ { n } \}$ in X that converges to $x \in X \backslash \bigcup _ { n = 1 } ^ { \infty } K _ { n }$
:::

::: {.solution}
Assume $X\ne\varnothing$, as is standard in the Baire category theorem.
Suppose for contradiction that
\[
X=\bigcup_{n=1}^{\infty}K_n,
\]
where every $K_n$ is closed and nowhere dense.

<1>1. If $U\subseteq X$ is nonempty and open, and $K\subseteq X$ is closed and nowhere dense, then there is a closed ball
\[
\overline B(x,r)
\]
with $r>0$ such that
\[
\overline B(x,r)\subseteq U\setminus K.
\]

::: {.proof}
Because $K$ is nowhere dense, it has empty interior. Thus the nonempty open set $U$ cannot be contained in $K$, so choose
\[
x\in U\setminus K.
\]
The set
\[
U\setminus K
\]
is open because $K$ is closed. Hence there exists $\rho>0$ such that
\[
B(x,\rho)\subseteq U\setminus K.
\]
Choose
\[
0<r<\rho.
\]
Then
\[
\overline B(x,r)\subseteq B(x,\rho)\subseteq U\setminus K.
\]
:::

<1>2. There are points $x_n\in X$ and radii $\delta_n>0$ such that for every $n\ge1$,
\[
\delta_n<2^{-n},
\]
\[
\overline B(x_{n+1},\delta_{n+1})
\subseteq
B(x_n,\delta_n),
\]
and
\[
\overline B(x_n,\delta_n)\cap K_n=\varnothing.
\]

::: {.proof}
Apply step <1>1 to
\[
U=X
\]
and $K_1$, choosing additionally
\[
\delta_1<\frac12.
\]
This gives the first ball.

Suppose $\overline B(x_n,\delta_n)$ has been chosen.
The open ball
\[
B(x_n,\delta_n)
\]
is nonempty. Apply step <1>1 to this open set and $K_{n+1}$.
Choose the resulting radius also small enough that
\[
\delta_{n+1}<\min\left\{2^{-(n+1)},\frac{\delta_n}{2}\right\}.
\]
Then
\[
\overline B(x_{n+1},\delta_{n+1})
\subseteq
B(x_n,\delta_n)\setminus K_{n+1}.
\]
This completes the induction.
:::

<1>3. The sequence $(x_n)$ is Cauchy.

::: {.proof}
If $m>n$, repeated nesting from step <1>2 gives
\[
x_m\in B(x_n,\delta_n).
\]
Hence
\[
d(x_m,x_n)<\delta_n<2^{-n}.
\]
Given $\varepsilon>0$, choose $N$ such that
\[
2^{-N}<\varepsilon.
\]
Then for $m>n\ge N$,
\[
d(x_m,x_n)<2^{-n}\le2^{-N}<\varepsilon.
\]
Thus $(x_n)$ is Cauchy.
:::

<1>4. There exists $x\in X$ such that
\[
x_n\to x.
\]

::: {.proof}
The space $X$ is complete and $(x_n)$ is Cauchy by step <1>3.
:::

<1>5. For every $n$,
\[
x\in\overline B(x_n,\delta_n).
\]

::: {.proof}
Fix $n$. For every $m>n$,
\[
x_m\in B(x_n,\delta_n)
\subseteq
\overline B(x_n,\delta_n)
\]
by the nesting in step <1>2.
The closed ball
\[
\overline B(x_n,\delta_n)
\]
is closed, and the tail $(x_m)_{m>n}$ converges to $x$. Therefore
\[
x\in\overline B(x_n,\delta_n).
\]
:::

<1>6. For every $n$,
\[
x\notin K_n.
\]

::: {.proof}
By step <1>5,
\[
x\in\overline B(x_n,\delta_n),
\]
while step <1>2 gives
\[
\overline B(x_n,\delta_n)\cap K_n=\varnothing.
\]
Hence $x\notin K_n$.
:::

<1>7. The assumed covering
\[
X=\bigcup_{n=1}^{\infty}K_n
\]
is impossible.

::: {.proof}
Step <1>4 gives $x\in X$, while step <1>6 gives
\[
x\notin\bigcup_{n=1}^{\infty}K_n.
\]
This contradicts the assumed equality.
:::

<1>8. Therefore a nonempty complete metric space cannot be a countable union of closed nowhere dense sets.

::: {.proof}
This is exactly the contradiction established in step <1>7.
:::

<1>9. Q.E.D.

::: {.proof}
Step <1>8 is the Baire category theorem in the form requested.
:::
:::
