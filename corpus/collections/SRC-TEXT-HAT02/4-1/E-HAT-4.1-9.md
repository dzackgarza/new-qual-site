---
schema: qual/card@1
id: E-HAT-4.1-9
kind: problem
title: "Extending the long exact sequence to $\\pi_0$"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher Section 4.1 Exercise 9 and the 2021-06-02 correction; corrected i^* to i_* in the stored statement.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09

---

Suppose we define $\pi_0(X, A, x_0)$ to be the quotient set $\pi_0(X, x_0) / i_*\bigl(\pi_0(A, x_0)\bigr)$ so that the long exact sequence of homotopy groups for the pair $(X, A)$ extends to $\cdots \to \pi_0(A, x_0) \stackrel{\iota_*}{\longrightarrow} \pi_0(X, x_0) \to \pi_0(X, A, x_0) \to 0$.

(a) Show that with this extension, the five-lemma holds for the map of long exact sequences induced by a map $(X, A, x_0) \to (Y, B, y_0)$, in the following form: One of the maps between the two sequences is a bijection if the four surrounding maps are bijections for all choices of $x_0$.

(b) Show that the long exact sequence of a triple $(X, A, B, x_0)$ can be extended only to the term $\pi_0(A, B, x_0)$ in general, and that the five-lemma holds for this extension.

::: {.solution}
For a pointed pair \((X,A,x_0)\), define
\[
\pi_0(X,A,x_0)
=\pi_0(X,x_0)/i_*\pi_0(A,x_0),
\]
where all components of \(X\) meeting \(A\) are collapsed to the distinguished element. Then
\[
\pi_0(A,x_0)\longrightarrow\pi_0(X,x_0)
\longrightarrow\pi_0(X,A,x_0)\longrightarrow0
\]
is exact as a sequence of pointed sets: the components of \(X\) mapping to the distinguished relative class are exactly those meeting \(A\), and the quotient map is surjective.

### (a) Five-lemma

Consider a map of pairs and the induced map between the two extended exact sequences. In degrees \(\ge2\) this is the ordinary five-lemma for groups (abelian for degrees \(>2\)). The only issue is the low-degree pointed-set tail.

The same diagram chase works there once it is phrased in terms of fibers over the distinguished element. Exactness says that at each term the fiber of the next map over the distinguished element is exactly the image of the preceding map. To prove surjectivity of the middle vertical map, lift a target element one step to the left or right using a neighboring bijection, correct the resulting discrepancy inside the distinguished fiber using exactness and the next neighboring bijection, and then lift the correction through the other neighboring bijection. To prove injectivity, apply the same argument to the difference in the group terms, or, in the \(\pi_0\)-terms, choose representatives of the two components and rebase at those representatives so that the relevant component becomes distinguished; exactness again reduces equality to membership in the preceding image.

The hypothesis that the four surrounding maps are bijections **for all choices of basepoint** is exactly what permits this rebasing at arbitrary components in the \(\pi_0\)-tail. Thus the middle map is both injective and surjective. Hence the five-lemma remains valid for the extended pair sequence in Hatcher's stated form.

### (b) Triple sequence

For \(B\subset A\subset X\), the triple sequence extends to
\[
\cdots\longrightarrow
\pi_1(X,A,x_0)
\xrightarrow{\partial}
\pi_0(A,B,x_0).
\]
The boundary sends a relative path in \((X,A)\) beginning at \(x_0\in B\) to the relative component of its endpoint in \(A\). Exactness at this last term is interpreted in the same pointed-set sense as above, and the five-lemma proof is identical after allowing all choices of basepoint.

In general there is no exact continuation to \(\pi_0(X,B,x_0)\). Here is an explicit example. Let
\[
X=X_0\amalg X_1
\]
be the disjoint union of two intervals. Let \(x_0=b_0\in X_0\), and let
\[
B=\{b_0,b_1\}
\]
with \(b_1\in X_1\). Let \(A\) contain \(B\) and one further point \(a_1\in X_1\), chosen so that \(a_1\) is a different component of the subspace \(A\) from \(b_1\).

The class of \(a_1\) is nontrivial in
\[
\pi_0(A,B,x_0),
\]
since its component of \(A\) does not meet \(B\). But under the natural map to
\[
\pi_0(X,B,x_0)
\]
it goes to the distinguished element, because \(a_1\) and \(b_1\) lie in the same component \(X_1\) of \(X\), and every component of \(X\) meeting \(B\) is collapsed in \(\pi_0(X,B)\).

On the other hand this class cannot lie in the image of
\[
\partial:\pi_1(X,A,x_0)\to\pi_0(A,B,x_0),
\]
because no path in \(X\) joins \(x_0\in X_0\) to \(a_1\in X_1\). Thus exactness would fail at \(\pi_0(A,B,x_0)\) if one appended \(\pi_0(X,B,x_0)\).

Therefore the triple sequence can in general be extended only through the term \(\pi_0(A,B,x_0)\), and the all-basepoints five-lemma remains valid up to that terminal term.
:::
