---
schema: qual/card@1
id: P-BKF05-7A
kind: problem
title: Count zeros of a quintic in a closed annulus
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
  note: Checked against the vendored UC Berkeley Fall 2005 preliminary-exam solution packet, which reproduces the problem statement with its solution.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked both Rouché estimates. The strict inequalities also
    exclude zeros on |z|=1 and |z|=2, so subtracting the two interior counts
    correctly answers the closed-annulus question.
---

::: {.problem}
Let
\[
f(z)=z^5+5z^3+z^2+z+1.
\]
How many zeros, counted with multiplicity, does \(f\) have in the annulus
\[
1\le |z|\le2?
\]
:::

::: {.solution}
Set
$$
g(z)=5z^3.
$$

<1>1. On the circle $\abs{z}=2$,
$$
\abs{f(z)-g(z)}<\abs{g(z)}.
$$

::: {.proof}
If $\abs{z}=2$, then
$$
\begin{aligned}
\abs{f(z)-g(z)}
&=
\abs{z^5+z^2+z+1}
\\
&\le
\abs z^5+\abs z^2+\abs z+1
\\
&=
32+4+2+1
\\
&=
39,
\end{aligned}
$$
whereas
$$
\abs{g(z)}=5\abs z^3=40.
$$
Thus the inequality is strict.
:::

<1>2. The polynomial $f$ has exactly three zeros, counted with
multiplicity, in $\abs{z}<2$.

::: {.proof}
By step <1>1 and Rouché's theorem, $f$ and $g$ have the same number of
zeros in $\abs z<2$, counted with multiplicity. The polynomial
$g(z)=5z^3$ has exactly three such zeros, all at $0$. Hence so does
$f$.
:::

<1>3. On the circle $\abs{z}=1$,
$$
\abs{f(z)-g(z)}<\abs{g(z)}.
$$

::: {.proof}
If $\abs z=1$, then
$$
\abs{f(z)-g(z)}
\le
\abs z^5+\abs z^2+\abs z+1
=
4,
$$
while
$$
\abs{g(z)}=5.
$$
Thus the inequality is again strict.
:::

<1>4. The polynomial $f$ has exactly three zeros, counted with
multiplicity, in $\abs z<1$.

::: {.proof}
Apply Rouché's theorem using step <1>3. Again $f$ and $g$ have the same
number of zeros in the disk, and $g(z)=5z^3$ has exactly three.
:::

<1>5. The polynomial $f$ has no zeros on either boundary circle
$\abs z=1$ or $\abs z=2$.

::: {.proof}
On either circle, steps <1>1 and <1>3 give
$$
\abs{f-g}<\abs g.
$$
If $f(z)=0$ at a point of one of those circles, then
$$
\abs{f(z)-g(z)}=\abs{g(z)},
$$
contradicting the strict inequality. Thus neither circle contains a
zero of $f$.
:::

<1>6. The number of zeros of $f$ in
$$
1\le\abs z\le2
$$
is
$$
\boxed{0}.
$$

::: {.proof}
Steps <1>2 and <1>4 show that the number of zeros in
$1\le\abs z<2$ is $3-3=0$, except that the inner boundary must be
checked separately. Step <1>5 shows that neither boundary circle
contains a zero. Hence the closed annulus contains no zeros.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 is the required count.
:::
:::
