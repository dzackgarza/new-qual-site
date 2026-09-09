---
schema: qual/card@1
id: P-HCAO23
kind: problem
title: Integral closure of a one-dimensional Noetherian domain is Noetherian
classification:
  areas:
  - algebra
  topics:
  - Integral Closure
  - Noetherian Rings
  - Dedekind Domains
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard Commutative Algebra oral-question extraction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Let $R$ be a one-dimensional Noetherian domain, and let $\widetilde R$ be its integral closure.
Prove that $\widetilde R$ is Noetherian.
:::

::: solution
Let
\[
K=\operatorname{Frac}(R),
\qquad
A=\widetilde R\subseteq K.
\]
We prove the special case of the Krull--Akizuki argument needed here.

<1>1. Let $M\subseteq K$ be any $R$-submodule and let $0\ne x\in R$.
Then $M/xM$ has finite length as an $R$-module.
::: proof
First suppose that $(R,\mathfrak m)$ is local. Put
\[
\ell=\operatorname{length}_R(R/xR).
\]
This is finite because $R/xR$ is a zero-dimensional Noetherian ring.

We claim that every nonzero finitely generated $R$-submodule
$N\subseteq K$ satisfies
\[
\operatorname{length}_R(N/xN)=\ell.
\]
Multiplying $N$ by a nonzero element of $K$ does not change this quotient up to
isomorphism, so we may assume
\[
0\ne N\subseteq R.
\]
Choose $0\ne d\in N$. If $d$ is not a unit, then in a one-dimensional local
domain the only prime containing $(d)$ is $\mathfrak m$, hence
\[
\sqrt{(d)}=\mathfrak m.
\]
Since $x\in\mathfrak m$ whenever $x$ is a nonunit, some power $x^c$ lies in
$(d)\subseteq N$; if $x$ or $d$ is a unit, the same containment holds with an
obvious choice of $c$. Thus for some $c\ge0$,
\[
x^cR\subseteq N\subseteq R.
\]

For every $n\ge1$, multiplication by powers of the nonzero element $x$ gives
isomorphisms between the successive quotients in
\[
N\supset xN\supset\cdots\supset x^nN,
\]
so
\[
\operatorname{length}_R(N/x^nN)
=n\operatorname{length}_R(N/xN).
\]
Similarly,
\[
\operatorname{length}_R(R/x^nR)=n\ell.
\]
From
\[
x^{n+c}R\subseteq x^nN\subseteq x^nR
\]
and $x^cR\subseteq N\subseteq R$, for $n\ge c$ we obtain
\[
(n-c)\ell
\le
n\operatorname{length}_R(N/xN)
\le
(n+c)\ell.
\]
Dividing by $n$ and taking arbitrarily large $n$ forces
\[
\operatorname{length}_R(N/xN)=\ell.
\]

Now return to an arbitrary $R$-submodule $M\subseteq K$. If $M/xM$ contained
a finite-length submodule of length greater than $\ell$, choose finitely many
elements of $M$ whose images generate such a submodule and let $N$ be the
finitely generated $R$-submodule they span. The image of $N/xN$ in $M/xM$
would then have length greater than $\ell$, contradicting the preceding
calculation. Hence every chain of submodules of $M/xM$ has length at most
$\ell$, so $M/xM$ has finite length.

For general $R$, the nonzero element $x$ is contained in only finitely many
maximal ideals $\mathfrak m_1,\ldots,\mathfrak m_s$, because the Noetherian
zero-dimensional ring $R/xR$ is Artinian. As an $R/xR$-module,
$M/xM$ decomposes into its localizations at these finitely many maximal ideals.
The local argument applied to each
\[
M_{\mathfrak m_i}\subseteq K
\]
shows that every summand has finite length. Therefore $M/xM$ has finite length
over $R$.
:::

<1>2. Every nonzero ideal $I\subseteq A$ contains a nonzero element of $R$.
::: proof
Choose $0\ne y\in I$. Since $y\in K$, write
\[
y=\frac ab
\]
with $0\ne a,b\in R$. Then
\[
a=by\in I
\]
because $b\in R\subseteq A$. Thus
\[
0\ne a\in I\cap R.
\]
:::

<1>3. Every ideal of $A$ is finitely generated.
::: proof
The zero ideal is finitely generated, so let $0\ne I\subseteq A$. By <1>2,
choose $0\ne x\in I\cap R$. Apply <1>1 to the $R$-submodule
\[
A\subseteq K.
\]
Then $A/xA$ has finite length over $R$. Hence its submodule
\[
I/xA\subseteq A/xA
\]
is finitely generated as an $R$-module. Choose
\[
y_1,\ldots,y_n\in I
\]
whose classes generate $I/xA$ over $R$.

For any $y\in I$, there exist $r_i\in R$ such that
\[
y-\sum_i r_i y_i\in xA.
\]
Thus
\[
y\in Ay_1+\cdots+Ay_n+Ax.
\]
Therefore
\[
I=(x,y_1,\ldots,y_n)
\]
as an ideal of $A$.
:::

<1>4. Hence $\widetilde R=A$ is Noetherian.
::: proof
A ring is Noetherian if and only if every ideal is finitely generated. This is
exactly <1>3.
:::
:::
