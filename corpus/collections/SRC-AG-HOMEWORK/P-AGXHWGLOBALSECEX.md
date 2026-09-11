---
schema: qual/card@1
id: P-AGXHWGLOBALSECEX
kind: problem
title: Global sections is left exact but not exact, and the exponential sequence
classification:
  areas:
  - algebraic-geometry
  topics:
  - Sheaf Cohomology
  - Exact Sequences
  - Global Sections
relations: []
review: draft
---

::: problem
For any open $U \subseteq X$ show that the functor
\[
\Gamma\qty{U, {-}}: \Sh(X) \to \mathsf{Ab}\mathsf{Grp}
\]
is left exact, but need not be exact.
:::

::: solution
We are given exactness of
\[
\xi: 0 \to \mcf_1 \xrightarrow{f} \mcf_2 \xrightarrow{g} \mcf_3 \to 0
.\]
Applying $\Gamma(X; {-})$, we want to show exactness of
\[
\xi_X: 0 \to \mcf_1(X) \xrightarrow{f_X} \mcf_2(X) \xrightarrow{g_X} \mcf_3(X) \to \cdots
.\]

**Exactness at $\mcf_1(X)$**:

- Use that $f$ is a monomorphism $\iff \ker f = \mathbf 0$ as a sheaf, so
\[
(\ker f)(U) = (\mathbf 0)(U) = 0
.\]
- Use that
\[
(\ker f)(U) &\da \ker f_U \da \ker( \mcf_1(U) \xrightarrow{f_U} \mcf_2(U)) \\
\implies \ker f_X &= (\ker f)(X) = (\mathbf 0)(X) = 0
.\]
- Why this works: the kernel presheaf is already a sheaf, so we can use the presheaf assignment $(\ker f)(U) = \ker f_U$ directly.
  This does not work for the cokernel sheaf, since the image presheaf needs to be sheafified.

Alternatively, a direct argument that $f_X$ is injective.
A fact we need: $\xi$ is exact iff it is exact on stalks, so there are commutative squares for all $p\in X$.

- Write the kernel out:
\[
\ker f_X \da \ts{ s\in \mcf_1(X) \st f_X(s) = 0 \in \mcf_2(X)}
.\]

- Suppose $s\in \mcf_1(X)$ and $f_X(s) = 0$ in $\mcf_2(X)$. Then
\[
(\mcf_2 \mid^X_p \circ f_X )(s) &= \mcf_2\mid^X_p( 0) = 0 \in (\mcf_2)_p \quad\text{ring morphisms send $0$ to $0$}\\
\implies (f_p \circ \mcf_1 \mid^X_p)(s) &= (\mcf_2 \mid^X_p \circ f_X)(s) = 0 \quad\text{by commutativity} \\
\implies \mcf_1 \mid^X_p (s) &= 0 \quad\text{left-cancel $f_p$ since it is mono}
,\]
which holds for all $p$.

- Claim: by the sheaf condition on $\mcf_1$, $s= 0 \in \mcf_1(X)$.
  - Fix $p$. For $s\in \mcf_1(X)$, write a representative $\mcf_1\mid^X_p(s) = [U, \tilde s\in \mcf_1(U)]$.

  > Recall $(U_1, s_1) \sim (U_2, s_2) \in \mcf_p \iff$ they are both equivalent to $(W, t)$ where $W \subseteq U_1 \intersect U_2$ and
  > \[
  > \mcf_1 \mid^{U_1}_W (s_1) = t = \mcf_1\mid^{U_2}_W (s_2)
  > .\]

  - Then $s_p \da \mcf_1 \mid^X_p(s) = 0 \sim (W, 0) \in (\mcf_1)_p$ means there is some $W_p$ and a lift $\tilde s(p) = 0 \in \mcf_1(W_p)$ with $\mcf_1\mid^{W_p}_p(\tilde s(p)) = s_p$.
  - But this holds for all $p$, and $\ts{W_p}_{p\in X} \covers X$, so by the gluing axiom for $\mcf_1$ the sections $\ts{ \tilde s(p) \in \mcf_1(W_p) \st p\in X}$ glue to a unique $\tilde s\in \mcf_1(X)$; by uniqueness $\tilde s = s = 0 \in \mcf_1(X)$.

**Exactness at $\mcf_2(X)$**:

- We want $\ker g_X = \im f_X$. First show $\im f_X \subseteq \ker g_X$, and let $s \in \im f_X \subseteq \mcf_2(X)$.
- Push $s$ into $(\mcf_2)_p$ and pull back to $f_X^{-1}(s) \in \mcf_1(X)$; by commutativity the former lies in $\im f_p$, so
\[
\mcf_2\mid^X_p(s) \in \im f_p = \ker g_p
.\]
- Then push $s \xrightarrow{g_X} \ell$, so $\mcf_3 \mid^X_p(\ell) = 0$ by commutativity.
  Since this is true at all stalks, $\ell = 0\in \mcf_3(X)$, so $s \in \ker g_X$.

**A counterexample**:

The exponential short exact sequence, assembled from groups:
\[
0 \to \ZZ \to \GG_a(\CC) \xrightarrow{\exp: z\mapsto e^{2\pi i z}} \GG_m(\CC\units) \to 0 \in \Grp
,\]
which sheafifies over $X\da \CC\units$ to
\[
0 \to \underline{\ZZ} \to \Hol_X({-}) \xrightarrow{\exp} \Hol_X({-})\units \to 0 \in \Sh(X, \Grp)
.\]
Here $\Hol_X({-})\units$ denotes the multiplicatively invertible functions, i.e. the nonvanishing functions.

Applying $\Gamma(X; {-})$ gives
\[
0 \to \ZZ \to \Hol_X(X) \xrightarrow{\exp} \Hol_X(X)\units \to 0
.\]
If this bottom sequence were exact, then every invertible holomorphic function would have a logarithm on all of $\CC\units$, but the identity function does not.
:::
