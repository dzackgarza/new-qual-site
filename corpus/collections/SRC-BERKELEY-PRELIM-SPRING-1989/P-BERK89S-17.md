---
schema: qual/card@1
id: P-BERK89S-17
kind: problem
title: An element satisfying $a^3=a+1$ forbids ideals of index below five
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: The retained PDF page confirms that part 1 concludes I=R; the extraction garbled the ideal symbol.
- event: solution-written
  by: chatgpt
  date: 2026-09-22
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: >-
    Showed that any nonzero ring containing a root of $x^3=x+1$ has at least
    five distinct elements, then used $\FF_5$ with $a=2$ for sharpness.
---

::: {.problem}
1. Let $R$ be a commutative ring with identity containing an element $a$ such that
   \[
   a^3=a+1.
   \]
   Let $I$ be an ideal of $R$ of index less than $5$. Prove that
   \[
   I=R.
   \]
2. Show that there exists a commutative ring with identity containing an element $a$ satisfying $a^3=a+1$ and containing an ideal of index $5$.

Here the index of $I$ means the order of the additive quotient $R/I$.
:::

::: {.solution}
<1>1. Let $S$ be a nonzero ring with identity and let $x\in S$ satisfy
$$
x^3=x+1.
$$
Then $0,1,x,x^2,x+1$ are five distinct elements of $S$.

::: {.proof}
The relation can be rewritten as
$$
x(x^2-1)=1,
$$
so $x$ is a unit. In particular, $x\neq0$ and $x^2\neq0$.

One also has $x\neq1$, since $x=1$ would give $1=2$ and hence $1=0$.
Similarly, $x\neq-1$, since $x=-1$ would give $-1=0$ and hence $1=0$.
Thus the four elements $0,1,x,x+1$ are pairwise distinct.

It remains to distinguish $x^2$ from the other four. We already know
$x^2\neq0$. If $x^2=1$, then $x^3=x$, contradicting $x^3=x+1$. If
$x^2=x$, then $x^3=x^2=x$, giving the same contradiction. Finally, if
$x^2=x+1$, then
$$
x^3=x(x+1)=x^2+x=2x+1.
$$
Comparing this with $x^3=x+1$ gives $x=0$, again a contradiction. Hence all
five displayed elements are distinct.
:::

<1>2. If $I$ is an ideal of $R$ with index less than $5$, then $I=R$.

::: {.proof}
Suppose $I\neq R$. Then the quotient ring $S=R/I$ is nonzero and has
identity $1+I$. The element
$$
x=a+I
$$
satisfies
$$
x^3=x+1
$$
because $a^3=a+1$ in $R$. By step <1>1, the ring $S$ has at least five
elements. But
$$
\abs{S}=\abs{R/I}=[R:I]<5,
$$
a contradiction. Therefore $I=R$.
:::

<1>3. There is an example with an ideal of index exactly $5$:
$$
\boxed{R=\FF_5,\qquad a=2,\qquad I=(0).}
$$

::: {.proof}
In $\FF_5$,
$$
2^3=8=3=2+1,
$$
so $a=2$ satisfies the required relation. The zero ideal has additive index
$$
[\FF_5:(0)]=\abs{\FF_5}=5.
$$
Thus this ring and ideal satisfy part (2).
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>2 proves part (1), and step <1>3 proves part (2).
:::
:::
