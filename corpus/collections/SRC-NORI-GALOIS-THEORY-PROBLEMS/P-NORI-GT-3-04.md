---
schema: qual/card@1
id: P-NORI-GT-3-04
kind: problem
title: Towers of quadratic extensions of $\mathbb F_p$ for $p\equiv 3 \pmod 4$
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against problem 3.4 of the retained Nori Galois Theory Problems PDF.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Stated the construction of Problem 3.3, on which this problem depends, from p. 1-2 of the Nori Galois Theory Problems PDF.
---

::: {.problem}
Problem 3.3 reads: Let $p$ be a prime which is $\equiv 1 \bmod 2^k$, but not congruent to $1$ modulo a higher power of $2$.
Assume $k \geq 2$.
Assume that $u_0 \in \mathbb{F}_p$ is not a square.
Construct a sequence of pairs $(E_n, u_n)$ where $E_n$ is a field and $u_n \in E_n$ as follows.
Define $(E_0, u_0) = (\mathbb{F}_p, u_0)$.
Assume that $(E_n, u_n)$ has been defined.
Let $E_{n+1}$ be a field extension of $E_n$ obtaing by adjoining a square-root $u_{n+1}$ of $u_n \in E_n$.
Show that $\deg(E_n/E_{n-1}) = 2$ for all $n > 0$.

Explain how you would construct a sequence of quadratic extensions when $k = 1$ in the previous problem.
:::

::: {.solution}
Here $k=1$ means
\[
p\equiv3\pmod4.
\]
The direct iteration from Problem 3.3 cannot start with an arbitrary nonsquare $u_0\in\mathbb F_p$ and retain the same valuation argument. Instead, first pass to the quadratic extension by adjoining a square root of $-1$.

<1>1. Since $p\equiv3\pmod4$, the element $-1$ is not a square in $\mathbb F_p$.

::: {.proof}
Euler's criterion gives
\[
(-1)^{(p-1)/2}=-1
\]
because $(p-1)/2$ is odd. Hence $-1$ is a nonsquare.
:::

<1>2. Choose $i$ with
\[
i^2=-1
\]
and set
\[
E_1=\mathbb F_p(i).
\]
Then
\[
[E_1:\mathbb F_p]=2
\]
and
\[
E_1\cong\mathbb F_{p^2}.
\]

::: {.proof}
By step <1>1, $X^2+1$ is irreducible over $\mathbb F_p$, so adjoining a root gives degree $2$. The resulting field has $p^2$ elements and hence is the unique field $\mathbb F_{p^2}$.
:::

<1>3. The exact power of $2$ dividing $p^2-1$ is at least $2^3$.

::: {.proof}
Factor
\[
p^2-1=(p-1)(p+1).
\]
Since $p\equiv3\pmod4$, one has $v_2(p-1)=1$ and $4\mid p+1$, so
\[
v_2(p^2-1)=v_2(p-1)+v_2(p+1)\ge3.
\]
Thus $|E_1^\times|=p^2-1$ has exact $2$-adic valuation $k'\ge3$.
:::

<1>4. Choose any nonsquare
\[
u_1\in E_1^\times.
\]

::: {.proof}
The cyclic group $E_1^\times$ has even order, so its subgroup of squares has index $2$. Hence nonsquares exist.
:::

<1>5. Starting from the pair $(E_1,u_1)$, define recursively
\[
E_{n+1}=E_n(u_{n+1}),
\qquad
u_{n+1}^2=u_n
\]
for $n\ge1$.

::: {.proof}
This is the same recursive construction as in Problem 3.3, now with base field $E_1\cong\mathbb F_{p^2}$ and initial nonsquare $u_1$.
:::

<1>6. Every extension in this recursive tail is quadratic:
\[
[E_{n+1}:E_n]=2
\qquad(n\ge1).
\]

::: {.proof}
Problem 3.3 applies verbatim to the finite field $E_1=\mathbb F_{p^2}$ because the exact power of $2$ dividing $|E_1^\times|=p^2-1$ is $2^{k'}$ with $k'\ge2$, by step <1>3, and $u_1$ is a nonsquare by step <1>4. Its conclusion is that every successive square-root adjunction has degree $2$.
:::

<1>7. Together with the first extension, this gives an infinite tower
\[
\mathbb F_p=E_0
\subset E_1
\subset E_2
\subset\cdots
\]
with
\[
\boxed{[E_{n+1}:E_n]=2\quad\text{for every }n\ge0.}
\]

::: {.proof}
Step <1>2 proves the degree statement for $E_1/E_0$, and step <1>6 proves it for every later stage.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>7 supplies the requested construction for the case $k=1$.
:::
:::
