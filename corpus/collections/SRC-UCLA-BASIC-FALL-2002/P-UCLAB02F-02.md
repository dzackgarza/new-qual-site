---
schema: qual/card@1
id: P-UCLAB02F-02
kind: problem
title: Least-upper-bound completeness implies Cauchy completeness of $\mathbb R$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 2 of the retained UCLA Basic Examination, Fall 2002 PDF.
---

::: {.problem}
Show why the least-upper-bound property of the real numbers -- every nonempty set bounded above has a least upper bound -- implies the Cauchy completeness property that every Cauchy sequence of real numbers converges.
:::

::: {.solution}
Let $(a_n)$ be a Cauchy sequence of real numbers.

<1>1. The sequence $(a_n)$ is bounded.

::: {.proof}
Choose $N$ such that
\[
|a_m-a_n|<1
\]
whenever $m,n\ge N$. Then for every $n\ge N$,
\[
|a_n|\le |a_N|+1.
\]
Together with the finitely many terms $a_1,\ldots,a_{N-1}$, this gives a global bound for the sequence.
:::

<1>2. For each $n$, the tail
\[
A_n=\{a_k:k\ge n\}
\]
has a least upper bound
\[
s_n=\sup A_n.
\]

::: {.proof}
Each tail $A_n$ is nonempty, and step <1>1 shows that it is bounded above. The least-upper-bound property therefore gives $s_n$.
:::

<1>3. The sequence $(s_n)$ is decreasing and bounded below.

::: {.proof}
Since
\[
A_{n+1}\subseteq A_n,
\]
one has
\[
s_{n+1}=\sup A_{n+1}\le \sup A_n=s_n.
\]
Also step <1>1 gives a lower bound $M$ for every $a_k$, hence for every nonempty tail $A_n$. Therefore $s_n\ge M$ for every $n$.
:::

<1>4. The set
\[
\{-s_n:n\in\mathbb N\}
\]
has a least upper bound, say $-L$.

::: {.proof}
By step <1>3, the sequence $(-s_n)$ is increasing. Since $(s_n)$ is bounded below, $(-s_n)$ is bounded above. Its set of values is nonempty, so the least-upper-bound property gives a real number
\[
-L=\sup\{-s_n:n\in\mathbb N\}.
\]
Equivalently,
\[
L=\inf\{s_n:n\in\mathbb N\}.
\]
:::

<1>5. For every $\varepsilon>0$, there exists $N$ such that for all $n\ge N$,
\[
a_n-\varepsilon<L\le a_n+\varepsilon.
\]

::: {.proof}
Fix $\varepsilon>0$. Since $(a_n)$ is Cauchy, choose $N$ such that
\[
|a_k-a_n|<\varepsilon
\]
whenever $k,n\ge N$.

Fix $n\ge N$. If $m\ge n$, then every element $a_k$ of $A_m$ has $k\ge m\ge n$, so
\[
a_n-\varepsilon<a_k<a_n+\varepsilon.
\]
Hence
\[
s_m=\sup A_m\le a_n+\varepsilon.
\]
Also $a_m\in A_m$ and $|a_m-a_n|<\varepsilon$, so
\[
s_m\ge a_m>a_n-\varepsilon.
\]
If $m<n$, then monotonicity from step <1>3 gives
\[
s_m\ge s_n\ge a_n>a_n-\varepsilon.
\]
Thus every $s_m$ is greater than $a_n-\varepsilon$, so their infimum satisfies
\[
L\ge a_n-\varepsilon.
\]
On the other hand, since $L\le s_n\le a_n+\varepsilon$,
\[
L\le a_n+\varepsilon.
\]
This proves the displayed inequalities.
:::

<1>6. The sequence $(a_n)$ converges to $L$.

::: {.proof}
Let $\varepsilon>0$. Apply step <1>5 with tolerance $\varepsilon/2$. For all sufficiently large $n$,
\[
a_n-\frac{\varepsilon}{2}<L\le a_n+\frac{\varepsilon}{2}.
\]
Hence
\[
|a_n-L|\le\frac{\varepsilon}{2}<\varepsilon.
\]
Therefore
\[
\boxed{a_n\to L}.
\]
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 proves that every Cauchy sequence of real numbers converges, using only the least-upper-bound property.
:::
:::
