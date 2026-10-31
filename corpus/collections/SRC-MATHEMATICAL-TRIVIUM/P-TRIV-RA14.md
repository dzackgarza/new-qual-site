---
schema: qual/card@1
id: P-TRIV-RA14
kind: problem
title: Double and iterated limits of $x+y\sin\frac1x$
classification:
  areas: [real-analysis]
  topics:
  - Iterated Limits
  - Limits
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

::: pf

::: {.pf-step #s1-1}

For $x\neq0$,
$$
\abs{f(x,y)}
\leq
\abs{x}+\abs{y}.
$$


::: pf-proof

Since
$$
f(x,y)=x+y\sin(1/x),
$$
the triangle inequality and $\abs{\sin(1/x)}\leq1$ give
$$
\abs{f(x,y)}
\leq
\abs{x}+\abs{y}.
$$

:::

:::

::: {.pf-step #s1-2}

If $x=0$, then
$$
f(0,y)=0.
$$


::: pf-proof

This is the second branch in the definition of $f$.

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
\boxed{
\lim_{(x,y)\to(0,0)}f(x,y)=0.
}
$$


::: pf-proof

For $x\neq0$, step [](#s1-1){.pf-ref} gives
$$
\abs{f(x,y)}
\leq
\abs{x}+\abs{y}
\longrightarrow0
$$
as $(x,y)\to(0,0)$. For $x=0$, step [](#s1-2){.pf-ref} gives the value $0$ exactly. Hence
the squeeze theorem gives the two-variable limit.

:::

:::

::: {.pf-step #s1-4}

For fixed $x\neq0$,
$$
\lim_{y\to0}f(x,y)=x.
$$


::: pf-proof

The term
$$
y\sin(1/x)
$$
tends to $0$ as $y\to0$ with $x$ fixed.

:::

:::

::: {.pf-step #s1-5}

At $x=0$,
$$
\lim_{y\to0}f(0,y)=0.
$$


::: pf-proof

By step [](#s1-2){.pf-ref}, the function is identically zero as a function of $y$ when
$x=0$.

:::

:::

::: {.pf-step #s1-6}

Thus the inner limit in $y$ is the function
$$
g(x)
=
\lim_{y\to0}f(x,y)
=
x.
$$


::: pf-proof

Combine steps [](#s1-4){.pf-ref} through [](#s1-5){.pf-ref}.

:::

:::

::: {.pf-step #s1-7}

Therefore
$$
\boxed{
\lim_{x\to0}
\left(
\lim_{y\to0}f(x,y)
\right)
=0.
}
$$


::: pf-proof

By step [](#s1-6){.pf-ref}, the outer limit is
$$
\lim_{x\to0}x=0.
$$

:::

:::

::: {.pf-step #s1-8}

Fix $y\neq0$. Then
$$
\lim_{x\to0}f(x,y)
$$
does not exist.


::: pf-proof

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

:::

::: {.pf-step #s1-9}

Hence
$$
\boxed{
\lim_{y\to0}
\left(
\lim_{x\to0}f(x,y)
\right)
\text{ does not exist}.
}
$$


::: pf-proof

By step [](#s1-8){.pf-ref}, the inner limit in $x$ is undefined for every $y\neq0$, so it is
not defined on any punctured neighborhood of $y=0$. Therefore the stated
iterated limit does not exist in the standard sense.

:::

:::

::: pf-qed

Steps [](#s1-3){.pf-ref} and [](#s1-7){.pf-ref}, and [](#s1-9){.pf-ref} give the double limit and both iterated-limit
answers.

:::

:::

:::
