---
schema: qual/card@1
id: P-ALGF18F
kind: problem
title: Roots of $x^q - x + 1$ over $\FF_q$; Galois degree $p$
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
  - Galois Theory
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked against Problems 8 and 9 of the official UCSD Algebra Qualifying Exam, Fall 2018 source; the polynomial and all three parts agree with the source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified the Frobenius recurrence, containment in the degree-p finite-field extension, and the resulting degree-p statement for every irreducible factor.
---

::: {.problem}
Suppose $p$ is prime and $q = p^n$ for some positive integer $n$.
Let $\FF_q$ be a finite field of order $q$ and $\overline{\FF}_q$ be an algebraic closure of $\FF_q$.
Suppose $\alpha \in \overline{\FF}_q$ is a zero of $x^q - x + 1$.

(a) Prove that $\alpha^{q^i} = \alpha - i$ for any positive integer $i$.

(b) Prove that $\cardinality{\mathrm{Gal}(\FF_q[\alpha]/\FF_q)} = p$.

(c) Prove that any irreducible factor of $x^q - x + 1 \in \FF_q[x]$ has degree $p$.
:::

::: {.solution}
Throughout, an integer $i$ occurring in an expression such as $\alpha-i$ is understood through its image in the prime field $\FF_p\subseteq\FF_q$.

::: pf

::: {.pf-step #s1}

For every positive integer $i$,
$$
\alpha^{q^i}=\alpha-i.
$$

::: pf-proof

Since $\alpha$ is a root of $x^q-x+1$,
$$
\alpha^q=\alpha-1.
$$
This is the case $i=1$.

Assume
$$
\alpha^{q^i}=\alpha-i.
$$
Raising both sides to the $q$th power gives
$$
\alpha^{q^{i+1}}=(\alpha-i)^q.
$$
The $q$th-power map is a field homomorphism in characteristic $p$, and every element of the prime field is fixed by it. Hence
$$
(\alpha-i)^q=\alpha^q-i=(\alpha-1)-i=\alpha-(i+1).
$$
Induction proves the formula for all $i\ge1$, proving part (a).

:::

:::

::: {.pf-step #s2}

The element $\alpha$ lies in $\FF_{q^p}$ but not in $\FF_q$.

::: pf-proof

Taking $i=p$ in step [](#s1){.pf-ref} and using characteristic $p$ gives
$$
\alpha^{q^p}=\alpha-p=\alpha.
$$
The roots of
$$
x^{q^p}-x
$$
in the algebraic closure are precisely the elements of $\FF_{q^p}$, so
$$
\alpha\in\FF_{q^p}.
$$
On the other hand,
$$
\alpha^q=\alpha-1\neq\alpha,
$$
so $\alpha$ is not fixed by the $q$th-power Frobenius and therefore
$$
\alpha\notin\FF_q.
$$

:::

:::

::: {.pf-step #s3}

One has
$$
[\FF_q(\alpha):\FF_q]=p.
$$

::: pf-proof

By step [](#s2){.pf-ref},
$$
\FF_q(\alpha)\subseteq\FF_{q^p}.
$$
Hence the tower law gives
$$
[\FF_q(\alpha):\FF_q]\mid
[\FF_{q^p}:\FF_q]=p.
$$
Since $p$ is prime, the degree is either $1$ or $p$.
The degree cannot be $1$ because $\alpha\notin\FF_q$ by step [](#s2){.pf-ref}.
Therefore it is $p$.

:::

:::

::: pf-step

The extension $\FF_q[\alpha]/\FF_q$ is Galois of degree $p$, so
$$
\cardinality{\operatorname{Gal}(\FF_q[\alpha]/\FF_q)}=p.
$$

::: pf-proof

Because $\alpha$ is algebraic over $\FF_q$,
$$
\FF_q[\alpha]=\FF_q(\alpha).
$$
By steps [](#s2){.pf-ref} and [](#s3){.pf-ref},
$$
\FF_q(\alpha)\subseteq\FF_{q^p}
$$
and both extensions of $\FF_q$ have degree $p$.
Hence
$$
\FF_q(\alpha)=\FF_{q^p}.
$$
The polynomial $x^{q^p}-x$ splits over $\FF_{q^p}$ and has derivative $-1$, so it is separable.
Therefore $\FF_{q^p}/\FF_q$ is Galois.
Its Galois group has order equal to the extension degree, namely $p$.
This proves part (b).

:::

:::

::: pf-step

Every irreducible factor of $x^q-x+1$ in $\FF_q[x]$ has degree $p$.

::: pf-proof

Let
$$
r(x)\in\FF_q[x]
$$
be an irreducible factor, and let $\beta$ be a root of $r$ in the algebraic closure.
Then $\beta$ is also a root of $x^q-x+1$, so the argument of step [](#s1){.pf-ref} gives
$$
\beta^{q^p}=\beta
\qquad\text{and}\qquad
\beta^q=\beta-1\neq\beta.
$$
Thus
$$
\beta\in\FF_{q^p}\setminus\FF_q.
$$
Exactly as in step [](#s3){.pf-ref},
$$
[\FF_q(\beta):\FF_q]=p.
$$
Since $r$ is the minimal polynomial of $\beta$ over $\FF_q$,
$$
\deg r=p.
$$
This proves part (c).

:::

:::

:::

:::
