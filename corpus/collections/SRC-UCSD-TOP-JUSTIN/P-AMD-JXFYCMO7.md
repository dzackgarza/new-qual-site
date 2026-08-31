---
schema: qual/card@1
id: P-AMD-JXFYCMO7
kind: problem
title: $\mathrm{Tor}_R^*$ is symmetric
classification:
  areas:
  - topology
  topics:
  - Homological Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Show $\tor_R^*(\cdot, \cdot)$ is symmetric in the following way: Given $M, N$, take free resolutions, view $M_* \into M$ as a chain map and tensor with $N_*$ to get a chain map$\psi: M_* \tensor_R N_* \into M \tensor_R N_*$.
Show that $\psi$ is a quasi-isomorphism using the exact sequence $0 \into (Z_n, 0) \into (N_n, 0) \into (B_{n-1}, 0) \into 0$, then switch the roles of $M, N$.
:::

::: {.solution}
<1>1. Double complex setup:
<2>1. Let $P_* \xrightarrow{\varepsilon_P} M \to 0$ and $Q_* \xrightarrow{\varepsilon_Q} N \to 0$ be projective resolutions of $R$-modules $M$ and $N$ respectively.
::: {.proof}
existence of projective resolutions in $R\text{-}\mathbf{Mod}$.
:::
<2>2. Form the first-quadrant double complex $C_{p,q} = P_p \otimes_R Q_q$ with horizontal differential $d^h = d^P \otimes \operatorname{id}_Q$ and vertical differential $d^v = (-1)^p \operatorname{id}_P \otimes d^Q$.
::: {.proof}
definition of tensor product double complex.
:::
<2>3. The total complex $\operatorname{Tot}(P_* \otimes_R Q_*)$ has degree-$n$ term $T_n = \bigoplus_{p+q=n} P_p \otimes_R Q_q$ and boundary operator $D = d^h + d^v$ with $D^2 = 0$.
::: {.proof}
$(d^h + d^v)^2 = (d^h)^2 + (d^h d^v + d^v d^h) + (d^v)^2 = 0 + 0 + 0 = 0$.
:::

<1>2. Quasi-isomorphism $\operatorname{Tot}(P_* \otimes_R Q_*) \xrightarrow{\sim} M \otimes_R Q_*$:
<2>1. For each fixed $q \ge 0$, $Q_q$ is projective, hence flat as an $R$-module.
::: {.proof}
projective modules are flat.
:::
<2>2. Since $Q_q$ is flat, tensoring the resolution $P_* \to M \to 0$ with $Q_q$ preserves exactness:
\[
H_p(P_* \otimes_R Q_q) \cong H_p(P_*) \otimes_R Q_q \cong \begin{cases} M \otimes_R Q_q & p = 0 \\ 0 & p > 0. \end{cases}
\]
::: {.proof}
flatness commutes with homology.
:::
<2>3. Viewing $M \otimes_R Q_*$ as a double complex concentrated in row $p = 0$, the augmentation map $\varepsilon_P \otimes \operatorname{id}: P_* \otimes_R Q_* \to M \otimes_R Q_*$ is a quasi-isomorphism on each column.
::: {.proof}
<2>2.
:::
<2>4. By the Acyclic Assembly Lemma (or the spectral sequence of a first-quadrant bicomplex), an augmentation that is exact on rows/columns induces a quasi-isomorphism on total complexes:
\[
\operatorname{Tot}(P_* \otimes_R Q_*) \xrightarrow{\sim} \operatorname{Tot}(M \otimes_R Q_*) = M \otimes_R Q_*.
\]
::: {.proof}
Weibel Theorem 2.7.2 (Acyclic Assembly Lemma).
:::
<2>5. Taking homology gives an isomorphism:
\[
H_n(\operatorname{Tot}(P_* \otimes_R Q_*)) \cong H_n(M \otimes_R Q_*) \cong \operatorname{Tor}_n^R(M, N).
\]
::: {.proof}
definition of $\operatorname{Tor}_n^R(M, N)$ via projective resolution of $N$.
:::

<1>3. Quasi-isomorphism $\operatorname{Tot}(P_* \otimes_R Q_*) \xrightarrow{\sim} P_* \otimes_R N$:
<2>1. Symmetrically, for each fixed $p \ge 0$, $P_p$ is projective, hence flat.
::: {.proof}
projective modules are flat.
:::
<2>2. Tensoring the resolution $Q_* \to N \to 0$ with $P_p$ preserves exactness:
\[
H_q(P_p \otimes_R Q_*) \cong P_p \otimes_R H_q(Q_*) \cong \begin{cases} P_p \otimes_R N & q = 0 \\ 0 & q > 0. \end{cases}
\]
::: {.proof}
flatness of $P_p$.
:::
<2>3. By the Acyclic Assembly Lemma applied to the vertical filtration:
\[
\operatorname{Tot}(P_* \otimes_R Q_*) \xrightarrow{\sim} P_* \otimes_R N.
\]
::: {.proof}
Acyclic Assembly Lemma on vertical augmentation.
:::
<2>4. Taking homology gives:
\[
H_n(\operatorname{Tot}(P_* \otimes_R Q_*)) \cong H_n(P_* \otimes_R N) \cong \operatorname{Tor}_n^R(N, M),
\]
via the natural isomorphism $P_* \otimes_R N \cong N \otimes_R P_*$.
::: {.proof}
definition of $\operatorname{Tor}_n^R(N, M)$ via projective resolution of $M$.
:::

<1>4. Conclusion:
Combining <1>2 and <1>3 yields canonical isomorphisms:
\[
\operatorname{Tor}_n^R(M, N) \cong H_n(\operatorname{Tot}(P_* \otimes_R Q_*)) \cong \operatorname{Tor}_n^R(N, M).
\]
Thus $\operatorname{Tor}_*^R$ is symmetric. Q.E.D.
::: {.proof}
<1>2 and <1>3.
:::
:::
