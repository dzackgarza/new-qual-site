---
schema: qual/card@1
id: P-ALGF18F
kind: problem
title: Roots of $x^q - x + 1$ over $\mathbb{F}_q$; Galois degree $p$
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

::: problem
Suppose $p$ is prime and $q = p^n$ for some positive integer $n$.
Let $\mathbb{F}_q$ be a finite field of order $q$ and $\overline{\mathbb{F}}_q$ be an algebraic closure of $\mathbb{F}_q$.
Suppose $\alpha \in \overline{\mathbb{F}}_q$ is a zero of $x^q - x + 1$.

(a) Prove that $\alpha^{q^i} = \alpha - i$ for any positive integer $i$.

(b) Prove that $|\mathrm{Gal}(\mathbb{F}_q[\alpha]/\mathbb{F}_q)| = p$.

(c) Prove that any irreducible factor of $x^q - x + 1 \in \mathbb{F}_q[x]$ has degree $p$.
:::

::: {.solution}
Throughout, an integer $i$ occurring in an expression such as $\alpha-i$ is understood through its image in the prime field $\mathbb F_p\subseteq\mathbb F_q$.

<1>1. For every positive integer $i$,
\[
\alpha^{q^i}=\alpha-i.
\]
::: {.proof}
Since $\alpha$ is a root of $x^q-x+1$,
\[
\alpha^q=\alpha-1.
\]
This is the case $i=1$.

Assume
\[
\alpha^{q^i}=\alpha-i.
\]
Raising both sides to the $q$th power gives
\[
\alpha^{q^{i+1}}=(\alpha-i)^q.
\]
The $q$th-power map is a field homomorphism in characteristic $p$, and every element of the prime field is fixed by it. Hence
\[
(\alpha-i)^q=\alpha^q-i=(\alpha-1)-i=\alpha-(i+1).
\]
Induction proves the formula for all $i\ge1$, proving part (a).
:::

<1>2. The element $\alpha$ lies in $\mathbb F_{q^p}$ but not in $\mathbb F_q$.
::: {.proof}
Taking $i=p$ in <1>1 and using characteristic $p$ gives
\[
\alpha^{q^p}=\alpha-p=\alpha.
\]
The roots of
\[
x^{q^p}-x
\]
in the algebraic closure are precisely the elements of $\mathbb F_{q^p}$, so
\[
\alpha\in\mathbb F_{q^p}.
\]
On the other hand,
\[
\alpha^q=\alpha-1\neq\alpha,
\]
so $\alpha$ is not fixed by the $q$th-power Frobenius and therefore
\[
\alpha\notin\mathbb F_q.
\]
:::

<1>3. One has
\[
[\mathbb F_q(\alpha):\mathbb F_q]=p.
\]
::: {.proof}
By <1>2,
\[
\mathbb F_q(\alpha)\subseteq\mathbb F_{q^p}.
\]
Hence the tower law gives
\[
[\mathbb F_q(\alpha):\mathbb F_q]\mid
[\mathbb F_{q^p}:\mathbb F_q]=p.
\]
Since $p$ is prime, the degree is either $1$ or $p$.
The degree cannot be $1$ because $\alpha\notin\mathbb F_q$ by <1>2.
Therefore it is $p$.
:::

<1>4. The extension $\mathbb F_q[\alpha]/\mathbb F_q$ is Galois of degree $p$, so
\[
\left|\operatorname{Gal}(\mathbb F_q[\alpha]/\mathbb F_q)\right|=p.
\]
::: {.proof}
Because $\alpha$ is algebraic over $\mathbb F_q$,
\[
\mathbb F_q[\alpha]=\mathbb F_q(\alpha).
\]
By <1>2 and <1>3,
\[
\mathbb F_q(\alpha)\subseteq\mathbb F_{q^p}
\]
and both extensions of $\mathbb F_q$ have degree $p$.
Hence
\[
\mathbb F_q(\alpha)=\mathbb F_{q^p}.
\]
The polynomial $x^{q^p}-x$ splits over $\mathbb F_{q^p}$ and has derivative $-1$, so it is separable.
Therefore $\mathbb F_{q^p}/\mathbb F_q$ is Galois.
Its Galois group has order equal to the extension degree, namely $p$.
This proves part (b).
:::

<1>5. Every irreducible factor of $x^q-x+1$ in $\mathbb F_q[x]$ has degree $p$.
::: {.proof}
Let
\[
r(x)\in\mathbb F_q[x]
\]
be an irreducible factor, and let $\beta$ be a root of $r$ in the algebraic closure.
Then $\beta$ is also a root of $x^q-x+1$, so the argument of <1>1 gives
\[
\beta^{q^p}=\beta
\qquad\text{and}\qquad
\beta^q=\beta-1\neq\beta.
\]
Thus
\[
\beta\in\mathbb F_{q^p}\setminus\mathbb F_q.
\]
Exactly as in <1>3,
\[
[\mathbb F_q(\beta):\mathbb F_q]=p.
\]
Since $r$ is the minimal polynomial of $\beta$ over $\mathbb F_q$,
\[
\deg r=p.
\]
This proves part (c).
:::
:::
