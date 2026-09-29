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

::: pf

::: {.pf-step #s1}

If $m=1$, then $G$ contains an element of order $m$; hence it
suffices to treat $m>1$, in which case
$$
m=p_1p_2\cdots p_k
$$
for distinct primes $p_1,\ldots,p_k$.

::: pf-proof

The identity $e$ has order $1$. If $m>1$, squarefreeness gives the
displayed factorization into distinct primes.

:::

:::

::: {.pf-step #s2}

For each $i\in\{1,\ldots,k\}$, there is an element
$a_i\in G$ of order $p_i$.

::: pf-proof

Since $p_i\mid m$ and $m\mid\lvert G\rvert$, one has
$p_i\mid\lvert G\rvert$. Cauchy's theorem therefore gives an element
$a_i\in G$ of order $p_i$.

:::

:::

::: {.pf-step #s3}

For
$$
g\coloneqq a_1a_2\cdots a_k,
$$
one has $g^m=e$.

::: pf-proof

The group $G$ is abelian, so
$$
g^m=a_1^m a_2^m\cdots a_k^m.
$$
For every $i$, step [](#s1){.pf-ref} gives $p_i\mid m$, while step [](#s2){.pf-ref} gives
$a_i^{p_i}=e$. Hence $a_i^m=e$ for every $i$, and therefore $g^m=e$.

:::

:::

::: {.pf-step #s4}

For every $i\in\{1,\ldots,k\}$,
$$
g^{m/p_i}\ne e.
$$

::: pf-proof

Fix $i$. Since $G$ is abelian,
$$
g^{m/p_i}
=\prod_{j=1}^k a_j^{m/p_i}.
$$
If $j\ne i$, then $p_j\mid m/p_i$, so step [](#s2){.pf-ref} gives
$a_j^{m/p_i}=e$. Thus
$$
g^{m/p_i}=a_i^{m/p_i}.
$$
The primes in step [](#s1){.pf-ref} are distinct, so
$p_i\nmid m/p_i$. Since $a_i$ has order $p_i$ by step [](#s2){.pf-ref},
$a_i^{m/p_i}\ne e$.

:::

:::

::: {.pf-step #s5}

The element $g$ has order
$$
\boxed{m}.
$$

::: pf-proof

Let $r$ be the order of $g$. By step [](#s3){.pf-ref}, $g^m=e$, so $r\mid m$.
Suppose $r<m$. Since $m$ is squarefree and $r$ is a proper divisor of
$m$, some prime $p_i$ appearing in step [](#s1){.pf-ref} does not divide $r$.
Because $r\mid m$, it follows that $r\mid m/p_i$. Hence
$g^{m/p_i}=e$, contradicting step [](#s4){.pf-ref}. Therefore $r=m$.

:::

:::

::: {.pf-step #s6}

The squarefree hypothesis cannot be omitted: for
$$
G=C_2\times C_2
\qquad\text{and}\qquad
m=4,
$$
one has $m\mid\lvert G\rvert$, but $G$ has no element of order $m$.

::: pf-proof

The group $C_2\times C_2$ has order $4$, while every nonidentity
element has order $2$. Thus $4$ divides the group order, but no element
has order $4$.

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} handles $m=1$. For $m>1$, step [](#s5){.pf-ref} constructs an element of
order $m$, and step [](#s6){.pf-ref} gives the required counterexample when $m$ is
not squarefree.

:::

:::

:::
