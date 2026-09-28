---
schema: qual/card@1
id: P-AGH5410NUMINEQ
kind: problem
title: A numerical inequality underlying the ampleness criterion on the cubic surface
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cubic Surfaces
  - Intersection Theory
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-19
  note: >-
    Read Hartshorne V.4.10 and the retained Egbert note, which supplies no
    proof and points only to Nagata/case analysis. The direct proof below is
    elementary. First prove that positive x_i with x_i+x_j<A and total sum
    at most 2A satisfy sum x_i^2<A^2. If s=sum b_i is at most 2a, this
    applies immediately. If s>2a, put t=s-2a and c_i=b_i-t. The five-term
    inequalities give c_i>0; the pair inequalities give
    c_i+c_j<a-2t; and sum c_i<2(a-2t). Applying the lemma and expanding
    sum(c_i+t)^2 gives exactly a^2 as the comparison value.
- event: solution-written
  by: chatgpt
  date: 2026-09-19
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-19
  note: >-
    Re-read the complete elementary proof. Checked strictness in both cases
    of the auxiliary lemma, the positivity of A=a-2t after translation, the
    identity sum c_i=2a-5t, and the final expansion back to a^2. No geometric
    input or later-card result is used.
---

::: {.problem}
A curious consequence of the implication (iv) $\Rightarrow$ (iii) of (4.11) is the following numerical fact: Given integers $a, b_1, \ldots, b_6$ such that $b_i>0$ for each $i$, $a-b_i-b_j>0$ for each $i, j$ and $2 a-\sum_{i \neq j} b_i>0$ for each $j$, we must necessarily have $a^2-\sum b_i^2>0$.
Prove this directly (for $a, b_1, \ldots, b_6 \in \RR$) using methods of freshman calculus.
:::

::: {.solution}
We use only the inequalities in the statement.  The pairwise condition is
needed only for distinct indices; if the phrase ``for each $i,j$'' is read
as also including $i=j$, that is a stronger hypothesis.

<1>1. We first prove the following elementary lemma.  Let
$$
A>0,
$$
and let
$$
x_1,\ldots,x_6>0
$$
satisfy
$$
x_i+x_j<A
\qquad(i\ne j)
$$
and
$$
\sum_{i=1}^6x_i\le2A.
$$
Then
$$
\boxed{\sum_{i=1}^6x_i^2<A^2.}
$$

::: {.proof}
Reorder the variables so that
$$
x_1\ge x_2\ge\cdots\ge x_6>0,
$$
and put
$$
S=\sum_i x_i.
$$

First suppose
$$
x_1\le\frac A2.
$$
Then
$$
\sum_i x_i^2
\le
x_1\sum_i x_i
\le
\frac A2\,2A
=A^2.
$$
The inequality is strict: equality would require both $S=2A$ and
$x_i=x_1=A/2$ for every $i$ with $x_i>0$, which would contradict
$$
x_1+x_2<A.
$$

Now suppose
$$
x_1>\frac A2.
$$
Since $x_i\le x_2$ for $i\ge2$,
$$
\sum_i x_i^2
\le
x_1^2+x_2(S-x_1).
$$
The hypotheses give
$$
x_2<A-x_1
$$
and
$$
S-x_1\le2A-x_1.
$$
Hence
$$
\sum_i x_i^2
<
x_1^2+(A-x_1)(2A-x_1).
$$
But
$$
\begin{aligned}
&x_1^2+(A-x_1)(2A-x_1)-A^2\\
&\qquad=
(2x_1-A)(x_1-A).
\end{aligned}
$$
Here
$$
2x_1-A>0,
$$
while $x_1<A$ because $x_2>0$ and $x_1+x_2<A$. Thus
$$
(2x_1-A)(x_1-A)<0,
$$
and again
$$
\sum_i x_i^2<A^2.
$$
This proves the lemma.
:::

<1>2. Put
$$
s=\sum_{i=1}^6 b_i.
$$
The hypotheses imply
$$
\boxed{a>0.}
$$

::: {.proof}
Every $b_i$ is positive, and for two distinct indices $i,j$ one has
$$
a>b_i+b_j>0.
$$
:::

<1>3. If
$$
s\le2a,
$$
then
$$
\boxed{\sum_i b_i^2<a^2.}
$$

::: {.proof}
Apply the lemma of step <1>1 with
$$
A=a,
\qquad
x_i=b_i.
$$
The hypotheses
$$
b_i>0,
\qquad
b_i+b_j<a
$$
are exactly the positivity and pairwise hypotheses of the lemma, while the
present case assumption is
$$
\sum_i b_i=s\le2a.
$$
Therefore
$$
\sum_i b_i^2<a^2.
$$
:::

<1>4. It remains to treat the case
$$
s>2a.
$$
Set
$$
t=s-2a>0
$$
and
$$
c_i=b_i-t.
$$
Then
$$
\boxed{c_i>0\text{ for every }i.}
$$

::: {.proof}
For each $i$, the third family of hypotheses gives
$$
2a-\sum_{j\ne i}b_j>0.
$$
Since
$$
\sum_{j\ne i}b_j=s-b_i,
$$
this says
$$
b_i>s-2a=t.
$$
Hence
$$
c_i=b_i-t>0.
$$
:::

<1>5. Put
$$
A=a-2t.
$$
Then
$$
\boxed{A>0}
$$
and, for distinct $i,j$,
$$
\boxed{c_i+c_j<A.}
$$

::: {.proof}
Using the pairwise hypothesis,
$$
\begin{aligned}
c_i+c_j
&=b_i+b_j-2t\\
&<a-2t\\
&=A.
\end{aligned}
$$
The left side is positive by step <1>4, so necessarily $A>0$.
:::

<1>6. The translated variables also satisfy
$$
\boxed{\sum_i c_i<2A.}
$$

::: {.proof}
Since
$$
s=2a+t,
$$
one has
$$
\sum_i c_i
=
s-6t
=
2a-5t.
$$
On the other hand,
$$
2A=2a-4t.
$$
Because $t>0$,
$$
2a-5t<2a-4t=2A.
$$
:::

<1>7. Therefore
$$
\boxed{\sum_i c_i^2<A^2.}
$$

::: {.proof}
Steps <1>4--<1>6 verify all hypotheses of the lemma in step <1>1 for the
six numbers $c_i$ and the positive number $A=a-2t$. Hence
$$
\sum_i c_i^2<A^2.
$$
:::

<1>8. In the case $s>2a$ one still has
$$
\boxed{\sum_i b_i^2<a^2.}
$$

::: {.proof}
Because
$$
b_i=c_i+t,
$$
step <1>7 gives
$$
\begin{aligned}
\sum_i b_i^2
&=
\sum_i(c_i+t)^2\\
&=
\sum_i c_i^2
+2t\sum_i c_i
+6t^2\\
&<
A^2
+2t(2a-5t)
+6t^2.
\end{aligned}
$$
Now substitute
$$
A=a-2t.
$$
Then
$$
\begin{aligned}
A^2+2t(2a-5t)+6t^2
&=(a-2t)^2+4at-10t^2+6t^2\\
&=a^2.
\end{aligned}
$$
Thus
$$
\sum_i b_i^2<a^2.
$$
:::

<1>9. Consequently
$$
\boxed{a^2-\sum_{i=1}^6b_i^2>0.}
$$

::: {.proof}
If $s\le2a$, this is step <1>3. If $s>2a$, it is step <1>8. These two cases
exhaust all possibilities.
:::

<1>10. Q.E.D.

::: {.proof}
Step <1>1 proves the elementary auxiliary inequality, and steps <1>2--<1>9
apply it directly to the hypotheses of the problem.
:::
:::
