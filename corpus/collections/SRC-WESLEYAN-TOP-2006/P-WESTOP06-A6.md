---
schema: qual/card@1
id: P-WESTOP06-A6
kind: problem
title: Maximal ideals and zero sets in rings of continuous functions
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: The retained extraction prints I(S)={f in C(X) | Z(f) contains X}, although the following sentences use S and its closure. It also literally asks, for compact X, that every ideal I equal I(S) for some closed S. Both points are source-sensitive and are not silently repaired.
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: The source defines I(S) by Z(f) containing X (a typo for S) and asks, for compact X, that every ideal of C(X) be I(S) for a closed S, which fails for the ideal (x) in C([0,1]). The statement now defines I(S) by Z(f) containing S and asks the converse for ideals closed in the supremum norm.
---

::: {.problem}
Recall the definition of a commutative ring with identity and of an ideal.

1. Use Zorn's Lemma to prove that every proper ideal is contained in a maximal ideal.
2. For a space $X$, let $C(X)$ be the ring of continuous real-valued functions and put
   \[
   Z(f)=\{x\in X:f(x)=0\}.
   \]
   For $S\subseteq X$, prove that
   \[
   I(S)=\{f\in C(X):Z(f)\supseteq S\}
   \]
   is an ideal in $C(X)$. Note that $I(\overline S)=I(S)$ and $S_1\subseteq S_2\Rightarrow I(S_1)\supseteq I(S_2)$.
3. Prove: for compact $X$, the converse holds for closed ideals: if $I$ is an ideal in $C(X)$ that is closed in the supremum norm, then $I=I(S)$ for some closed $S$.
4. Determine the maximal ideals in $C(X)$ when $X$ is compact.
:::

::: {.solution}

::: pf

::: pf-step

A commutative ring with identity is a commutative ring \(R\) with an element \(1\) satisfying \(1r=r\) for every \(r\in R\); an ideal \(I\subseteq R\) is an additive subgroup such that \(rI\subseteq I\) for every \(r\in R\).


::: pf-proof

These are the definitions used in the remaining steps.

:::

:::

::: {.pf-step #s1-2}

Every proper ideal \(J\) of a commutative ring \(R\) with identity is contained in a maximal ideal.


::: pf-proof

Let
\[
\mathcal P=\{I\subsetneq R:I\text{ is an ideal and }J\subseteq I\},
\]
ordered by inclusion. This poset is nonempty because \(J\in\mathcal P\). If \(\mathcal C\subseteq\mathcal P\) is a chain, then
\[
U=\bigcup_{I\in\mathcal C}I
\]
is an ideal containing \(J\): for two elements of \(U\), the chain condition puts both in one member of \(\mathcal C\), and closure under multiplication by elements of \(R\) is immediate. Moreover \(U\ne R\), since \(1\in U\) would put \(1\) in some \(I\in\mathcal C\), contradicting that \(I\) is proper. Thus every chain has an upper bound in \(\mathcal P\). By Zorn's lemma, \(\mathcal P\) has a maximal element \(M\). If \(M\subseteq I\subsetneq R\) for an ideal \(I\), then \(I\in\mathcal P\), so maximality in \(\mathcal P\) gives \(I=M\). Hence \(M\) is a maximal ideal of \(R\) containing \(J\).

:::

:::

::: {.pf-step #s1-4}

The set \(I(S)\) is an ideal,
\[
I(\overline S)=I(S),
\qquad
S_1\subseteq S_2\Longrightarrow
I(S_1)\supseteq I(S_2).
\]


::: pf-proof

If \(f,g\) vanish on \(S\), then \(f-g\) vanishes on \(S\), and if \(h\in C(X)\), then \(hf\) vanishes on \(S\). Thus \(I(S)\) is an ideal.

For every \(f\in C(X)\), the zero set \(Z(f)=f^{-1}(\{0\})\) is closed. Hence \(S\subseteq Z(f)\) if and only if \(\overline S\subseteq Z(f)\), proving the equality. Finally, if \(S_1\subseteq S_2\), every function vanishing on \(S_2\) also vanishes on \(S_1\), which gives the reversed inclusion.

:::

:::

::: {.pf-step #s1-5}

Let \(X\) be compact and let \(I\subseteq C(X)\) be an ideal closed in the supremum norm. Put
\[
S=\bigcap_{f\in I}Z(f).
\]
Then \(S\) is closed and \(I=I(S)\).


::: pf-proof

The set \(S\) is an intersection of closed sets, hence closed, and every \(f\in I\) vanishes on \(S\), so \(I\subseteq I(S)\).

Conversely, let \(g\in I(S)\) and \(\varepsilon>0\). The set
\[
K=\{x\in X:\abs{g(x)}\ge\varepsilon\}
\]
is closed in the compact space \(X\), hence compact, and \(K\cap S=\varnothing\) because \(g\) vanishes on \(S\). For each \(x\in K\) there is \(f_x\in I\) with \(f_x(x)\ne0\), so \(f_x^2>0\) on an open neighborhood of \(x\). Finitely many of these neighborhoods cover \(K\); let \(h\) be the sum of the corresponding \(f_{x_i}^2\). Then \(h\in I\), \(h\ge0\) on \(X\), and \(h>0\) on \(K\), so \(\delta=\min_K h>0\) when \(K\ne\varnothing\).

For \(n\ge1\), the function \(n/(1+nh)\) is continuous, so
\[
g_n=g\cdot\frac{nh}{1+nh}\in I.
\]
Moreover
\[
\abs{g-g_n}=\frac{\abs g}{1+nh}.
\]
On \(K\) this is at most \(\norm{g}_\infty/(1+n\delta)\), and off \(K\) it is less than \(\varepsilon\). Hence \(\norm{g-g_n}_\infty\le\varepsilon\) for all large \(n\). Since \(\varepsilon\) was arbitrary, \(g\) lies in the closure of \(I\), which is \(I\). Therefore \(I(S)\subseteq I\).

:::

:::

::: {.pf-step #s1-6}

If \(X\) is compact, then the maximal ideals of \(C(X)\) are exactly
\[
\boxed{M_x=\{f\in C(X):f(x)=0\},\qquad x\in X.}
\]


::: pf-proof

For each \(x\in X\), evaluation
\[
\operatorname{ev}_x:C(X)\longrightarrow\RR,
\qquad
f\longmapsto f(x),
\]
is a surjective ring homomorphism with kernel \(M_x\). Hence
\[
C(X)/M_x\cong\RR,
\]
so \(M_x\) is maximal.

Conversely, let \(M\) be a maximal ideal. The family of zero sets \(\{Z(f):f\in M\}\) has the finite-intersection property. Indeed, if \(f_1,\ldots,f_n\in M\) had
\[
\bigcap_{i=1}^n Z(f_i)=\varnothing,
\]
then
\[
g=f_1^2+\cdots+f_n^2\in M
\]
would have no zeros. Thus \(1/g\in C(X)\), so \(1=g(1/g)\in M\), contradicting that \(M\) is proper. Since \(X\) is compact, the full intersection
\[
\bigcap_{f\in M}Z(f)
\]
is nonempty. Choose \(x\) in it. Then every \(f\in M\) vanishes at \(x\), so \(M\subseteq M_x\). Because both \(M\) and \(M_x\) are maximal ideals, \(M=M_x\).

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} proves part \(1\); step [](#s1-4){.pf-ref} proves part \(2\); step [](#s1-5){.pf-ref} proves part \(3\); and step [](#s1-6){.pf-ref} gives the maximal ideals requested in part \(4\).

:::

:::

:::
