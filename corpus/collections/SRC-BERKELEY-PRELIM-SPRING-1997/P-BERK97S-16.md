---
schema: qual/card@1
id: P-BERK97S-16
kind: problem
title: A finite-dimensional reduced commutative complex algebra has nontrivial idempotents
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
- event: solution-written
  by: chatgpt
  date: 2026-09-23
---

::: {.problem}
Let $A$ be a finite-dimensional commutative algebra with identity over $\mathbb C$, with
\[
\dim_{\mathbb C}A\ge2.
\]
Suppose
\[
a^2\ne0
\]
for every nonzero $a\in A$. Show that the equation
\[
a^2=a
\]
has at least three distinct solutions in $A$.
:::

::: {.solution}
<1>1. For every $x\in A$, the minimal polynomial of $x$ over $\CC$ has
no repeated root.

::: {.proof}
Let $m_x(t)$ be the minimal polynomial of $x$. Since $\CC$ is
algebraically closed,
$$
m_x(t)=\prod_{i=1}^r(t-\lambda_i)^{e_i}
$$
for distinct $\lambda_i\in\CC$ and positive integers $e_i$.

Suppose some $e_j\geq2$, and put
$$
b(t)\coloneqq\frac{m_x(t)}{t-\lambda_j}.
$$
Then $\deg b<\deg m_x$, so minimality of $m_x$ gives
$$
b(x)\neq0.
$$
On the other hand, $m_x$ divides $b^2$: the factor
$(t-\lambda_j)^{e_j}$ occurs in $b^2$ with exponent
$2e_j-2\geq e_j$, and every other factor of $m_x$ occurs in $b^2$ with
at least its required exponent. Hence
$$
b(x)^2=0,
$$
contrary to the hypothesis. Therefore every $e_i=1$.
:::

<1>2. There is an element $x\in A$ whose minimal polynomial has at least
two distinct roots.

::: {.proof}
Since $\dim_{\CC}A\geq2$, choose
$$
x\notin\CC\cdot1.
$$
If the minimal polynomial of $x$ had degree $1$, then
$x=\lambda1$ for some $\lambda\in\CC$, contrary to the choice of $x$.
Thus $\deg m_x\geq2$. By step <1>1, all roots of $m_x$ are distinct, so
there are at least two of them.
:::

<1>3. There is an idempotent $e\in A$ with
$$
e\neq0,
\qquad
e\neq1.
$$

::: {.proof}
Write
$$
m_x(t)=\prod_{i=1}^r(t-\lambda_i),
\qquad
r\geq2.
$$
By Lagrange interpolation there is a polynomial $q(t)$ of degree at most
$r-1$ such that
$$
q(\lambda_1)=1,
\qquad
q(\lambda_i)=0
\quad(2\leq i\leq r).
$$
The polynomial $q^2-q$ vanishes at every root of the squarefree polynomial
$m_x$, so
$$
m_x\mid(q^2-q).
$$
Consequently
$$
e\coloneqq q(x)
$$
satisfies $e^2=e$.

Moreover, $q$ is nonzero and has degree less than $\deg m_x$, so
$q(x)\neq0$ by minimality of $m_x$. Likewise $q-1$ is nonzero because
$q(\lambda_2)=0$, and
$$
\deg(q-1)<\deg m_x,
$$
so $(q-1)(x)\neq0$. Hence $e\neq1$.
:::

<1>4. The equation $a^2=a$ has at least three distinct solutions in $A$.

::: {.proof}
The elements
$$
\boxed{0,\qquad1,\qquad e}
$$
are idempotent, and step <1>3 shows that they are pairwise distinct.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required conclusion.
:::
:::
