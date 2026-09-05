---
schema: qual/card@1
id: P-X6IHG
kind: problem
title: The Lefschetz fixed-point theorem for degree-one maps $S^2\to S^2$, a fixed-point-free
  map $\RR^2\to\RR^2$, and a degree-one map with exactly one fixed point
classification:
  areas:
  - topology
  topics:
  - Fixed Points
  - Degree
  - Counterexamples
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked all three parts against problem 6 of the official UGA Spring 2019 topology exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-05
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Verified the Lefschetz-number calculation and the translation example, including continuity and degree of its one-point-compactification extension.
---

::: problem
(i) Use the Lefschetz fixed point theorem to show that any degree-one map
\[
f:S^2\longrightarrow S^2
\]
has at least one fixed point.

(ii) Give an example of a map
\[
f:\RR^2\longrightarrow\RR^2
\]
having no fixed points.

(iii) Give an example of a degree-one map
\[
f:S^2\longrightarrow S^2
\]
having exactly one fixed point.
:::

::: {.solution}
<1>1. Every degree-one map $f:S^2\to S^2$ has a fixed point.
::: {.proof}
With rational coefficients,
\[
H_i(S^2;\QQ)\cong
\begin{cases}
\QQ,&i=0,2,\\
0,&\text{otherwise}.
\end{cases}
\]
Because $S^2$ is connected, $f_*$ is the identity on $H_0$ and therefore has trace $1$ there.
On $H_2$, the induced map is multiplication by the degree of $f$, which is also $1$.
Hence the Lefschetz number is
\[
L(f)
=\sum_i(-1)^i\operatorname{tr}(f_*|H_i(S^2;\QQ))
=1+1
=2.
\]
Since $L(f)\neq0$, the Lefschetz fixed point theorem implies that $f$ has a fixed point.
:::

<1>2. A nonzero translation of $\RR^2$ has no fixed points.
::: {.proof}
For example, define
\[
T:\RR^2\longrightarrow\RR^2,
\qquad
T(x,y)=(x+1,y).
\]
If $T(x,y)=(x,y)$, then $x+1=x$, which is impossible.
Thus $T$ is fixed-point-free.
:::

<1>3. The translation $T$ extends to a homeomorphism
\[
\widehat T:S^2\longrightarrow S^2
\]
of the one-point compactification
\[
S^2\cong\RR^2\cup\{\infty\}
\]
by setting
\[
\widehat T(\infty)=\infty.
\]
::: {.proof}
The translation $T$ is a homeomorphism and is proper: if $K\subset\RR^2$ is compact, then
\[
T^{-1}(K)=K-(1,0)
\]
is compact.
For a neighborhood
\[
U=(\RR^2\setminus K)\cup\{\infty\}
\]
of $\infty$ in the one-point compactification,
\[
\widehat T^{-1}(U)
=
(\RR^2\setminus T^{-1}(K))\cup\{\infty\},
\]
which is again a neighborhood of $\infty$.
Thus the extension is continuous at $\infty$ as well as on $\RR^2$.
The same argument applies to $T^{-1}$, so $\widehat T$ is a homeomorphism.
:::

<1>4. The map $\widehat T$ has degree $1$.
::: {.proof}
For $s\in[0,1]$, let
\[
T_s(x,y)=(x+s,y).
\]
Each $T_s$ is a proper homeomorphism of $\RR^2$.
The extensions fixing $\infty$ vary continuously with $s$: if $K\subset\RR^2$ is compact, then
\[
C=\{u-se_1:u\in K,\ 0\le s\le1\}
\]
is compact, and $x\notin C$ implies
\[
x+se_1\notin K
\qquad
(0\le s\le1).
\]
Hence a neighborhood of $\infty$ complementary to $C$ is carried, for every $s$, into the neighborhood complementary to $K$.
Thus
\[
\widehat T_s:S^2\longrightarrow S^2
\]
is a homotopy from
\[
\widehat T_0=\operatorname{id}_{S^2}
\]
to
\[
\widehat T_1=\widehat T.
\]
Degree is invariant under homotopy, so
\[
\deg\widehat T
=
\deg\operatorname{id}_{S^2}
=1.
\]
:::

<1>5. The map $\widehat T$ has exactly one fixed point.
::: {.proof}
By <1>2, it has no fixed point in the open subset $\RR^2\subset S^2$.
By definition,
\[
\widehat T(\infty)=\infty.
\]
Hence its fixed-point set is exactly
\[
\{\infty\}.
\]
Together with <1>4, this gives the required degree-one example for part (iii).
:::
:::
