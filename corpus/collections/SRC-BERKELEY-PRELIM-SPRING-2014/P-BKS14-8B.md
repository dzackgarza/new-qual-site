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

::: pf

::: {.pf-step #s1}

If
$$
d=1,
$$
then $B$ already has integer entries.

::: pf-proof

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

:::

::: {.pf-step #s2}

Suppose
$$
d>1.
$$
Then the reduction of $A$ modulo $d$ lies in the finite group
$$
\operatorname{GL}_n(\ZZ/d\ZZ).
$$

::: pf-proof

The matrix $A$ has integer entries and
$$
\det A=1.
$$
Therefore its determinant is a unit modulo $d$, so its reduction is
invertible over $\ZZ/d\ZZ$. The ring $\ZZ/d\ZZ$ is finite, hence so is
the group of invertible $n\times n$ matrices over it.

:::

:::

::: {.pf-step #s3}

There exists a positive integer $m$ such that
$$
A^m\equiv I\pmod d.
$$

::: pf-proof

The element represented by $A$ in the finite group from step [](#s2){.pf-ref} has
finite order. Let $m$ be that order.

:::

:::

::: {.pf-step #s4}

For this $m$, there is an integer matrix $D$ such that
$$
A^m=I+dD.
$$

::: pf-proof

Step [](#s3){.pf-ref} says every entry of
$$
A^m-I
$$
is divisible by $d$. Divide those entries by $d$.

:::

:::

::: {.pf-step #s5}

The matrix
$$
dC^{-1}
$$
has integer entries.

::: pf-proof

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

:::

::: {.pf-step #s6}

The matrix $B^m$ has integer entries.

::: pf-proof

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
Using step [](#s4){.pf-ref},
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
[](#s4){.pf-ref} and [](#s5){.pf-ref}. Hence so does $B^m$.

:::

:::

::: {.pf-step #s7}

Therefore there exists a positive integer
$$
\boxed{m}
$$
such that every entry of $B^m$ is an integer.

::: pf-proof

Step [](#s1){.pf-ref} handles $d=1$. For $d>1$, choose the positive integer from step
[](#s3){.pf-ref} and apply step [](#s6){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s7){.pf-ref} is the required result.

:::

:::

:::
