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
---

::: {.problem}
Recall the definition of a commutative ring with identity and of an ideal.

1. Use Zorn's Lemma to prove that every proper ideal is contained in a maximal ideal.
2. For a space $X$, let $C(X)$ be the ring of continuous real-valued functions and put
   \[
   Z(f)=\{x\in X:f(x)=0\}.
   \]
   The retained extraction defines
   \[
   I(S)=\{f\in C(X):Z(f)\supseteq X\},
   \]
   while immediately asserting $I(\overline S)=I(S)$ and $S_1\subseteq S_2\Rightarrow I(S_1)\supseteq I(S_2)$. Prove the requested ideal assertions, retaining this notation gap as source-sensitive.
3. The retained source next asks: for compact $X$, prove the converse that if $I$ is an ideal in $C(X)$, then $I=I(S)$ for some closed $S$. Record and address the statement as printed.
4. Determine the maximal ideals in $C(X)$ when $X$ is compact.
:::

For the intended vanishing ideal, write
\[
I_{\mathrm{van}}(S)=\{f\in C(X):Z(f)\supseteq S\}.
\]

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

::: {.pf-step #s1-3}

With the retained literal definition
\[
I(S)=\{f\in C(X):Z(f)\supseteq X\},
\]
one has \(I(S)=\{0\}\) for every \(S\subseteq X\); consequently \(I(\overline S)=I(S)\) and \(S_1\subseteq S_2\Rightarrow I(S_1)\supseteq I(S_2)\) hold trivially.


::: pf-proof

The condition \(Z(f)\supseteq X\) means exactly that \(f(x)=0\) for every \(x\in X\), hence \(f=0\). Therefore the displayed set is the zero ideal and is independent of \(S\). The two asserted relations follow because both sides are always \(\{0\}\).

:::

:::

::: {.pf-step #s1-4}

For the intended definition \(I_{\mathrm{van}}(S)\), the set \(I_{\mathrm{van}}(S)\) is an ideal,
\[
I_{\mathrm{van}}(\overline S)=I_{\mathrm{van}}(S),
\qquad
S_1\subseteq S_2\Longrightarrow
I_{\mathrm{van}}(S_1)\supseteq I_{\mathrm{van}}(S_2).
\]


::: pf-proof

If \(f,g\) vanish on \(S\), then \(f-g\) vanishes on \(S\), and if \(h\in C(X)\), then \(hf\) vanishes on \(S\). Thus \(I_{\mathrm{van}}(S)\) is an ideal.

For every \(f\in C(X)\), the zero set \(Z(f)=f^{-1}(\{0\})\) is closed. Hence \(S\subseteq Z(f)\) if and only if \(\overline S\subseteq Z(f)\), proving the equality. Finally, if \(S_1\subseteq S_2\), every function vanishing on \(S_2\) also vanishes on \(S_1\), which gives the reversed inclusion.

:::

:::

::: {.pf-step #s1-5}

The converse in part \(3\) is false as printed, and it remains false after replacing the retained \(X\) by the intended \(S\).


::: pf-proof

With the literal definition, every \(I(S)\) is \(\{0\}\), so any nonzero proper ideal is already a counterexample.

For the intended definition, take \(X=[0,1]\) and let
\[
J=(x)=\{xg(x):g\in C([0,1])\},
\]
where \(x\) denotes the identity function. Suppose \(J=I_{\mathrm{van}}(S)\) for some closed \(S\subseteq[0,1]\). Since \(x\in J\), every point of \(S\) must lie in \(Z(x)=\{0\}\), so \(S\) is either \(\varnothing\) or \(\{0\}\). If \(S=\varnothing\), then \(I_{\mathrm{van}}(S)=C([0,1])\), but \(J\) is proper because every element of \(J\) vanishes at \(0\). If \(S=\{0\}\), then \(\sqrt{x}\in I_{\mathrm{van}}(\{0\})\), while \(\sqrt{x}\notin J\): an equality \(\sqrt{x}=xg(x)\) would force \(g(x)=1/\sqrt{x}\) for \(x>0\), which cannot extend continuously to \(0\). Thus no such closed \(S\) exists.

:::

:::

::: {.pf-step #s1-6}

If \(X\) is compact Hausdorff, then the maximal ideals of \(C(X)\) are exactly
\[
\boxed{M_x=\{f\in C(X):f(x)=0\},\qquad x\in X.}
\]


::: pf-proof

For each \(x\in X\), evaluation
\[
\operatorname{ev}_x:C(X)\longrightarrow\mathbb R,
\qquad
f\longmapsto f(x),
\]
is a surjective ring homomorphism with kernel \(M_x\). Hence
\[
C(X)/M_x\cong\mathbb R,
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

Step [](#s1-2){.pf-ref} proves part \(1\); steps [](#s1-3){.pf-ref} and [](#s1-4){.pf-ref} address the literal and intended readings of part \(2\); step [](#s1-5){.pf-ref} resolves the false converse in part \(3\); and step [](#s1-6){.pf-ref} gives the maximal ideals requested in part \(4\).

:::

:::
