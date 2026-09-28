---
schema: qual/card@1
id: P-BKS14-8B
kind: problem
title: Some power of $C^{-1}AC$ is integral when $A$ is an integer matrix with $\det A=1$
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
  note: Independently checked the unimodular case, finite-order reduction modulo |det C|, adjugate denominator clearing, and the conjugation identity for B^m.
---

::: {.problem}
Let $B=C^{-1}AC$, where $A$ and $C$ are $n\times n$ matrices with integer entries, $\det A=1$, and $\det C\ne0$. Prove that there exists a positive integer $m$ such that every entry of $B^m$ is an integer.
:::

::: {.solution}
Set
$$
d\coloneqq\abs{\det C}.
$$

<1>1. If
$$
d=1,
$$
then $B$ already has integer entries.

::: {.proof}
The adjugate formula gives
$$
C^{-1}
=
\frac{\operatorname{adj}(C)}{\det C}.
$$
If $\abs{\det C}=1$, then $C^{-1}$ has integer entries. Since $A$ and
$C$ also have integer entries,
$$
B=C^{-1}AC
$$
is an integer matrix. Thus one may take $m=1$.
:::

<1>2. Suppose
$$
d>1.
$$
Then the reduction of $A$ modulo $d$ lies in the finite group
$$
\operatorname{GL}_n(\ZZ/d\ZZ).
$$

::: {.proof}
The matrix $A$ has integer entries and
$$
\det A=1.
$$
Therefore its determinant is a unit modulo $d$, so its reduction is
invertible over $\ZZ/d\ZZ$. The ring $\ZZ/d\ZZ$ is finite, hence so is
the group of invertible $n\times n$ matrices over it.
:::

<1>3. There exists a positive integer $m$ such that
$$
A^m\equiv I\pmod d.
$$

::: {.proof}
The element represented by $A$ in the finite group from step <1>2 has
finite order. Let $m$ be that order.
:::

<1>4. For this $m$, there is an integer matrix $D$ such that
$$
A^m=I+dD.
$$

::: {.proof}
Step <1>3 says every entry of
$$
A^m-I
$$
is divisible by $d$. Divide those entries by $d$.
:::

<1>5. The matrix
$$
dC^{-1}
$$
has integer entries.

::: {.proof}
The adjugate formula gives
$$
C^{-1}
=
\frac{\operatorname{adj}(C)}{\det C}.
$$
Since
$$
d=\abs{\det C},
$$
one has
$$
dC^{-1}
=
\pm\operatorname{adj}(C),
$$
whose entries are integers because $C$ has integer entries.
:::

<1>6. The matrix $B^m$ has integer entries.

::: {.proof}
Because
$$
B=C^{-1}AC,
$$
the conjugation factors telescope:
$$
B^m
=
C^{-1}A^mC.
$$
Using step <1>4,
$$
\begin{aligned}
B^m
&=
C^{-1}(I+dD)C\\
&=
I+dC^{-1}DC\\
&=
I+(dC^{-1})DC.
\end{aligned}
$$
The matrices $dC^{-1}$, $D$, and $C$ all have integer entries by steps
<1>4 and <1>5. Hence so does $B^m$.
:::

<1>7. Therefore there exists a positive integer
$$
\boxed{m}
$$
such that every entry of $B^m$ is an integer.

::: {.proof}
Step <1>1 handles $d=1$. For $d>1$, choose the positive integer from step
<1>3 and apply step <1>6.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>7 is the required result.
:::
:::
