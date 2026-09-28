---
schema: qual/card@1
id: P-AGAFFINEH1
kind: problem
title: Vanishing of $H^1$ on coherent ideal sheaves forces affineness
classification:
  areas:
  - algebraic-geometry
  topics:
  - Serre Criterion
  - Cohomology
  - Affine Schemes
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the Harvard sample qualifying-exam algebraic-geometry PDF; the source asks for this vanishing criterion, weakening Noetherianity, and a non-quasicompact counterexample.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
Prove that if $X$ is a Noetherian scheme with $H^1(X, \mathcal{I}) = 0$ for every coherent sheaf of ideals $\mathcal{I}$, then $X$ is affine.

Can the Noetherian hypothesis be weakened?
Give an example showing the statement fails without quasicompactness.
:::

::: {.solution}
Assume first that $X$ is Noetherian and that
\[
H^1(X,\mathcal I)=0
\]
for every coherent ideal sheaf $\mathcal I\subseteq\mathcal O_X$.

<1>1. Every closed point $x\in X$ has an affine neighborhood of the form
\[
X_f=\{p\in X:f_p\in\mathcal O_{X,p}^{\times}\}
\]
for some global function $f\in\Gamma(X,\mathcal O_X)$.
::: {.proof}
Choose an affine open neighborhood
\[
U=\operatorname{Spec}A
\]
of $x$, and let $\mathfrak m\subset A$ be the maximal ideal corresponding to $x$.
Put
\[
Z=X\setminus U,
\qquad
Z'=Z\cup\{x\}.
\]
Because $X$ is Noetherian, the reduced closed subschemes with underlying spaces $Z$ and $Z'$ are cut out by coherent ideal sheaves
\[
\mathcal I'\subseteq\mathcal I\subseteq\mathcal O_X,
\]
where $\mathcal I$ cuts out $Z$ and $\mathcal I'$ cuts out $Z'$.

On $U$, one has
\[
\mathcal I|_U=\mathcal O_U,
\qquad
\mathcal I'|_U=\widetilde{\mathfrak m}.
\]
Hence $\mathcal I/\mathcal I'$ is supported at $x$ and
\[
\Gamma(X,\mathcal I/\mathcal I')\cong A/\mathfrak m.
\]
From
\[
0\longrightarrow\mathcal I'
\longrightarrow\mathcal I
\longrightarrow\mathcal I/\mathcal I'
\longrightarrow0
\]
and $H^1(X,\mathcal I')=0$, the map
\[
\Gamma(X,\mathcal I)
\longrightarrow
\Gamma(X,\mathcal I/\mathcal I')
\]
is surjective.  Choose $f\in\Gamma(X,\mathcal I)$ mapping to
\[
1\in A/\mathfrak m.
\]
Then $f_x$ is a unit, so $x\in X_f$.  On the other hand, $f$ lies in the ideal cutting out $Z$, so it cannot be a unit at any point of $Z$.  Thus
\[
x\in X_f\subseteq U.
\]
Inside the affine scheme $U=\operatorname{Spec}A$, this open set is the distinguished open
\[
X_f=D(f|_U),
\]
and is therefore affine.
:::

<1>2. Finitely many affine principal opens
\[
X_{f_1},\ldots,X_{f_n}
\]
of the form constructed in <1>1 cover $X$.
::: {.proof}
Let $W$ be the union of all affine opens $X_f$ obtained from global functions.  By <1>1, every closed point of $X$ belongs to $W$.

If $X\setminus W$ were nonempty, it would be a nonempty closed subset of the Noetherian space $X$, hence would contain a closed point.  That contradicts the preceding sentence.  Therefore
\[
W=X.
\]
Since a Noetherian scheme is quasi-compact, finitely many of these opens cover $X$.
:::

<1>3. The functions $f_1,\ldots,f_n$ from <1>2 generate the unit ideal in
\[
A=\Gamma(X,\mathcal O_X).
\]
::: {.proof}
Consider the sheaf map
\[
\Phi:\mathcal O_X^{\oplus n}\longrightarrow\mathcal O_X,
\qquad
(a_1,\ldots,a_n)\longmapsto\sum_{i=1}^n a_i f_i.
\]
At every point $p\in X$, some $f_i$ is a unit in $\mathcal O_{X,p}$ because the opens $X_{f_i}$ cover $X$.  Hence $\Phi$ is surjective.  Let
\[
\mathcal F=\ker\Phi.
\]

For $0\le i\le n$, let $\mathcal F_i$ be the intersection of $\mathcal F$ with the first $i$ summands of $\mathcal O_X^{\oplus n}$.  Then
\[
0=\mathcal F_0\subseteq\mathcal F_1\subseteq\cdots\subseteq\mathcal F_n=\mathcal F,
\]
and projection to the $i$th coordinate identifies
\[
\mathcal F_i/\mathcal F_{i-1}
\]
with a coherent ideal sheaf of $\mathcal O_X$.  The hypothesis therefore gives
\[
H^1(X,\mathcal F_i/\mathcal F_{i-1})=0
\]
for every $i$.  The long exact cohomology sequences for
\[
0\to\mathcal F_{i-1}\to\mathcal F_i
\to\mathcal F_i/\mathcal F_{i-1}\to0
\]
inductively give
\[
H^1(X,\mathcal F)=0.
\]

Taking global sections of
\[
0\to\mathcal F\to\mathcal O_X^{\oplus n}
\xrightarrow{\Phi}\mathcal O_X\to0
\]
now shows that
\[
A^{\oplus n}\longrightarrow A,
\qquad
(a_i)\longmapsto\sum_i a_i f_i
\]
is surjective.  In particular there are $a_i\in A$ with
\[
\sum_i a_i f_i=1.
\]
Thus the $f_i$ generate the unit ideal.
:::

<1>4. The scheme $X$ is affine.
::: {.proof}
Put
\[
A=\Gamma(X,\mathcal O_X).
\]
Since $X$ is Noetherian, it is quasi-compact and quasi-separated.  For every global function $f$, restriction therefore identifies
\[
A_f\cong\Gamma(X_f,\mathcal O_X).
\]
Consequently, when $X_f$ is affine, the canonical morphism
\[
\eta:X\longrightarrow\operatorname{Spec}A
\]
restricts to an isomorphism
\[
X_f\xrightarrow{\sim}D(f).
\]

By <1>2, the opens $X_{f_i}$ cover $X$.  By <1>3, the $f_i$ generate the unit ideal in $A$, so the distinguished opens $D(f_i)$ cover $\operatorname{Spec}A$.  Thus $\eta$ is an isomorphism on open covers of both source and target, and therefore is an isomorphism globally.  Hence
\[
X\cong\operatorname{Spec}A
\]
is affine.
:::

<1>5. The Noetherian hypothesis can be weakened as follows: it is enough that $X$ be quasi-compact and quasi-separated and that
\[
H^1(X,\mathcal I)=0
\]
for every finite-type quasi-coherent ideal sheaf $\mathcal I\subseteq\mathcal O_X$.
::: {.proof}
Every quasi-coherent ideal sheaf is a filtered colimit of its finite-type quasi-coherent ideal subsheaves.  On a quasi-compact quasi-separated scheme, cohomology of quasi-coherent sheaves commutes with filtered colimits.  Hence the stated hypothesis implies
\[
H^1(X,\mathcal J)=0
\]
for every quasi-coherent ideal sheaf $\mathcal J$.

The affineness argument of <1>1--<1>4 then applies in the general quasi-coherent form.  In particular, if one wants to retain the literal hypothesis involving coherent ideals, Noetherian may be replaced by the assumption that $X$ is quasi-compact, quasi-separated, and coherent, so that every finite-type quasi-coherent ideal is coherent.
:::

<1>6. Quasi-compactness cannot be omitted.
::: {.proof}
Let
\[
X=\coprod_{n\ge1}\operatorname{Spec}k
\]
be an infinite disjoint union of points over a field $k$.  For every quasi-coherent sheaf $\mathcal F$,
\[
H^i(X,\mathcal F)
\cong
\prod_{n\ge1}
H^i(\operatorname{Spec}k,\mathcal F|_{\operatorname{Spec}k})
=0
\qquad(i>0).
\]
Thus in particular $H^1(X,\mathcal I)=0$ for every coherent ideal sheaf $\mathcal I$.

But $X$ is not quasi-compact, whereas every affine scheme is quasi-compact.  Hence $X$ is not affine.  This gives the required counterexample.
:::

<1>7. Q.E.D.
::: {.proof}
Step <1>4 proves the Noetherian statement, step <1>5 gives the weakening, and step <1>6 shows that quasi-compactness cannot be omitted.
:::
:::
