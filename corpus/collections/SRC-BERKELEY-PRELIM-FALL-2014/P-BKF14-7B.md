---
schema: qual/card@1
id: P-BKF14-7B
kind: problem
title: Congruence classes of real symmetric $n\times n$ matrices
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Removed the stray accent on C in CAC^T = B against Fall_2014_Exam.pdf page 18 problem 7B.
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained Fall 2014 solution packet: Sylvester's
    law of inertia classifies the congruence classes by three nonnegative
    integers summing to n.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked compatibility of the convention CAC^T with ordinary congruence
    and the stars-and-bars count of inertia triples.
---

::: {.problem}
Let $n$ be a fixed positive integer, and define two $n$ by $n$ real symmetric matrices $A$ and $B$ to be equivalent if there is a non-singular real matrix $C$ with $CAC^T = B$ (where $C^T$ is the transpose of $C$). How many equivalence classes are there?
:::

::: {.solution}
<1>1. Every real symmetric $n\times n$ matrix is equivalent to a
matrix of the form
$$
\operatorname{diag}
\bigl(
I_p,-I_q,0_r
\bigr),
\qquad
p+q+r=n,
$$
for some nonnegative integers $p,q,r$.

::: {.proof}
By Sylvester's law of inertia, for every real symmetric matrix $A$
there is an invertible real matrix $P$ such that
$$
P^TAP
=
\operatorname{diag}(I_p,-I_q,0_r)
$$
for some $p,q,r\ge0$ with $p+q+r=n$. Taking $C=P^T$ gives
$$
CAC^T=P^TAP,
$$
so this is exactly the equivalence relation in the problem.
:::

<1>2. Two matrices
$$
\operatorname{diag}(I_p,-I_q,0_r)
\quad\text{and}\quad
\operatorname{diag}(I_{p'},-I_{q'},0_{r'})
$$
are equivalent if and only if
$$
(p,q,r)=(p',q',r').
$$

::: {.proof}
Sylvester's law of inertia also states that the numbers of positive,
negative, and zero squares are invariant under real congruence. Hence
equivalent matrices have the same triple. Conversely, equal triples
give identical displayed normal forms.
:::

<1>3. The equivalence classes are therefore in bijection with the
nonnegative integer solutions of
$$
p+q+r=n.
$$

::: {.proof}
Existence follows from step <1>1 and uniqueness from step <1>2.
:::

<1>4. The number of such triples is
$$
\binom{n+2}{2}
=
\frac{(n+1)(n+2)}2.
$$

::: {.proof}
By the stars-and-bars count, the number of nonnegative solutions of
$p+q+r=n$ is
$$
\binom{n+3-1}{3-1}
=
\binom{n+2}{2}.
$$
:::

<1>5. Hence the number of equivalence classes is
$$
\boxed{\frac{(n+1)(n+2)}2}.
$$

::: {.proof}
Combine steps <1>3 and <1>4.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required count.
:::
:::
