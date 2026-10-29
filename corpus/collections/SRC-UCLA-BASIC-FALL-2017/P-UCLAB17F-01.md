---
schema: qual/card@1
id: P-UCLAB17F-01
kind: problem
title: Orthogonal polynomials of degree at most three
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
  note: Checked against the vendored UCLA Basic Examination, Fall 2017, `assets/attachments/basic-17F.pdf`.
---

::: {.problem}
Let $V$ be the complex vector space of polynomials of degree at most $3$.

(a) Show that
$$
\langle f,g\rangle=\int_{-1}^1 f(t)\overline{g(t)}\,dt
$$
defines an inner product on $V$.

(b) Find an orthonormal basis of $V$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For $f,g\in V$, the quantity
$$
\langle f,g\rangle
=
\int_{-1}^1f(t)\overline{g(t)}\,dt
$$
is conjugate symmetric:
$$
\langle f,g\rangle
=
\overline{\langle g,f\rangle}.
$$


::: pf-proof

$$
\begin{aligned}
\overline{\langle g,f\rangle}
&=
\overline{
\int_{-1}^1g(t)\overline{f(t)}\,dt
}\\
&=
\int_{-1}^1
\overline{g(t)}f(t)\,dt\\
&=
\langle f,g\rangle.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-2}

The form is linear in the first variable and conjugate-linear in the second.


::: pf-proof

For $\alpha,\beta\in\CC$,
$$
\begin{aligned}
\langle \alpha f+\beta h,g\rangle
&=
\int_{-1}^1
(\alpha f+\beta h)\overline g\,dt\\
&=
\alpha\langle f,g\rangle
+
\beta\langle h,g\rangle.
\end{aligned}
$$
Similarly,
$$
\langle f,\alpha g+\beta h\rangle
=
\overline{\alpha}\langle f,g\rangle
+
\overline{\beta}\langle f,h\rangle.
$$

:::

:::

::: {.pf-step #s1-3}

For every $f\in V$,
$$
\langle f,f\rangle\ge0,
$$
with equality if and only if $f=0$.


::: pf-proof

One has
$$
\langle f,f\rangle
=
\int_{-1}^1|f(t)|^2\,dt
\ge0.
$$
If the integral is zero, the continuous nonnegative function
$$
|f(t)|^2
$$
must vanish identically on $[-1,1]$.
Hence $f(t)=0$ for every $t$ in that interval.
A polynomial vanishing on infinitely many points is the zero polynomial.
Thus $f=0$.
The converse is immediate.

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\boxed{
\langle f,g\rangle
=
\int_{-1}^1f(t)\overline{g(t)}\,dt
}
$$
defines an inner product on $V$.


::: pf-proof

Steps [](#s1-1){.pf-ref} through [](#s1-3){.pf-ref} verify conjugate symmetry, sesquilinearity, and positive definiteness.

:::

:::

::: {.pf-step #s1-5}

Define
$$
p_0(t)=1,
\qquad
p_1(t)=t,
$$
$$
p_2(t)=3t^2-1,
\qquad
p_3(t)=5t^3-3t.
$$
Then $p_0,p_1,p_2,p_3$ are pairwise orthogonal.


::: pf-proof

The functions $p_0,p_2$ are even and $p_1,p_3$ are odd.
Hence every inner product between one even and one odd polynomial vanishes by symmetry of the interval.

It remains to check the even-even and odd-odd pairs.
First,
$$
\begin{aligned}
\langle p_0,p_2\rangle
&=
\int_{-1}^1(3t^2-1)\,dt\\
&=
3\cdot\frac23-2\\
&=0.
\end{aligned}
$$
Also,
$$
\begin{aligned}
\langle p_1,p_3\rangle
&=
\int_{-1}^1t(5t^3-3t)\,dt\\
&=
5\int_{-1}^1t^4\,dt
-
3\int_{-1}^1t^2\,dt\\
&=
5\cdot\frac25
-
3\cdot\frac23\\
&=
0.
\end{aligned}
$$
Thus all distinct pairs are orthogonal.

:::

:::

::: {.pf-step #s1-6}

Their squared norms are
$$
\|p_0\|^2=2,
\qquad
\|p_1\|^2=\frac23,
$$
$$
\|p_2\|^2=\frac85,
\qquad
\|p_3\|^2=\frac87.
$$


::: pf-proof

For $p_0$ and $p_1$,
$$
\|p_0\|^2
=
\int_{-1}^1 1\,dt
=2,
$$
$$
\|p_1\|^2
=
\int_{-1}^1t^2\,dt
=
\frac23.
$$

For $p_2$,
$$
\begin{aligned}
\|p_2\|^2
&=
\int_{-1}^1(3t^2-1)^2\,dt\\
&=
9\int_{-1}^1t^4\,dt
-
6\int_{-1}^1t^2\,dt
+
\int_{-1}^1 1\,dt\\
&=
9\cdot\frac25
-
6\cdot\frac23
+
2\\
&=
\frac85.
\end{aligned}
$$

For $p_3$,
$$
\begin{aligned}
\|p_3\|^2
&=
\int_{-1}^1(5t^3-3t)^2\,dt\\
&=
25\int_{-1}^1t^6\,dt
-
30\int_{-1}^1t^4\,dt
+
9\int_{-1}^1t^2\,dt\\
&=
25\cdot\frac27
-
30\cdot\frac25
+
9\cdot\frac23\\
&=
\frac87.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-7}

Therefore an orthonormal basis is
$$
\boxed{
\left\{
\frac1{\sqrt2},
\quad
\sqrt{\frac32}\,t,
\quad
\sqrt{\frac58}\,(3t^2-1),
\quad
\sqrt{\frac78}\,(5t^3-3t)
\right\}.
}
$$


::: pf-proof

By step [](#s1-5){.pf-ref}, the four displayed polynomials are mutually orthogonal.
Step [](#s1-6){.pf-ref} gives the normalization factors.
Their degrees are
$$
0,1,2,3,
$$
so they are linearly independent.
Since $\dim_{\CC}V=4$, they form a basis.
After normalization, it is orthonormal.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} proves part (a), and step [](#s1-7){.pf-ref} proves part (b).

:::

:::

:::
