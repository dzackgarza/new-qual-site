---
schema: qual/card@1
id: P-TRIV-RA14
kind: problem
title: Double and iterated limits of $x+y\sin\frac1x$
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, Problem 14, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Repaired the garbled iterated-limit notation against Real Analysis Problem 14 on page 9 of the source PDF.
---

::: {.problem}
Find $\lim_{(x,y) \to (0,0)} f(x,y)$, where
$$
f(x,y) = \begin{cases} x + y \sin\frac{1}{x}, & x \neq 0, \\ 0, & x = 0. \end{cases}
$$
Do the limits $\lim_{x \to 0}\left(\lim_{y \to 0} f(x,y)\right)$ and $\lim_{y \to 0}\left(\lim_{x \to 0} f(x,y)\right)$ exist?
:::

::: {.solution}
<1>1. For $x\neq0$,
$$
|f(x,y)|
\leq
|x|+|y|.
$$

::: {.proof}
Since
$$
f(x,y)=x+y\sin(1/x),
$$
the triangle inequality and $|\sin(1/x)|\leq1$ give
$$
|f(x,y)|
\leq
|x|+|y|.
$$
:::

<1>2. If $x=0$, then
$$
f(0,y)=0.
$$

::: {.proof}
This is the second branch in the definition of $f$.
:::

<1>3. Therefore
$$
\boxed{
\lim_{(x,y)\to(0,0)}f(x,y)=0.
}
$$

::: {.proof}
For $x\neq0$, step <1>1 gives
$$
|f(x,y)|
\leq
|x|+|y|
\longrightarrow0
$$
as $(x,y)\to(0,0)$. For $x=0$, step <1>2 gives the value $0$ exactly. Hence
the squeeze theorem gives the two-variable limit.
:::

<1>4. For fixed $x\neq0$,
$$
\lim_{y\to0}f(x,y)=x.
$$

::: {.proof}
The term
$$
y\sin(1/x)
$$
tends to $0$ as $y\to0$ with $x$ fixed.
:::

<1>5. At $x=0$,
$$
\lim_{y\to0}f(0,y)=0.
$$

::: {.proof}
By step <1>2, the function is identically zero as a function of $y$ when
$x=0$.
:::

<1>6. Thus the inner limit in $y$ is the function
$$
g(x)
=
\lim_{y\to0}f(x,y)
=
x.
$$

::: {.proof}
Combine steps <1>4--<1>5.
:::

<1>7. Therefore
$$
\boxed{
\lim_{x\to0}
\left(
\lim_{y\to0}f(x,y)
\right)
=0.
}
$$

::: {.proof}
By step <1>6, the outer limit is
$$
\lim_{x\to0}x=0.
$$
:::

<1>8. Fix $y\neq0$. Then
$$
\lim_{x\to0}f(x,y)
$$
does not exist.

::: {.proof}
Choose
$$
x_n
=
\frac1{\pi/2+2\pi n}
$$
and
$$
z_n
=
\frac1{3\pi/2+2\pi n}.
$$
Then
$$
x_n\to0,
\qquad
z_n\to0,
$$
while
$$
\sin(1/x_n)=1
$$
and
$$
\sin(1/z_n)=-1.
$$
Hence
$$
f(x_n,y)=x_n+y\longrightarrow y,
$$
whereas
$$
f(z_n,y)=z_n-y\longrightarrow -y.
$$
Since $y\neq0$, the two subsequential limits differ.
:::

<1>9. Hence
$$
\boxed{
\lim_{y\to0}
\left(
\lim_{x\to0}f(x,y)
\right)
\text{ does not exist}.
}
$$

::: {.proof}
By step <1>8, the inner limit in $x$ is undefined for every $y\neq0$, so it is
not defined on any punctured neighborhood of $y=0$. Therefore the stated
iterated limit does not exist in the standard sense.
:::

<1>10. Q.E.D.

::: {.proof}
Steps <1>3, <1>7, and <1>9 give the double limit and both iterated-limit
answers.
:::
:::
