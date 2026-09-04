---
schema: qual/card@1
id: P-XXLEK
kind: problem
title: Open sets in a second-countable regular space as countable unions of closed
  sets, with a continuous $f:X\to[0,1]$ positive on $U$
classification:
  areas:
  - topology
  topics:
  - Separation Axioms
  - Countability
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-04
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-04
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-04
  note: Checked the normality reduction, dyadic Urysohn construction, and uniformly convergent positive sum.
---

::: {.problem}
Recall that a topological space is **regular** if for every point $p \in X$ and for every closed subset $F \subset X$ not containing $p$, there exist disjoint open sets $U, V \subset X$ with $p \in U$ and $F \subset V$.

Let $X$ be a regular space that has a countable basis for its topology, and let $U$ be an open subset of $X$.

a. Show that $U$ is a countable union of closed subsets of $X$.

b. Show that there is a continuous function $f : X \to [0,1]$ such that $f (x) > 0$ for $x \in U$ and $f (x) = 0$ for $x \notin U$.
:::

::: {.solution}
<1>1. Fix a countable basis
\[
\mathcal B=\{B_1,B_2,\dots\}
\]
for $X$, and for each $n\ge1$ define
\[
F_n=
\begin{cases}
\overline{B_n},&\overline{B_n}\subseteq U,\\
\varnothing,&\text{otherwise}.
\end{cases}
\]
Then every $F_n$ is closed and
\[
U=\bigcup_{n=1}^{\infty}F_n.
\]
::: {.proof}
Each $F_n$ is closed by definition, and every nonempty $F_n$ is contained in $U$, so
\[
\bigcup_{n=1}^{\infty}F_n\subseteq U.
\]

Conversely, fix $x\in U$ and put
\[
C=X\setminus U.
\]
The set $C$ is closed and does not contain $x$.
By regularity there are disjoint open sets $V,W\subseteq X$ such that
\[
x\in V,
\qquad
C\subseteq W.
\]
Since $V\cap W=\varnothing$,
\[
\overline V\subseteq X\setminus W\subseteq U.
\]
Choose a basis element $B_n$ with
\[
x\in B_n\subseteq V.
\]
Then
\[
x\in\overline{B_n}
\subseteq
\overline V
\subseteq U,
\]
so $F_n=\overline{B_n}$ and $x\in F_n$.
Thus $U\subseteq\bigcup_nF_n$.
This proves part (a).
:::

<1>2. Every second-countable space is Lindelöf, and every subspace of a second-countable space is second-countable and hence Lindelöf.
::: {.proof}
Let $Y$ be second-countable with basis $\{C_1,C_2,\dots\}$, and let $\mathcal U$ be an open cover of $Y$.
For each basis element $C_n$ for which there exists $O\in\mathcal U$ satisfying
\[
C_n\subseteq O,
\]
choose one such $O_n$.
There are only countably many chosen sets.

If $y\in Y$, choose $O\in\mathcal U$ containing $y$.
The basis property gives some $C_n$ with
\[
y\in C_n\subseteq O,
\]
so $O_n$ was chosen and contains $y$.
Hence the chosen $O_n$ form a countable subcover.
Thus $Y$ is Lindelöf.

If $Z\subseteq Y$, then
\[
\{C_n\cap Z:n\ge1\}
\]
is a countable basis for the subspace topology on $Z$.
Therefore every subspace is also second-countable and hence Lindelöf.
:::

<1>3. The space $X$ is normal: any two disjoint closed sets in $X$ have disjoint open neighborhoods.
::: {.proof}
Let $A,B\subseteq X$ be disjoint closed sets.
If either set is empty, they are separated by the disjoint open sets $X$ and $\varnothing$.
Assume henceforth that both are nonempty.
For each $a\in A$, regularity gives an open set $P_a$ containing $a$ such that
\[
\overline{P_a}\cap B=\varnothing.
\]
Indeed, separate $a$ and the closed set $B$ by disjoint open sets $P_a,Q_a$ with $B\subseteq Q_a$; then
\[
\overline{P_a}\subseteq X\setminus Q_a.
\]
By <1>2, the subspace $A$ is Lindelöf, so choose a countable subcover
\[
A\subseteq\bigcup_{n\ge1}P_n
\]
with
\[
\overline{P_n}\cap B=\varnothing
\qquad(n\ge1).
\]

Similarly choose open sets $Q_n$ such that
\[
B\subseteq\bigcup_{n\ge1}Q_n,
\qquad
\overline{Q_n}\cap A=\varnothing
\qquad(n\ge1).
\]
Define
\[
P
=
\bigcup_{n\ge1}
\left(
P_n\setminus\bigcup_{j=1}^{n}\overline{Q_j}
\right)
\]
and
\[
Q
=
\bigcup_{n\ge1}
\left(
Q_n\setminus\bigcup_{j=1}^{n}\overline{P_j}
\right).
\]
Each set in these unions is open, because only finitely many closed sets are removed from an open set.
Thus $P$ and $Q$ are open.

Every point of $A$ lies in $P$: if $a\in P_n$, then $a$ lies in none of the sets $\overline{Q_j}$, since each $\overline{Q_j}$ is disjoint from $A$.
Similarly $B\subseteq Q$.

Finally $P\cap Q=\varnothing$.
If a point lay in the $n$th summand defining $P$ and the $m$th summand defining $Q$, then either $n\le m$ or $m\le n$.
If $n\le m$, the $m$th summand of $Q$ omits $\overline{P_n}$ and therefore omits $P_n$.
If $m\le n$, the $n$th summand of $P$ omits $\overline{Q_m}$ and therefore omits $Q_m$.
Both cases are impossible.
Hence $X$ is normal.
:::

<1>4. In a normal space, if $C$ is closed and $G$ is open with $C\subseteq G$, then there is an open set $V$ such that
\[
C\subseteq V\subseteq\overline V\subseteq G.
\]
::: {.proof}
The closed sets $C$ and $X\setminus G$ are disjoint.
By normality choose disjoint open sets $V,W$ with
\[
C\subseteq V,
\qquad
X\setminus G\subseteq W.
\]
Then
\[
\overline V\subseteq X\setminus W\subseteq G.
\]
:::

<1>5. Urysohn separation holds in $X$: if $A,B\subseteq X$ are disjoint closed sets, then there is a continuous map
\[
h:X\to[0,1]
\]
with
\[
h|_A=0,
\qquad
h|_B=1.
\]
::: {.proof}
By <1>3, $X$ is normal.
For $m\ge0$, let
\[
D_m=\left\{\frac{k}{2^m}:0\le k\le2^m\right\},
\qquad
D=\bigcup_{m\ge0}D_m.
\]
Thus $D_0\subseteq D_1\subseteq\cdots$ and $D$ is the set of dyadic rationals in $[0,1]$.
We construct open sets $V_r$ for $r\in D$ such that
\[
A\subseteq V_0,
\qquad
V_1=X\setminus B,
\qquad
\overline{V_r}\subseteq V_s
\quad\text{whenever }r<s.
\]

First apply <1>4 to
\[
A\subseteq X\setminus B
\]
to choose $V_0$ with
\[
A\subseteq V_0\subseteq\overline{V_0}\subseteq X\setminus B=V_1.
\]
Suppose the sets $V_r$ have been defined for every $r\in D_m$ and satisfy the required nesting there.
For each adjacent pair $r<s$ in $D_m$, apply <1>4 to the closed set $\overline{V_r}$ inside the open set $V_s$ to define the new midpoint set $V_{(r+s)/2}$, where $(r+s)/2\in D_{m+1}\setminus D_m$, so that
\[
\overline{V_r}
\subseteq
V_{(r+s)/2}
\subseteq
\overline{V_{(r+s)/2}}
\subseteq
V_s.
\]
Together with the previously defined sets, these midpoint inclusions imply
\[
\overline{V_q}\subseteq V_t
\qquad(q<t,\ q,t\in D_{m+1})
\]
by inserting the finitely many adjacent dyadics between $q$ and $t$.
Induction therefore constructs all the $V_r$ and gives the required nesting for every $r<s$ in $D$.

Define
\[
h(x)=
\inf\{r\in D:x\in V_r\},
\]
with the convention that the infimum of the empty set is $1$.
Since $A\subseteq V_0$, one has $h=0$ on $A$.
Since every $V_r$ is contained in $V_1=X\setminus B$, no point of $B$ lies in any $V_r$, so $h=1$ on $B$.

It remains to prove continuity.
For $0<\alpha\le1$,
\[
\{x:h(x)<\alpha\}
=
\bigcup_{\substack{r\in D\\r<\alpha}}V_r,
\]
which is open.
Indeed, membership in the right side implies $h(x)\le r<\alpha$.
Conversely, if $h(x)<\alpha$, choose dyadics
\[
h(x)<r<\alpha.
\]
By the definition of infimum there is $q<r$ with $x\in V_q$, and the nesting gives $x\in V_r$.

For $0\le\alpha<1$,
\[
\{x:h(x)>\alpha\}
=
\bigcup_{\substack{r\in D\\r>\alpha}}
\left(X\setminus\overline{V_r}\right),
\]
which is also open.
For the nontrivial direction, if $h(x)>\alpha$, choose dyadics
\[
\alpha<r<s<h(x).
\]
Then $x\notin V_s$, and
\[
\overline{V_r}\subseteq V_s,
\]
so $x\notin\overline{V_r}$.
Conversely, if $x\notin\overline{V_r}$ for some $r>\alpha$, then $x\notin V_q$ for every $q<r$, because $V_q\subseteq V_r\subseteq\overline{V_r}$.
Hence $h(x)\ge r>\alpha$.

Thus the inverse images of all open rays in $[0,1]$ are open, so $h$ is continuous.
This proves the stated separation result.
:::

<1>6. For every $n\ge1$, there is a continuous function
\[
g_n:X\to[0,1]
\]
such that
\[
g_n=1\text{ on }F_n,
\qquad
g_n=0\text{ on }X\setminus U.
\]
::: {.proof}
The sets $F_n$ and $X\setminus U$ are disjoint closed subsets of $X$, because <1>1 gives $F_n\subseteq U$.
Apply <1>5 with
\[
A=X\setminus U,
\qquad
B=F_n.
\]
The resulting function has the required values.
:::

<1>7. Define
\[
f(x)=\sum_{n=1}^{\infty}2^{-n}g_n(x).
\]
Then $f:X\to[0,1]$ is continuous.
::: {.proof}
Because $0\le g_n(x)\le1$,
\[
0\le f(x)\le\sum_{n=1}^{\infty}2^{-n}=1.
\]
Moreover the tail after the $N$th partial sum satisfies, uniformly in $x$,
\[
\left|
\sum_{n>N}2^{-n}g_n(x)
\right|
\le
\sum_{n>N}2^{-n}
=2^{-N}.
\]
Hence the partial sums converge uniformly to $f$.
Each partial sum is continuous.

For completeness, fix $x\in X$ and $\varepsilon>0$.
Choose $N$ with $2^{1-N}<\varepsilon/3$.
Continuity of the $N$th partial sum $s_N$ gives a neighborhood $O$ of $x$ on which
\[
|s_N(y)-s_N(x)|<\varepsilon/3.
\]
For $y\in O$,
\[
|f(y)-f(x)|
\le
|f(y)-s_N(y)|
+|s_N(y)-s_N(x)|
+|s_N(x)-f(x)|
<\varepsilon.
\]
Thus $f$ is continuous.
:::

<1>8. The function $f$ satisfies
\[
f(x)>0\quad(x\in U),
\qquad
f(x)=0\quad(x\notin U).
\]
::: {.proof}
If $x\notin U$, then <1>6 gives $g_n(x)=0$ for every $n$, so $f(x)=0$.

If $x\in U$, then <1>1 gives some $n$ with $x\in F_n$.
By <1>6,
\[
g_n(x)=1.
\]
All summands in <1>7 are nonnegative, so
\[
f(x)\ge2^{-n}>0.
\]
This proves part (b).
:::
:::
