---
schema: qual/card@1
id: P-BKS14-6A
kind: problem
title: Minimal polynomials of multiplication maps in finite rings
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
  note: Checked against the vendored UC Berkeley Spring 2014 preliminary examination PDF.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked polynomial evaluation on multiplication operators and the dual-numbers counterexample.
---

::: {.problem}
Let $R$ be a finite ring with identity and characteristic $p$. For a subring $S\subseteq R$, not necessarily containing an identity, regard $S$ as an $\FF_p$-vector space.
For $a\in S$, let
$$
T_a^S:S\to S,\qquad T_a^S(x)=ax.
$$

(a) Show that if $1\in S$, then the minimal polynomial of $T_a^S$ equals the minimal polynomial of $T_a^R$.

(b) Give an example of $p,R,S,a$ for which the conclusion in (a) is false.
:::

::: {.solution}
<1>1. Let
$$
q(t)=\sum_{j=0}^d c_jt^j
\in
\FF_p[t].
$$
For every $x\in S$,
$$
q(T_a^S)(x)
=
q(a)x
$$
whenever $1\in S$.

::: {.proof}
For every $j\geq0$,
$$
(T_a^S)^j(x)=a^jx,
$$
where the $j=0$ term is $x=1x$. Therefore
$$
\begin{aligned}
q(T_a^S)(x)
&=
\sum_{j=0}^dc_j(T_a^S)^j(x)\\
&=
\sum_{j=0}^dc_ja^jx\\
&=
q(a)x.
\end{aligned}
$$
:::

<1>2. If $1\in S$, then
$$
q(T_a^S)=0
\quad\Longleftrightarrow\quad
q(a)=0.
$$

::: {.proof}
If $q(a)=0$, step <1>1 gives
$$
q(T_a^S)(x)=0
$$
for every $x\in S$.

Conversely, if $q(T_a^S)=0$, evaluate the zero operator at
$$
1\in S.
$$
Step <1>1 gives
$$
0=q(T_a^S)(1)=q(a).
$$
:::

<1>3. For the multiplication operator on $R$,
$$
q(T_a^R)=0
\quad\Longleftrightarrow\quad
q(a)=0.
$$

::: {.proof}
The same computation as in steps <1>1--<1>2 applies to $R$, which
contains its identity $1$.
:::

<1>4. If $1\in S$, the minimal polynomials of $T_a^S$ and $T_a^R$ are
equal.

::: {.proof}
Steps <1>2 and <1>3 show that exactly the same polynomials in
$\FF_p[t]$ annihilate the two operators. Their unique monic annihilating
polynomials of least positive degree are therefore equal. This proves
part (a).
:::

<1>5. For part (b), take
$$
p=2,
\qquad
R=\FF_2[t]/(t^2),
$$
write
$$
a=\overline t,
$$
and let
$$
S=\{0,a\}\subseteq R.
$$
Then $S$ is a subring of $R$ that does not contain $1$.

::: {.proof}
The set $S$ is closed under addition because
$$
a+a=0
$$
in characteristic $2$, and it is closed under multiplication because
$$
a^2=0.
$$
Its two elements are $0$ and $a$, whereas the identity of $R$ is
$1\notin S$.
:::

<1>6. On $S$, the operator $T_a^S$ is zero, so its minimal polynomial is
$$
t.
$$

::: {.proof}
One has
$$
T_a^S(0)=0
$$
and
$$
T_a^S(a)=a^2=0.
$$
Thus $T_a^S=0$. The minimal polynomial of the zero operator on the
nonzero vector space $S$ is $t$.
:::

<1>7. On $R$, the operator $T_a^R$ is nonzero but satisfies
$$
(T_a^R)^2=0.
$$
Hence its minimal polynomial is
$$
t^2.
$$

::: {.proof}
The square vanishes because
$$
(T_a^R)^2=T_{a^2}^R=0.
$$
But the operator itself is nonzero since
$$
T_a^R(1)=a\neq0.
$$
Thus its minimal polynomial divides $t^2$ but not $t$, so it is $t^2$.
:::

<1>8. The conclusion of part (a) fails in this example.

::: {.proof}
By steps <1>6 and <1>7, the two minimal polynomials are respectively
$$
t
\qquad\text{and}\qquad
t^2,
$$
which are different.
:::

<1>9. Q.E.D.

::: {.proof}
Step <1>4 proves part (a), and step <1>8 supplies the requested example
for part (b).
:::
:::
