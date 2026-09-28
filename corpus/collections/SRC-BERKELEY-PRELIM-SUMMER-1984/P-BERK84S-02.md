---
schema: qual/card@1
id: P-BERK84S-02
kind: problem
title: Irreducibility of a sparse integer polynomial
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 2 of the vendored Berkeley Preliminary Exam, Summer 1984.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified the translation by 7 and Eisenstein divisibility at the prime 7, including the constant term modulo 49.
---

::: {.problem}
Let Z be the ring of integers and $\mathbb { Z } [ x ]$ the polynomial ring over Z. Show that

$$
x ^ { 6 } + 5 3 9 x ^ { 5 } - 5 1 1 x + 8 4 7
$$

is irreducible in $\mathbb { Z } [ x ]$
:::


::: {.solution}
Let
\[
f(x)=x^6+539x^5-511x+847.
\]
Apply the change of variable $x\mapsto x-7$.

<1>1. The translated polynomial $f(x-7)$ is Eisenstein at $7$.
::: {.proof}
Expanding gives
\[
\begin{aligned}
f(x-7)={}&x^6+497x^5-18130x^4+257250x^3\\
&-1812755x^2+6369342x-8936900.
\end{aligned}
\]
Every non-leading coefficient is divisible by $7$:
\[
7\mid497,\quad
7\mid18130,\quad
7\mid257250,\quad
7\mid1812755,\quad
7\mid6369342,\quad
7\mid8936900.
\]
The leading coefficient is $1$, so it is not divisible by $7$. Moreover,
\[
-8936900\equiv14\pmod{49},
\]
so $49\nmid8936900$.
Therefore Eisenstein's criterion at the prime $7$ shows that $f(x-7)$ is irreducible in $\mathbb Q[x]$.
:::

<1>2. Hence $f(x)$ is irreducible in $\mathbb Z[x]$.
::: {.proof}
The substitution
\[
\tau:\mathbb Q[x]\longrightarrow\mathbb Q[x],
\qquad
\tau(g)(x)=g(x-7),
\]
is a ring automorphism, with inverse $g(x)\mapsto g(x+7)$. Thus $f$ is reducible in $\mathbb Q[x]$ if and only if $f(x-7)$ is reducible in $\mathbb Q[x]$. By <1>1, $f$ is therefore irreducible in $\mathbb Q[x]$.

Finally, $f$ is monic, hence primitive. Gauss's lemma then implies that irreducibility in $\mathbb Q[x]$ is equivalent to irreducibility in $\mathbb Z[x]$. Therefore
\[
\boxed{x^6+539x^5-511x+847\text{ is irreducible in }\mathbb Z[x].}
\]
:::
:::
