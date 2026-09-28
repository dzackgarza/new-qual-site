---
schema: qual/card@1
id: P-BKS16-2A
kind: problem
title: Integration by parts on $\RR$ for $L^2$ functions with $L^2$ derivatives
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-25
  note: Checked the statement and retained proof idea against Problem 2A in the vendored Berkeley Spring 2016 solution packet.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the Cauchy-Schwarz integrability claims, existence of boundary sequences with fg tending to zero, and passage from finite-interval integration by parts to the improper integrals.
---

::: {.problem}
Suppose that $f$ and $g$ are continuously differentiable real-valued functions on $\RR$ with $f,g,f',g'\in L^2(\RR)$.
Show that
$$
\int_{-\infty}^{\infty} f g'\,dx=-\int_{-\infty}^{\infty} f'g\,dx.
$$
(Recall that $L^2(\RR)$ is the set of integrable functions $h$ such that $\int_{-\infty}^{\infty}|h|^2\,dx<\infty$.)
:::

::: {.solution}
<1>1. The functions
$$
fg',
\qquad
f'g,
\qquad
fg
$$
belong to $L^1(\RR)$.

::: {.proof}
By the Cauchy--Schwarz inequality,
$$
\int_{\RR}\abs{fg'}
\leq
\left(\int_{\RR}\abs f^2\right)^{1/2}
\left(\int_{\RR}\abs{g'}^2\right)^{1/2}
<\infty.
$$
The same argument with $f'$ and $g$ shows that $f'g\in L^1(\RR)$, and the same argument with $f$ and $g$ shows that $fg\in L^1(\RR)$.
:::

<1>2. There are sequences
$$
x_j\longrightarrow-\infty,
\qquad
y_j\longrightarrow+\infty
$$
such that
$$
f(x_j)g(x_j)\longrightarrow0,
\qquad
f(y_j)g(y_j)\longrightarrow0.
$$

::: {.proof}
Set
$$
h(x)=\abs{f(x)g(x)}.
$$
By step <1>1, $h\in L^1(\RR)$. For each positive integer $j$, there must be some $y_j>j$ with
$$
h(y_j)<\frac1j.
$$
Indeed, otherwise $h(x)\geq1/j$ for every $x>j$, contradicting integrability. Likewise, there is some $x_j<-j$ with
$$
h(x_j)<\frac1j.
$$
These choices have the required limits.
:::

<1>3. For every $j$,
$$
\int_{x_j}^{y_j}fg'\,dx
+
\int_{x_j}^{y_j}f'g\,dx
=
f(y_j)g(y_j)-f(x_j)g(x_j).
$$

::: {.proof}
Since $f$ and $g$ are continuously differentiable,
$$
(fg)'=f'g+fg'.
$$
Integrate this identity on the finite interval $[x_j,y_j]$ and apply the fundamental theorem of calculus.
:::

<1>4. Passing to the limit in step <1>3 gives
$$
\int_{-\infty}^{\infty}fg'\,dx
+
\int_{-\infty}^{\infty}f'g\,dx
=
0.
$$

::: {.proof}
By step <1>1, both $fg'$ and $f'g$ are absolutely integrable. Since
$$
x_j\to-\infty,
\qquad
y_j\to+\infty,
$$
their integrals over $[x_j,y_j]$ converge to their integrals over $\RR$. By step <1>2, the boundary term on the right-hand side of step <1>3 converges to $0$. Taking $j\to\infty$ proves the displayed identity.
:::

<1>5. Therefore
$$
\boxed{
\int_{-\infty}^{\infty}fg'\,dx
=
-\int_{-\infty}^{\infty}f'g\,dx
}.
$$

::: {.proof}
Rearrange the identity in step <1>4.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required identity.
:::
:::
