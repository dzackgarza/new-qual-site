---
schema: qual/card@1
id: P-BKF12-8A
kind: problem
title: Elements of squarefree order dividing the order of a finite abelian group
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked against Problem 8A in the retained Fall 2012 Berkeley prelim exam
    and independently reviewed the retained solution packet F12_Solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the Cauchy-theorem construction, the order argument for the product,
    and the Klein four-group counterexample.
---

::: {.problem}
Let $G$ be a finite Abelian group of order $n$. Suppose $m$ is a square-free (not divisible by the square of a prime), positive integer dividing $n$. Show that $G$ contains an element of order $m$. Give an example to show that this need not be true if $m$ is not assumed to be square-free.
:::

::: {.solution}
Let $e$ denote the identity element of $G$.

<1>1. If $m=1$, then $G$ contains an element of order $m$; hence it
suffices to treat $m>1$, in which case
$$
m=p_1p_2\cdots p_k
$$
for distinct primes $p_1,\ldots,p_k$.

::: {.proof}
The identity $e$ has order $1$. If $m>1$, squarefreeness gives the
displayed factorization into distinct primes.
:::

<1>2. For each $i\in\{1,\ldots,k\}$, there is an element
$a_i\in G$ of order $p_i$.

::: {.proof}
Since $p_i\mid m$ and $m\mid\lvert G\rvert$, one has
$p_i\mid\lvert G\rvert$. Cauchy's theorem therefore gives an element
$a_i\in G$ of order $p_i$.
:::

<1>3. For
$$
g\coloneqq a_1a_2\cdots a_k,
$$
one has $g^m=e$.

::: {.proof}
The group $G$ is abelian, so
$$
g^m=a_1^m a_2^m\cdots a_k^m.
$$
For every $i$, step <1>1 gives $p_i\mid m$, while step <1>2 gives
$a_i^{p_i}=e$. Hence $a_i^m=e$ for every $i$, and therefore $g^m=e$.
:::

<1>4. For every $i\in\{1,\ldots,k\}$,
$$
g^{m/p_i}\ne e.
$$

::: {.proof}
Fix $i$. Since $G$ is abelian,
$$
g^{m/p_i}
=\prod_{j=1}^k a_j^{m/p_i}.
$$
If $j\ne i$, then $p_j\mid m/p_i$, so step <1>2 gives
$a_j^{m/p_i}=e$. Thus
$$
g^{m/p_i}=a_i^{m/p_i}.
$$
The primes in step <1>1 are distinct, so
$p_i\nmid m/p_i$. Since $a_i$ has order $p_i$ by step <1>2,
$a_i^{m/p_i}\ne e$.
:::

<1>5. The element $g$ has order
$$
\boxed{m}.
$$

::: {.proof}
Let $r$ be the order of $g$. By step <1>3, $g^m=e$, so $r\mid m$.
Suppose $r<m$. Since $m$ is squarefree and $r$ is a proper divisor of
$m$, some prime $p_i$ appearing in step <1>1 does not divide $r$.
Because $r\mid m$, it follows that $r\mid m/p_i$. Hence
$g^{m/p_i}=e$, contradicting step <1>4. Therefore $r=m$.
:::

<1>6. The squarefree hypothesis cannot be omitted: for
$$
G=C_2\times C_2
\qquad\text{and}\qquad
m=4,
$$
one has $m\mid\lvert G\rvert$, but $G$ has no element of order $m$.

::: {.proof}
The group $C_2\times C_2$ has order $4$, while every nonidentity
element has order $2$. Thus $4$ divides the group order, but no element
has order $4$.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>1 handles $m=1$. For $m>1$, step <1>5 constructs an element of
order $m$, and step <1>6 gives the required counterexample when $m$ is
not squarefree.
:::
:::
