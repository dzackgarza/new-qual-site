---
schema: qual/card@1
id: P-AGH2213QUASICOMPACT
kind: problem
title: Quasi-compactness of spectra and noetherian topological spaces
classification:
  areas:
  - algebraic-geometry
  topics:
  - Affine Schemes
  - Quasi-Compactness
  - Noetherian Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the collection's Hartshorne II.2.13 statement and source-order placement after II.2.12.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
A topological space is **quasi-compact** if every open cover has a finite subcover.

a. Show that a topological space is noetherian if and only if every open subset is quasi-compact.

b. If $X$ is an affine scheme, show that $\operatorname{sp}(X)$ is quasi-compact, but not in general noetherian.
We say a scheme $X$ is quasi-compact if $\operatorname{sp}(X)$ is.

c. If $A$ is a noetherian ring, show that $\operatorname{sp}(\Spec A)$ is a noetherian topological space.

d. Give an example to show that $\operatorname{sp}(\Spec A)$ can be noetherian even when $A$ is not.
:::

::: {.solution}

::: pf

::: {.pf-step #noetherian-implies-opens-quasicompact}
If a topological space $X$ is noetherian, then every open subset of $X$ is quasi-compact.

::: pf-proof
Let $U\subseteq X$ be open and suppose
\[
U=\bigcup_{\alpha\in A}U_\alpha
\]
is an open cover, with each $U_\alpha$ open in the subspace $U$.  Since $U$ itself is open in $X$, every $U_\alpha$ is open in $X$.

Suppose there is no finite subcover.  Choose $\alpha_1$.  Since $U_{\alpha_1}\ne U$, choose $\alpha_2$ such that
\[
U_{\alpha_2}\not\subseteq U_{\alpha_1}.
\]
Inductively, since no finite union covers $U$, choose $\alpha_{n+1}$ with
\[
U_{\alpha_{n+1}}
\not\subseteq
U_{\alpha_1}\cup\cdots\cup U_{\alpha_n}.
\]
Then
\[
U_{\alpha_1}
\subsetneq
U_{\alpha_1}\cup U_{\alpha_2}
\subsetneq
U_{\alpha_1}\cup U_{\alpha_2}\cup U_{\alpha_3}
\subsetneq\cdots
\]
is a strictly ascending chain of open subsets of $X$, contradicting noetherianity.  Hence a finite subcover exists.
:::

:::

::: {.pf-step #opens-quasicompact-implies-noetherian}
Conversely, if every open subset of $X$ is quasi-compact, then $X$ is noetherian.

::: pf-proof
Let
\[
U_1\subseteq U_2\subseteq U_3\subseteq\cdots
\]
be an ascending chain of open subsets and put
\[
U=\bigcup_{n\ge1}U_n.
\]
The set $U$ is open.  By hypothesis it is quasi-compact, and the family $\{U_n\}$ is an open cover of $U$.  Hence finitely many of the $U_n$ cover $U$.

Because the chain is nested, if $N$ is the largest index among that finite subcover, then
\[
U=U_N.
\]
Thus
\[
U_n=U_N
\]
for every $n\ge N$, so every ascending chain of opens stabilizes.  This is the noetherian condition.
:::

:::

::: {.pf-step #noetherian-iff-opens-quasicompact}
Therefore
\[
\boxed{
X\text{ is noetherian}
\iff
\text{every open subset of }X\text{ is quasi-compact}.
}
\]

::: pf-proof
Combine steps [](#noetherian-implies-opens-quasicompact){.pf-ref} and [](#opens-quasicompact-implies-noetherian){.pf-ref}.
:::

:::

::: {.pf-step #spec-a-is-quasicompact}
For every ring $A$, the affine spectrum
\[
X=\operatorname{Spec}A
\]
is quasi-compact.

::: pf-proof
Let
\[
X=\bigcup_{\alpha\in A_0}U_\alpha
\]
be an arbitrary open cover.  Distinguished opens form a basis, so refine this cover by distinguished opens
\[
X=\bigcup_{\lambda\in\Lambda}D(f_\lambda),
\]
with each $D(f_\lambda)$ contained in one of the original $U_\alpha$.

The equality of the union with all of $X$ means that no prime ideal contains every $f_\lambda$.  Equivalently,
\[
V((f_\lambda)_{\lambda\in\Lambda})=\varnothing.
\]
Hence
\[
\sqrt{(f_\lambda)_{\lambda\in\Lambda}}=A,
\]
so
\[
1\in(f_\lambda)_{\lambda\in\Lambda}.
\]
Membership in an ideal is a finite linear combination, so there exist finitely many indices
\[
\lambda_1,\ldots,\lambda_r
\]
and coefficients $a_i\in A$ such that
\[
1=\sum_{i=1}^ra_if_{\lambda_i}.
\]
No prime can contain all these finitely many $f_{\lambda_i}$, hence
\[
X=D(f_{\lambda_1})\cup\cdots\cup D(f_{\lambda_r}).
\]
Choosing the corresponding finitely many original cover members gives a finite subcover.
:::

:::

::: {.pf-step #spec-not-noetherian-example}
An affine spectrum need not be noetherian.  For example,
\[
A=k[x_1,x_2,x_3,\ldots]
\]
has non-noetherian spectrum.

::: pf-proof
Consider the ideals
\[
I_n=(x_1,\ldots,x_n).
\]
Then
\[
I_1\subsetneq I_2\subsetneq I_3\subsetneq\cdots.
\]
The corresponding closed subsets form a descending chain
\[
V(I_1)
\supseteq
V(I_2)
\supseteq
V(I_3)
\supseteq\cdots.
\]
This chain is strict.  Indeed, the prime ideal
\[
\mathfrak p_n=(x_1,\ldots,x_n)
\]
belongs to $V(I_n)$ but not to $V(I_{n+1})$, since
\[
x_{n+1}\notin\mathfrak p_n.
\]
Thus the descending chain of closed subsets does not stabilize, so $\operatorname{Spec}A$ is not noetherian.
:::

:::

::: {.pf-step #noetherian-a-gives-noetherian-spec}
If $A$ is a noetherian ring, then
\[
\operatorname{Spec}A
\]
is a noetherian topological space.

::: pf-proof
Let
\[
V(I_1)
\supseteq
V(I_2)
\supseteq
V(I_3)
\supseteq\cdots
\]
be a descending chain of closed subsets.  Since
\[
V(I)=V(\sqrt I),
\]
this corresponds to an ascending chain of radical ideals
\[
\sqrt{I_1}
\subseteq
\sqrt{I_2}
\subseteq
\sqrt{I_3}
\subseteq\cdots.
\]
Because $A$ is noetherian, every ascending chain of ideals stabilizes.  Hence the radical ideals stabilize and therefore the original closed subsets stabilize.  Thus the spectrum is noetherian.
:::

:::

::: {.pf-step #noetherian-spec-nonnoetherian-a-example}
The converse to step [](#noetherian-a-gives-noetherian-spec){.pf-ref} fails.  Let
\[
A
=
k[x_1,x_2,x_3,\ldots]
/(\,x_ix_j: i,j\ge1\,).
\]
Then $A$ is not noetherian, but
\[
\operatorname{Spec}A
\]
has one point and is therefore noetherian.

::: pf-proof
Let
\[
\mathfrak m=(\bar x_1,\bar x_2,\ldots)\subseteq A.
\]
By construction,
\[
\mathfrak m^2=0,
\]
and
\[
A/\mathfrak m\cong k.
\]
Thus $\mathfrak m$ is maximal.

Every element of $\mathfrak m$ is nilpotent, so every prime ideal of $A$ contains $\mathfrak m$.  Since $\mathfrak m$ is maximal, it is the unique prime ideal.  Hence
\[
\operatorname{Spec}A=\{\mathfrak m\},
\]
a one-point topological space, which is noetherian.

On the other hand, $\mathfrak m$ is not finitely generated as an ideal.  Because
\[
\mathfrak m^2=0,
\]
multiplication of a generator in $\mathfrak m$ by an arbitrary element of $A$ only scales it by the image of that element in
\[
A/\mathfrak m=k.
\]
Thus an ideal generated by finitely many elements of $\mathfrak m$ is merely their finite-dimensional $k$-linear span.  The vectors
\[
\bar x_1,\bar x_2,\ldots
\]
are linearly independent, so they cannot be generated by finitely many of them.  Hence $A$ is not noetherian.
:::

:::

::: pf-qed
Steps [](#noetherian-implies-opens-quasicompact){.pf-ref}, [](#opens-quasicompact-implies-noetherian){.pf-ref} and [](#noetherian-iff-opens-quasicompact){.pf-ref} prove part (a), steps [](#spec-a-is-quasicompact){.pf-ref} and [](#spec-not-noetherian-example){.pf-ref} prove part (b), step [](#noetherian-a-gives-noetherian-spec){.pf-ref} proves part (c), and step [](#noetherian-spec-nonnoetherian-a-example){.pf-ref} proves part (d).
:::

:::

:::
