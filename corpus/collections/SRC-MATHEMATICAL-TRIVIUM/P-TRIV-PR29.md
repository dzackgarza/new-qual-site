---
schema: qual/card@1
id: P-TRIV-PR29
kind: problem
title: Markov chain of a die rolled onto adjacent faces
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Probability, Problem 29, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md. Flash contains one or more nonprinting control bytes at this source position; they were removed from the authored card as nonsemantic extraction artifacts.
---

::: {.problem}
A dice is turned randomly from one face to one of four adjoined faces.
Suppose it fell 6 at $t = 0$ . Find the probability $P _ { n } , n \geqslant 1$ , that after n such turns it will show 6 again.
Find the limit $\operatorname* { l i m } _ { n \to \infty } P _ { n }$
:::

::: {.solution}
Track only whether the upper face is $6$, opposite to $6$, or one of the four side faces. Let the corresponding probabilities after $n$ turns be $a_n,b_n,c_n$, with
\[
(a_0,b_0,c_0)=(1,0,0).
\]
Then $P_n=a_n$.

<1>1. The transition recurrences are
\[
a_{n+1}=\frac14c_n,
\qquad
b_{n+1}=\frac14c_n,
\qquad
c_{n+1}=a_n+b_n+\frac12c_n.
\]

::: {.proof}
From top face $6$, every one of the four adjacent choices is a side face, so the next state is certainly $c$. The same holds from the face opposite $6$. From any side face, among its four adjacent faces one is $6$, one is opposite $6$, and two are side faces. This gives transition probabilities $1/4,1/4,1/2$ from state $c$.
:::

<1>2. For every $n\geq1$,
\[
a_n=b_n.
\]

::: {.proof}
Step <1>1 gives both $a_{n+1}$ and $b_{n+1}$ as $c_n/4$ for every $n\geq0$.
:::

<1>3. For $n\geq1$,
\[
c_n=1-2a_n
\]
and hence
\[
a_{n+1}=\frac14-\frac12a_n.
\]

::: {.proof}
The three states partition all possibilities, so $a_n+b_n+c_n=1$. Apply step <1>2 to obtain $c_n=1-2a_n$, then substitute into the first recurrence of step <1>1.
:::

<1>4. The fixed point of the recurrence in step <1>3 is
\[
a_*=\frac16.
\]

::: {.proof}
Solve
\[
a_*=\frac14-\frac12a_*.
\]
This gives $(3/2)a_*=1/4$, hence $a_*=1/6$.
:::

<1>5. Since $a_1=0$, the recurrence solves to
\[
\boxed{
P_n=a_n=\frac16\left(1-\left(-\frac12\right)^{n-1}\right),
\qquad n\geq1.}
\]

::: {.proof}
Subtract the fixed point from step <1>3:
\[
a_{n+1}-\frac16
=-\frac12\left(a_n-\frac16\right).
\]
Iterating from $a_1=0$ gives
\[
a_n-\frac16
=\left(-\frac12\right)^{n-1}\left(-\frac16\right),
\]
which is the displayed formula.
:::

<1>6. Therefore
\[
\boxed{\lim_{n\to\infty}P_n=\frac16}.
\]

::: {.proof}
In step <1>5, $(-1/2)^{n-1}\to0$.
:::

<1>7. Q.E.D.

::: {.proof}
Steps <1>5--<1>6 give the requested return probability and its limiting value.
:::
:::
