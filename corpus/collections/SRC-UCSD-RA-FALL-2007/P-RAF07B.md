---
schema: qual/card@1
id: P-RAF07B
kind: problem
title: "Semifinite measures and approximation by finite-measure subsets"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 2 of the official UCSD Fall 2007 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Recall that a measure $\mu$ is semifinite if for any $E \in \mathcal{M}$ with $\mu(E) = \infty$, there exists $F \in \mathcal{M}$ with $F \subset E$ and $0 < \mu(F) < \infty$.
Show that if $\mu$ is semifinite, then for any $E \in \mathcal{M}$,
$$
\mu(E) = \sup\{\mu(F) : F \in \mathcal{M},\; F \subset E,\; \mu(F) < \infty\}.
$$
:::


::: solution
<1>1. The finite-measure case is immediate.
::: proof
Set
\[
S_E:=\sup\{\mu(F):F\in\mathcal M,\ F\subset E,\ \mu(F)<\infty\}.
\]
Every admissible $F$ satisfies $\mu(F)\le\mu(E)$, so $S_E\le\mu(E)$. If $\mu(E)<\infty$, then $F=E$ is admissible, hence
\[
S_E\ge\mu(E).
\]
Thus $S_E=\mu(E)$ in this case.
:::

<1>2. Treat the case $\mu(E)=\infty$ by contradiction.
::: proof
Suppose $\mu(E)=\infty$ but $S_E<\infty$. Choose measurable sets $F_n\subset E$ with $\mu(F_n)<\infty$ and
\[
\mu(F_n)>S_E-\frac1n.
\]
Let
\[
G_n:=\bigcup_{k=1}^n F_k.
\]
Then $G_n\subset E$, $\mu(G_n)<\infty$, and $(G_n)$ is increasing. Since every $G_n$ is admissible,
\[
\mu(G_n)\le S_E.
\]
On the other hand $G_n\supset F_n$, so $\mu(G_n)>S_E-1/n$. Hence
\[
\mu(G_n)\longrightarrow S_E.
\]
With
\[
G:=\bigcup_{n=1}^\infty G_n,
\]
continuity from below gives
\[
\mu(G)=S_E<\infty.
\]
Therefore
\[
\mu(E\setminus G)=\infty,
\]
because otherwise
\[
\mu(E)=\mu(G)+\mu(E\setminus G)<\infty.
\]
By semifiniteness, there is a measurable $H\subset E\setminus G$ such that
\[
0<\mu(H)<\infty.
\]
Then $G\cup H\subset E$ and
\[
\mu(G\cup H)=\mu(G)+\mu(H)=S_E+\mu(H)>S_E,
\]
while $\mu(G\cup H)<\infty$. This contradicts the definition of $S_E$.

Thus $S_E=\infty=\mu(E)$. Combining both cases,
\[
\boxed{
\mu(E)=\sup\{\mu(F):F\subset E,\ F\in\mathcal M,\ \mu(F)<\infty\}.}
\]
:::
:::
