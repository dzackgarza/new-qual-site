---
schema: qual/card@1
id: P-ALGF20A
kind: problem
title: Normal $N$ with $\gcd(m,\varphi(n))=1$; cyclic implies abelian; counterexample
classification:
  areas:
  - algebra
  topics:
  - Group Theory
  - Normal Subgroups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked against Problem 1 of the official UCSD Algebra Qualifying Exam, Fall 2020 source; both parts and the gcd hypothesis agree with the source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified that conjugation factors through G/N and has trivial image, and that A4 with its normal Klein four subgroup satisfies the counterexample hypotheses.
---

::: problem
Suppose that $G$ is a finite group that has a normal subgroup $N$ with the following properties: the order of $N$ is $n$, $G/N$ is a cyclic group of order $m$, and $\gcd(m, \varphi(n)) = 1$ where $\varphi(n) := |\{ k \mid 1 \leq k \leq n,\; (k,n) = 1 \}|$.

(1) Prove that if $N$ is cyclic, then $G$ is abelian.

(2) Give an example where $N$ is abelian, but $G$ is not.
:::

::: {.solution}
<1>1. If $N$ is cyclic, then conjugation by $G$ acts trivially on $N$.
::: {.proof}
Because $N\trianglelefteq G$, conjugation defines a homomorphism
\[
c:G\longrightarrow \operatorname{Aut}(N).
\]
If $N$ is cyclic, then $N$ is abelian, so every element of $N$ centralizes $N$. Hence
\[
N\subseteq \ker c,
\]
and $c$ factors through a homomorphism
\[
\bar c:G/N\longrightarrow \operatorname{Aut}(N).
\]
Therefore the order of $\operatorname{im}\bar c$ divides both
\[
|G/N|=m
\]
and
\[
|\operatorname{Aut}(N)|=\varphi(n),
\]
since a cyclic group of order $n$ has exactly $\varphi(n)$ automorphisms. The hypothesis
\[
\gcd(m,\varphi(n))=1
\]
forces $|\operatorname{im}\bar c|=1$. Thus every element of $G$ centralizes $N$, i.e.
\[
N\subseteq Z(G).
\]
:::

<1>2. If $N$ is cyclic, then $G$ is abelian.
::: {.proof}
Choose $g\in G$ such that $gN$ generates the cyclic group $G/N$. Every element of $G$ has the form
\[
g^r a,
\qquad a\in N.
\]
By <1>1, $N\subseteq Z(G)$. Hence for $a,b\in N$,
\[
(g^r a)(g^s b)
=g^{r+s}ab
=g^{r+s}ba
=(g^s b)(g^r a).
\]
Thus every pair of elements of $G$ commutes, so $G$ is abelian. This proves part (1).
:::

<1>3. The pair
\[
G=A_4,
\qquad
N=\{1,(12)(34),(13)(24),(14)(23)\}
\]
is an example for part (2).
::: {.proof}
The subgroup $N$ is the Klein four group, so it is abelian of order
\[
n=4.
\]
Conjugation in $A_4$ permutes the three double transpositions, hence preserves $N$; therefore $N\trianglelefteq A_4$. Since
\[
|A_4/N|=3,
\]
the quotient is cyclic of order
\[
m=3.
\]
Moreover
\[
\varphi(n)=\varphi(4)=2,
\qquad
\gcd(3,2)=1.
\]
Finally, $A_4$ is nonabelian; for example
\[
(123)(124)\ne(124)(123).
\]
Thus all hypotheses are satisfied, $N$ is abelian, and $G$ is not abelian.
:::
:::
