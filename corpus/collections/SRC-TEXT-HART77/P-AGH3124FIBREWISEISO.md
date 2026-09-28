---
schema: qual/card@1
id: P-AGH3124FIBREWISEISO
kind: problem
title: Fibrewise isomorphic invertible sheaves differ by a pullback
classification:
  areas:
  - algebraic-geometry
  topics:
  - Semicontinuity
  - Invertible Sheaves
  - Flat Morphisms
  - Picard Group
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Exercise III.12.4 and its Corollary III.12.9 hint. The proof uses constancy of
    fibrewise h^0 for F=L tensor M^{-1}, cohomology and base change to identify f_*F
    as a line bundle, and the fibrewise evaluation map to recover F as its pullback.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
Let $Y$ be an integral scheme of finite type over an algebraically closed field $k$.
Let $f: X \to Y$ be a flat projective morphism whose fibres are all integral schemes.
Let $\mcl, \mcm$ be invertible sheaves on $X$, and assume for each $y \in Y$ that $\mcl_y \cong \mcm_y$ on the fibre $X_y$.

Show that there is an invertible sheaf $\mcn$ on $Y$ such that $\mcl \cong \mcm \tensor f^* \mcn$.

Hint: use the results of this section to show that $f_*(\mcl \tensor \mcm^{-1})$ is locally free of rank $1$ on $Y$.
:::

::: {.solution}
Put
$$
\mcf=\mcl\tensor\mcm^{-1}.
$$
Then \(\mcf\) is invertible on \(X\), and the hypothesis says
$$
\mcf_y\cong\mco_{X_y}
$$
for every \(y\in Y\).

<1>1. The sheaf \(\mcf\) is flat over \(Y\), and
$$
h^0(X_y,\mcf_y)=1
$$
for every \(y\in Y\).

::: {.proof}
Since \(f\) is flat, \(\mco_X\) is flat over \(Y\). Locally on \(X\), the
invertible sheaf \(\mcf\) is isomorphic to \(\mco_X\), so \(\mcf\) is also
flat over \(Y\).

For every closed point \(y\in Y\), the residue field is \(k\), because
\(Y\) is of finite type over the algebraically closed field \(k\). The
fibre \(X_y\) is integral and projective over \(k\), hence
$$
H^0(X_y,\mco_{X_y})=k.
$$
Thus
$$
h^0(X_y,\mcf_y)=1
$$
at every closed point.

By [[T-COHBC|semicontinuity]], the locus where
$$
h^0(X_y,\mcf_y)\ge2
$$
is closed. If it were nonempty, then, since a finite-type \(k\)-scheme is
Jacobson, it would contain a closed point, contrary to the preceding
paragraph. On the other hand constants give
$$
h^0(X_y,\mco_{X_y})\ge1
$$
for every fibre, and \(\mcf_y\cong\mco_{X_y}\). Hence
$$
h^0(X_y,\mcf_y)=1
$$
for all \(y\in Y\).
:::

<1>2. The sheaf
$$
\mcn=f_*\mcf
$$
is invertible on \(Y\), and formation of \(f_*\mcf\) commutes with every
residue-field base change:
$$
\mcn\tensor\kappa(y)
\xrightarrow{\sim}
H^0(X_y,\mcf_y).
$$

::: {.proof}
The base \(Y\) is integral, hence reduced. By step <1>1, \(\mcf\) is
coherent and flat over \(Y\), and the function
$$
y\longmapsto h^0(X_y,\mcf_y)
$$
is constantly \(1\). The Grauert/base-change statement in
[[T-COHBC|cohomology and base change]] therefore gives that
$$
f_*\mcf
$$
is locally free of rank \(1\), with the displayed base-change
isomorphism. A locally free sheaf of rank \(1\) is invertible, so
\(\mcn=f_*\mcf\) is the required line bundle candidate on \(Y\).
:::

<1>3. The canonical evaluation morphism
$$
\epsilon:f^*\mcn=f^*f_*\mcf\longrightarrow\mcf
$$
restricts to an isomorphism on every fibre \(X_y\).

::: {.proof}
By the base-change isomorphism of step <1>2, the restriction of
\(\epsilon\) to \(X_y\) is the ordinary evaluation map
$$
H^0(X_y,\mcf_y)\tensor_{\kappa(y)}\mco_{X_y}
\longrightarrow
\mcf_y.
$$
Choose an isomorphism
$$
\mcf_y\cong\mco_{X_y}.
$$
Step <1>1 gives
$$
H^0(X_y,\mcf_y)\cong\kappa(y),
$$
and under this identification the evaluation map is
$$
\kappa(y)\tensor_{\kappa(y)}\mco_{X_y}
\longrightarrow
\mco_{X_y},
\qquad
a\tensor s\longmapsto as,
$$
which is an isomorphism.
:::

<1>4. The evaluation morphism
$$
\epsilon:f^*\mcn\longrightarrow\mcf
$$
is an isomorphism on \(X\).

::: {.proof}
Let
$$
\mcc=\operatorname{coker}(\epsilon).
$$
This is coherent. Fix \(x\in X\), put \(y=f(x)\), and take the stalk at
\(x\). By step <1>3, tensoring the stalk sequence with \(\kappa(y)\)
kills the cokernel:
$$
\mcc_x/\mfm_y\mcc_x=0,
$$
where \(\mfm_y\mco_{X,x}\subseteq\mfm_x\). Nakayama's lemma therefore
gives
$$
\mcc_x=0.
$$
Since this holds for every \(x\), the map \(\epsilon\) is surjective.

Both its source and target are invertible sheaves. Locally at \(x\),
\(\epsilon_x\) is therefore a surjective endomorphism between free
rank-one \(\mco_{X,x}\)-modules. It is multiplication by a generator of
the unit ideal, hence by a unit. Thus \(\epsilon_x\) is an isomorphism
for every \(x\), so \(\epsilon\) is an isomorphism globally.
:::

<1>5. There is an invertible sheaf \(\mcn\) on \(Y\) such that
$$
\mcl\cong\mcm\tensor f^*\mcn.
$$

::: {.proof}
By step <1>4,
$$
\mcl\tensor\mcm^{-1}
=\mcf
\cong
f^*\mcn.
$$
Tensoring by \(\mcm\) gives
$$
\boxed{\mcl\cong\mcm\tensor f^*\mcn}.
$$
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required conclusion.
:::
:::
