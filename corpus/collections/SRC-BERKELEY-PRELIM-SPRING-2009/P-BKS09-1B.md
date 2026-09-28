---
schema: qual/card@1
id: P-BKS09-1B
kind: problem
title: Higher derivative test for local extrema
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
  note: Restored the lost arrow in f and math delimiters against s09solutions.pdf page 4 problem 1B.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: >-
    Independently checked the sign argument from f^{[n]}(a)>0, treating n=1
    separately because the retained source proof implicitly assumes n≥2.
---

::: {.problem}
Let $I \subseteq \mathbb{R}$ be an open interval, and let $f : I \to \mathbb{R}$ have continuous $k$-th derivatives $f^{[k]}$ on $I$ for $k \leq n - 1$. Let $a \in I$ be a point such that $f^{[k]}(a) = 0$ for all $1 \leq k \leq n - 1$, $f^{[n]}(a)$ exists and $f^{[n]}(a) > 0$. Prove that $f$ has a local minimum at $a$ if $n$ is even, and has no local extremum at $a$ if $n$ is odd.
:::

::: {.solution}
<1>1. If $n=1$, then $f$ has no local extremum at $a$.

::: {.proof}
Here $f'(a)>0$. By the definition of the derivative, there is
$\delta>0$ such that whenever $0<\abs{x-a}<\delta$,
$$
\frac{f(x)-f(a)}{x-a}>0.
$$
Thus
$$
f(x)<f(a)
\quad\text{for }a-\delta<x<a,
$$
while
$$
f(x)>f(a)
\quad\text{for }a<x<a+\delta.
$$
Hence $a$ is neither a local minimum nor a local maximum.
:::

<1>2. Suppose $n\geq2$. Then for all $t$ sufficiently close to $a$ with
$t\neq a$,
$$
\frac{f^{[n-1]}(t)}{t-a}>0.
$$

::: {.proof}
Since $n\geq2$, the hypothesis includes
$$
f^{[n-1]}(a)=0.
$$
The existence and positivity of $f^{[n]}(a)$ give
$$
\lim_{t\to a}
\frac{f^{[n-1]}(t)-f^{[n-1]}(a)}{t-a}
=
f^{[n]}(a)
>0.
$$
Therefore the displayed quotient is positive on some punctured neighborhood
of $a$.
:::

<1>3. Under the hypotheses of step <1>2, for every $x$ sufficiently close
to $a$ with $x\neq a$, there exists a point $c$ strictly between $a$ and
$x$ such that
$$
f(x)-f(a)
=
\frac{f^{[n-1]}(c)}{(n-1)!}(x-a)^{n-1}.
$$

::: {.proof}
Apply Taylor's theorem with Lagrange remainder to order $n-2$ on the interval
with endpoints $a$ and $x$. It gives
$$
f(x)
=
f(a)
+
\sum_{k=1}^{n-2}
\frac{f^{[k]}(a)}{k!}(x-a)^k
+
\frac{f^{[n-1]}(c)}{(n-1)!}(x-a)^{n-1}
$$
for some $c$ strictly between $a$ and $x$. Since
$f^{[k]}(a)=0$ for $1\leq k\leq n-2$, the sum vanishes.
:::

<1>4. If $n$ is even, then $f$ has a strict local minimum at $a$.

::: {.proof}
Take $x$ sufficiently close to $a$, as in steps <1>2 and <1>3.

If $x>a$, then $c>a$, so step <1>2 gives
$f^{[n-1]}(c)>0$. Also $x-a>0$, hence step <1>3 gives
$f(x)-f(a)>0$.

If $x<a$, then $c<a$, so step <1>2 gives
$f^{[n-1]}(c)<0$. Since $n$ is even, $n-1$ is odd and therefore
$(x-a)^{n-1}<0$. The product in step <1>3 is again positive.

Thus $f(x)>f(a)$ for every sufficiently close $x\neq a$.
:::

<1>5. If $n\geq3$ is odd, then $f$ has no local extremum at $a$.

::: {.proof}
For $x>a$ sufficiently close to $a$, the argument in step <1>4 gives
$f^{[n-1]}(c)>0$ and $(x-a)^{n-1}>0$, hence
$$
f(x)>f(a).
$$

For $x<a$ sufficiently close to $a$, one has
$f^{[n-1]}(c)<0$. Now $n-1$ is even, so $(x-a)^{n-1}>0$, and step <1>3
gives
$$
f(x)<f(a).
$$
Therefore every neighborhood of $a$ contains values of $f$ both below and
above $f(a)$.
:::

<1>6. The required parity conclusion holds for every positive integer $n$.

::: {.proof}
If $n$ is even, then $n\geq2$ and step <1>4 gives a local minimum. If $n$
is odd, either $n=1$ and step <1>1 applies, or $n\geq3$ and step <1>5
applies.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 is exactly the required conclusion.
:::
:::
