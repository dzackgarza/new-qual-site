---
schema: qual/card@1
id: P-BKF06-4B
kind: problem
title: Irreducibility of $f(x^3)$ when a root of $f$ has no cube root
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 4B of the retained Berkeley Fall 2006 preliminary-exam solution packet f06solution.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained tower-degree argument. A cube root b
    of a has degree three over Q(a) because x^3-a has no root in Q(a), and
    [Q(b):Q]=3 deg(f) matches deg(f(x^3)).
---

::: {.problem}
Let $f(x)\in\mathbb Q[x]$ be irreducible.
Suppose there is a field extension $F/\mathbb Q$ containing a root $a$ of $f(x)$ such that $F$ contains no cube root of $a$.
Show that $f(x^3)$ is irreducible over $\mathbb Q$.
:::

::: {.solution}
Let
$$
n=\deg f,
$$
and choose a cube root $b$ of $a$ in an algebraic closure, so that
$$
b^3=a.
$$

<1>1. One has
$$
[\QQ(a):\QQ]=n.
$$

::: {.proof}
The element $a$ is a root of the irreducible polynomial
$f\in\QQ[x]$. Hence, up to multiplication by a nonzero rational
constant, $f$ is the minimal polynomial of $a$ over $\QQ$. Therefore
the degree of the simple extension $\QQ(a)/\QQ$ is $n$.
:::

<1>2. The polynomial
$$
x^3-a
$$
is irreducible over $\QQ(a)$.

::: {.proof}
Since $a\in F$, one has
$$
\QQ(a)\subseteq F.
$$
By hypothesis, $F$ contains no cube root of $a$. Therefore
$x^3-a$ has no root in $\QQ(a)$.

A reducible cubic polynomial over a field has a linear factor and
hence a root in that field. Thus the cubic $x^3-a$ is irreducible
over $\QQ(a)$.
:::

<1>3. One has
$$
[\QQ(b):\QQ(a)]=3.
$$

::: {.proof}
Because $b^3=a$, the element $a$ belongs to $\QQ(b)$, so
$$
\QQ(a)\subseteq\QQ(b).
$$
The element $b$ is a root of $x^3-a$, which is irreducible over
$\QQ(a)$ by step <1>2. Hence its degree over $\QQ(a)$ is $3$.
:::

<1>4. The degree of $b$ over $\QQ$ is
$$
[\QQ(b):\QQ]=3n.
$$

::: {.proof}
By the tower law and steps <1>1 and <1>3,
$$
\begin{aligned}
[\QQ(b):\QQ]
&=
[\QQ(b):\QQ(a)]
[\QQ(a):\QQ]
\\
&=
3n.
\end{aligned}
$$
:::

<1>5. The element $b$ is a root of $f(x^3)$, whose degree is $3n$.

::: {.proof}
Since $b^3=a$ and $f(a)=0$,
$$
f(b^3)=f(a)=0.
$$
Thus $b$ is a root of $f(x^3)$. Also
$$
\deg f(x^3)=3\deg f=3n.
$$
:::

<1>6. The polynomial
$$
\boxed{f(x^3)}
$$
is irreducible over $\QQ$.

::: {.proof}
Let $m_b(x)$ be the minimal polynomial of $b$ over $\QQ$. By step
<1>4,
$$
\deg m_b=3n.
$$
By step <1>5, $m_b$ divides $f(x^3)$ in $\QQ[x]$, and
$f(x^3)$ also has degree $3n$. Hence the two polynomials differ only
by a nonzero rational scalar. Since $m_b$ is irreducible,
$f(x^3)$ is irreducible.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 proves the required conclusion.
:::
:::
