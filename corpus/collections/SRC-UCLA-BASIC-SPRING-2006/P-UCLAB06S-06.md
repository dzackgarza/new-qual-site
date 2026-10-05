---
schema: qual/card@1
id: P-UCLAB06S-06
kind: problem
title: Compactness of a set of Lipschitz functions with unit $L^2$ norm in $C[0,1]$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 6 of the retained UCLA Basic Examination Spring 2006 PDF.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked Problem 6 on page 2 of basic-06S.pdf, cleaned the LaTeX, and added an erratum remark that the strict Lipschitz inequality makes W non-closed so (B) fails as stated.
---

::: {.problem}
Let $W$ be the subset of the space $C[0,1]$ of real-valued, continuous functions on $[0,1]$ satisfying the conditions:
\[
|f(x) - f(y)| < |x - y| \qquad \int_0^1 f(x)^2\,dx = 1
\]

(A) Prove that $W$ is uniformly bounded, i.e., there exists $M > 0$ such that $|f(x)| \leq M$ for all $x \in [0,1]$. Hint: Show first that $|f(0)| \leq 2$ for all $f \in W$.

(B) Prove that $W$ is a compact subset of $C[0,1]$ under the sup norm $\|f\|_\infty = \sup_{x \in [0,1]} |f(x)|$.
:::

::: {.remark}
Erratum: with the strict inequality of the source, read for $x \neq y$ (for $x = y$ it would make $W$ empty), part (B) is false because $W$ is not closed. Let $c = \frac{-1 + \sqrt{11/3}}{2}$, so that $g(x) = x + c$ satisfies $\int_0^1 g^2 = \frac13 + c + c^2 = 1$. For $n \ge 2$ choose $c_n$ with $\int_0^1 \bigl((1 - \frac1n)x + c_n\bigr)^2\,dx = 1$ and $c_n \to c$, and put $f_n(x) = (1 - \frac1n)x + c_n$. Then $|f_n(x) - f_n(y)| = (1 - \frac1n)|x - y| < |x - y|$ for $x \neq y$, so $f_n \in W$, and $f_n \to g$ uniformly, but $|g(1) - g(0)| = 1 = |1 - 0|$, so $g \notin W$. Part (B) holds when the condition is $|f(x) - f(y)| \le |x - y|$ for all $x, y \in [0,1]$: that set is closed, and it is uniformly bounded by (A) and equicontinuous, hence compact by the Arzelà–Ascoli theorem.
:::

::: {.solution}
Interpret the source's strict inequality as applying to
\[
x\ne y.
\]
Part (A) is true, while part (B) is false as printed.

<1>1. For every $f\in W$ and every $x\in[0,1]$,
\[
|f(x)-f(0)|<x
\]
when $x>0$, and hence
\[
|f(x)|
\le
|f(0)|+1.
\]

::: {.proof}
The defining inequality gives
\[
|f(x)-f(0)|
<
|x-0|
=x
\]
for $x>0$.
Since
\[
x\le1,
\]
the triangle inequality gives
\[
|f(x)|
\le
|f(0)|+|f(x)-f(0)|
<
|f(0)|+1.
\]
:::

<1>2. For every $f\in W$,
\[
\boxed{|f(0)|\le2}.
\]

::: {.proof}
Suppose instead that
\[
|f(0)|>2.
\]
Then for every
\[
x\in[0,1],
\]
step <1>1 gives
\[
|f(x)|
\ge
|f(0)|-|f(x)-f(0)|
>
|f(0)|-1
>
1.
\]
Therefore
\[
f(x)^2>1
\]
for every $x\in[0,1]$.
Integrating gives
\[
\int_0^1f(x)^2\,dx>1,
\]
contradicting the defining condition
\[
\int_0^1f(x)^2\,dx=1.
\]
Hence
\[
|f(0)|\le2.
\]
:::

<1>3. The family $W$ is uniformly bounded; for example,
\[
\boxed{|f(x)|\le3}
\]
for every $f\in W$ and every $x\in[0,1]$.

::: {.proof}
By steps <1>1--<1>2,
\[
|f(x)|
\le
|f(0)|+1
\le
3.
\]
Thus the single constant
\[
M=3
\]
works for all $f\in W$ and all $x\in[0,1]$.
This proves part (A).
:::

<1>4. Let
\[
c=\frac{-1+\sqrt{11/3}}2
\]
and define
\[
g(x)=x+c.
\]
Then
\[
\int_0^1g(x)^2\,dx=1.
\]

::: {.proof}
One computes
\[
\int_0^1(x+c)^2\,dx
=
\frac13+c+c^2.
\]
The chosen value of $c$ satisfies
\[
c^2+c-\frac23=0,
\]
so
\[
\frac13+c+c^2
=
\frac13+\frac23
=1.
\]
:::

<1>5. For $n\ge2$, set
\[
a_n=1-\frac1n.
\]
There exists a real number $c_n$ such that
\[
\int_0^1(a_nx+c_n)^2\,dx=1
\]
and
\[
c_n\to c.
\]

::: {.proof}
The condition is
\[
\frac{a_n^2}{3}+a_nc_n+c_n^2=1.
\]
Solving this quadratic for $c_n$ gives
\[
c_n
=
\frac{-a_n+\sqrt{4-\frac13a_n^2}}2,
\]
choosing the branch that is continuous at $a_n=1$ and yields
\[
c
=
\frac{-1+\sqrt{11/3}}2.
\]
Since
\[
a_n\to1,
\]
continuity of this expression gives
\[
c_n\to c.
\]
:::

<1>6. Define
\[
f_n(x)=a_nx+c_n.
\]
Then
\[
f_n\in W
\]
for every $n\ge2$.

::: {.proof}
By step <1>5,
\[
\int_0^1f_n(x)^2\,dx=1.
\]
Also for
\[
x\ne y,
\]
\[
|f_n(x)-f_n(y)|
=
a_n|x-y|.
\]
Since
\[
0<a_n<1,
\]
one has
\[
|f_n(x)-f_n(y)|
<
|x-y|.
\]
Thus $f_n$ satisfies both defining conditions of $W$.
:::

<1>7. One has
\[
f_n\to g
\]
uniformly on $[0,1]$.

::: {.proof}
For $x\in[0,1]$,
\[
\begin{aligned}
|f_n(x)-g(x)|
&=
|(a_n-1)x+(c_n-c)|\\
&\le
|a_n-1|+|c_n-c|.
\end{aligned}
\]
The right side tends to $0$ because
\[
a_n\to1
\]
and
\[
c_n\to c.
\]
Hence the convergence is uniform.
:::

<1>8. The limit $g$ does not belong to $W$.

::: {.proof}
Although step <1>4 gives
\[
\int_0^1g^2=1,
\]
one has
\[
|g(1)-g(0)|
=
|1+c-c|
=1
=
|1-0|.
\]
Thus the strict Lipschitz inequality fails for the pair $(0,1)$.
Hence
\[
g\notin W.
\]
:::

<1>9. Therefore $W$ is not closed in $C[0,1]$ with the supremum norm.

::: {.proof}
By step <1>6,
\[
f_n\in W
\]
for all $n$.
By step <1>7,
\[
f_n\to g
\]
in the supremum norm.
By step <1>8,
\[
g\notin W.
\]
Thus $W$ is not closed.
:::

<1>10. Consequently part (B) is false as printed.

::: {.proof}
The normed space
\[
C[0,1]
\]
is Hausdorff, and every compact subset of a Hausdorff space is closed.
Step <1>9 shows that $W$ is not closed.
Therefore
\[
\boxed{W\text{ is not compact}.}
\]
:::

<1>11. If the source's strict inequality is replaced by
\[
|f(x)-f(y)|
\le
|x-y|,
\]
then the corrected family is compact.

::: {.proof}
The proof of part (A) above still gives uniform boundedness.
The common Lipschitz constant $1$ gives equicontinuity.
The corrected family is closed under uniform limits: the non-strict Lipschitz inequality passes to the limit, and so does the condition
\[
\int_0^1f^2=1
\]
because uniform convergence implies uniform convergence of squares on a uniformly bounded family.
Therefore Arzelà--Ascoli gives compactness.
:::

<1>12. Q.E.D.

::: {.proof}
Step <1>3 proves part (A).
Steps <1>4--<1>10 prove that part (B) is false for the literal strict inequality.
Step <1>11 records the corrected non-strict version for which the intended compactness conclusion holds.
:::
:::
