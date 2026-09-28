---
schema: qual/card@1
id: P-BERK83SU-04
kind: problem
title: Derivative zero on an interval implies equal endpoint values
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Starting from completeness, bisection gives Bolzano-Weierstrass on
    a closed interval. This yields the extreme value theorem for
    continuous functions. Fermat's interior-extremum lemma then gives
    Rolle's theorem and the mean value theorem, whose application to f
    gives f(b)-f(a)=f'(c)(b-a)=0.
---

::: {.problem}
Outline a proof, starting from basic properties of the real numbers, of the following theorem.

Let $f:[a,b]\to\mathbb R$ be continuous and differentiable on $(a,b)$, with
\[
f'(x)=0\qquad(x\in(a,b)).
\]
Then $f(b)=f(a)$.
:::

::: {.solution}
We use the least-upper-bound property of $\RR$ as the basic
completeness property.

<1>1. Every sequence in a closed bounded interval $[a,b]$ has a
convergent subsequence with limit in $[a,b]$.

<2>1. From any infinite sequence $(x_n)$ in $[a,b]$, one can construct
nested closed intervals
$$
I_1\supseteq I_2\supseteq\cdots
$$
such that $I_k$ contains infinitely many terms of the sequence and
$$
\operatorname{length}(I_k)=\frac{b-a}{2^k}.
$$

::: {.proof}
Bisect $[a,b]$. At least one half contains infinitely many terms of the
sequence; call such a half $I_1$. Bisect $I_1$ and choose a half
containing infinitely many terms; call it $I_2$. Continue inductively.
:::

<2>2. The nested intervals of step <2>1 have exactly one common point
$c\in[a,b]$.

::: {.proof}
Write
$$
I_k=[\alpha_k,\beta_k].
$$
The sequence $(\alpha_k)$ is increasing and bounded above, so by the
least-upper-bound property it has a supremum
$$
c=\sup_k\alpha_k.
$$
For every $k$ and every $j\geq k$,
$$
\alpha_j\leq\beta_k,
$$
so $c\leq\beta_k$. Also $\alpha_k\leq c$. Hence
$$
c\in I_k
$$
for every $k$. If $c'$ were another common point, then
$$
\abs{c-c'}\leq\operatorname{length}(I_k)
\longrightarrow0,
$$
so $c'=c$.
:::

<2>3. The original sequence has a subsequence converging to $c$.

::: {.proof}
Choose inductively indices
$$
n_1<n_2<\cdots
$$
with $x_{n_k}\in I_k$, possible because every $I_k$ contains
infinitely many terms. Since both $x_{n_k}$ and $c$ lie in $I_k$,
$$
\abs{x_{n_k}-c}
\leq
\operatorname{length}(I_k)
\longrightarrow0.
$$
Thus $x_{n_k}\to c$.
:::

<2>4. Q.E.D.

::: {.proof}
Step <2>3 proves step <1>1.
:::

<1>2. Every continuous function
$$
g:[a,b]\longrightarrow\RR
$$
is bounded.

::: {.proof}
Suppose $g$ were unbounded. Then for every positive integer $n$ one
could choose $x_n\in[a,b]$ with
$$
\abs{g(x_n)}>n.
$$
By step <1>1, some subsequence satisfies
$$
x_{n_k}\longrightarrow c\in[a,b].
$$
Continuity gives
$$
g(x_{n_k})\longrightarrow g(c),
$$
so the subsequence $(g(x_{n_k}))$ is bounded, contradicting
$$
\abs{g(x_{n_k})}>n_k\longrightarrow\infty.
$$
:::

<1>3. Every continuous function
$$
g:[a,b]\longrightarrow\RR
$$
attains both its maximum and its minimum.

<2>1. The function $g$ attains its maximum.

::: {.proof}
By step <1>2, the set
$$
g([a,b])
$$
is nonempty and bounded above. Let
$$
M=\sup g([a,b]).
$$
For every positive integer $n$, choose $x_n\in[a,b]$ such that
$$
M-\frac1n<g(x_n)\leq M.
$$
By step <1>1, a subsequence satisfies
$$
x_{n_k}\longrightarrow c\in[a,b].
$$
Continuity gives
$$
g(x_{n_k})\longrightarrow g(c),
$$
while the defining inequalities imply
$$
g(x_{n_k})\longrightarrow M.
$$
Therefore $g(c)=M$.
:::

<2>2. The function $g$ attains its minimum.

::: {.proof}
Apply step <2>1 to the continuous function $-g$.
:::

<2>3. Q.E.D.

::: {.proof}
Steps <2>1 and <2>2 prove step <1>3.
:::

<1>4. If $g$ is differentiable at an interior point $c$ and has a
local maximum or local minimum at $c$, then
$$
g'(c)=0.
$$

::: {.proof}
Suppose first that $c$ is a local maximum. For all sufficiently small
$h>0$,
$$
\frac{g(c+h)-g(c)}{h}\leq0,
$$
whereas for all sufficiently small $h<0$,
$$
\frac{g(c+h)-g(c)}{h}\geq0.
$$
If the derivative exists, both one-sided limits equal $g'(c)$, so
$$
g'(c)\leq0
\qquad\text{and}\qquad
g'(c)\geq0.
$$
Hence $g'(c)=0$. For a local minimum, apply the same argument to $-g$.
:::

<1>5. Rolle's theorem follows: if $g$ is continuous on $[a,b]$,
differentiable on $(a,b)$, and
$$
g(a)=g(b),
$$
then there is $c\in(a,b)$ such that
$$
g'(c)=0.
$$

::: {.proof}
By step <1>3, $g$ attains a maximum and a minimum on $[a,b]$. If these
values are equal, then $g$ is constant and every $c\in(a,b)$ satisfies
$g'(c)=0$. Otherwise, because $g(a)=g(b)$, at least one of the maximum
or minimum is attained at an interior point $c\in(a,b)$. Step <1>4
then gives $g'(c)=0$.
:::

<1>6. The mean value theorem follows: if $g$ is continuous on $[a,b]$
and differentiable on $(a,b)$, then for some $c\in(a,b)$,
$$
g(b)-g(a)=g'(c)(b-a).
$$

::: {.proof}
Define
$$
h(x)
=
g(x)
-
\frac{g(b)-g(a)}{b-a}(x-a).
$$
Then $h$ is continuous on $[a,b]$, differentiable on $(a,b)$, and
$$
h(a)=g(a)=h(b).
$$
By step <1>5, there is $c\in(a,b)$ with $h'(c)=0$. Thus
$$
0
=
g'(c)
-
\frac{g(b)-g(a)}{b-a},
$$
which rearranges to the stated identity.
:::

<1>7. For the function in the problem,
$$
\boxed{f(b)=f(a)}.
$$

::: {.proof}
Apply step <1>6 to $f$. There is $c\in(a,b)$ such that
$$
f(b)-f(a)
=
f'(c)(b-a).
$$
The hypothesis gives $f'(c)=0$, hence
$$
f(b)-f(a)=0.
$$
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>7 is the required conclusion.
:::
:::
