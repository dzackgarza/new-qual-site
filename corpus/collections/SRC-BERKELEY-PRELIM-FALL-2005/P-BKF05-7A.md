---
schema: qual/card@1
id: P-BKF05-7A
kind: problem
title: Zeros of a quintic in a closed annulus
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

::: pf

::: {.pf-step #rouche-bound-at-2}
On the circle $\abs{z}=2$,
$$
\abs{f(z)-g(z)}<\abs{g(z)}.
$$

::: pf-proof
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

:::

::: {.pf-step #three-zeros-in-disk-2}
The polynomial $f$ has exactly three zeros, counted with
multiplicity, in $\abs{z}<2$.

::: pf-proof
By step [](#rouche-bound-at-2){.pf-ref} and Rouché's theorem, $f$ and $g$ have the same number of
zeros in $\abs z<2$, counted with multiplicity. The polynomial
$g(z)=5z^3$ has exactly three such zeros, all at $0$. Hence so does
$f$.
:::

:::

::: {.pf-step #rouche-bound-at-1}
On the circle $\abs{z}=1$,
$$
\abs{f(z)-g(z)}<\abs{g(z)}.
$$

::: pf-proof
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

:::

::: {.pf-step #three-zeros-in-disk-1}
The polynomial $f$ has exactly three zeros, counted with
multiplicity, in $\abs z<1$.

::: pf-proof
Apply Rouché's theorem using step [](#rouche-bound-at-1){.pf-ref}. Again $f$ and $g$ have the same
number of zeros in the disk, and $g(z)=5z^3$ has exactly three.
:::

:::

::: {.pf-step #no-zeros-on-boundary}
The polynomial $f$ has no zeros on either boundary circle
$\abs z=1$ or $\abs z=2$.

::: pf-proof
On either circle, steps [](#rouche-bound-at-2){.pf-ref} and [](#rouche-bound-at-1){.pf-ref} give
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

:::

::: {.pf-step #zero-count-annulus}
The number of zeros of $f$ in
$$
1\le\abs z\le2
$$
is
$$
\boxed{0}.
$$

::: pf-proof
Steps [](#three-zeros-in-disk-2){.pf-ref} and [](#three-zeros-in-disk-1){.pf-ref} show that the number of zeros in
$1\le\abs z<2$ is $3-3=0$. Step [](#no-zeros-on-boundary){.pf-ref} shows that the circle
$\abs z=2$ contains no zero. Hence the closed annulus contains no zeros.
:::

:::

::: pf-qed
Step [](#zero-count-annulus){.pf-ref} is the required count.
:::

:::

:::
