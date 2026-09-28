---
schema: qual/card@1
id: P-BERK77S-20
kind: problem
title: The solution space of the infinite linear system $x_n+x_{n+2}+x_{n+4}=0$
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
  note: The signs in the extracted first equation were garbled; the retained PDF page confirms that every displayed equation uses plus signs.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    The recurrence separates the odd and even subsequences. Each satisfies
    y_k+y_{k+1}+y_{k+2}=0, which implies period three. Choosing
    x_1,x_2,x_3,x_4 freely determines x_5=-x_1-x_3 and
    x_6=-x_2-x_4 and then the entire six-periodic solution, so exactly four
    free parameters are required.
---

::: {.problem}
Determine all solutions to the infinite system
\[
x_n+x_{n+2}+x_{n+4}=0,
\qquad n=1,2,3,\dots,
\]
in the infinitely many unknowns $x_1,x_2,\dots$.

How many free parameters are required?
:::

::: {.solution}
<1>1. The system is equivalent to the recurrence
$$
x_{n+4}=-x_n-x_{n+2},
\qquad
n\geq1.
$$

::: {.proof}
This is obtained by solving the equation
$$
x_n+x_{n+2}+x_{n+4}=0
$$
for its last term.
:::

<1>2. The odd-indexed subsequence satisfies
$$
x_{n+6}=x_n
$$
for every odd $n\geq1$.

::: {.proof}
For odd $n$, step <1>1 gives
$$
x_{n+4}=-x_n-x_{n+2}.
$$
Applying the same recurrence with $n$ replaced by $n+2$,
$$
\begin{aligned}
x_{n+6}
&=
-x_{n+2}-x_{n+4}\\
&=
-x_{n+2}-(-x_n-x_{n+2})\\
&=
x_n.
\end{aligned}
$$
:::

<1>3. The even-indexed subsequence also satisfies
$$
x_{n+6}=x_n
$$
for every even $n\geq2$.

::: {.proof}
The calculation in step <1>2 uses only the recurrence and therefore applies
unchanged to even $n$.
:::

<1>4. Choose arbitrary scalars
$$
a,b,c,d
$$
and set
$$
x_1=a,\qquad
x_2=b,\qquad
x_3=c,\qquad
x_4=d.
$$
Then the first two equations force
$$
x_5=-a-c,
\qquad
x_6=-b-d.
$$

::: {.proof}
For $n=1$,
$$
x_1+x_3+x_5=0,
$$
so
$$
x_5=-x_1-x_3=-a-c.
$$
For $n=2$,
$$
x_2+x_4+x_6=0,
$$
so
$$
x_6=-x_2-x_4=-b-d.
$$
:::

<1>5. The complete solution determined by $a,b,c,d$ is
$$
\boxed{
\begin{aligned}
x_{6m+1}&=a,\\
x_{6m+2}&=b,\\
x_{6m+3}&=c,\\
x_{6m+4}&=d,\\
x_{6m+5}&=-a-c,\\
x_{6m+6}&=-b-d,
\end{aligned}
\qquad
m=0,1,2,\ldots.
}
$$

::: {.proof}
Step <1>4 gives the first six terms. Steps <1>2--<1>3 give
$$
x_{n+6}=x_n
$$
for every $n\geq1$, so those six values repeat and yield the displayed
formula.
:::

<1>6. Every sequence in step <1>5 satisfies the infinite system.

::: {.proof}
It is enough to verify the recurrence over one period. The odd-indexed
triples are cyclic permutations of
$$
a,\ c,\ -a-c,
$$
whose sum is zero. The even-indexed triples are cyclic permutations of
$$
b,\ d,\ -b-d,
$$
whose sum is zero. Hence
$$
x_n+x_{n+2}+x_{n+4}=0
$$
for every $n\geq1$.
:::

<1>7. Every solution of the infinite system occurs uniquely in the form
given in step <1>5.

::: {.proof}
Given any solution, define
$$
a=x_1,\quad
b=x_2,\quad
c=x_3,\quad
d=x_4.
$$
Step <1>4 forces $x_5$ and $x_6$, and step <1>1 then recursively determines
every later term. Steps <1>2--<1>3 show that the recursively determined
sequence is exactly the one in step <1>5. Thus the representation is both
exhaustive and unique.
:::

<1>8. Exactly
$$
\boxed{4}
$$
free parameters are required.

::: {.proof}
The four values
$$
a,b,c,d
$$
in step <1>5 may be chosen independently, and step <1>7 shows that every
solution is uniquely determined by them. Hence the solution space has four
free parameters.
:::

<1>9. Q.E.D.

::: {.proof}
Steps <1>5--<1>8 give all solutions and the number of free parameters.
:::
:::
