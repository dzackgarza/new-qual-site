---
schema: qual/card@1
id: P-TOPOLOGY-PHD-F95-05
kind: problem
title: Compactness of the closed unit interval
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Euclidean Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: Checked the statement against Section I, problem 5 of the 23 September 1995 topology qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-06
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Proved compactness directly from the open-cover definition using the least
    upper bound property of the real numbers, without invoking Heine--Borel.
---

::: {.problem}
State the definition of compactness for topological spaces.
Prove from your definition that the closed unit interval $[0,1]$ is compact.
:::

::: {.solution}
A topological space $X$ is **compact** if every open cover of $X$ has a finite subcover.
Explicitly, whenever $\{U_\alpha\}_{\alpha\in I}$ is a family of open subsets of $X$ satisfying
\[
X=\bigcup_{\alpha\in I}U_\alpha,
\]
there are $\alpha_1,\ldots,\alpha_n\in I$ such that
\[
X=U_{\alpha_1}\cup\cdots\cup U_{\alpha_n}.
\]

We prove directly from this definition that $[0,1]$ is compact.

<1>1. Fix an arbitrary open cover $\mathcal U$ of $[0,1]$ and define
\[
S=\left\{x\in[0,1]:[0,x]\text{ is covered by finitely many members of }\mathcal U\right\}.
\]
Then $S$ is nonempty and bounded above.
::: {.proof}
Since $\mathcal U$ covers $[0,1]$, some $U_0\in\mathcal U$ contains $0$.
Thus the singleton interval
\[
[0,0]=\{0\}
\]
is covered by the one member $U_0$, so $0\in S$.
Hence $S\ne\varnothing$.
Also $S\subseteq[0,1]$, so $1$ is an upper bound for $S$.
:::

<1>2. Let
\[
s=\sup S.
\]
Then $s=1$.
::: {.proof}
The supremum exists by <1>1 and the least-upper-bound property of $\RR$.
Suppose for contradiction that $s<1$.
Because $\mathcal U$ covers $[0,1]$, choose $U\in\mathcal U$ with
\[
s\in U.
\]
Since $U$ is open in the subspace $[0,1]$, there is $\varepsilon>0$ such that
\[
(s-\varepsilon,s+\varepsilon)\cap[0,1]\subseteq U.
\]
Set
\[
\delta=\min\left\{\frac{\varepsilon}{2},\frac{1-s}{2}\right\}>0.
\]
By the definition of $s=\sup S$, there is $x\in S$ with
\[
x>s-\delta.
\]
Indeed, if no such $x$ existed, then $s-\delta<s$ would be an upper bound for $S$.

Because $x\in S$, finitely many members of $\mathcal U$ cover $[0,x]$.
Moreover,
\[
x>s-\delta\ge s-\frac{\varepsilon}{2}>s-\varepsilon
\]
and
\[
s+\delta\le s+\frac{\varepsilon}{2}<s+\varepsilon.
\]
Therefore $U$ contains the whole interval
\[
[x,s+\delta].
\]
Adding $U$ to the finite cover of $[0,x]$ gives a finite cover of
\[
[0,s+\delta].
\]
Thus $s+\delta\in S$.
But $s+\delta>s$, contradicting that $s$ is an upper bound for $S$.
Hence $s=1$.
:::

<1>3. The whole interval $[0,1]$ has a finite subcover from $\mathcal U$.
::: {.proof}
Choose $U_1\in\mathcal U$ with $1\in U_1$.
Since $U_1$ is open in $[0,1]$, there is $\varepsilon>0$ such that
\[
(1-\varepsilon,1]\subseteq U_1.
\]
By <1>2,
\[
\sup S=1.
\]
Hence there exists $x\in S$ with
\[
x>1-\varepsilon;
\]
otherwise $1-\varepsilon$ would be an upper bound for $S$ smaller than its supremum.
Because $x\in S$, there are finitely many members of $\mathcal U$ covering $[0,x]$.
Together with $U_1$, they cover
\[
[0,x]\cup(1-\varepsilon,1]=[0,1].
\]
Thus $\mathcal U$ has a finite subcover of $[0,1]$.
:::

<1>4. Therefore $[0,1]$ is compact.
::: {.proof}
The open cover $\mathcal U$ in <1>1 was arbitrary, and <1>3 produced a finite subcover.
This is exactly the definition of compactness.
Hence
\[
\boxed{[0,1]\text{ is compact}.}
\]
:::
:::
