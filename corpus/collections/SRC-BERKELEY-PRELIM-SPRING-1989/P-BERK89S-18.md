---
schema: qual/card@1
id: P-BERK89S-18
kind: problem
title: Separate continuity plus compact-image preservation implies continuity on $\mathbb R^2$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-22
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: >-
    Converted a hypothetical discontinuity sequence into a convergent sequence
    of nearby interpolation points whose image has a missing limit point,
    contradicting compact-image preservation.
---

::: {.problem}
Let $f:\mathbb R^2\to\mathbb R$ satisfy:

1. for every $y_0\in\mathbb R$, the function $x\mapsto f(x,y_0)$ is continuous;
2. for every $x_0\in\mathbb R$, the function $y\mapsto f(x_0,y)$ is continuous;
3. $f(K)$ is compact whenever $K\subset\mathbb R^2$ is compact.

Prove that $f$ is continuous.
:::

::: {.solution}
::: pf

::: {.pf-step #discontinuity-sequence}
Suppose $f$ is discontinuous at $(a,b)\in\RR^2$. Then there are
$(x_n,y_n)\to(a,b)$, a number $\varepsilon>0$, and a subsequence, again
indexed by $n$, such that
$$
f(x_n,y_n)\longrightarrow L
$$
for some $L\neq f(a,b)$.

::: pf-proof
By the sequential criterion for continuity, discontinuity at $(a,b)$ gives
$\varepsilon>0$ and a sequence $(x_n,y_n)\to(a,b)$ such that
$$
\abs{f(x_n,y_n)-f(a,b)}\geq\varepsilon
$$
for every $n$.

The set
$$
K_0=\{(a,b)\}\cup\{(x_n,y_n):n\geq1\}
$$
is compact. By hypothesis, $f(K_0)$ is compact in $\RR$, so the sequence
$f(x_n,y_n)$ has a convergent subsequence. Relabel it so that
$$
f(x_n,y_n)\to L.
$$
Passing to the limit in the preceding inequality gives
$\abs{L-f(a,b)}\geq\varepsilon$, hence $L\neq f(a,b)$.
:::

:::

::: {.pf-step #sequences-defined}
Set
$$
c=f(a,b),
\qquad
c_n=f(a,y_n),
\qquad
v_n=f(x_n,y_n).
$$
Then $c_n\to c$ and $v_n\to L$.

::: pf-proof
The convergence $v_n\to L$ is step [](#discontinuity-sequence){.pf-ref}. Since $y_n\to b$ and the function
$$
y\longmapsto f(a,y)
$$
is continuous by hypothesis (2), one has
$$
c_n=f(a,y_n)\longrightarrow f(a,b)=c.
$$
:::

:::

::: {.pf-step #interpolation-points}
After discarding finitely many terms, there are numbers $t_n$ and
points $\xi_n$ between $a$ and $x_n$ such that
$$
f(\xi_n,y_n)=t_n,
\qquad
t_n\longrightarrow L,
\qquad
t_n\neq L
$$
for every $n$.

::: pf-proof
Because $c_n\to c$, $v_n\to L$, and $c\neq L$, one has $c_n\neq v_n$ for
all sufficiently large $n$. For each such $n$, choose
$$
0<\lambda_n<\frac1n
$$
so that
$$
t_n=(1-\lambda_n)v_n+\lambda_n c_n
$$
is not equal to $L$. This is possible because, as $\lambda$ varies between
$0$ and $1/n$, the affine expression
$(1-\lambda)v_n+\lambda c_n$ can equal the fixed number $L$ for at most one
value of $\lambda$.

The number $t_n$ lies strictly between $c_n$ and $v_n$. For fixed $n$, the
function
$$
x\longmapsto f(x,y_n)
$$
is continuous by hypothesis (1). Since its values at $a$ and $x_n$ are
$c_n$ and $v_n$, the intermediate value theorem gives a point $\xi_n$
between $a$ and $x_n$ such that $f(\xi_n,y_n)=t_n$.

Finally,
$$
t_n-v_n=\lambda_n(c_n-v_n)\longrightarrow0,
$$
because $(c_n-v_n)$ is bounded and $\lambda_n\to0$. Since $v_n\to L$, it
follows that $t_n\to L$.
:::

:::

::: {.pf-step #k-not-compact-image}
The set
$$
K=\{(a,b)\}\cup\{(\xi_n,y_n):n\geq1\}
$$
is compact, but $f(K)$ is not compact.

::: pf-proof
Since $\xi_n$ lies between $a$ and $x_n$ and $x_n\to a$, one has
$\xi_n\to a$. Together with $y_n\to b$, this gives
$$
(\xi_n,y_n)\longrightarrow(a,b).
$$
Thus $K$ is a convergent sequence together with its limit and is compact.

By construction,
$$
f(K)=\{c\}\cup\{t_n:n\geq1\}.
$$
The sequence $t_n$ converges to $L$, while $L\neq c$ by step [](#discontinuity-sequence){.pf-ref} and
$t_n\neq L$ for every $n$ by step [](#interpolation-points){.pf-ref}. Hence $L$ is a limit point of
$f(K)$ that does not belong to $f(K)$. Therefore $f(K)$ is not closed in
$\RR$, and so it is not compact.
:::

:::

::: {.pf-step #f-continuous}
The function $f$ is continuous on $\RR^2$.

::: pf-proof
If $f$ were discontinuous at any point, steps [](#discontinuity-sequence){.pf-ref}, [](#sequences-defined){.pf-ref}, [](#interpolation-points){.pf-ref}, and [](#k-not-compact-image){.pf-ref} would produce a
compact set $K\subset\RR^2$ for which $f(K)$ is not compact, contradicting
hypothesis (3). Thus no discontinuity point exists.
:::

:::

::: pf-qed
Step [](#f-continuous){.pf-ref} is the required conclusion.
:::

:::
:::
