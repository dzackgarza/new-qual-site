---
schema: qual/card@1
id: P-AGH447DUALOFAMORPHISM
kind: problem
title: The dual isogeny $\hat f$ satisfies $f \circ \hat f = n$ and $\deg \hat f = \deg f$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Elliptic Curves
  - Jacobians
  - Curves
relations: []
review: draft
---

::: problem
Let $X$ and $X'$ be elliptic curves over $k$, with base points $P_0, P_0'$.

a. If $f: X \to X'$ is any morphism, use (4.11) to show that $f^*: \Pic X' \to \Pic X$ induces a homomorphism $\hat{f}: (X', P_0') \to (X, P_0)$. We call this the **dual** of $f$.

b. If $f: X \to X'$ and $g: X' \to X''$ are two morphisms, then $\widehat{g \circ f} = \hat{f} \circ \hat{g}$.

c. Assume $f(P_0)=P_0'$, and let $n=\deg f$. Show that if $Q \in X$ is any point, and $f(Q)=Q'$, then $\hat{f}(Q')=n_X(Q)$. (Do the separable and purely inseparable cases separately, then combine.) Conclude that $f \circ \hat{f}=n_{X'}$ and $\hat{f} \circ f=n_X$.

d. \* If $f, g: X \to X'$ are two morphisms preserving the base points $P_0, P_0'$, then $\widehat{f+g} = \hat{f}+\hat{g}$.

    Hints: It is enough to show for any $\mcl \in \Pic X'$, that $(f+g)^* \mcl \cong f^* \mcl \tensor g^* \mcl$. For any $f$, let $\Gamma_f: X \to X \times X'$ be the graph morphism. Then it is enough to show (for $\mcl'=p_2^* \mcl$) that
$$
\Gamma_{f+g}^*(\mcl')=\Gamma_f^* \mcl' \tensor \Gamma_g^* \mcl' .
$$
    Let $\sigma: X \to X \times X'$ be the section $x \mapsto (x, P_0')$. Define a subgroup $\Pic_\sigma$ of $\Pic(X\times X')$ consisting of those $\mcl$ which have degree 0 along each fibre of $p_1$ and satisfy $\sigma^* \mcl = 0 \in \Pic(X)$. Note that this subgroup is isomorphic to the group $\Pic^{\circ}(X'/X)$ used in the definition of the Jacobian variety. Hence there is a 1-1 correspondence between morphisms $f: X \to X'$ and elements $\mcl_f \in \Pic_\sigma$ (this defines $\mcl_f$). Now compute explicitly to show that $\Gamma_g^*(\mcl_f)=\Gamma_f^*(\mcl_g)$ for any $f, g$. Use the fact that $\mcl_{f+g}=\mcl_f \tensor \mcl_g$, and the fact that for any $\mcl$ on $X'$, $p_2^* \mcl \in \Pic_\sigma^{\circ}$ to prove the result.

e. Using (d), show that for any $n \in \ZZ$, $\hat{n}_X=n_X$. Conclude that $\deg n_X=n^2$.

f. Show for any $f$ that $\deg \hat{f}=\deg f$.
:::
